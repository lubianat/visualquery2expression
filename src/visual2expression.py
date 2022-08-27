import json
from pathlib import Path

HERE = Path(__file__).parent.resolve()
DATA = HERE.parent.joinpath("data").resolve()

visual_query = json.loads(DATA.joinpath("example_visual_query.json").read_text())


if __name__ == "__main__":
    main()
