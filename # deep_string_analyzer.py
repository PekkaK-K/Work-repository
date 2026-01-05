# deep_string_analyzer.py
"""
Syvällinen merkkijonojen käsittelyohjelma.

Tämä ohjelma demonstroi:
- ohjelman rakenteen (importit, vakiot, luokat, funktiot, main)
- merkkijonojen analysointia, normalisointia ja tilastointia
- tokenisointia, frekvenssianalyysiä, n-grammeja
- merkkikohtaista analytiikkaa
- tekstin muokkausta ja transformaatioita
- CLI-valikkopohjaisen käyttöliittymän

Ohjelma on tarkoituksella pitkä, syvällinen ja monipuolinen.
"""

# 1) IMPORTIT
import string
import unicodedata
from collections import Counter, defaultdict
from typing import Dict, List, Tuple


# 2) VAKIOT JA GLOBAALIT
VOWELS = "aeiouyäöAEIOUYÄÖ"
PUNCT = string.punctuation
DEFAULT_TEXT = (
    "Tämä on syvällinen esimerkkiteksti, jota käytetään merkkijonojen "
    "käsittelyn demonstraatioon. Ohjelma analysoi sanoja, merkkejä, "
    "frekvenssejä, n-grammeja ja paljon muuta!"
)


# 3) LUOKAT
class TextNormalizer:
    """Tekstin normalisointiin liittyvät toiminnot."""

    def remove_punctuation(self, text: str) -> str:
        return "".join(ch for ch in text if ch not in PUNCT)

    def to_lower(self, text: str) -> str:
        return text.lower()

    def to_upper(self, text: str) -> str:
        return text.upper()

    def normalize_unicode(self, text: str) -> str:
        """Normalisoi tekstin Unicode NFC -muotoon."""
        return unicodedata.normalize("NFC", text)

    def strip_whitespace(self, text: str) -> str:
        return " ".join(text.split())

    def full_normalize(self, text: str) -> str:
        """Täydellinen normalisointi."""
        text = self.normalize_unicode(text)
        text = self.strip_whitespace(text)
        return text


class CharacterAnalyzer:
    """Merkkikohtainen analytiikka."""

    def count_vowels(self, text: str) -> int:
        return sum(1 for ch in text if ch in VOWELS)

    def count_consonants(self, text: str) -> int:
        return sum(
            1 for ch in text
            if ch.isalpha() and ch not in VOWELS
        )

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

    def ngrams(self, words: List[str], n: int) -> Dict[Tuple[str, ...], int]:
        if len(words) < n:
            return {}
        grams = [tuple(words[i:i+n]) for i in range(len(words)-n+1)]
        return dict(Counter(grams))


class TextTransformer:
    """Tekstin muokkaus ja transformaatio."""

    def reverse(self, text: str) -> str:
        return text[::-1]

    def to_title_case(self, text: str) -> str:
        return text.title()

    def highlight(self, text: str, term: str) -> str:
        if not term:
            return text
        return text.replace(term, f"[{term}]")

    def leetspeak(self, text: str) -> str:
        mapping = {
            "a": "4", "A": "4",
            "e": "3", "E": "3",
            "i": "1", "I": "1",
            "o": "0", "O": "0",
            "s": "5", "S": "5",
            "t": "7", "T": "7",
        }
        return "".join(mapping.get(ch, ch) for ch in text)


# 4) APUFUNKTIOT
def print_menu():
    print("\n=== SYVÄLLINEN MERKKIJONOANALYSAATTORI ===")
    print("1) Merkkikohtainen analyysi")
    print("2) Sanakohtainen analyysi")
    print("3) N-gram-analyysi")
    print("4) Tekstin normalisointi")
    print("5) Tekstin transformaatio")
    print("6) Korosta alimerkkijono")
    print("7) Palauta oletusteksti")
    print("8) Näytä nykyinen teksti")
    print("0) Lopeta")


def read_text(current: str) -> str:
    print("\nNykyinen teksti:")
    print(f"\"{current}\"")
    new = input("\nAnna uusi teksti (Enter säilyttää nykyisen): ")
    return new if new.strip() else current


def wait():
    input("\nPaina Enter jatkaaksesi...")


# 5) PÄÄOHJELMA
def main():
    normalizer = TextNormalizer()
    char_an = CharacterAnalyzer()
    word_an = WordAnalyzer()
    transformer = TextTransformer()

    text = DEFAULT_TEXT

    print("Tervetuloa syvälliseen merkkijonoanalyysiohjelmaan!")
    print(f"Oletusteksti:\n{text}")

    while True:
        print_menu()
        choice = input("Valinta: ").strip()

        if choice == "0":
            print("Kiitos käytöstä!")
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
            for w, c in sorted(word_an.word_frequency(words).items(), key=lambda x: (-x[1], x[0])):
                print(f"{w}: {c}")
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
                print(f"{gram}: {cnt}")
            wait()

        elif choice == "4":
            text = read_text(text)
            print("\n--- Normalisointi ---")
            print("Unicode-normalisointi (NFC):")
            print(normalizer.normalize_unicode(text))
            print("\nWhitespace-normalisointi:")
            print(normalizer.strip_whitespace(text))
            print("\nTäydellinen normalisointi:")
            print(normalizer.full_normalize(text))
            wait()

        elif choice == "5":
            text = read_text(text)
            print("\n--- Transformaatio ---")
            print("Käännetty:")
            print(transformer.reverse(text))
            print("\nTitle Case:")
            print(transformer.to_title_case(text))
            print("\nLeetspeak:")
            print(transformer.leetspeak(text))
            wait()

        elif choice == "6":
            text = read_text(text)
            term = input("Anna korostettava termi: ")
            print("\nKorostettu teksti:")
            print(transformer.highlight(text, term))
            wait()

        elif choice == "7":
            text = DEFAULT_TEXT
            print("Oletusteksti palautettu.")
            wait()

        elif choice == "8":
            print("\nNykyinen teksti:")
            print(text)
            wait()

        else:
            print("Tuntematon valinta.")
            wait()


if __name__ == "__main__":
    main()