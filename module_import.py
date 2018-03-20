import importlib

def dynamic_import(module):
    print importlib.import_module(module)
    return importlib.import_module(module)

def runmodule(module,*argv):
    print module,argv
    loadmodule=dynamic_import(module)
    print loadmodule
    getattr(loadmodule.Main(),argv[0])(argv[1:])

    

if __name__ == "__main__":
    runmodule("WebAttack.HTTP_correlation.s.ff","show","jsahgdjhasgdjhasgd")