# ai_text_analyzer.py
"""
Syvällinen merkkijono- ja tekstianalysaattori, jossa on yksinkertainen
"tekoälypohjainen" analyysi ilman ulkoisia kirjastoja.

Ohjelma demonstroi:
- ohjelmarakenteen (importit, vakiot, luokat, funktiot, main)
- merkkikohtaisen ja sanakohtaisen analyysin
- heuristisen, sääntöpohjaisen "AI-analyysin" (sentimentti, tyyli, selkeys)
- valikkopohjaisen CLI:n
"""

# 1) IMPORTIT
import string
import unicodedata
from collections import Counter
from typing import Dict, List, Tuple


# 2) VAKIOT JA GLOBAALIT
VOWELS = "aeiouyäöAEIOUYÄÖ"
PUNCT = string.punctuation

DEFAULT_TEXT = (
    "Tämä on esimerkkiteksti, jota käytetään tekoälypohjaisen analyysin "
    "demonstrointiin. Teksti voi olla positiivinen, negatiivinen tai neutraali, "
    "ja analytiikka yrittää päätellä siitä jotain älykkäästi."
)

POSITIVE_WORDS = {
    "hyvä", "loistava", "erinomainen", "mahtava", "positiivinen", "upea",
    "onnistunut", "mukava", "tykkään", "rakastan", "helppo", "sujuva",
    "turvallinen", "vakaa", "tehokas", "onnistuminen"
}

NEGATIVE_WORDS = {
    "huono", "surkea", "viallinen", "negatiivinen", "ongelma", "vaikea",
    "hidas", "epäselvä", "turhauttava", "vihaan", "ärsyttävä", "epäonnistui",
    "riski", "vaara", "bugi", "virhe"
}

FORMAL_MARKERS = {
    "hyväksytty", "sopimus", "projektisuunnitelma", "dokumentaatio",
    "toteutus", "arkkitehtuuri", "vaatimusmäärittely", "kokous", "päätös"
}

INFORMAL_MARKERS = {
    "lol", "heh", "jee", "jees", "xD", "haha", "moro", "tsau", "moi",
    "no joo", "niinku", "kaveri"
}


# 3) LUOKAT
class TextNormalizer:
    """Tekstin normalisointiin liittyvät toiminnot."""

    def remove_punctuation(self, text: str) -> str:
        return "".join(ch for ch in text if ch not in PUNCT)

    def normalize_unicode(self, text: str) -> str:
        return unicodedata.normalize("NFC", text)

    def strip_whitespace(self, text: str) -> str:
        return " ".join(text.split())

    def to_lower(self, text: str) -> str:
        return text.lower()

    def full_normalize(self, text: str) -> str:
        text = self.normalize_unicode(text)
        text = self.strip_whitespace(text)
        text = self.to_lower(text)
        return text


class CharacterAnalyzer:
    """Merkkikohtainen analytiikka."""

    def count_vowels(self, text: str) -> int:
        return sum(1 for ch in text if ch in VOWELS)

    def count_consonants(self, text: str) -> int:
        return sum(1 for ch in text if ch.isalpha() and ch not in VOWELS)

    def count_digits(self, text: str) -> int:
        return sum(1 for ch in text if ch.isdigit())

    def count_special(self, text: str) -> int:
        return sum(1 for ch in text if not ch.isalnum() and not ch.isspace())

    def char_frequency(self, text: str) -> Dict[str, int]:
        return dict(Counter(text))


class WordAnalyzer:
    """Sanojen analysointi ja tokenisointi."""

    def tokenize(self, text: str) -> List[str]:
        cleaned = "".join(ch if ch.isalnum() else " " for ch in text)
        return [w for w in cleaned.split() if w]

    def word_frequency(self, words: List[str]) -> Dict[str, int]:
        return dict(Counter(words))

    def longest_word(self, words: List[str]) -> str:
        return max(words, key=len) if words else ""

    def shortest_word(self, words: List[str]) -> str:
        return min(words, key=len) if words else ""

    def average_word_length(self, words: List[str]) -> float:
        if not words:
            return 0.0
        return sum(len(w) for w in words) / len(words)

    def sentence_split(self, text: str) -> List[str]:
        sentences = []
        current = []
        for ch in text:
            current.append(ch)
            if ch in ".!?":
                sentence = "".join(current).strip()
                if sentence:
                    sentences.append(sentence)
                current = []
        if current:
            sentence = "".join(current).strip()
            if sentence:
                sentences.append(sentence)
        return sentences

    def ngrams(self, words: List[str], n: int) -> Dict[Tuple[str, ...], int]:
        if len(words) < n:
            return {}
        grams = [tuple(words[i:i+n]) for i in range(len(words)-n+1)]
        return dict(Counter(grams))


