SEND_TYPE_ATTR = "String  sendXsiTypes""
TRANSPORT_NAME = "String  transport_name""
CHARACTER_SET_ENCODING = "String  javax.xml.soap.character-set-encoding""
TRANSPORT_PROPERTY = "String  java.protocol.handler.pkgs""
WSDL_SERVICE = "String  wsdl.service""
WSDL_PORT_NAME = "String  wsdl.portName""
JAXRPC_SERVICE = "String  wsdl.service""
JAXRPC_PORTTYPE_NAME = "String  wsdl.portName""
FAULT_ON_NO_RESPONSE = "String  call.FaultOnNoResponse""
CHECK_MUST_UNDERSTAND = "String  call.CheckMustUnderstand""
ATTACHMENT_ENCAPSULATION_FORMAT = "String  attachment_encapsulation_format""
ATTACHMENT_ENCAPSULATION_FORMAT_MIME = "String  axis.attachment.style.mime""
ATTACHMENT_ENCAPSULATION_FORMAT_DIME = "String  axis.attachment.style.dime""
ATTACHMENT_ENCAPSULATION_FORMAT_MTOM = "String  axis.attachment.style.mtom""
CONNECTION_TIMEOUT_PROPERTY = "String  axis.connection.timeout""
STREAMING_PROPERTY = "String  axis.streaming""
def Call():
'''public Call(final Service service)
public Call(final String url)
public Call(final URL url)
'''
pass
def setProperty():
'''public void setProperty(final String name, final Object value)
'''
pass
def getProperty():
'''public Object getProperty(final String name)
'''
pass
def removeProperty():
'''public void removeProperty(final String name)
'''
pass
def getPropertyNames():
'''public Iterator getPropertyNames()
'''
pass
def isPropertySupported():
'''public boolean isPropertySupported(final String name)
'''
pass
def setUsername():
'''public void setUsername(final String username)
'''
pass
def getUsername():
'''public String getUsername()
'''
pass
def setPassword():
'''public void setPassword(final String password)
'''
pass
def getPassword():
'''public String getPassword()
'''
pass
def setMaintainSession():
'''public void setMaintainSession(final boolean yesno)
'''
pass
def getMaintainSession():
'''public boolean getMaintainSession()
'''
pass
def setOperationStyle():
'''public void setOperationStyle(final String operationStyle)
public void setOperationStyle(final Style operationStyle)
'''
pass
def getOperationStyle():
'''public Style getOperationStyle()
'''
pass
def setOperationUse():
'''public void setOperationUse(final String operationUse)
public void setOperationUse(final Use operationUse)
'''
pass
def getOperationUse():
'''public Use getOperationUse()
'''
pass
def setUseSOAPAction():
'''public void setUseSOAPAction(final boolean useSOAPAction)
'''
pass
def useSOAPAction():
'''public boolean useSOAPAction()
'''
pass
def setSOAPActionURI():
'''public void setSOAPActionURI(final String SOAPActionURI)
'''
pass
def getSOAPActionURI():
'''public String getSOAPActionURI()
'''
pass
def setEncodingStyle():
'''public void setEncodingStyle(final String namespaceURI)
'''
pass
def getEncodingStyle():
'''public String getEncodingStyle()
'''
pass
def setTargetEndpointAddress():
'''public void setTargetEndpointAddress(final String address)
public void setTargetEndpointAddress(final URL address)
'''
pass
def getTargetEndpointAddress():
'''public String getTargetEndpointAddress()
'''
pass
def getTimeout():
'''public Integer getTimeout()
'''
pass
def setTimeout():
'''public void setTimeout(final Integer timeout)
'''
pass
def getStreaming():
'''public boolean getStreaming()
'''
pass
def setStreaming():
'''public void setStreaming(final boolean useStreaming)
'''
pass
def isParameterAndReturnSpecRequired():
'''public boolean isParameterAndReturnSpecRequired(final QName operationName)
'''
pass
def addParameter():
'''public void addParameter(final QName paramName, final QName xmlType, final ParameterMode parameterMode)
public void addParameter(final QName paramName, final QName xmlType, final Class javaType, final ParameterMode parameterMode)
public void addParameter(final String paramName, final QName xmlType, final ParameterMode parameterMode)
public void addParameter(final String paramName, final QName xmlType, final Class javaType, final ParameterMode parameterMode)
'''
pass
def addParameterAsHeader():
'''public void addParameterAsHeader(final QName paramName, final QName xmlType, final ParameterMode parameterMode, final ParameterMode headerMode)
public void addParameterAsHeader(final QName paramName, final QName xmlType, final Class javaType, final ParameterMode parameterMode, final ParameterMode headerMode)
'''
pass
def getParameterTypeByName():
'''public QName getParameterTypeByName(final String paramName)
'''
pass
def getParameterTypeByQName():
'''public QName getParameterTypeByQName(final QName paramQName)
'''
pass
def setReturnType():
'''public void setReturnType(final QName type)
public void setReturnType(final QName xmlType, final Class javaType)
'''
pass
def setReturnTypeAsHeader():
'''public void setReturnTypeAsHeader(final QName xmlType)
public void setReturnTypeAsHeader(final QName xmlType, final Class javaType)
'''
pass
def getReturnType():
'''public QName getReturnType()
'''
pass
def setReturnQName():
'''public void setReturnQName(final QName qname)
'''
pass
def setReturnClass():
'''public void setReturnClass(final Class cls)
'''
pass
def removeAllParameters():
'''public void removeAllParameters()
'''
pass
def getOperationName():
'''public QName getOperationName()
'''
pass
def setOperationName():
'''public void setOperationName(final QName opName)
public void setOperationName(final String opName)
'''
pass
def setOperation():
'''public void setOperation(final String opName)
public void setOperation(final QName portName, final String opName)
public void setOperation(final QName portName, final QName opName)
public void setOperation(final OperationDesc operation)
'''
pass
def getPortName():
'''public QName getPortName()
'''
pass
def setPortName():
'''public void setPortName(final QName portName)
'''
pass
def getPortTypeName():
'''public QName getPortTypeName()
'''
pass
def setPortTypeName():
'''public void setPortTypeName(final QName portType)
'''
pass
def setSOAPVersion():
'''public void setSOAPVersion(final SOAPConstants soapConstants)
'''
pass
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
pass
def invokeOneWay():
'''public void invokeOneWay(final Object[] params)
'''
pass
def setTransportForProtocol():
'''public static void setTransportForProtocol(final String protocol, final Class transportClass)
'''
pass
def initialize():
'''public static synchronized void initialize()
'''
pass
def addTransportPackage():
'''public static synchronized void addTransportPackage(final String packageName)
'''
pass
def run():
'''public Object run()
public void run()
'''
pass
def setTransport():
'''public void setTransport(final Transport trans)
'''
pass
def getTransportForProtocol():
'''public Transport getTransportForProtocol(final String protocol)
'''
pass
def setRequestMessage():
'''public void setRequestMessage(final Message msg)
'''
pass
def getResponseMessage():
'''public Message getResponseMessage()
'''
pass
def getMessageContext():
'''public MessageContext getMessageContext()
'''
pass
def addHeader():
'''public void addHeader(final SOAPHeaderElement header)
'''
pass
def clearHeaders():
'''public void clearHeaders()
'''
pass
def getTypeMapping():
'''public TypeMapping getTypeMapping()
'''
pass
def registerTypeMapping():
'''public void registerTypeMapping(final Class javaType, final QName xmlType, final SerializerFactory sf, final DeserializerFactory df)
public void registerTypeMapping(final Class javaType, final QName xmlType, final SerializerFactory sf, final DeserializerFactory df, final boolean force)
public void registerTypeMapping(final Class javaType, final QName xmlType, final Class sfClass, final Class dfClass)
public void registerTypeMapping(final Class javaType, final QName xmlType, final Class sfClass, final Class dfClass, final boolean force)
'''
pass
def setOption():
'''public void setOption(final String name, final Object value)
'''
pass
def getOutputParams():
'''public Map getOutputParams()
'''
pass
def getOutputValues():
'''public List getOutputValues()
'''
pass
def getService():
'''public Service getService()
'''
pass
def setSOAPService():
'''public void setSOAPService(final SOAPService service)
'''
pass
def setClientHandlers():
'''public void setClientHandlers(final Handler reqHandler, final Handler respHandler)
'''
pass
def addAttachmentPart():
'''public void addAttachmentPart(final Object attachment)
'''
pass
def addFault():
'''public void addFault(final QName qname, final Class cls, final QName xmlType, final boolean isComplex)
'''
pass
def getOperation():
'''public OperationDesc getOperation()
'''
pass
def clearOperation():
'''public void clearOperation()
'''
pass
