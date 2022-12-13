SEND_TYPE_ATTR = "String  \"sendXsiTypes\""
TRANSPORT_NAME = "String  \"transport_name\""
CHARACTER_SET_ENCODING = "String  \"javax.xml.soap.character-set-encoding\""
TRANSPORT_PROPERTY = "String  \"java.protocol.handler.pkgs\""
WSDL_SERVICE = "String  \"wsdl.service\""
WSDL_PORT_NAME = "String  \"wsdl.portName\""
JAXRPC_SERVICE = "String  \"wsdl.service\""
JAXRPC_PORTTYPE_NAME = "String  \"wsdl.portName\""
FAULT_ON_NO_RESPONSE = "String  \"call.FaultOnNoResponse\""
CHECK_MUST_UNDERSTAND = "String  \"call.CheckMustUnderstand\""
ATTACHMENT_ENCAPSULATION_FORMAT = "String  \"attachment_encapsulation_format\""
ATTACHMENT_ENCAPSULATION_FORMAT_MIME = "String  \"axis.attachment.style.mime\""
ATTACHMENT_ENCAPSULATION_FORMAT_DIME = "String  \"axis.attachment.style.dime\""
ATTACHMENT_ENCAPSULATION_FORMAT_MTOM = "String  \"axis.attachment.style.mtom\""
CONNECTION_TIMEOUT_PROPERTY = "String  \"axis.connection.timeout\""
STREAMING_PROPERTY = "String  \"axis.streaming\""
def Call():
    '''public Call(final Service service)
    public Call(final String url)
    public Call(final URL url)
    '''
def setProperty():
    '''public void setProperty(final String name, final Object value)
    '''
def getProperty():
    '''public Object getProperty(final String name)
    '''
def removeProperty():
    '''public void removeProperty(final String name)
    '''
def getPropertyNames():
    '''public Iterator getPropertyNames()
    '''
def isPropertySupported():
    '''public boolean isPropertySupported(final String name)
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
def setMaintainSession():
    '''public void setMaintainSession(final boolean yesno)
    '''
def getMaintainSession():
    '''public boolean getMaintainSession()
    '''
def setOperationStyle():
    '''public void setOperationStyle(final String operationStyle)
    public void setOperationStyle(final Style operationStyle)
    '''
def getOperationStyle():
    '''public Style getOperationStyle()
    '''
def setOperationUse():
    '''public void setOperationUse(final String operationUse)
    public void setOperationUse(final Use operationUse)
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
    '''public void setEncodingStyle(final String namespaceURI)
    '''
def getEncodingStyle():
    '''public String getEncodingStyle()
    '''
def setTargetEndpointAddress():
    '''public void setTargetEndpointAddress(final String address)
    public void setTargetEndpointAddress(final URL address)
    '''
def getTargetEndpointAddress():
    '''public String getTargetEndpointAddress()
    '''
def getTimeout():
    '''public Integer getTimeout()
    '''
def setTimeout():
    '''public void setTimeout(final Integer timeout)
    '''
def getStreaming():
    '''public boolean getStreaming()
    '''
def setStreaming():
    '''public void setStreaming(final boolean useStreaming)
    '''
def isParameterAndReturnSpecRequired():
    '''public boolean isParameterAndReturnSpecRequired(final QName operationName)
    '''
def addParameter():
    '''public void addParameter(final QName paramName, final QName xmlType, final ParameterMode parameterMode)
    public void addParameter(final QName paramName, final QName xmlType, final Class javaType, final ParameterMode parameterMode)
    public void addParameter(final String paramName, final QName xmlType, final ParameterMode parameterMode)
    public void addParameter(final String paramName, final QName xmlType, final Class javaType, final ParameterMode parameterMode)
    '''
def addParameterAsHeader():
    '''public void addParameterAsHeader(final QName paramName, final QName xmlType, final ParameterMode parameterMode, final ParameterMode headerMode)
    public void addParameterAsHeader(final QName paramName, final QName xmlType, final Class javaType, final ParameterMode parameterMode, final ParameterMode headerMode)
    '''
def getParameterTypeByName():
    '''public QName getParameterTypeByName(final String paramName)
    '''
def getParameterTypeByQName():
    '''public QName getParameterTypeByQName(final QName paramQName)
    '''