class AITextAnalyzer:
    """
    Yksinkertainen, heuristinen "tekoälyanalyytikko".

    Ei oikeaa ML:ää, vaan:
    - sentimentti (positiivinen, negatiivinen, neutraali)
    - tyyli (muodollinen / epämuodollinen)
    - selkeys (esim. lauseiden pituus, sanapituus)
    - kokonaisarvio ja tulkinta luonnollisella kielellä
    """

    def __init__(self, normalizer: TextNormalizer, word_analyzer: WordAnalyzer):
        self.normalizer = normalizer
        self.word_analyzer = word_analyzer

    def sentiment_score(self, words: List[str]) -> int:
        score = 0
        for w in words:
            if w in POSITIVE_WORDS:
                score += 1
            if w in NEGATIVE_WORDS:
                score -= 1
        return score

    def sentiment_label(self, score: int) -> str:
        if score > 2:
            return "voimakkaasti positiivinen"
        if score > 0:
            return "lievästi positiivinen"
        if score == 0:
            return "neutraali"
        if score < -2:
            return "voimakkaasti negatiivinen"
        return "lievästi negatiivinen"

    def style_score(self, words: List[str]) -> str:
        lower_words = set(words)
        formal_hits = len(lower_words & FORMAL_MARKERS)
        informal_hits = len(lower_words & INFORMAL_MARKERS)

        if formal_hits > informal_hits and formal_hits > 0:
            return "muodollinen / asiallinen"
        if informal_hits > formal_hits and informal_hits > 0:
            return "epämuodollinen / puhekielinen"
        return "neutraali / sekamuotoinen"

    def clarity_score(self, sentences: List[str], words: List[str]) -> float:
        if not sentences:
            return 0.0
        avg_words_per_sentence = len(words) / len(sentences)
        return avg_words_per_sentence

    def complexity_label(self, avg_word_len: float, avg_words_per_sentence: float) -> str:
        if avg_word_len <= 4 and avg_words_per_sentence <= 12:
            return "helppolukuinen ja ytimekäs"
        if avg_word_len <= 6 and avg_words_per_sentence <= 20:
            return "kohtalaisen selkeä"
        if avg_word_len > 6 or avg_words_per_sentence > 25:
            return "melko raskas ja monimutkainen"
        return "keskitasoinen luettavuus"

    def analyze(self, text: str) -> Dict[str, str]:
        normalized = self.normalizer.full_normalize(text)
        words = self.word_analyzer.tokenize(normalized)
        sentences = self.word_analyzer.sentence_split(text)

        sentiment = self.sentiment_score(words)
        sentiment_label = self.sentiment_label(sentiment)
        style = self.style_score(words)
        clarity_raw = self.clarity_score(sentences, words)
        avg_len = self.word_analyzer.average_word_length(words)
        complexity = self.complexity_label(avg_len, clarity_raw)

        # Yksinkertainen "tulkintateksti"
        interpretation_lines = []

        interpretation_lines.append(
            f"Tekstin yleissävy vaikuttaa olevan {sentiment_label}."
        )
        interpretation_lines.append(
            f"Tyyli on pääosin {style}."
        )
        interpretation_lines.append(
            f"Lauseiden määrä: {len(sentences)}, sanojen määrä: {len(words)}."
        )
        interpretation_lines.append(
            f"Keskimäärin noin {clarity_raw:.1f} sanaa per lause ja "
            f"keskimääräinen sanapituus {avg_len:.1f} merkkiä."
        )
        interpretation_lines.append(
            f"Kokonaisuutena teksti on {complexity}."
        )

        if sentiment > 2 and "risk" in normalized:
            interpretation_lines.append(
                "Teksti on positiivinen, mutta mainitsee riskejä – "
                "mahdollisesti myönteinen suunnitelma, jossa huomioidaan riskit."
            )
        elif sentiment < -2 and clarity_raw > 20:
            interpretation_lines.append(
                "Teksti on melko negatiivinen ja pitkälauseinen – "
                "voi viitata turhautumiseen tai monimutkaiseen ongelmaan."
            )
        elif sentiment == 0 and "projekti" in normalized:
            interpretation_lines.append(
                "Tekstin sävy on neutraali ja liittynee projektikuvaus- tai "
                "raportointityyppiseen sisältöön."
            )

        return {
            "sentiment_label": sentiment_label,
            "style": style,
            "complexity": complexity,
            "summary": "\n".join(interpretation_lines),
        }


