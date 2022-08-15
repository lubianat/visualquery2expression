import pytest
import json
from pathlib import Path

HERE = Path(__file__).parent.resolve()
DATA = HERE.parent.joinpath("data")


def test_visual_query_rendering():
    subject_type = "Disease"
    object_type = "Symptom"

    target = json.loads(DATA.joinpath("example_visual_query.json").read_text())
    result = render_visual_expression(subject_type, object_type)
    assert target == result
