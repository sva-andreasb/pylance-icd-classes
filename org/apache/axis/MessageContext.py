ENGINE_HANDLER = "String  \"engine.handler\""
TRANS_URL = "String  \"transport.url\""
QUIT_REQUESTED = "String  \"quit.requested\""
AUTHUSER = "String  \"authenticatedUser\""
CALL = "String  \"call_object\""
IS_MSG = "String  \"isMsg\""
ATTACHMENTS_DIR = "String  \"attachments.directory\""
ACCEPTMISSINGPARAMS = "String  \"acceptMissingParams\""
WSDLGEN_INTFNAMESPACE = "String  \"axis.wsdlgen.intfnamespace\""
WSDLGEN_SERV_LOC_URL = "String  \"axis.wsdlgen.serv.loc.url\""
HTTP_TRANSPORT_VERSION = "String  \"axis.transport.version\""
SECURITY_PROVIDER = "String  \"securityProvider\""
def getOperation():
    '''returns OperationDesc\n\n
    getOperation()\n
    '''
def setOperation():
    '''returns None\n\n
    setOperation(final OperationDesc operation)\n
    '''
def getPossibleOperationsByQName():
    '''returns OperationDesc[]\n\n
    getPossibleOperationsByQName(final QName qname)\n
    '''
def getOperationByQName():
    '''returns OperationDesc\n\n
    getOperationByQName(final QName qname)\n
    '''
def ():
    '''returns MessageContext\n\n
    (final AxisEngine engine)\n
    '''
def setTypeMappingRegistry():
    '''returns None\n\n
    setTypeMappingRegistry(final TypeMappingRegistry reg)\n
    '''
def getTypeMappingRegistry():
    '''returns TypeMappingRegistry\n\n
    getTypeMappingRegistry()\n
    '''
def getTypeMapping():
    '''returns TypeMapping\n\n
    getTypeMapping()\n
    '''
def getTransportName():
    '''returns String\n\n
    getTransportName()\n
    '''
def setTransportName():
    '''returns None\n\n
    setTransportName(final String transportName)\n
    '''
def getSOAPConstants():
    '''returns SOAPConstants\n\n
    getSOAPConstants()\n
    '''
def setSOAPConstants():
    '''returns None\n\n
    setSOAPConstants(final SOAPConstants soapConstants)\n
    '''
def getSchemaVersion():
    '''returns SchemaVersion\n\n
    getSchemaVersion()\n
    '''
def setSchemaVersion():
    '''returns None\n\n
    setSchemaVersion(final SchemaVersion schemaVersion)\n
    '''
def getSession():
    '''returns Session\n\n
    getSession()\n
    '''
def setSession():
    '''returns None\n\n
    setSession(final Session session)\n
    '''
def isEncoded():
    '''returns boolean\n\n
    isEncoded()\n
    '''
def setMaintainSession():
    '''returns None\n\n
    setMaintainSession(final boolean yesno)\n
    '''
def getMaintainSession():
    '''returns boolean\n\n
    getMaintainSession()\n
    '''
def getRequestMessage():
    '''returns Message\n\n
    getRequestMessage()\n
    '''
def setRequestMessage():
    '''returns None\n\n
    setRequestMessage(final Message reqMsg)\n
    '''
def getResponseMessage():
    '''returns Message\n\n
    getResponseMessage()\n
    '''
def setResponseMessage():
    '''returns None\n\n
    setResponseMessage(final Message respMsg)\n
    '''
def getCurrentMessage():
    '''returns Message\n\n
    getCurrentMessage()\n
    '''
def getMessage():
    '''returns SOAPMessage\n\n
    getMessage()\n
    '''
def setCurrentMessage():
    '''returns None\n\n
    setCurrentMessage(final Message curMsg)\n
    '''
def setMessage():
    '''returns None\n\n
    setMessage(final SOAPMessage message)\n
    '''
def getPastPivot():
    '''returns boolean\n\n
    getPastPivot()\n
    '''
def setPastPivot():
    '''returns None\n\n
    setPastPivot(final boolean pastPivot)\n
    '''
def setTimeout():
    '''returns None\n\n
    setTimeout(final int value)\n
    '''
def getTimeout():
    '''returns int\n\n
    getTimeout()\n
    '''
def getClassLoader():
    '''returns ClassLoader\n\n
    getClassLoader()\n
    '''
def setClassLoader():
    '''returns None\n\n
    setClassLoader(final ClassLoader cl)\n
    '''
def getTargetService():
    '''returns String\n\n
    getTargetService()\n
    '''
def getAxisEngine():
    '''returns AxisEngine\n\n
    getAxisEngine()\n
    '''
def setTargetService():
    '''returns None\n\n
    setTargetService(final String tServ)\n
    '''
def getService():
    '''returns SOAPService\n\n
    getService()\n
    '''
def setService():
    '''returns None\n\n
    setService(final SOAPService sh)\n
    '''
def isClient():
    '''returns boolean\n\n
    isClient()\n
    '''
def getStrProp():
    '''returns String\n\n
    getStrProp(final String propName)\n
    '''
def isPropertyTrue():
    '''returns boolean\n\n
    isPropertyTrue(final String propName)\n
    isPropertyTrue(final String propName, final boolean defaultVal)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String name, final Object value)\n
    '''
def containsProperty():
    '''returns boolean\n\n
    containsProperty(final String name)\n
    '''
def getPropertyNames():
    '''returns Iterator\n\n
    getPropertyNames()\n
    '''
def getAllPropertyNames():
    '''returns Iterator\n\n
    getAllPropertyNames()\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String name)\n
    '''
def setPropertyParent():
    '''returns None\n\n
    setPropertyParent(final Hashtable parent)\n
    '''
def setUsername():
    '''returns None\n\n
    setUsername(final String username)\n
    '''
def getUsername():
    '''returns String\n\n
    getUsername()\n
    '''
def setPassword():
    '''returns None\n\n
    setPassword(final String password)\n
    '''
def getPassword():
    '''returns String\n\n
    getPassword()\n
    '''
def getOperationStyle():
    '''returns Style\n\n
    getOperationStyle()\n
    '''
def getOperationUse():
    '''returns Use\n\n
    getOperationUse()\n
    '''
def setUseSOAPAction():
    '''returns None\n\n
    setUseSOAPAction(final boolean useSOAPAction)\n
    '''
def useSOAPAction():
    '''returns boolean\n\n
    useSOAPAction()\n
    '''
def setSOAPActionURI():
    '''returns None\n\n
    setSOAPActionURI(final String SOAPActionURI)\n
    '''
def getSOAPActionURI():
    '''returns String\n\n
    getSOAPActionURI()\n
    '''
def setEncodingStyle():
    '''returns None\n\n
    setEncodingStyle(String namespaceURI)\n
    '''
def getEncodingStyle():
    '''returns String\n\n
    getEncodingStyle()\n
    '''
def removeProperty():
    '''returns None\n\n
    removeProperty(final String propName)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def isHighFidelity():
    '''returns boolean\n\n
    isHighFidelity()\n
    '''
def setHighFidelity():
    '''returns None\n\n
    setHighFidelity(final boolean highFidelity)\n
    '''
def getRoles():
    '''returns String[]\n\n
    getRoles()\n
    '''
def setRoles():
    '''returns None\n\n
    setRoles(final String[] roles)\n
    '''