# 4) APUFUNKTIOT
def print_menu() -> None:
    print("\n=== TEKOÄLYPOHJAINEN TEKSTIANALYSAATTORI ===")
    print("1) Merkkikohtainen analyysi")
    print("2) Sanakohtainen analyysi")
    print("3) N-gram-analyysi")
    print("4) Normalisointiesimerkit")
    print("5) Tekoälypohjainen analyysi (sentimentti, tyyli, selkeys)")
    print("6) Näytä nykyinen teksti / vaihda teksti")
    print("7) Palauta oletusteksti")
    print("0) Lopeta")


def read_text(current: str) -> str:
    print("\nNykyinen teksti:")
    print(f"\"{current}\"")
    new = input("\nAnna uusi teksti (Enter säilyttää nykyisen): ")
    return new if new.strip() else current


def wait() -> None:
    input("\nPaina Enter jatkaaksesi...")


def print_word_freq(freqs: Dict[str, int]) -> None:
    if not freqs:
        print("Ei sanoja.")
        return
    for w, c in sorted(freqs.items(), key=lambda x: (-x[1], x[0])):
        print(f"{w}: {c}")


# 5) PÄÄOHJELMA
def main() -> None:
    normalizer = TextNormalizer()
    char_an = CharacterAnalyzer()
    word_an = WordAnalyzer()
    ai_an = AITextAnalyzer(normalizer, word_an)

    text = DEFAULT_TEXT

    print("Tervetuloa tekoälypohjaiseen tekstianalysaattoriin!")
    print("Voit syöttää oman tekstin ja analysoida sitä eri näkökulmista.")
    print(f"\nOletusteksti:\n{text}")

    while True:
        print_menu()
        choice = input("Valinta: ").strip()

        if choice == "0":
            print("Kiitos käytöstä, nähdään taas!")
            break

        elif choice == "1":
            text = read_text(text)
            print("\n--- Merkkikohtainen analyysi ---")
            print(f"Vokaaleja: {char_an.count_vowels(text)}")
            print(f"Konsonantteja: {char_an.count_consonants(text)}")
            print(f"Numeroita: {char_an.count_digits(text)}")
            print(f"Erikoismerkkejä: {char_an.count_special(text)}")
            print("\nMerkkifrekvenssit:")
            for ch, cnt in sorted(char_an.char_frequency(text).items()):
                print(f"{repr(ch)}: {cnt}")
            wait()

        elif choice == "2":
            text = read_text(text)
            words = word_an.tokenize(text)
            print("\n--- Sanakohtainen analyysi ---")
            print(f"Sanoja yhteensä: {len(words)}")
            print(f"Pisin sana: {word_an.longest_word(words)}")
            print(f"Lyhyin sana: {word_an.shortest_word(words)}")
            print(f"Keskimääräinen sanapituus: {word_an.average_word_length(words):.2f}")
            print("\nSanat frekvensseittäin:")
            print_word_freq(word_an.word_frequency(words))
            wait()

        elif choice == "3":
            text = read_text(text)
            words = word_an.tokenize(text)
            try:
                n = int(input("Anna n-grammin koko (esim. 2 tai 3): "))
            except ValueError:
                print("Virheellinen syöte.")
                wait()
                continue
            grams = word_an.ngrams(words, n)
            print(f"\n--- {n}-grammit ---")
            for gram, cnt in sorted(grams.items(), key=lambda x: (-x[1], x[0])):
                print(f"{' '.join(gram)}: {cnt}")
            wait()

        elif choice == "4":
            text = read_text(text)
            print("\n--- Normalisointi ---")
            print("Unicode NFC -normalisointi:")
            print(normalizer.normalize_unicode(text))
            print("\nWhitespace-normalisointi:")
            print(normalizer.strip_whitespace(text))
            print("\nTäysi normalisointi (NFC + whitespace + lowercase):")
            print(normalizer.full_normalize(text))
            wait()

        elif choice == "5":
            text = read_text(text)
            print("\n--- Tekoälypohjainen analyysi ---")
            result = ai_an.analyze(text)
            print(f"\nSentimentti: {result['sentiment_label']}")
            print(f"Tyyli: {result['style']}")
            print(f"Luettavuus / monimutkaisuus: {result['complexity']}")
            print("\nYhteenveto ja tulkinta:")
            print(result["summary"])
            wait()

        elif choice == "6":
            text = read_text(text)
            print("\nUusi nykyinen teksti:")
            print(text)
            wait()

        elif choice == "7":
            text = DEFAULT_TEXT
            print("Oletusteksti palautettu.")
            print(text)
            wait()

        else:
            print("Tuntematon valinta.")
            wait()


if __name__ == "__main__":
    main()