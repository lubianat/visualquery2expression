import json
from pathlib import Path

HERE = Path(__file__).parent.resolve()
DATA = HERE.parent.joinpath("data").resolve()


def main():
    visual_query = json.loads(DATA.joinpath("example_visual_query.json").read_text())
    print(json.dumps(visual_query, indent=4))

    line = visual_query["branches"][0]["line"]
    subject_type = line["sType"].split("#")[-1]
    object = line["values"][0]["uri"].split("/")[-1]
    property_label = line["p"].split("#")[-1]
    s_expression = (
        f"(AND {subject_type} (JOIN {subject_type}.{property_label} {object}))"
    )
    print(s_expression)


if __name__ == "__main__":
    main()
