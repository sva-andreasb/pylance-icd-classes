GENERATE_JAVA_14 = "String  \"1.4\""
GENERATE_JAVA_15 = "String  \"1.5\""
SAVE_NAMESPACES_FIRST = "String  \"SAVE_NAMESPACES_FIRST\""
SAVE_SYNTHETIC_DOCUMENT_ELEMENT = "String  \"SAVE_SYNTHETIC_DOCUMENT_ELEMENT\""
SAVE_PRETTY_PRINT = "String  \"SAVE_PRETTY_PRINT\""
SAVE_PRETTY_PRINT_INDENT = "String  \"SAVE_PRETTY_PRINT_INDENT\""
SAVE_PRETTY_PRINT_OFFSET = "String  \"SAVE_PRETTY_PRINT_OFFSET\""
SAVE_AGGRESSIVE_NAMESPACES = "String  \"SAVE_AGGRESSIVE_NAMESPACES\""
SAVE_USE_DEFAULT_NAMESPACE = "String  \"SAVE_USE_DEFAULT_NAMESPACE\""
SAVE_IMPLICIT_NAMESPACES = "String  \"SAVE_IMPLICIT_NAMESPACES\""
SAVE_SUGGESTED_PREFIXES = "String  \"SAVE_SUGGESTED_PREFIXES\""
SAVE_FILTER_PROCINST = "String  \"SAVE_FILTER_PROCINST\""
SAVE_USE_OPEN_FRAGMENT = "String  \"SAVE_USE_OPEN_FRAGMENT\""
SAVE_OUTER = "String  \"SAVE_OUTER\""
SAVE_INNER = "String  \"SAVE_INNER\""
SAVE_NO_XML_DECL = "String  \"SAVE_NO_XML_DECL\""
SAVE_SUBSTITUTE_CHARACTERS = "String  \"SAVE_SUBSTITUTE_CHARACTERS\""
SAVE_OPTIMIZE_FOR_SPEED = "String  \"SAVE_OPTIMIZE_FOR_SPEED\""
SAVE_CDATA_LENGTH_THRESHOLD = "String  \"SAVE_CDATA_LENGTH_THRESHOLD\""
SAVE_CDATA_ENTITY_COUNT_THRESHOLD = "String  \"SAVE_CDATA_ENTITY_COUNT_THRESHOLD\""
SAVE_SAX_NO_NSDECLS_IN_ATTRIBUTES = "String  \"SAVE_SAX_NO_NSDECLS_IN_ATTRIBUTES\""
LOAD_REPLACE_DOCUMENT_ELEMENT = "String  \"LOAD_REPLACE_DOCUMENT_ELEMENT\""
LOAD_STRIP_WHITESPACE = "String  \"LOAD_STRIP_WHITESPACE\""
LOAD_STRIP_COMMENTS = "String  \"LOAD_STRIP_COMMENTS\""
LOAD_STRIP_PROCINSTS = "String  \"LOAD_STRIP_PROCINSTS\""
LOAD_LINE_NUMBERS = "String  \"LOAD_LINE_NUMBERS\""
LOAD_LINE_NUMBERS_END_ELEMENT = "String  \"LOAD_LINE_NUMBERS_END_ELEMENT\""
LOAD_SAVE_CDATA_BOOKMARKS = "String  \"LOAD_SAVE_CDATA_BOOKMARKS\""
LOAD_SUBSTITUTE_NAMESPACES = "String  \"LOAD_SUBSTITUTE_NAMESPACES\""
LOAD_TRIM_TEXT_BUFFER = "String  \"LOAD_TRIM_TEXT_BUFFER\""
LOAD_ADDITIONAL_NAMESPACES = "String  \"LOAD_ADDITIONAL_NAMESPACES\""
LOAD_MESSAGE_DIGEST = "String  \"LOAD_MESSAGE_DIGEST\""
LOAD_USE_DEFAULT_RESOLVER = "String  \"LOAD_USE_DEFAULT_RESOLVER\""
LOAD_USE_XMLREADER = "String  \"LOAD_USE_XMLREADER\""
XQUERY_CURRENT_NODE_VAR = "String  \"XQUERY_CURRENT_NODE_VAR\""
XQUERY_VARIABLE_MAP = "String  \"XQUERY_VARIABLE_MAP\""
CHARACTER_ENCODING = "String  \"CHARACTER_ENCODING\""
ERROR_LISTENER = "String  \"ERROR_LISTENER\""
DOCUMENT_TYPE = "String  \"DOCUMENT_TYPE\""
DOCUMENT_SOURCE_NAME = "String  \"DOCUMENT_SOURCE_NAME\""
COMPILE_SUBSTITUTE_NAMES = "String  \"COMPILE_SUBSTITUTE_NAMES\""
COMPILE_NO_VALIDATION = "String  \"COMPILE_NO_VALIDATION\""
COMPILE_NO_UPA_RULE = "String  \"COMPILE_NO_UPA_RULE\""
COMPILE_NO_PVR_RULE = "String  \"COMPILE_NO_PVR_RULE\""
COMPILE_NO_ANNOTATIONS = "String  \"COMPILE_NO_ANNOTATIONS\""
COMPILE_DOWNLOAD_URLS = "String  \"COMPILE_DOWNLOAD_URLS\""
COMPILE_MDEF_NAMESPACES = "String  \"COMPILE_MDEF_NAMESPACES\""
VALIDATE_ON_SET = "String  \"VALIDATE_ON_SET\""
VALIDATE_TREAT_LAX_AS_SKIP = "String  \"VALIDATE_TREAT_LAX_AS_SKIP\""
VALIDATE_STRICT = "String  \"VALIDATE_STRICT\""
VALIDATE_TEXT_ONLY = "String  \"VALIDATE_TEXT_ONLY\""
UNSYNCHRONIZED = "String  \"UNSYNCHRONIZED\""
ENTITY_RESOLVER = "String  \"ENTITY_RESOLVER\""
BASE_URI = "String  \"BASE_URI\""
SCHEMA_CODE_PRINTER = "String  \"SCHEMA_CODE_PRINTER\""
GENERATE_JAVA_VERSION = "String  \"GENERATE_JAVA_VERSION\""
COPY_USE_NEW_SYNC_DOMAIN = "String  \"COPY_USE_NEW_LOCALE\""
LOAD_ENTITY_BYTES_LIMIT = "String  \"LOAD_ENTITY_BYTES_LIMIT\""
def ():
    '''returns XmlOptions\n\n
    ()\n
    (final XmlOptions other)\n
    '''
