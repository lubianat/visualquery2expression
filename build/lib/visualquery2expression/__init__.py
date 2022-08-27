def render_visual_expression(subject_type, object_type, object_label, relation):
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
                    "s": f"?{subject_projection}",
                    "p": f"http://www.semanticweb.org/lubianat/ontologies/2022/4/sparnanatural_wisecube#{relation}",
                    "o": f"?{object_projection}",
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
