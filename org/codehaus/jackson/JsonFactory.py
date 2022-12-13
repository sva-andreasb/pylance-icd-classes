FORMAT_NAME_JSON = "String  JSON""
def JsonFactory():
'''public JsonFactory()
public JsonFactory(final ObjectCodec oc)
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
def version():
'''public Version version()
'''
pass
def configure():
'''public final JsonFactory configure(final JsonParser.Feature f, final boolean state)
public final JsonFactory configure(final JsonGenerator.Feature f, final boolean state)
'''
pass
def enable():
'''public JsonFactory enable(final JsonParser.Feature f)
public JsonFactory enable(final JsonGenerator.Feature f)
'''
pass
def disable():
'''public JsonFactory disable(final JsonParser.Feature f)
public JsonFactory disable(final JsonGenerator.Feature f)
'''
pass
def isEnabled():
'''public final boolean isEnabled(final JsonParser.Feature f)
public final boolean isEnabled(final JsonGenerator.Feature f)
'''
pass
def enableParserFeature():
'''public final void enableParserFeature(final JsonParser.Feature f)
'''
pass
def disableParserFeature():
'''public final void disableParserFeature(final JsonParser.Feature f)
'''
pass
def setParserFeature():
'''public final void setParserFeature(final JsonParser.Feature f, final boolean state)
'''
pass
def isParserFeatureEnabled():
'''public final boolean isParserFeatureEnabled(final JsonParser.Feature f)
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
def enableGeneratorFeature():
'''public final void enableGeneratorFeature(final JsonGenerator.Feature f)
'''
pass
def disableGeneratorFeature():
'''public final void disableGeneratorFeature(final JsonGenerator.Feature f)
'''
pass
def setGeneratorFeature():
'''public final void setGeneratorFeature(final JsonGenerator.Feature f, final boolean state)
'''
pass
def isGeneratorFeatureEnabled():
'''public final boolean isGeneratorFeatureEnabled(final JsonGenerator.Feature f)
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
def setCodec():
'''public JsonFactory setCodec(final ObjectCodec oc)
'''
pass
def getCodec():
'''public ObjectCodec getCodec()
'''
pass
def createJsonParser():
'''public JsonParser createJsonParser(final File f)
public JsonParser createJsonParser(final URL url)
public JsonParser createJsonParser(InputStream in)
public JsonParser createJsonParser(Reader r)
public JsonParser createJsonParser(final byte[] data)
public JsonParser createJsonParser(final byte[] data, final int offset, final int len)
public JsonParser createJsonParser(final String content)
'''
pass
def createJsonGenerator():
'''public JsonGenerator createJsonGenerator(OutputStream out, final JsonEncoding enc)
public JsonGenerator createJsonGenerator(Writer out)
public JsonGenerator createJsonGenerator(final OutputStream out)
public JsonGenerator createJsonGenerator(final File f, final JsonEncoding enc)
'''
pass
def _getBufferRecycler():
'''public BufferRecycler _getBufferRecycler()
'''
pass
