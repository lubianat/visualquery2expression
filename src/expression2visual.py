import json
from pathlib import Path
import sexpdata

HERE = Path(__file__).parent.resolve()
DATA = HERE.parent.joinpath("data").resolve()


def main():
    s_expression = sexpdata.loads(DATA.joinpath("example_expression.txt").read_text())
    print(s_expression)
    reserved_words = ["AND", "JOIN"]

    for symbol in s_expression:
        if isinstance(symbol, list):
            continue

        (symbol._val)


if __name__ == "__main__":
    main()