def setReturnType():
    '''public void setReturnType(final QName type)
    public void setReturnType(final QName xmlType, final Class javaType)
    '''
def setReturnTypeAsHeader():
    '''public void setReturnTypeAsHeader(final QName xmlType)
    public void setReturnTypeAsHeader(final QName xmlType, final Class javaType)
    '''
def getReturnType():
    '''public QName getReturnType()
    '''
def setReturnQName():
    '''public void setReturnQName(final QName qname)
    '''
def setReturnClass():
    '''public void setReturnClass(final Class cls)
    '''
def removeAllParameters():
    '''public void removeAllParameters()
    '''
def getOperationName():
    '''public QName getOperationName()
    '''
def setOperationName():
    '''public void setOperationName(final QName opName)
    public void setOperationName(final String opName)
    '''
def setOperation():
    '''public void setOperation(final String opName)
    public void setOperation(final QName portName, final String opName)
    public void setOperation(final QName portName, final QName opName)
    public void setOperation(final OperationDesc operation)
    '''
def getPortName():
    '''public QName getPortName()
    '''
def setPortName():
    '''public void setPortName(final QName portName)
    '''
def getPortTypeName():
    '''public QName getPortTypeName()
    '''
def setPortTypeName():
    '''public void setPortTypeName(final QName portType)
    '''
def setSOAPVersion():
    '''public void setSOAPVersion(final SOAPConstants soapConstants)
    '''
def invoke():
    '''public Object invoke(final QName operationName, final Object[] params)
    public Object invoke(final Object[] params)
    public SOAPEnvelope invoke(Message msg)
    public SOAPEnvelope invoke(final SOAPEnvelope env)
    public Object invoke(final String namespace, final String method, final Object[] args)
    public Object invoke(final String method, final Object[] args)
    public Object invoke(final RPCElement body)
    public void invoke()
    '''
def invokeOneWay():
    '''public void invokeOneWay(final Object[] params)
    '''
def setTransportForProtocol():
    '''public static void setTransportForProtocol(final String protocol, final Class transportClass)
    '''
def initialize():
    '''public static synchronized void initialize()
    '''
def addTransportPackage():
    '''public static synchronized void addTransportPackage(final String packageName)
    '''
def run():
    '''public Object run()
    public void run()
    '''
def setTransport():
    '''public void setTransport(final Transport trans)
    '''
def getTransportForProtocol():
    '''public Transport getTransportForProtocol(final String protocol)
    '''
def setRequestMessage():
    '''public void setRequestMessage(final Message msg)
    '''
def getResponseMessage():
    '''public Message getResponseMessage()
    '''
def getMessageContext():
    '''public MessageContext getMessageContext()
    '''
def addHeader():
    '''public void addHeader(final SOAPHeaderElement header)
    '''
def clearHeaders():
    '''public void clearHeaders()
    '''
def getTypeMapping():
    '''public TypeMapping getTypeMapping()
    '''
def registerTypeMapping():
    '''public void registerTypeMapping(final Class javaType, final QName xmlType, final SerializerFactory sf, final DeserializerFactory df)
    public void registerTypeMapping(final Class javaType, final QName xmlType, final SerializerFactory sf, final DeserializerFactory df, final boolean force)
    public void registerTypeMapping(final Class javaType, final QName xmlType, final Class sfClass, final Class dfClass)
    public void registerTypeMapping(final Class javaType, final QName xmlType, final Class sfClass, final Class dfClass, final boolean force)
    '''
def setOption():
    '''public void setOption(final String name, final Object value)
    '''
def getOutputParams():
    '''public Map getOutputParams()
    '''
def getOutputValues():
    '''public List getOutputValues()
    '''
def getService():
    '''public Service getService()
    '''
def setSOAPService():
    '''public void setSOAPService(final SOAPService service)
    '''
def setClientHandlers():
    '''public void setClientHandlers(final Handler reqHandler, final Handler respHandler)
    '''
def addAttachmentPart():
    '''public void addAttachmentPart(final Object attachment)
    '''
def addFault():
    '''public void addFault(final QName qname, final Class cls, final QName xmlType, final boolean isComplex)
    '''
def getOperation():
    '''public OperationDesc getOperation()
    '''
def clearOperation():
    '''public void clearOperation()
    '''
