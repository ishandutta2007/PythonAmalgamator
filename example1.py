import sys
import sympy
import traceback
import inspect


def run_user_code(envdir):
    p = list(sympy.primerange(1, 100))
    source = input(">>> ")
    print(p)
    try:
        exec(source, envdir)
    except Exception:
        print("Exception in user code:")
        print("-"*60)
        traceback.print_exc(file=sys.stdout)
        print("-"*60)

envdir = {}
while True:
    run_user_code(envdir)
