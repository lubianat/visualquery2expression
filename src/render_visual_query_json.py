from asyncio.windows_events import NULL
import json


subject_type = "Disease"
object_type = "Symptom"


def render_visual_expression(subject_type, object_type):
    subject_projection = f"?{subject_type.lower()}"
    object_projection = f"?{object_type.lower()}"

    variables = [subject_projection, object_projection]
    visual_query_json = {
        "distinct": True,
        "variables": variables,
        "defaultLang": "en",
        "order": None,
        "branches": [
            {
                "line": {
                    "s": "?disease",
                    "p": "http://www.semanticweb.org/lubianat/ontologies/2022/4/sparnanatural_wisecube#has_symptom",
                    "o": "?symptom",
                    "sType": "http://www.semanticweb.org/lubianat/ontologies/2022/4/sparnanatural_wisecube#Disease",
                    "oType": "http://www.semanticweb.org/lubianat/ontologies/2022/4/sparnanatural_wisecube#Symptom",
                    "values": [
                        {
                            "label": "abdominal cramps",
                            "uri": "http://www.wikidata.org/entity/Q3002092",
                        }
                    ],
                },
                "children": [],
            }
        ],
    }

    return visual_query_json
