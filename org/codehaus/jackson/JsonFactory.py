FORMAT_NAME_JSON = "String  \"JSON\""
def ():
    '''returns JsonFactory\n\n
    ()\n
    (final ObjectCodec oc)\n
    '''
def getFormatName():
    '''returns String\n\n
    getFormatName()\n
    '''
def hasFormat():
    '''returns MatchStrength\n\n
    hasFormat(final InputAccessor acc)\n
    '''
def version():
    '''returns Version\n\n
    version()\n
    '''
def enable():
    '''returns JsonFactory\n\n
    enable(final JsonParser.Feature f)\n
    enable(final JsonGenerator.Feature f)\n
    '''
def disable():
    '''returns JsonFactory\n\n
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
def setCodec():
    '''returns JsonFactory\n\n
    setCodec(final ObjectCodec oc)\n
    '''
def getCodec():
    '''returns ObjectCodec\n\n
    getCodec()\n
    '''
def createJsonParser():
    '''returns JsonParser\n\n
    createJsonParser(final File f)\n
    createJsonParser(final URL url)\n
    createJsonParser(InputStream in)\n
    createJsonParser(Reader r)\n
    createJsonParser(final byte[] data)\n
    createJsonParser(final byte[] data, final int offset, final int len)\n
    createJsonParser(final String content)\n
    '''
def createJsonGenerator():
    '''returns JsonGenerator\n\n
    createJsonGenerator(OutputStream out, final JsonEncoding enc)\n
    createJsonGenerator(Writer out)\n
    createJsonGenerator(final OutputStream out)\n
    createJsonGenerator(final File f, final JsonEncoding enc)\n
    '''
def _getBufferRecycler():
    '''returns BufferRecycler\n\n
    _getBufferRecycler()\n
    '''
