# aritmetiikka_ohjelma.py
"""
Yksinkertainen aritmetiikkaohjelma, joka demonstroi
Python-projektin rakennetta ja moduulimaista ajattelua
yhden tiedoston sisällä.
"""

# 1) Importit
import math
from dataclasses import dataclass
from typing import List

# 2) Vakiot ja "globaalit"
PI = math.pi
MAX_HISTORY = 20


# 3) Luokat ja datarakenteet
@dataclass
class Operation:
    """Kuvaa yhtä laskutoimitusta."""
    name: str
    a: float
    b: float
    result: float


class Calculator:
    """Yksinkertainen laskin, joka pitää kirjaa historiasta."""

    def __init__(self) -> None:
        self.history: List[Operation] = []

    def _store(self, name: str, a: float, b: float, result: float) -> float:
        op = Operation(name, a, b, result)
        self.history.append(op)
        if len(self.history) > MAX_HISTORY:
            # poistetaan vanhin, jos historia kasvaa liian suureksi
            self.history.pop(0)
        return result

    def add(self, a: float, b: float) -> float:
        return self._store("summa", a, b, a + b)

    def subtract(self, a: float, b: float) -> float:
        return self._store("erotus", a, b, a - b)

    def multiply(self, a: float, b: float) -> float:
        return self._store("tulo", a, b, a * b)

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Nollalla ei voi jakaa")
        return self._store("osamäärä", a, b, a / b)

    def power(self, a: float, b: float) -> float:
        return self._store("potenssi", a, b, a ** b)

    def history_as_str(self) -> str:
        lines = []
        for op in self.history:
            lines.append(f"{op.name}: {op.a} ja {op.b} -> {op.result}")
        return "\n".join(lines) if lines else "Ei vielä historiaa."


# 4) Apufunktiot (modulaarinen logiikka erillään pääohjelmasta)
def read_number(prompt: str) -> float:
    """Lukee luvun käyttäjältä, hyväksyy myös pilkun desimaalierottimena."""
    while True:
        raw = input(prompt)
        try:
            return float(raw.replace(",", "."))
        except ValueError:
            print("Anna kelvollinen luku (esim. 3.14).")


def print_menu() -> None:
    print("\n=== Aritmetiikkaohjelma ===")
    print("1) Summa")
    print("2) Erotus")
    print("3) Tulo")
    print("4) Jakolasku")
    print("5) Potenssi")
    print("6) Näytä historia")
    print("0) Lopeta")


def handle_binary_op(calc: Calculator, op_name: str) -> None:
    """Käsittelee kahden luvun laskutoimituksen."""
    a = read_number("Anna ensimmäinen luku: ")
    b = read_number("Anna toinen luku: ")

    ops = {
        "1": calc.add,
        "2": calc.subtract,
        "3": calc.multiply,
        "4": calc.divide,
        "5": calc.power,
    }

    func = ops[op_name]
    try:
        result = func(a, b)
        print(f"Tulos: {result}")
    except ValueError as e:
        print(f"Virhe: {e}")


# 5) Pääohjelma (main) ja entry point
def main() -> None:
    calc = Calculator()

    print(f"Tervetuloa aritmetiikkaohjelmaan (PI ≈ {PI:.2f})")

    while True:
        print_menu()
        choice = input("Valinta: ").strip()

        if choice == "0":
            print("Kiitos käytöstä!")
            break
        elif choice in {"1", "2", "3", "4", "5"}:
            handle_binary_op(calc, choice)
        elif choice == "6":
            print(calc.history_as_str())
        else:
            print("Tuntematon valinta.")


if __name__ == "__main__":
    main()