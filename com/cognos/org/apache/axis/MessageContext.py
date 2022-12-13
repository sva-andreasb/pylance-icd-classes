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
    '''public OperationDesc getOperation()
    '''
def setOperation():
    '''public void setOperation(final OperationDesc operation)
    '''
def getPossibleOperationsByQName():
    '''public OperationDesc[] getPossibleOperationsByQName(final QName qname)
    '''
def getOperationByQName():
    '''public OperationDesc getOperationByQName(final QName qname)
    '''
def getCurrentContext():
    '''public static MessageContext getCurrentContext()
    '''
def MessageContext():
    '''public MessageContext(final AxisEngine engine)
    '''
def setTypeMappingRegistry():
    '''public void setTypeMappingRegistry(final TypeMappingRegistry reg)
    '''
def getTypeMappingRegistry():
    '''public TypeMappingRegistry getTypeMappingRegistry()
    '''
def getTypeMapping():
    '''public TypeMapping getTypeMapping()
    '''
def getTransportName():
    '''public String getTransportName()
    '''
def setTransportName():
    '''public void setTransportName(final String transportName)
    '''
def getSOAPConstants():
    '''public SOAPConstants getSOAPConstants()
    '''
def setSOAPConstants():
    '''public void setSOAPConstants(final SOAPConstants soapConstants)
    '''
def getSchemaVersion():
    '''public SchemaVersion getSchemaVersion()
    '''
def setSchemaVersion():
    '''public void setSchemaVersion(final SchemaVersion schemaVersion)
    '''
def getSession():
    '''public Session getSession()
    '''
def setSession():
    '''public void setSession(final Session session)
    '''
def isEncoded():
    '''public boolean isEncoded()
    '''
def setMaintainSession():
    '''public void setMaintainSession(final boolean yesno)
    '''
def getMaintainSession():
    '''public boolean getMaintainSession()
    '''
def getRequestMessage():
    '''public Message getRequestMessage()
    '''
def setRequestMessage():
    '''public void setRequestMessage(final Message reqMsg)
    '''
def getResponseMessage():
    '''public Message getResponseMessage()
    '''
def setResponseMessage():
    '''public void setResponseMessage(final Message respMsg)
    '''
def getCurrentMessage():
    '''public Message getCurrentMessage()
    '''
def getMessage():
    '''public SOAPMessage getMessage()
    '''
def setCurrentMessage():
    '''public void setCurrentMessage(final Message curMsg)
    '''
def setMessage():
    '''public void setMessage(final SOAPMessage message)
    '''
def getPastPivot():
    '''public boolean getPastPivot()
    '''
def setPastPivot():
    '''public void setPastPivot(final boolean pastPivot)
    '''
def setTimeout():
    '''public void setTimeout(final int value)
    '''
def getTimeout():
    '''public int getTimeout()
    '''
def getClassLoader():
    '''public ClassLoader getClassLoader()
    '''
def setClassLoader():
    '''public void setClassLoader(final ClassLoader cl)
    '''
def getTargetService():
    '''public String getTargetService()
    '''
def getAxisEngine():
    '''public AxisEngine getAxisEngine()
    '''
def setTargetService():
    '''public void setTargetService(final String tServ)
    '''
def getService():
    '''public SOAPService getService()
    '''
def setService():
    '''public void setService(final SOAPService sh)
    '''
def isClient():
    '''public boolean isClient()
    '''
def getStrProp():
    '''public String getStrProp(final String propName)
    '''
def isPropertyTrue():
    '''public boolean isPropertyTrue(final String propName)
    public boolean isPropertyTrue(final String propName, final boolean defaultVal)
    '''
def setProperty():
    '''public void setProperty(final String name, final Object value)
    '''
def containsProperty():
    '''public boolean containsProperty(final String name)
    '''
def getPropertyNames():
    '''public Iterator getPropertyNames()
    '''
def getAllPropertyNames():
    '''public Iterator getAllPropertyNames()
    '''
def getProperty():
    '''public Object getProperty(final String name)
    '''
def setPropertyParent():
    '''public void setPropertyParent(final Hashtable parent)
    '''
def setUsername():
    '''public void setUsername(final String username)
    '''
def getUsername():
    '''public String getUsername()
    '''
def setPassword():
    '''public void setPassword(final String password)
    '''
def getPassword():
    '''public String getPassword()
    '''
def getOperationStyle():
    '''public Style getOperationStyle()
    '''
def getOperationUse():
    '''public Use getOperationUse()
    '''
def setUseSOAPAction():
    '''public void setUseSOAPAction(final boolean useSOAPAction)
    '''
def useSOAPAction():
    '''public boolean useSOAPAction()
    '''
def setSOAPActionURI():
    '''public void setSOAPActionURI(final String SOAPActionURI)
    '''
def getSOAPActionURI():
    '''public String getSOAPActionURI()
    '''
def setEncodingStyle():
    '''public void setEncodingStyle(String namespaceURI)
    '''
def getEncodingStyle():
    '''public String getEncodingStyle()
    '''
def removeProperty():
    '''public void removeProperty(final String propName)
    '''
def reset():
    '''public void reset()
    '''
def isHighFidelity():
    '''public boolean isHighFidelity()
    '''
def setHighFidelity():
    '''public void setHighFidelity(final boolean highFidelity)
    '''
def getRoles():
    '''public String[] getRoles()
    '''
def setRoles():
    '''public void setRoles(final String[] roles)
    '''
def dispose():
    '''public synchronized void dispose()
    '''
