FORMAT_NAME_JSON = "String  \"JSON\""
def JsonFactory():
    '''    public JsonFactory()
    public JsonFactory(final ObjectCodec oc)
    '''
def getFormatName():
    '''    public String getFormatName()
    '''
def hasFormat():
    '''    public MatchStrength hasFormat(final InputAccessor acc)
    '''
def version():
    '''    public Version version()
    '''
def configure():
    '''    public final JsonFactory configure(final JsonParser.Feature f, final boolean state)
    public final JsonFactory configure(final JsonGenerator.Feature f, final boolean state)
    '''
def enable():
    '''    public JsonFactory enable(final JsonParser.Feature f)
    public JsonFactory enable(final JsonGenerator.Feature f)
    '''
def disable():
    '''    public JsonFactory disable(final JsonParser.Feature f)
    public JsonFactory disable(final JsonGenerator.Feature f)
    '''
def isEnabled():
    '''    public final boolean isEnabled(final JsonParser.Feature f)
    public final boolean isEnabled(final JsonGenerator.Feature f)
    '''
def enableParserFeature():
    '''    public final void enableParserFeature(final JsonParser.Feature f)
    '''
def disableParserFeature():
    '''    public final void disableParserFeature(final JsonParser.Feature f)
    '''
def setParserFeature():
    '''    public final void setParserFeature(final JsonParser.Feature f, final boolean state)
    '''
def isParserFeatureEnabled():
    '''    public final boolean isParserFeatureEnabled(final JsonParser.Feature f)
    '''
def getInputDecorator():
    '''    public InputDecorator getInputDecorator()
    '''
def setInputDecorator():
    '''    public JsonFactory setInputDecorator(final InputDecorator d)
    '''
def enableGeneratorFeature():
    '''    public final void enableGeneratorFeature(final JsonGenerator.Feature f)
    '''
def disableGeneratorFeature():
    '''    public final void disableGeneratorFeature(final JsonGenerator.Feature f)
    '''
def setGeneratorFeature():
    '''    public final void setGeneratorFeature(final JsonGenerator.Feature f, final boolean state)
    '''
def isGeneratorFeatureEnabled():
    '''    public final boolean isGeneratorFeatureEnabled(final JsonGenerator.Feature f)
    '''
def getCharacterEscapes():
    '''    public CharacterEscapes getCharacterEscapes()
    '''
def setCharacterEscapes():
    '''    public JsonFactory setCharacterEscapes(final CharacterEscapes esc)
    '''
def getOutputDecorator():
    '''    public OutputDecorator getOutputDecorator()
    '''
def setOutputDecorator():
    '''    public JsonFactory setOutputDecorator(final OutputDecorator d)
    '''
def setCodec():
    '''    public JsonFactory setCodec(final ObjectCodec oc)
    '''
def getCodec():
    '''    public ObjectCodec getCodec()
    '''
def createJsonParser():
    '''    public JsonParser createJsonParser(final File f)
    public JsonParser createJsonParser(final URL url)
    public JsonParser createJsonParser(InputStream in)
    public JsonParser createJsonParser(Reader r)
    public JsonParser createJsonParser(final byte[] data)
    public JsonParser createJsonParser(final byte[] data, final int offset, final int len)
    public JsonParser createJsonParser(final String content)
    '''
def createJsonGenerator():
    '''    public JsonGenerator createJsonGenerator(OutputStream out, final JsonEncoding enc)
    public JsonGenerator createJsonGenerator(Writer out)
    public JsonGenerator createJsonGenerator(final OutputStream out)
    public JsonGenerator createJsonGenerator(final File f, final JsonEncoding enc)
    '''
def _getBufferRecycler():
    '''    public BufferRecycler _getBufferRecycler()
    '''
