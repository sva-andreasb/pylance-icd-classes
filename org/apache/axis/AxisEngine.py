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
def ():
    '''returns AxisEngine\n\n
    (final EngineConfiguration config)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def cleanup():
    '''returns None\n\n
    cleanup()\n
    '''
def saveConfiguration():
    '''returns None\n\n
    saveConfiguration()\n
    '''
def getConfig():
    '''returns EngineConfiguration\n\n
    getConfig()\n
    '''
def hasSafePassword():
    '''returns boolean\n\n
    hasSafePassword()\n
    '''
def setAdminPassword():
    '''returns None\n\n
    setAdminPassword(final String pw)\n
    '''
def setShouldSaveConfig():
    '''returns None\n\n
    setShouldSaveConfig(final boolean shouldSaveConfig)\n
    '''
def getHandler():
    '''returns Handler\n\n
    getHandler(final String name)\n
    '''
def getService():
    '''returns SOAPService\n\n
    getService(final String name)\n
    '''
def getTransport():
    '''returns Handler\n\n
    getTransport(final String name)\n
    '''
def getTypeMappingRegistry():
    '''returns TypeMappingRegistry\n\n
    getTypeMappingRegistry()\n
    '''
def getGlobalRequest():
    '''returns Handler\n\n
    getGlobalRequest()\n
    '''
def getGlobalResponse():
    '''returns Handler\n\n
    getGlobalResponse()\n
    '''
def getActorURIs():
    '''returns ArrayList\n\n
    getActorURIs()\n
    '''
def addActorURI():
    '''returns None\n\n
    addActorURI(final String uri)\n
    '''
def removeActorURI():
    '''returns None\n\n
    removeActorURI(final String uri)\n
    '''
def refreshGlobalOptions():
    '''returns None\n\n
    refreshGlobalOptions()\n
    '''
def getApplicationSession():
    '''returns Session\n\n
    getApplicationSession()\n
    '''
def getClassCache():
    '''returns ClassCache\n\n
    getClassCache()\n
    '''
