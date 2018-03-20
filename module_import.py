import importlib

def dynamic_import(module):
    return importlib.import_module(module)

def runmoduleW(module,*argv):
    print '------------',module,argv
    loadmodule=dynamic_import(module)
    getattr(loadmodule.Main(),argv[0])(argv[1:])

def runmoduleI(module,*argv):
    print '------------',module,argv[1]
    loadmodule=dynamic_import(module)
    getattr(loadmodule.Main(argv[1]),argv[0])()


    

if __name__ == "__main__":
    runmoduleI("InfoGet.IPinfo_._IP","getplace","2.2.2.2")