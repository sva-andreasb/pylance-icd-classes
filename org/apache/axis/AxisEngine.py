PROP_XML_DECL = "String  \"sendXMLDeclaration\""
PROP_DEBUG_LEVEL = "String  \"debugLevel\""
PROP_DEBUG_FILE = "String  \"debugFile\""
PROP_DOMULTIREFS = "String  \"sendMultiRefs\""
PROP_DISABLE_PRETTY_XML = "String  \"disablePrettyXML\""
PROP_ENABLE_NAMESPACE_PREFIX_OPTIMIZATION = "String  \"enableNamespacePrefixOptimization\""
PROP_PASSWORD = "String  \"adminPassword\""
PROP_SYNC_CONFIG = "String  \"syncConfiguration\""
PROP_SEND_XSI = "String  \"sendXsiTypes\""
PROP_ATTACHMENT_DIR = "String  \"attachments.Directory\""
PROP_ATTACHMENT_IMPLEMENTATION = "String  \"attachments.implementation\""
PROP_ATTACHMENT_CLEANUP = "String  \"attachment.DirectoryCleanUp\""
PROP_DEFAULT_CONFIG_CLASS = "String  \"axis.engineConfigClass\""
PROP_SOAP_VERSION = "String  \"defaultSOAPVersion\""
PROP_SOAP_ALLOWED_VERSION = "String  \"singleSOAPVersion\""
PROP_TWOD_ARRAY_ENCODING = "String  \"enable2DArrayEncoding\""
PROP_XML_ENCODING = "String  \"axis.xmlEncoding\""
PROP_XML_REUSE_SAX_PARSERS = "String  \"axis.xml.reuseParsers\""
PROP_BYTE_BUFFER_BACKING = "String  \"axis.byteBuffer.backing\""
PROP_BYTE_BUFFER_CACHE_INCREMENT = "String  \"axis.byteBuffer.cacheIncrement\""
PROP_BYTE_BUFFER_RESIDENT_MAX_SIZE = "String  \"axis.byteBuffer.residentMaxSize\""
PROP_BYTE_BUFFER_WORK_BUFFER_SIZE = "String  \"axis.byteBuffer.workBufferSize\""
PROP_EMIT_ALL_TYPES = "String  \"emitAllTypesInWSDL\""
PROP_DOTNET_SOAPENC_FIX = "String  \"dotNetSoapEncFix\""
PROP_BP10_COMPLIANCE = "String  \"ws-i.bp10Compliance\""
DEFAULT_ATTACHMENT_IMPL = "String  \"org.apache.axis.attachments.AttachmentsImpl\""
ENV_ATTACHMENT_DIR = "String  \"axis.attachments.Directory\""
ENV_SERVLET_REALPATH = "String  \"servlet.realpath\""
ENV_SERVLET_CONTEXT = "String  \"servletContext\""
def getCurrentMessageContext():
    '''public static MessageContext getCurrentMessageContext()
    '''
def AxisEngine():
    '''public AxisEngine(final EngineConfiguration config)
    '''
def init():
    '''public void init()
    '''
def cleanup():
    '''public void cleanup()
    '''
def saveConfiguration():
    '''public void saveConfiguration()
    '''
def getConfig():
    '''public EngineConfiguration getConfig()
    '''
def hasSafePassword():
    '''public boolean hasSafePassword()
    '''
def setAdminPassword():
    '''public void setAdminPassword(final String pw)
    '''
def setShouldSaveConfig():
    '''public void setShouldSaveConfig(final boolean shouldSaveConfig)
    '''
def getHandler():
    '''public Handler getHandler(final String name)
    '''
def getService():
    '''public SOAPService getService(final String name)
    '''
def getTransport():
    '''public Handler getTransport(final String name)
    '''
def getTypeMappingRegistry():
    '''public TypeMappingRegistry getTypeMappingRegistry()
    '''
def getGlobalRequest():
    '''public Handler getGlobalRequest()
    '''
def getGlobalResponse():
    '''public Handler getGlobalResponse()
    '''
def getActorURIs():
    '''public ArrayList getActorURIs()
    '''
def addActorURI():
    '''public void addActorURI(final String uri)
    '''
def removeActorURI():
    '''public void removeActorURI(final String uri)
    '''
def normaliseOptions():
    '''public static void normaliseOptions(final Handler handler)
    '''
def refreshGlobalOptions():
    '''public void refreshGlobalOptions()
    '''
def getApplicationSession():
    '''public Session getApplicationSession()
    '''
def getClassCache():
    '''public ClassCache getClassCache()
    '''
