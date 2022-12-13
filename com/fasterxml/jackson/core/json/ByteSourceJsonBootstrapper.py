UTF8_BOM_1 = "byte  -17"
UTF8_BOM_2 = "byte  -69"
UTF8_BOM_3 = "byte  -65"
def ByteSourceJsonBootstrapper():
'''public ByteSourceJsonBootstrapper(final IOContext ctxt, final InputStream in)
public ByteSourceJsonBootstrapper(final IOContext ctxt, final byte[] inputBuffer, final int inputStart, final int inputLen)
'''
pass
def detectEncoding():
'''public JsonEncoding detectEncoding()
'''
pass
def skipUTF8BOM():
'''public static int skipUTF8BOM(final DataInput input)
'''
pass
def constructReader():
'''public Reader constructReader()
'''
pass
def constructParser():
'''public JsonParser constructParser(final int parserFeatures, final ObjectCodec codec, final ByteQuadsCanonicalizer rootByteSymbols, final CharsToNameCanonicalizer rootCharSymbols, final int factoryFeatures)
'''
pass
def hasJSONFormat():
'''public static MatchStrength hasJSONFormat(final InputAccessor acc)
'''
pass
