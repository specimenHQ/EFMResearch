import importlib.util
import json
import sys
from pathlib import Path

candidate_dir = Path(sys.argv[1]).resolve()
common_path = Path(sys.argv[2]).resolve()
sys.path.insert(0, str(candidate_dir))
from line_mapper import LineIndex

spec = importlib.util.spec_from_file_location("common_evaluation", common_path)
module = importlib.util.module_from_spec(spec)
sys.modules["common_evaluation"] = module
spec.loader.exec_module(module)

checks, failures = module.evaluate(LineIndex)
print(json.dumps({"checks": checks, "failures": failures}, ensure_ascii=False))
