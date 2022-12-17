def ():
    '''returns JavaServiceDesc\n\n
    ()\n
    '''
def getStyle():
    '''returns Style\n\n
    getStyle()\n
    '''
def setStyle():
    '''returns None\n\n
    setStyle(final Style style)\n
    '''
def getUse():
    '''returns Use\n\n
    getUse()\n
    '''
def setUse():
    '''returns None\n\n
    setUse(final Use use)\n
    '''
def isWrapped():
    '''returns boolean\n\n
    isWrapped()\n
    '''
def getWSDLFile():
    '''returns String\n\n
    getWSDLFile()\n
    '''
def setWSDLFile():
    '''returns None\n\n
    setWSDLFile(final String wsdlFileName)\n
    '''
def getAllowedMethods():
    '''returns List\n\n
    getAllowedMethods()\n
    '''
def setAllowedMethods():
    '''returns None\n\n
    setAllowedMethods(final List allowedMethods)\n
    '''
def getImplClass():
    '''returns Class\n\n
    getImplClass()\n
    '''
def setImplClass():
    '''returns None\n\n
    setImplClass(final Class implClass)\n
    '''
def getTypeMapping():
    '''returns TypeMapping\n\n
    getTypeMapping()\n
    '''
def setTypeMapping():
    '''returns None\n\n
    setTypeMapping(final TypeMapping tm)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def getDocumentation():
    '''returns String\n\n
    getDocumentation()\n
    '''
def setDocumentation():
    '''returns None\n\n
    setDocumentation(final String documentation)\n
    '''
def getStopClasses():
    '''returns ArrayList\n\n
    getStopClasses()\n
    '''
def setStopClasses():
    '''returns None\n\n
    setStopClasses(final ArrayList stopClasses)\n
    '''
def getDisallowedMethods():
    '''returns List\n\n
    getDisallowedMethods()\n
    '''
def setDisallowedMethods():
    '''returns None\n\n
    setDisallowedMethods(final List disallowedMethods)\n
    '''
def removeOperationDesc():
    '''returns None\n\n
    removeOperationDesc(final OperationDesc operation)\n
    '''
def addOperationDesc():
    '''returns None\n\n
    addOperationDesc(final OperationDesc operation)\n
    '''
def getOperations():
    '''returns ArrayList\n\n
    getOperations()\n
    '''
def getOperationsByName():
    '''returns OperationDesc[]\n\n
    getOperationsByName(final String methodName)\n
    '''
def getOperationByName():
    '''returns OperationDesc\n\n
    getOperationByName(final String methodName)\n
    '''
def getOperationByElementQName():
    '''returns OperationDesc\n\n
    getOperationByElementQName(final QName qname)\n
    '''
def getOperationsByQName():
    '''returns OperationDesc[]\n\n
    getOperationsByQName(final QName qname)\n
    '''
def compare():
    '''returns int\n\n
    compare(final Object o1, final Object o2)\n
    '''
def loadServiceDescByIntrospection():
    '''returns None\n\n
    loadServiceDescByIntrospection()\n
    loadServiceDescByIntrospection(final Class implClass)\n
    loadServiceDescByIntrospection(final Class cls, final TypeMapping tm)\n
    '''
def setNamespaceMappings():
    '''returns None\n\n
    setNamespaceMappings(final List namespaces)\n
    '''
def getDefaultNamespace():
    '''returns String\n\n
    getDefaultNamespace()\n
    '''
def setDefaultNamespace():
    '''returns None\n\n
    setDefaultNamespace(final String namespace)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String name, final Object value)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String name)\n
    '''
def getEndpointURL():
    '''returns String\n\n
    getEndpointURL()\n
    '''
def setEndpointURL():
    '''returns None\n\n
    setEndpointURL(final String endpointURL)\n
    '''
def getTypeMappingRegistry():
    '''returns TypeMappingRegistry\n\n
    getTypeMappingRegistry()\n
    '''
def setTypeMappingRegistry():
    '''returns None\n\n
    setTypeMappingRegistry(final TypeMappingRegistry tmr)\n
    '''
def isInitialized():
    '''returns boolean\n\n
    isInitialized()\n
    '''
