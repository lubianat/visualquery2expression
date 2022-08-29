import pytest
import json
from pathlib import Path
from visualquery2expression import *

HERE = Path(__file__).parent.resolve()
DATA = HERE.joinpath("data")


def test_s_expression_rendering():
    target = json.loads(DATA.joinpath("example_visual_query.json").read_text())
    result = render_visual_query(
        subject_type="Disease",
        object_type="Symptom",
        relation="has_symptom",
        object_label="abdominal_cramps",
        object_qid="Q3002092",
    )
    assert target == result


def test_visual_query_rendering():
    target = json.loads(DATA.joinpath("example_visual_query.json").read_text())

    s_expression = DATA.joinpath("example_expression.txt").read_text()
    print(s_expression)
    result = get_visual_query_from_s_expression(s_expression)
    assert target == result
