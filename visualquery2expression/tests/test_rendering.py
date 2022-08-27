import pytest
import json
from pathlib import Path
from visualquery2expression import *

HERE = Path(__file__).parent.resolve()
DATA = HERE.joinpath("data")


def test_s_expression_rendering():
    target = json.loads(DATA.joinpath("example_visual_query.json").read_text())
    result = render_visual_expression(
        subject_type="Disease",
        object_type="Symptom",
        relation="has_symptom",
        object_label="abdominal_cramps",
        object="Q3002092",
    )
    assert target == result