def setSaveNamespacesFirst():
    '''returns XmlOptions\n\n
    setSaveNamespacesFirst()\n
    '''
def setSavePrettyPrint():
    '''returns XmlOptions\n\n
    setSavePrettyPrint()\n
    '''
def setSavePrettyPrintIndent():
    '''returns XmlOptions\n\n
    setSavePrettyPrintIndent(final int indent)\n
    '''
def setSavePrettyPrintOffset():
    '''returns XmlOptions\n\n
    setSavePrettyPrintOffset(final int offset)\n
    '''
def setCharacterEncoding():
    '''returns XmlOptions\n\n
    setCharacterEncoding(final String encoding)\n
    '''
def setDocumentType():
    '''returns XmlOptions\n\n
    setDocumentType(final SchemaType type)\n
    '''
def setErrorListener():
    '''returns XmlOptions\n\n
    setErrorListener(final Collection c)\n
    '''
def setSaveAggressiveNamespaces():
    '''returns XmlOptions\n\n
    setSaveAggressiveNamespaces()\n
    '''
def setSaveAggresiveNamespaces():
    '''returns XmlOptions\n\n
    setSaveAggresiveNamespaces()\n
    '''
def setSaveSyntheticDocumentElement():
    '''returns XmlOptions\n\n
    setSaveSyntheticDocumentElement(final QName name)\n
    '''
def setUseDefaultNamespace():
    '''returns XmlOptions\n\n
    setUseDefaultNamespace()\n
    '''
def setSaveImplicitNamespaces():
    '''returns XmlOptions\n\n
    setSaveImplicitNamespaces(final Map implicitNamespaces)\n
    '''
def setSaveSuggestedPrefixes():
    '''returns XmlOptions\n\n
    setSaveSuggestedPrefixes(final Map suggestedPrefixes)\n
    '''
def setSaveFilterProcinst():
    '''returns XmlOptions\n\n
    setSaveFilterProcinst(final String filterProcinst)\n
    '''
def setSaveSubstituteCharacters():
    '''returns XmlOptions\n\n
    setSaveSubstituteCharacters(final XmlOptionCharEscapeMap characterReplacementMap)\n
    '''
def setSaveUseOpenFrag():
    '''returns XmlOptions\n\n
    setSaveUseOpenFrag()\n
    '''
def setSaveOuter():
    '''returns XmlOptions\n\n
    setSaveOuter()\n
    '''
def setSaveInner():
    '''returns XmlOptions\n\n
    setSaveInner()\n
    '''
def setSaveNoXmlDecl():
    '''returns XmlOptions\n\n
    setSaveNoXmlDecl()\n
    '''
def setSaveCDataLengthThreshold():
    '''returns XmlOptions\n\n
    setSaveCDataLengthThreshold(final int cdataLengthThreshold)\n
    '''
def setSaveCDataEntityCountThreshold():
    '''returns XmlOptions\n\n
    setSaveCDataEntityCountThreshold(final int cdataEntityCountThreshold)\n
    '''
def setUseCDataBookmarks():
    '''returns XmlOptions\n\n
    setUseCDataBookmarks()\n
    '''
