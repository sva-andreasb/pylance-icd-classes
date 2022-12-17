FORMAT_NAME_JSON = "String  \"JSON\""
def ():
    '''returns JsonFactory\n\n
    ()\n
    (final ObjectCodec oc)\n
    '''
def copy():
    '''returns JsonFactory\n\n
    copy()\n
    '''
def requiresPropertyOrdering():
    '''returns boolean\n\n
    requiresPropertyOrdering()\n
    '''
def canHandleBinaryNatively():
    '''returns boolean\n\n
    canHandleBinaryNatively()\n
    '''
def canUseCharArrays():
    '''returns boolean\n\n
    canUseCharArrays()\n
    '''
def canParseAsync():
    '''returns boolean\n\n
    canParseAsync()\n
    '''
def canUseSchema():
    '''returns boolean\n\n
    canUseSchema(final FormatSchema schema)\n
    '''
def getFormatName():
    '''returns String\n\n
    getFormatName()\n
    '''
def hasFormat():
    '''returns MatchStrength\n\n
    hasFormat(final InputAccessor acc)\n
    '''
def requiresCustomCodec():
    '''returns boolean\n\n
    requiresCustomCodec()\n
    '''
def version():
    '''returns Version\n\n
    version()\n
    '''
def enable():
    '''returns JsonFactory\n\n
    enable(final Feature f)\n
    enable(final JsonParser.Feature f)\n
    enable(final JsonGenerator.Feature f)\n
    '''
def disable():
    '''returns JsonFactory\n\n
    disable(final Feature f)\n
    disable(final JsonParser.Feature f)\n
    disable(final JsonGenerator.Feature f)\n
    '''
def getInputDecorator():
    '''returns InputDecorator\n\n
    getInputDecorator()\n
    '''
def setInputDecorator():
    '''returns JsonFactory\n\n
    setInputDecorator(final InputDecorator d)\n
    '''
def getCharacterEscapes():
    '''returns CharacterEscapes\n\n
    getCharacterEscapes()\n
    '''
def setCharacterEscapes():
    '''returns JsonFactory\n\n
    setCharacterEscapes(final CharacterEscapes esc)\n
    '''
def getOutputDecorator():
    '''returns OutputDecorator\n\n
    getOutputDecorator()\n
    '''
def setOutputDecorator():
    '''returns JsonFactory\n\n
    setOutputDecorator(final OutputDecorator d)\n
    '''
def setRootValueSeparator():
    '''returns JsonFactory\n\n
    setRootValueSeparator(final String sep)\n
    '''
def getRootValueSeparator():
    '''returns String\n\n
    getRootValueSeparator()\n
    '''
def setCodec():
    '''returns JsonFactory\n\n
    setCodec(final ObjectCodec oc)\n
    '''
def getCodec():
    '''returns ObjectCodec\n\n
    getCodec()\n
    '''
def createParser():
    '''returns JsonParser\n\n
    createParser(final File f)\n
    createParser(final URL url)\n
    createParser(final InputStream in)\n
    createParser(final Reader r)\n
    createParser(final byte[] data)\n
    createParser(final byte[] data, final int offset, final int len)\n
    createParser(final String content)\n
    createParser(final char[] content)\n
    createParser(final char[] content, final int offset, final int len)\n
    createParser(final DataInput in)\n
    '''
def createNonBlockingByteArrayParser():
    '''returns JsonParser\n\n
    createNonBlockingByteArrayParser()\n
    '''
def createJsonParser():
    '''returns JsonParser\n\n
    createJsonParser(final File f)\n
    createJsonParser(final URL url)\n
    createJsonParser(final InputStream in)\n
    createJsonParser(final Reader r)\n
    createJsonParser(final byte[] data)\n
    createJsonParser(final byte[] data, final int offset, final int len)\n
    createJsonParser(final String content)\n
    '''
def createGenerator():
    '''returns JsonGenerator\n\n
    createGenerator(final OutputStream out, final JsonEncoding enc)\n
    createGenerator(final OutputStream out)\n
    createGenerator(final Writer w)\n
    createGenerator(final File f, final JsonEncoding enc)\n
    createGenerator(final DataOutput out, final JsonEncoding enc)\n
    createGenerator(final DataOutput out)\n
    '''
def createJsonGenerator():
    '''returns JsonGenerator\n\n
    createJsonGenerator(final OutputStream out, final JsonEncoding enc)\n
    createJsonGenerator(final Writer out)\n
    createJsonGenerator(final OutputStream out)\n
    '''
def _getBufferRecycler():
    '''returns BufferRecycler\n\n
    _getBufferRecycler()\n
    '''
def enabledByDefault():
    '''returns boolean\n\n
    enabledByDefault()\n
    '''
def enabledIn():
    '''returns boolean\n\n
    enabledIn(final int flags)\n
    '''
def getMask():
    '''returns int\n\n
    getMask()\n
    '''
