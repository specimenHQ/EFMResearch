import json
import sys
from pathlib import Path

candidate_dir = Path(sys.argv[1]).resolve()
common_dir = Path(sys.argv[2]).resolve()
sys.path.insert(0, str(candidate_dir))
sys.path.insert(0, str(common_dir))
from line_mapper import LineIndex
from post_green_evaluation import evaluate

checks, failures = evaluate(LineIndex)
print(json.dumps({"checks": checks, "failures": failures}, ensure_ascii=False))
