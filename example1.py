import sys
import sympy
import traceback
import inspect
import importlib.util
import pprint as pp
from pathlib import Path
import shutil

current_dir = Path.cwd()
current_file_path = Path(__file__).absolute()
module_path = importlib.util.find_spec("sympy").origin
print(
    module_path,
    "<= open this path and write before return raise Exception('Deliberate') and run again",
)
try:
    p = list(sympy.primerange(3, 10))  # Your sympy function
    print(p)
except Exception as e:
    tb = traceback.format_exc()
    lines = tb.split("\n")
    lines = [s.strip() for s in lines]
    paths = []
    for l in lines:
        if "C:\\" in l:
            pot_paths = l.split(" ")
            # print("pot_path",pot_paths)
            for pot_path in pot_paths:
                if "C:\\" in pot_path:
                    paths.append(pot_path)
                    break
    paths = [s.strip().replace(",", "").replace('"', "") for s in paths]
    paths = list(set(paths))
    pp.pprint(paths)
    print(current_file_path)
if len(paths) == 0:
    paths = ["C:\\Python310\\Lib\\site-packages\\sympy\\ntheory\\generate.py"]
    pp.pprint(paths)

for path in paths:
    print("copytnig", path, "to", current_dir + "/" + path.split("/")[-1])
    shutil.copyfile(path, current_dir + "/" + path.split("/")[-1])
