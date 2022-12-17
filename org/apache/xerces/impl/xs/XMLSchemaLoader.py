SYMBOL_TABLE = "String  \"http://apache.org/xml/properties/internal/symbol-table\""
ERROR_REPORTER = "String  \"http://apache.org/xml/properties/internal/error-reporter\""
ENTITY_RESOLVER = "String  \"http://apache.org/xml/properties/internal/entity-resolver\""
XMLGRAMMAR_POOL = "String  \"http://apache.org/xml/properties/internal/grammar-pool\""
def ():
    '''returns XMLSchemaLoader\n\n
    ()\n
    (final SymbolTable symbolTable)\n
    '''
def getRecognizedFeatures():
    '''returns String[]\n\n
    getRecognizedFeatures()\n
    '''
def getFeature():
    '''returns boolean\n\n
    getFeature(final String s)\n
    '''
def setFeature():
    '''returns None\n\n
    setFeature(final String s, final boolean generateSyntheticAnnotations)\n
    '''
def getRecognizedProperties():
    '''returns String[]\n\n
    getRecognizedProperties()\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String s)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String s, final Object fjaxpSource)\n
    '''
def setLocale():
    '''returns None\n\n
    setLocale(final Locale locale)\n
    '''
def getLocale():
    '''returns Locale\n\n
    getLocale()\n
    '''
def setErrorHandler():
    '''returns None\n\n
    setErrorHandler(final XMLErrorHandler xmlErrorHandler)\n
    '''
def getErrorHandler():
    '''returns XMLErrorHandler\n\n
    getErrorHandler()\n
    '''
def setEntityResolver():
    '''returns None\n\n
    setEntityResolver(final XMLEntityResolver fUserEntityResolver)\n
    '''
def getEntityResolver():
    '''returns XMLEntityResolver\n\n
    getEntityResolver()\n
    '''
def loadGrammar():
    '''returns Grammar\n\n
    loadGrammar(final XMLInputSource[] array)\n
    loadGrammar(final XMLInputSource xmlInputSource)\n
    '''
def getFeatureDefault():
    '''returns Boolean\n\n
    getFeatureDefault(final String s)\n
    '''
def getPropertyDefault():
    '''returns Object\n\n
    getPropertyDefault(final String s)\n
    '''
def reset():
    '''returns None\n\n
    reset(final XMLComponentManager xmlComponentManager)\n
    '''
def getConfig():
    '''returns DOMConfiguration\n\n
    getConfig()\n
    '''
def load():
    '''returns XSModel\n\n
    load(final LSInput lsInput)\n
    '''
def loadInputList():
    '''returns XSModel\n\n
    loadInputList(final LSInputList list)\n
    '''
def loadURI():
    '''returns XSModel\n\n
    loadURI(final String s)\n
    '''
def loadURIList():
    '''returns XSModel\n\n
    loadURIList(final StringList list)\n
    '''
def canSetParameter():
    '''returns boolean\n\n
    canSetParameter(final String s, final Object o)\n
    '''
def getParameter():
    '''returns Object\n\n
    getParameter(final String s)\n
    '''
def getParameterNames():
    '''returns DOMStringList\n\n
    getParameterNames()\n
    '''
def setParameter():
    '''returns None\n\n
    setParameter(final String s, final Object o)\n
    '''
def getGlobalElementDecl():
    '''returns XSElementDecl\n\n
    getGlobalElementDecl(final QName qName)\n
    '''
def resize():
    '''returns None\n\n
    resize(final int n, final int n2)\n
    '''
def addLocation():
    '''returns None\n\n
    addLocation(final String s)\n
    '''
def getLocationArray():
    '''returns String[]\n\n
    getLocationArray()\n
    '''
def getFirstLocation():
    '''returns String\n\n
    getFirstLocation()\n
    '''
def getLength():
    '''returns int\n\n
    getLength()\n
    '''
