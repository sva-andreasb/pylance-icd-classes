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
def ():
    '''returns Call\n\n
    (final Service service)\n
    (final String url)\n
    (final URL url)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String name, final Object value)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String name)\n
    '''
def removeProperty():
    '''returns None\n\n
    removeProperty(final String name)\n
    '''
def getPropertyNames():
    '''returns Iterator\n\n
    getPropertyNames()\n
    '''
def isPropertySupported():
    '''returns boolean\n\n
    isPropertySupported(final String name)\n
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
def setMaintainSession():
    '''returns None\n\n
    setMaintainSession(final boolean yesno)\n
    '''
def getMaintainSession():
    '''returns boolean\n\n
    getMaintainSession()\n
    '''
def setOperationStyle():
    '''returns None\n\n
    setOperationStyle(final String operationStyle)\n
    setOperationStyle(final Style operationStyle)\n
    '''
def getOperationStyle():
    '''returns Style\n\n
    getOperationStyle()\n
    '''
def setOperationUse():
    '''returns None\n\n
    setOperationUse(final String operationUse)\n
    setOperationUse(final Use operationUse)\n
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
    setEncodingStyle(final String namespaceURI)\n
    '''
def getEncodingStyle():
    '''returns String\n\n
    getEncodingStyle()\n
    '''
def setTargetEndpointAddress():
    '''returns None\n\n
    setTargetEndpointAddress(final String address)\n
    setTargetEndpointAddress(final URL address)\n
    '''
def getTargetEndpointAddress():
    '''returns String\n\n
    getTargetEndpointAddress()\n
    '''
def getTimeout():
    '''returns Integer\n\n
    getTimeout()\n
    '''
def setTimeout():
    '''returns None\n\n
    setTimeout(final Integer timeout)\n
    '''
def getStreaming():
    '''returns boolean\n\n
    getStreaming()\n
    '''
def setStreaming():
    '''returns None\n\n
    setStreaming(final boolean useStreaming)\n
    '''
def isParameterAndReturnSpecRequired():
    '''returns boolean\n\n
    isParameterAndReturnSpecRequired(final QName operationName)\n
    '''
def addParameter():
    '''returns None\n\n
    addParameter(final QName paramName, final QName xmlType, final ParameterMode parameterMode)\n
    addParameter(final QName paramName, final QName xmlType, final Class javaType, final ParameterMode parameterMode)\n
    addParameter(final String paramName, final QName xmlType, final ParameterMode parameterMode)\n
    addParameter(final String paramName, final QName xmlType, final Class javaType, final ParameterMode parameterMode)\n
    '''
def addParameterAsHeader():
    '''returns None\n\n
    addParameterAsHeader(final QName paramName, final QName xmlType, final ParameterMode parameterMode, final ParameterMode headerMode)\n
    addParameterAsHeader(final QName paramName, final QName xmlType, final Class javaType, final ParameterMode parameterMode, final ParameterMode headerMode)\n
    '''
def getParameterTypeByName():
    '''returns QName\n\n
    getParameterTypeByName(final String paramName)\n
    '''
def getParameterTypeByQName():
    '''returns QName\n\n
    getParameterTypeByQName(final QName paramQName)\n
    '''
def setReturnType():
    '''returns None\n\n
    setReturnType(final QName type)\n
    setReturnType(final QName xmlType, final Class javaType)\n
    '''
def setReturnTypeAsHeader():
    '''returns None\n\n
    setReturnTypeAsHeader(final QName xmlType)\n
    setReturnTypeAsHeader(final QName xmlType, final Class javaType)\n
    '''
def getReturnType():
    '''returns QName\n\n
    getReturnType()\n
    '''
def setReturnQName():
    '''returns None\n\n
    setReturnQName(final QName qname)\n
    '''
def setReturnClass():
    '''returns None\n\n
    setReturnClass(final Class cls)\n
    '''
def removeAllParameters():
    '''returns None\n\n
    removeAllParameters()\n
    '''
def getOperationName():
    '''returns QName\n\n
    getOperationName()\n
    '''
def setOperationName():
    '''returns None\n\n
    setOperationName(final QName opName)\n
    setOperationName(final String opName)\n
    '''
def setOperation():
    '''returns None\n\n
    setOperation(final String opName)\n
    setOperation(final QName portName, final String opName)\n
    setOperation(final QName portName, final QName opName)\n
    setOperation(final OperationDesc operation)\n
    '''
def getPortName():
    '''returns QName\n\n
    getPortName()\n
    '''
def setPortName():
    '''returns None\n\n
    setPortName(final QName portName)\n
    '''
def getPortTypeName():
    '''returns QName\n\n
    getPortTypeName()\n
    '''
def setPortTypeName():
    '''returns None\n\n
    setPortTypeName(final QName portType)\n
    '''
def setSOAPVersion():
    '''returns None\n\n
    setSOAPVersion(final SOAPConstants soapConstants)\n
    '''
def invoke():
    '''returns None\n\n
    invoke(final QName operationName, final Object[] params)\n
    invoke(final Object[] params)\n
    invoke(Message msg)\n
    invoke(final SOAPEnvelope env)\n
    invoke(final String namespace, final String method, final Object[] args)\n
    invoke(final String method, final Object[] args)\n
    invoke(final RPCElement body)\n
    invoke()\n
    '''
def invokeOneWay():
    '''returns None\n\n
    invokeOneWay(final Object[] params)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    '''
def setTransport():
    '''returns None\n\n
    setTransport(final Transport trans)\n
    '''
def getTransportForProtocol():
    '''returns Transport\n\n
    getTransportForProtocol(final String protocol)\n
    '''
def setRequestMessage():
    '''returns None\n\n
    setRequestMessage(final Message msg)\n
    '''
def getResponseMessage():
    '''returns Message\n\n
    getResponseMessage()\n
    '''
def getMessageContext():
    '''returns MessageContext\n\n
    getMessageContext()\n
    '''
def addHeader():
    '''returns None\n\n
    addHeader(final SOAPHeaderElement header)\n
    '''
def clearHeaders():
    '''returns None\n\n
    clearHeaders()\n
    '''
def getTypeMapping():
    '''returns TypeMapping\n\n
    getTypeMapping()\n
    '''
def registerTypeMapping():
    '''returns None\n\n
    registerTypeMapping(final Class javaType, final QName xmlType, final SerializerFactory sf, final DeserializerFactory df)\n
    registerTypeMapping(final Class javaType, final QName xmlType, final SerializerFactory sf, final DeserializerFactory df, final boolean force)\n
    registerTypeMapping(final Class javaType, final QName xmlType, final Class sfClass, final Class dfClass)\n
    registerTypeMapping(final Class javaType, final QName xmlType, final Class sfClass, final Class dfClass, final boolean force)\n
    '''
def setOption():
    '''returns None\n\n
    setOption(final String name, final Object value)\n
    '''
def getOutputParams():
    '''returns Map\n\n
    getOutputParams()\n
    '''
def getOutputValues():
    '''returns List\n\n
    getOutputValues()\n
    '''
def getService():
    '''returns Service\n\n
    getService()\n
    '''
def setSOAPService():
    '''returns None\n\n
    setSOAPService(final SOAPService service)\n
    '''
def setClientHandlers():
    '''returns None\n\n
    setClientHandlers(final Handler reqHandler, final Handler respHandler)\n
    '''
def addAttachmentPart():
    '''returns None\n\n
    addAttachmentPart(final Object attachment)\n
    '''
def addFault():
    '''returns None\n\n
    addFault(final QName qname, final Class cls, final QName xmlType, final boolean isComplex)\n
    '''
def getOperation():
    '''returns OperationDesc\n\n
    getOperation()\n
    '''
def clearOperation():
    '''returns None\n\n
    clearOperation()\n
    '''
