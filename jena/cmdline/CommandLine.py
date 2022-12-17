def ():
    '''returns CommandLine\n\n
    ()\n
    '''
def setHook():
    '''returns None\n\n
    setHook(final ArgHandler argHandler)\n
    '''
def setUsage():
    '''returns None\n\n
    setUsage(final String usageMessage)\n
    '''
def hasArgs():
    '''returns boolean\n\n
    hasArgs()\n
    '''
def hasItems():
    '''returns boolean\n\n
    hasItems()\n
    '''
def args():
    '''returns Iterator<Arg>\n\n
    args()\n
    '''
def numArgs():
    '''returns int\n\n
    numArgs()\n
    '''
def numItems():
    '''returns int\n\n
    numItems()\n
    '''
def pushItem():
    '''returns None\n\n
    pushItem(final String s)\n
    '''
def isIndirectItem():
    '''returns boolean\n\n
    isIndirectItem(final int i)\n
    '''
def getItem():
    '''returns String\n\n
    getItem(final int i)\n
    getItem(final int i, final boolean withIndirect)\n
    '''
def process():
    '''returns None\n\n
    process(final String[] argv)\n
    '''
def ignoreArgument():
    '''returns boolean\n\n
    ignoreArgument(final String argStr)\n
    '''
def endProcessing():
    '''returns boolean\n\n
    endProcessing(final String argStr)\n
    '''
def handleUnrecognizedArg():
    '''returns None\n\n
    handleUnrecognizedArg(final String argStr)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final ArgDecl argDecl)\n
    contains(final String s)\n
    '''
def hasArg():
    '''returns boolean\n\n
    hasArg(final String argName)\n
    hasArg(final ArgDecl argDecl)\n
    '''
def getArg():
    '''returns Arg\n\n
    getArg(final ArgDecl argDecl)\n
    getArg(String s)\n
    '''
def getValue():
    '''returns String\n\n
    getValue(final ArgDecl argDecl)\n
    getValue(final String argName)\n
    '''
def getValues():
    '''returns List<String>\n\n
    getValues(final ArgDecl argDecl)\n
    getValues(final String argName)\n
    '''
def add():
    '''returns CommandLine\n\n
    add(final String argName, final boolean hasValue)\n
    add(final boolean hasValue, final String argName)\n
    add(final ArgDecl arg)\n
    '''
def allowItemIndirect():
    '''returns boolean\n\n
    allowItemIndirect()\n
    '''
def setAllowItemIndirect():
    '''returns None\n\n
    setAllowItemIndirect(final boolean allowItemIndirect)\n
    '''
def isIgnoreIndirectionMarker():
    '''returns boolean\n\n
    isIgnoreIndirectionMarker()\n
    '''
def getIndirectionMarker():
    '''returns String\n\n
    getIndirectionMarker()\n
    '''
def setIndirectionMarker():
    '''returns None\n\n
    setIndirectionMarker(final String indirectionMarker)\n
    '''
def setIgnoreIndirectionMarker():
    '''returns None\n\n
    setIgnoreIndirectionMarker(final boolean ignoreIndirectionMarker)\n
    '''
def trace():
    '''returns ArgHandler\n\n
    trace()\n
    '''
def action():
    '''returns None\n\n
    action(final String arg, final String val)\n
    '''
