SCOPE_PER_ACCESS = "int  0"
SCOPE_PER_REQUEST = "int  1"
SCOPE_SINGLETON = "int  2"
def ():
    '''returns WSDDDeployableItem\n\n
    ()\n
    (final Element e)\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def setQName():
    '''returns None\n\n
    setQName(final QName qname)\n
    '''
def getQName():
    '''returns QName\n\n
    getQName()\n
    '''
def getType():
    '''returns QName\n\n
    getType()\n
    '''
def setType():
    '''returns None\n\n
    setType(final QName type)\n
    '''
def setParameter():
    '''returns None\n\n
    setParameter(final String name, final String value)\n
    '''
def getParameter():
    '''returns String\n\n
    getParameter(final String name)\n
    '''
def getParametersTable():
    '''returns LockableHashtable\n\n
    getParametersTable()\n
    '''
def setOptionsHashtable():
    '''returns None\n\n
    setOptionsHashtable(final Hashtable hashtable)\n
    '''
def writeParamsToContext():
    '''returns None\n\n
    writeParamsToContext(final SerializationContext context)\n
    '''
def removeParameter():
    '''returns None\n\n
    removeParameter(final String name)\n
    '''
def getJavaClass():
    '''returns Class\n\n
    getJavaClass()\n
    '''