def setSaveSaxNoNSDeclsInAttributes():
    '''returns XmlOptions\n\n
    setSaveSaxNoNSDeclsInAttributes()\n
    '''
def setLoadReplaceDocumentElement():
    '''returns XmlOptions\n\n
    setLoadReplaceDocumentElement(final QName replacement)\n
    '''
def setLoadStripWhitespace():
    '''returns XmlOptions\n\n
    setLoadStripWhitespace()\n
    '''
def setLoadStripComments():
    '''returns XmlOptions\n\n
    setLoadStripComments()\n
    '''
def setLoadStripProcinsts():
    '''returns XmlOptions\n\n
    setLoadStripProcinsts()\n
    '''
def setLoadLineNumbers():
    '''returns XmlOptions\n\n
    setLoadLineNumbers()\n
    setLoadLineNumbers(final String option)\n
    '''
def setLoadSubstituteNamespaces():
    '''returns XmlOptions\n\n
    setLoadSubstituteNamespaces(final Map substNamespaces)\n
    '''
def setLoadTrimTextBuffer():
    '''returns XmlOptions\n\n
    setLoadTrimTextBuffer()\n
    '''
def setLoadAdditionalNamespaces():
    '''returns XmlOptions\n\n
    setLoadAdditionalNamespaces(final Map nses)\n
    '''
def setLoadMessageDigest():
    '''returns XmlOptions\n\n
    setLoadMessageDigest()\n
    '''
def setLoadUseDefaultResolver():
    '''returns XmlOptions\n\n
    setLoadUseDefaultResolver()\n
    '''
def setLoadUseXMLReader():
    '''returns XmlOptions\n\n
    setLoadUseXMLReader(final XMLReader xmlReader)\n
    '''
def setXqueryCurrentNodeVar():
    '''returns XmlOptions\n\n
    setXqueryCurrentNodeVar(final String varName)\n
    '''
def setXqueryVariables():
    '''returns XmlOptions\n\n
    setXqueryVariables(final Map varMap)\n
    '''
def setDocumentSourceName():
    '''returns XmlOptions\n\n
    setDocumentSourceName(final String documentSourceName)\n
    '''
def setCompileSubstituteNames():
    '''returns XmlOptions\n\n
    setCompileSubstituteNames(final Map nameMap)\n
    '''
def setCompileNoValidation():
    '''returns XmlOptions\n\n
    setCompileNoValidation()\n
    '''
def setCompileNoUpaRule():
    '''returns XmlOptions\n\n
    setCompileNoUpaRule()\n
    '''
def setCompileNoPvrRule():
    '''returns XmlOptions\n\n
    setCompileNoPvrRule()\n
    '''
def setCompileNoAnnotations():
    '''returns XmlOptions\n\n
    setCompileNoAnnotations()\n
    '''
def setCompileDownloadUrls():
    '''returns XmlOptions\n\n
    setCompileDownloadUrls()\n
    '''
def setCompileMdefNamespaces():
    '''returns XmlOptions\n\n
    setCompileMdefNamespaces(final Set mdefNamespaces)\n
    '''
def setValidateOnSet():
    '''returns XmlOptions\n\n
    setValidateOnSet()\n
    '''
def setValidateTreatLaxAsSkip():
    '''returns XmlOptions\n\n
    setValidateTreatLaxAsSkip()\n
    '''
def setValidateStrict():
    '''returns XmlOptions\n\n
    setValidateStrict()\n
    '''
def setUnsynchronized():
    '''returns XmlOptions\n\n
    setUnsynchronized()\n
    '''
def setEntityResolver():
    '''returns XmlOptions\n\n
    setEntityResolver(final EntityResolver resolver)\n
    '''
def setBaseURI():
    '''returns XmlOptions\n\n
    setBaseURI(final URI baseURI)\n
    '''
def setSchemaCodePrinter():
    '''returns XmlOptions\n\n
    setSchemaCodePrinter(final SchemaCodePrinter printer)\n
    '''
def setGenerateJavaVersion():
    '''returns XmlOptions\n\n
    setGenerateJavaVersion(final String source)\n
    '''
def setCopyUseNewSynchronizationDomain():
    '''returns XmlOptions\n\n
    setCopyUseNewSynchronizationDomain(final boolean useNewSyncDomain)\n
    '''
def setLoadEntityBytesLimit():
    '''returns XmlOptions\n\n
    setLoadEntityBytesLimit(final int entityBytesLimit)\n
    '''
def put():
    '''returns None\n\n
    put(final Object option)\n
    put(final Object option, final Object value)\n
    put(final Object option, final int value)\n
    '''
def hasOption():
    '''returns boolean\n\n
    hasOption(final Object option)\n
    '''
def get():
    '''returns Object\n\n
    get(final Object option)\n
    '''
def remove():
    '''returns None\n\n
    remove(final Object option)\n
    '''
