def ():
    '''returns NamespaceContext\n\n
    (final ErrorReporter fReporter, final SymbolTable fSymbolTable)\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def startNamespacesScope():
    '''returns int\n\n
    startNamespacesScope()\n
    '''
def currentContext():
    '''returns int\n\n
    currentContext()\n
    '''
def endNamespacesScope():
    '''returns int\n\n
    endNamespacesScope()\n
    '''
def nsDeclCount():
    '''returns int\n\n
    nsDeclCount(final int n)\n
    '''
def nsDeclPrefix():
    '''returns int\n\n
    nsDeclPrefix(final int n, final int n2)\n
    '''
def nsDeclURI():
    '''returns int\n\n
    nsDeclURI(final int n, final int n2)\n
    '''
def setNSDeclURI():
    '''returns None\n\n
    setNSDeclURI(final int n, final int n2, final int n3)\n
    '''
def nsDeclQName():
    '''returns int\n\n
    nsDeclQName(final int n, final int n2)\n
    '''
def prefixMapping():
    '''returns int\n\n
    prefixMapping(int n, final int n2)\n
    '''
def totalMappingsCount():
    '''returns int\n\n
    totalMappingsCount(int n)\n
    '''
def inScopeNamespaces():
    '''returns int\n\n
    inScopeNamespaces(int n, final int[] array)\n
    '''
def createPrefixMapping():
    '''returns boolean\n\n
    createPrefixMapping(final int n, final int n2, final int n3, final boolean b)\n
    '''
def setNamespaceURI():
    '''returns boolean\n\n
    setNamespaceURI(final int n, final QName qName)\n
    '''
def checkDuplicateNamespaces():
    '''returns boolean\n\n
    checkDuplicateNamespaces(final QName qName)\n
    '''
