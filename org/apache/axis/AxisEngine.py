PROP_XML_DECL = "String  sendXMLDeclaration""
PROP_DEBUG_LEVEL = "String  debugLevel""
PROP_DEBUG_FILE = "String  debugFile""
PROP_DOMULTIREFS = "String  sendMultiRefs""
PROP_DISABLE_PRETTY_XML = "String  disablePrettyXML""
PROP_ENABLE_NAMESPACE_PREFIX_OPTIMIZATION = "String  enableNamespacePrefixOptimization""
PROP_PASSWORD = "String  adminPassword""
PROP_SYNC_CONFIG = "String  syncConfiguration""
PROP_SEND_XSI = "String  sendXsiTypes""
PROP_ATTACHMENT_DIR = "String  attachments.Directory""
PROP_ATTACHMENT_IMPLEMENTATION = "String  attachments.implementation""
PROP_ATTACHMENT_CLEANUP = "String  attachment.DirectoryCleanUp""
PROP_DEFAULT_CONFIG_CLASS = "String  axis.engineConfigClass""
PROP_SOAP_VERSION = "String  defaultSOAPVersion""
PROP_SOAP_ALLOWED_VERSION = "String  singleSOAPVersion""
PROP_TWOD_ARRAY_ENCODING = "String  enable2DArrayEncoding""
PROP_XML_ENCODING = "String  axis.xmlEncoding""
PROP_XML_REUSE_SAX_PARSERS = "String  axis.xml.reuseParsers""
PROP_BYTE_BUFFER_BACKING = "String  axis.byteBuffer.backing""
PROP_BYTE_BUFFER_CACHE_INCREMENT = "String  axis.byteBuffer.cacheIncrement""
PROP_BYTE_BUFFER_RESIDENT_MAX_SIZE = "String  axis.byteBuffer.residentMaxSize""
PROP_BYTE_BUFFER_WORK_BUFFER_SIZE = "String  axis.byteBuffer.workBufferSize""
PROP_EMIT_ALL_TYPES = "String  emitAllTypesInWSDL""
PROP_DOTNET_SOAPENC_FIX = "String  dotNetSoapEncFix""
PROP_BP10_COMPLIANCE = "String  ws-i.bp10Compliance""
DEFAULT_ATTACHMENT_IMPL = "String  org.apache.axis.attachments.AttachmentsImpl""
ENV_ATTACHMENT_DIR = "String  axis.attachments.Directory""
ENV_SERVLET_REALPATH = "String  servlet.realpath""
ENV_SERVLET_CONTEXT = "String  servletContext""
def getCurrentMessageContext():
'''public static MessageContext getCurrentMessageContext()
'''
pass
def AxisEngine():
'''public AxisEngine(final EngineConfiguration config)
'''
pass
def init():
'''public void init()
'''
pass
def cleanup():
'''public void cleanup()
'''
pass
def saveConfiguration():
'''public void saveConfiguration()
'''
pass
def getConfig():
'''public EngineConfiguration getConfig()
'''
pass
def hasSafePassword():
'''public boolean hasSafePassword()
'''
pass
def setAdminPassword():
'''public void setAdminPassword(final String pw)
'''
pass
def setShouldSaveConfig():
'''public void setShouldSaveConfig(final boolean shouldSaveConfig)
'''
pass
def getHandler():
'''public Handler getHandler(final String name)
'''
pass
def getService():
'''public SOAPService getService(final String name)
'''
pass
def getTransport():
'''public Handler getTransport(final String name)
'''
pass
def getTypeMappingRegistry():
'''public TypeMappingRegistry getTypeMappingRegistry()
'''
pass
def getGlobalRequest():
'''public Handler getGlobalRequest()
'''
pass
def getGlobalResponse():
'''public Handler getGlobalResponse()
'''
pass
def getActorURIs():
'''public ArrayList getActorURIs()
'''
pass
def addActorURI():
'''public void addActorURI(final String uri)
'''
pass
def removeActorURI():
'''public void removeActorURI(final String uri)
'''
pass
def normaliseOptions():
'''public static void normaliseOptions(final Handler handler)
'''
pass
def refreshGlobalOptions():
'''public void refreshGlobalOptions()
'''
pass
def getApplicationSession():
'''public Session getApplicationSession()
'''
pass
def getClassCache():
'''public ClassCache getClassCache()
'''
pass