DEFAULT_METADATA_PATH = "String  \"file:ont-policy.rdf;file:etc/ont-policy.rdf\""
NS = "String  \"http://jena.hpl.hp.com/schemas/2003/03/ont-manager#\""
ANCHOR = "String  \"#\""
def ():
    '''returns OntDocumentManager\n\n
    ()\n
    (final String path)\n
    (final FileManager fileMgr, final String path)\n
    (final Model config)\n
    (final FileManager fileMgr, final Model config)\n
    '''
def getFileManager():
    '''returns FileManager\n\n
    getFileManager()\n
    '''
def setReadHook():
    '''returns ReadHook\n\n
    setReadHook(final ReadHook hook)\n
    '''
def getReadHook():
    '''returns ReadHook\n\n
    getReadHook()\n
    '''
def setFileManager():
    '''returns None\n\n
    setFileManager()\n
    setFileManager(final FileManager fileMgr)\n
    '''
def getMetadataSearchPath():
    '''returns String\n\n
    getMetadataSearchPath()\n
    '''
def setMetadataSearchPath():
    '''returns None\n\n
    setMetadataSearchPath(final String path, final boolean replace)\n
    '''
def setReadFailureHandler():
    '''returns None\n\n
    setReadFailureHandler(final ReadFailureHandler rfHandler)\n
    '''
def getReadFailureHandler():
    '''returns ReadFailureHandler\n\n
    getReadFailureHandler()\n
    '''
def configure():
    '''returns None\n\n
    configure(final Model config)\n
    configure(final Model config, final boolean reset)\n
    '''
def reset():
    '''returns None\n\n
    reset(final boolean reload)\n
    reset()\n
    '''
def listDocuments():
    '''returns Iterator<String>\n\n
    listDocuments()\n
    '''
def doAltURLMapping():
    '''returns String\n\n
    doAltURLMapping(final String uri)\n
    '''
def getModel():
    '''returns Model\n\n
    getModel(final String uri)\n
    '''
def addAltEntry():
    '''returns None\n\n
    addAltEntry(final String docURI, final String locationURL)\n
    '''
def addModel():
    '''returns None\n\n
    addModel(final String docURI, final Model model)\n
    addModel(final String docURI, final Model model, final boolean replace)\n
    '''
def forget():
    '''returns None\n\n
    forget(final String docURI)\n
    '''
def getOntology():
    '''returns OntModel\n\n
    getOntology(final String uri, final OntModelSpec spec)\n
    '''
def getProcessImports():
    '''returns boolean\n\n
    getProcessImports()\n
    '''
def getCacheModels():
    '''returns boolean\n\n
    getCacheModels()\n
    '''
def setProcessImports():
    '''returns None\n\n
    setProcessImports(final boolean processImports)\n
    '''
def setCacheModels():
    '''returns None\n\n
    setCacheModels(final boolean cacheModels)\n
    '''
def addIgnoreImport():
    '''returns None\n\n
    addIgnoreImport(final String uri)\n
    '''
def removeIgnoreImport():
    '''returns None\n\n
    removeIgnoreImport(final String uri)\n
    '''
def listIgnoredImports():
    '''returns Iterator<String>\n\n
    listIgnoredImports()\n
    '''
def ignoringImport():
    '''returns boolean\n\n
    ignoringImport(final String uri)\n
    '''
def clearCache():
    '''returns None\n\n
    clearCache()\n
    '''
def loadImports():
    '''returns None\n\n
    loadImports(final OntModel model)\n
    '''
def loadImport():
    '''returns None\n\n
    loadImport(final OntModel model, final String uri)\n
    '''
def unloadImport():
    '''returns None\n\n
    unloadImport(final OntModel model, final String uri)\n
    '''
def getLoadedPolicyURL():
    '''returns String\n\n
    getLoadedPolicyURL()\n
    '''
def readModel():
    '''returns Model\n\n
    readModel(final Model toRead, final String URL)\n
    '''
def afterRead():
    '''returns None\n\n
    afterRead(final Model model, final String source, final OntDocumentManager odm)\n
    '''
def beforeRead():
    '''returns String\n\n
    beforeRead(final Model model, final String source, final OntDocumentManager odm)\n
    '''
