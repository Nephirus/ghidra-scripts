# Bookmark all unreferenced functions
#@author Jiri Kerestes
#@category Custom.Python
#@keybinding 
#@menupath 
#@toolbar 

for fn in currentProgram.getFunctionManager().getFunctions(getAddressFactory().getAddress("0"), True) :
    if not getReferencesTo(fn.entryPoint):
        createBookmark(fn.entryPoint, "unreferenced functions", str(fn))
