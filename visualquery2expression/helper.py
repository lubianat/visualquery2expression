"""A series of functions to convert s-expressions and visual queries

The code here converts between the Visual Query JSON format used in
the backend of [Sparnatural](https://github.com/sparna-git/Sparnatural)
and S-expressions compatible with statistical learning of the sort used
by https://dki-lab.github.io/GrailQA/.

"""
import sexpdata


def convert_visual_query_to_expression(visual_query):
    """
    Given a Sparnatural visual query JSON, gets a Wisecube-style s-expression.
    Args:
      visual_query (dict): a visual query JSON parsed into a python dictionary.

    Returns:
      str: An Wisecube-style s-expression
    """
    line = visual_query["branches"][0]["line"]
    subject_type = line["sType"].split("#")[-1]
    object_qid = line["values"][0]["label"].replace(" ", "_")
    object_label = line["values"][0]["uri"].split("/")[-1]
    property_label = line["p"].split("#")[-1]
    s_expression = (
        f"(AND {subject_type}"
        f" (JOIN {subject_type}.{property_label}"
        f" {object_qid}={object_label}))"
    )
    return s_expression


def render_visual_query(subject_type, object_type, object_label, relation, object_qid):
    """
    Renders a simple Sparnatural JSON given a series of objects for a triple.
    """
    subject_projection = f"?{subject_type.lower()}"
    object_projection = f"?{object_type.lower()}"
    object_label = object_label.replace("_", " ")
    variables = [subject_projection, object_projection]
    prefix = (
        "http://www.semanticweb.org/lubianat/ontologies/2022/4/sparnanatural_wisecube"
    )
    visual_query_json = {
        "distinct": True,
        "variables": variables,
        "defaultLang": "en",
        "order": None,
        "branches": [
            {
                "line": {
                    "s": subject_projection,
                    "p": f"{prefix}#{relation}",
                    "o": object_projection,
                    "sType": f"{prefix}#{subject_type}",
                    "oType": f"{prefix}#{object_type}",
                    "values": [
                        {
                            "label": object_label,
                            "uri": f"http://www.wikidata.org/entity/{object_qid}",
                        }
                    ],
                },
                "children": [],
            }
        ],
    }

    return visual_query_json


def get_visual_query_from_s_expression(s_expression):
    """
    Provided a s_expression in the Wisecube format, returns a visual query.

    """
    s_expression = sexpdata.loads(s_expression)
    relationlabel2object = {"has_symptom": "Symptom"}
    relationlabel2subject = {"has_symptom": "Disease"}

    for symbol in s_expression:
        if isinstance(symbol, list):
            relation = symbol[1]._val.split(".")[1]
            object_composed = symbol[2]._val.split("=")
            print(relation)
            object_type = relationlabel2object[relation]
            subject_type = relationlabel2subject[relation]
            object_label = object_composed[0]
            object_qid = object_composed[1]
    return render_visual_query(
        subject_type, object_type, object_label, relation, object_qid
    )
