FORMAT_NAME_JSON = "String  \"JSON\""
def JsonFactory():
    '''    public JsonFactory()
    public JsonFactory(final ObjectCodec oc)
    '''
def copy():
    '''    public JsonFactory copy()
    '''
def requiresPropertyOrdering():
    '''    public boolean requiresPropertyOrdering()
    '''
def canHandleBinaryNatively():
    '''    public boolean canHandleBinaryNatively()
    '''
def canUseCharArrays():
    '''    public boolean canUseCharArrays()
    '''
def canParseAsync():
    '''    public boolean canParseAsync()
    '''
def canUseSchema():
    '''    public boolean canUseSchema(final FormatSchema schema)
    '''
def getFormatName():
    '''    public String getFormatName()
    '''
def hasFormat():
    '''    public MatchStrength hasFormat(final InputAccessor acc)
    '''
def requiresCustomCodec():
    '''    public boolean requiresCustomCodec()
    '''
def version():
    '''    public Version version()
    '''
def configure():
    '''    public final JsonFactory configure(final Feature f, final boolean state)
    public final JsonFactory configure(final JsonParser.Feature f, final boolean state)
    public final JsonFactory configure(final JsonGenerator.Feature f, final boolean state)
    '''
def enable():
    '''    public JsonFactory enable(final Feature f)
    public JsonFactory enable(final JsonParser.Feature f)
    public JsonFactory enable(final JsonGenerator.Feature f)
    '''
def disable():
    '''    public JsonFactory disable(final Feature f)
    public JsonFactory disable(final JsonParser.Feature f)
    public JsonFactory disable(final JsonGenerator.Feature f)
    '''
def isEnabled():
    '''    public final boolean isEnabled(final Feature f)
    public final boolean isEnabled(final JsonParser.Feature f)
    public final boolean isEnabled(final JsonGenerator.Feature f)
    '''
def getInputDecorator():
    '''    public InputDecorator getInputDecorator()
    '''
def setInputDecorator():
    '''    public JsonFactory setInputDecorator(final InputDecorator d)
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
def setRootValueSeparator():
    '''    public JsonFactory setRootValueSeparator(final String sep)
    '''
def getRootValueSeparator():
    '''    public String getRootValueSeparator()
    '''
def setCodec():
    '''    public JsonFactory setCodec(final ObjectCodec oc)
    '''
def getCodec():
    '''    public ObjectCodec getCodec()
    '''
def createParser():
    '''    public JsonParser createParser(final File f)
    public JsonParser createParser(final URL url)
    public JsonParser createParser(final InputStream in)
    public JsonParser createParser(final Reader r)
    public JsonParser createParser(final byte[] data)
    public JsonParser createParser(final byte[] data, final int offset, final int len)
    public JsonParser createParser(final String content)
    public JsonParser createParser(final char[] content)
    public JsonParser createParser(final char[] content, final int offset, final int len)
    public JsonParser createParser(final DataInput in)
    '''
def createNonBlockingByteArrayParser():
    '''    public JsonParser createNonBlockingByteArrayParser()
    '''
def createJsonParser():
    '''    public JsonParser createJsonParser(final File f)
    public JsonParser createJsonParser(final URL url)
    public JsonParser createJsonParser(final InputStream in)
    public JsonParser createJsonParser(final Reader r)
    public JsonParser createJsonParser(final byte[] data)
    public JsonParser createJsonParser(final byte[] data, final int offset, final int len)
    public JsonParser createJsonParser(final String content)
    '''
def createGenerator():
    '''    public JsonGenerator createGenerator(final OutputStream out, final JsonEncoding enc)
    public JsonGenerator createGenerator(final OutputStream out)
    public JsonGenerator createGenerator(final Writer w)
    public JsonGenerator createGenerator(final File f, final JsonEncoding enc)
    public JsonGenerator createGenerator(final DataOutput out, final JsonEncoding enc)
    public JsonGenerator createGenerator(final DataOutput out)
    '''
def createJsonGenerator():
    '''    public JsonGenerator createJsonGenerator(final OutputStream out, final JsonEncoding enc)
    public JsonGenerator createJsonGenerator(final Writer out)
    public JsonGenerator createJsonGenerator(final OutputStream out)
    '''
def _getBufferRecycler():
    '''    public BufferRecycler _getBufferRecycler()
    '''
def collectDefaults():
    '''    public static int collectDefaults()
    '''
def enabledByDefault():
    '''    public boolean enabledByDefault()
    '''
def enabledIn():
    '''    public boolean enabledIn(final int flags)
    '''
def getMask():
    '''    public int getMask()
    '''
