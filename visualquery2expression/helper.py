import json


def convert_visual_query_to_expression(visual_query):
    print(json.dumps(visual_query, indent=4))
    line = visual_query["branches"][0]["line"]
    subject_type = line["sType"].split("#")[-1]
    object = line["values"][0]["label"].replace(" ", "_")
    object_label = line["values"][0]["uri"].split("/")[-1]
    property_label = line["p"].split("#")[-1]
    s_expression = f"(AND {subject_type} (JOIN {subject_type}.{property_label} {object}={object_label}))"
    return s_expression


def render_visual_expression(subject_type, object_type, object_label, relation, object):
    subject_projection = f"?{subject_type.lower()}"
    object_projection = f"?{object_type.lower()}"
    object_label = object_label.replace("_", " ")
    variables = [subject_projection, object_projection]
    visual_query_json = {
        "distinct": True,
        "variables": variables,
        "defaultLang": "en",
        "order": None,
        "branches": [
            {
                "line": {
                    "s": subject_projection,
                    "p": f"http://www.semanticweb.org/lubianat/ontologies/2022/4/sparnanatural_wisecube#{relation}",
                    "o": object_projection,
                    "sType": f"http://www.semanticweb.org/lubianat/ontologies/2022/4/sparnanatural_wisecube#{subject_type}",
                    "oType": f"http://www.semanticweb.org/lubianat/ontologies/2022/4/sparnanatural_wisecube#{object_type}",
                    "values": [
                        {
                            "label": object_label,
                            "uri": f"http://www.wikidata.org/entity/{object}",
                        }
                    ],
                },
                "children": [],
            }
        ],
    }

    return visual_query_json
