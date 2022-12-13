FORMAT_NAME_JSON = "String  JSON""
def JsonFactory():
'''public JsonFactory()
public JsonFactory(final ObjectCodec oc)
'''
pass
def copy():
'''public JsonFactory copy()
'''
pass
def requiresPropertyOrdering():
'''public boolean requiresPropertyOrdering()
'''
pass
def canHandleBinaryNatively():
'''public boolean canHandleBinaryNatively()
'''
pass
def canUseCharArrays():
'''public boolean canUseCharArrays()
'''
pass
def canParseAsync():
'''public boolean canParseAsync()
'''
pass
def canUseSchema():
'''public boolean canUseSchema(final FormatSchema schema)
'''
pass
def getFormatName():
'''public String getFormatName()
'''
pass
def hasFormat():
'''public MatchStrength hasFormat(final InputAccessor acc)
'''
pass
def requiresCustomCodec():
'''public boolean requiresCustomCodec()
'''
pass
def version():
'''public Version version()
'''
pass
def configure():
'''public final JsonFactory configure(final Feature f, final boolean state)
public final JsonFactory configure(final JsonParser.Feature f, final boolean state)
public final JsonFactory configure(final JsonGenerator.Feature f, final boolean state)
'''
pass
def enable():
'''public JsonFactory enable(final Feature f)
public JsonFactory enable(final JsonParser.Feature f)
public JsonFactory enable(final JsonGenerator.Feature f)
'''
pass
def disable():
'''public JsonFactory disable(final Feature f)
public JsonFactory disable(final JsonParser.Feature f)
public JsonFactory disable(final JsonGenerator.Feature f)
'''
pass
def isEnabled():
'''public final boolean isEnabled(final Feature f)
public final boolean isEnabled(final JsonParser.Feature f)
public final boolean isEnabled(final JsonGenerator.Feature f)
'''
pass
def getInputDecorator():
'''public InputDecorator getInputDecorator()
'''
pass
def setInputDecorator():
'''public JsonFactory setInputDecorator(final InputDecorator d)
'''
pass
def getCharacterEscapes():
'''public CharacterEscapes getCharacterEscapes()
'''
pass
def setCharacterEscapes():
'''public JsonFactory setCharacterEscapes(final CharacterEscapes esc)
'''
pass
def getOutputDecorator():
'''public OutputDecorator getOutputDecorator()
'''
pass
def setOutputDecorator():
'''public JsonFactory setOutputDecorator(final OutputDecorator d)
'''
pass
def setRootValueSeparator():
'''public JsonFactory setRootValueSeparator(final String sep)
'''
pass
def getRootValueSeparator():
'''public String getRootValueSeparator()
'''
pass
def setCodec():
'''public JsonFactory setCodec(final ObjectCodec oc)
'''
pass
def getCodec():
'''public ObjectCodec getCodec()
'''
pass
def createParser():
'''public JsonParser createParser(final File f)
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
pass
def createNonBlockingByteArrayParser():
'''public JsonParser createNonBlockingByteArrayParser()
'''
pass
def createJsonParser():
'''public JsonParser createJsonParser(final File f)
public JsonParser createJsonParser(final URL url)
public JsonParser createJsonParser(final InputStream in)
public JsonParser createJsonParser(final Reader r)
public JsonParser createJsonParser(final byte[] data)
public JsonParser createJsonParser(final byte[] data, final int offset, final int len)
public JsonParser createJsonParser(final String content)
'''
pass
def createGenerator():
'''public JsonGenerator createGenerator(final OutputStream out, final JsonEncoding enc)
public JsonGenerator createGenerator(final OutputStream out)
public JsonGenerator createGenerator(final Writer w)
public JsonGenerator createGenerator(final File f, final JsonEncoding enc)
public JsonGenerator createGenerator(final DataOutput out, final JsonEncoding enc)
public JsonGenerator createGenerator(final DataOutput out)
'''
pass
def createJsonGenerator():
'''public JsonGenerator createJsonGenerator(final OutputStream out, final JsonEncoding enc)
public JsonGenerator createJsonGenerator(final Writer out)
public JsonGenerator createJsonGenerator(final OutputStream out)
'''
pass
def _getBufferRecycler():
'''public BufferRecycler _getBufferRecycler()
'''
pass
def collectDefaults():
'''public static int collectDefaults()
'''
pass
def enabledByDefault():
'''public boolean enabledByDefault()
'''
pass
def enabledIn():
'''public boolean enabledIn(final int flags)
'''
pass
def getMask():
'''public int getMask()
'''
pass
