def initFromTypeSystem():
    '''returns None\n\n
    initFromTypeSystem(final SchemaTypeSystemImpl system, final Set newNamespaces)\n
    '''
def setImportingTypeLoader():
    '''returns None\n\n
    setImportingTypeLoader(final SchemaTypeLoader loader)\n
    '''
def setErrorListener():
    '''returns None\n\n
    setErrorListener(final Collection errorListener)\n
    '''
def error():
    '''returns None\n\n
    error(final String message, final int code, final XmlObject loc)\n
    error(final String code, final Object[] args, final XmlObject loc)\n
    '''
def recover():
    '''returns None\n\n
    recover(final String code, final Object[] args, final XmlObject loc)\n
    '''
def warning():
    '''returns None\n\n
    warning(final String message, final int code, final XmlObject loc)\n
    warning(final String code, final Object[] args, final XmlObject loc)\n
    '''
def info():
    '''returns None\n\n
    info(final String message)\n
    info(final String code, final Object[] args)\n
    '''
def setGivenTypeSystemName():
    '''returns None\n\n
    setGivenTypeSystemName(final String name)\n
    '''
def setTargetSchemaTypeSystem():
    '''returns None\n\n
    setTargetSchemaTypeSystem(final SchemaTypeSystemImpl target)\n
    '''
def addSchemaDigest():
    '''returns None\n\n
    addSchemaDigest(final byte[] digest)\n
    '''
def sts():
    '''returns SchemaTypeSystemImpl\n\n
    sts()\n
    '''
def shouldDownloadURI():
    '''returns boolean\n\n
    shouldDownloadURI(final String uriString)\n
    '''
def setOptions():
    '''returns None\n\n
    setOptions(final XmlOptions options)\n
    '''
def getEntityResolver():
    '''returns EntityResolver\n\n
    getEntityResolver()\n
    '''
def noUpa():
    '''returns boolean\n\n
    noUpa()\n
    '''
def noPvr():
    '''returns boolean\n\n
    noPvr()\n
    '''
def noAnn():
    '''returns boolean\n\n
    noAnn()\n
    '''
def allowPartial():
    '''returns boolean\n\n
    allowPartial()\n
    '''
def getRecovered():
    '''returns int\n\n
    getRecovered()\n
    '''
def setBindingConfig():
    '''returns None\n\n
    setBindingConfig(final BindingConfig config)\n
    '''
def getBindingConfig():
    '''returns BindingConfig\n\n
    getBindingConfig()\n
    '''
def getPackageOverride():
    '''returns String\n\n
    getPackageOverride(final String namespace)\n
    '''
def getJavaPrefix():
    '''returns String\n\n
    getJavaPrefix(final String namespace)\n
    '''
def getJavaSuffix():
    '''returns String\n\n
    getJavaSuffix(final String namespace)\n
    '''
def getJavaname():
    '''returns String\n\n
    getJavaname(final QName qname, final int kind)\n
    '''
def notFoundError():
    '''returns None\n\n
    notFoundError(final QName itemName, final int code, final XmlObject loc, final boolean recovered)\n
    '''
def sourceNameForUri():
    '''returns String\n\n
    sourceNameForUri(final String uri)\n
    '''
def sourceCopyMap():
    '''returns Map\n\n
    sourceCopyMap()\n
    '''
def setBaseUri():
    '''returns None\n\n
    setBaseUri(final URI uri)\n
    '''
def relativize():
    '''returns String\n\n
    relativize(final String uri)\n
    '''
def computeSavedFilename():
    '''returns String\n\n
    computeSavedFilename(final String uri)\n
    '''
def addSourceUri():
    '''returns None\n\n
    addSourceUri(final String uri, String nameToUse)\n
    '''
def getErrorListener():
    '''returns Collection\n\n
    getErrorListener()\n
    '''
def getS4SLoader():
    '''returns SchemaTypeLoader\n\n
    getS4SLoader()\n
    '''
def getSchemasDir():
    '''returns File\n\n
    getSchemasDir()\n
    '''
def setSchemasDir():
    '''returns None\n\n
    setSchemasDir(final File _schemasDir)\n
    '''
