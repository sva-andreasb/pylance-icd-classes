def ():
    '''returns ScopeWithTypeVariables\n\n
    (final String[] typeVarNames, final IScope delegate)\n
    '''
def lookupType():
    '''returns UnresolvedType\n\n
    lookupType(final String name, final IHasPosition location)\n
    '''
def getWorld():
    '''returns World\n\n
    getWorld()\n
    '''
def getEnclosingType():
    '''returns ResolvedType\n\n
    getEnclosingType()\n
    '''
def getMessageHandler():
    '''returns IMessageHandler\n\n
    getMessageHandler()\n
    '''
def lookupFormal():
    '''returns FormalBinding\n\n
    lookupFormal(final String name)\n
    '''
def getFormal():
    '''returns FormalBinding\n\n
    getFormal(final int i)\n
    '''
def getFormalCount():
    '''returns int\n\n
    getFormalCount()\n
    '''
def getImportedPrefixes():
    '''returns String[]\n\n
    getImportedPrefixes()\n
    '''
def getImportedNames():
    '''returns String[]\n\n
    getImportedNames()\n
    '''
def message():
    '''returns None\n\n
    message(final IMessage.Kind kind, final IHasPosition location, final String message)\n
    message(final IMessage.Kind kind, final IHasPosition location1, final IHasPosition location2, final String message)\n
    message(final IMessage aMessage)\n
    '''
