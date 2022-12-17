XMLNS = "String  \"http://www.w3.org/XML/1998/namespace\""
NSDECL = "String  \"http://www.w3.org/xmlns/2000/\""
def ():
    '''returns NamespaceSupport\n\n
    ()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def pushContext():
    '''returns None\n\n
    pushContext()\n
    '''
def popContext():
    '''returns None\n\n
    popContext()\n
    '''
def declarePrefix():
    '''returns boolean\n\n
    declarePrefix(final String s, final String s2)\n
    '''
def processName():
    '''returns String[]\n\n
    processName(final String s, final String[] array, final boolean b)\n
    '''
def getURI():
    '''returns String\n\n
    getURI(final String s)\n
    '''
def getPrefixes():
    '''returns Enumeration\n\n
    getPrefixes()\n
    getPrefixes(final String s)\n
    '''
def getPrefix():
    '''returns String\n\n
    getPrefix(final String s)\n
    '''
def getDeclaredPrefixes():
    '''returns Enumeration\n\n
    getDeclaredPrefixes()\n
    '''
def setNamespaceDeclUris():
    '''returns None\n\n
    setNamespaceDeclUris(final boolean namespaceDeclUris)\n
    '''
def isNamespaceDeclUris():
    '''returns boolean\n\n
    isNamespaceDeclUris()\n
    '''
