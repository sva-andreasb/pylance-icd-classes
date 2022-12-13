UTF8_BOM_1 = "byte  -17"
UTF8_BOM_2 = "byte  -69"
UTF8_BOM_3 = "byte  -65"
def ByteSourceJsonBootstrapper():
    '''public ByteSourceJsonBootstrapper(final IOContext ctxt, final InputStream in)
    public ByteSourceJsonBootstrapper(final IOContext ctxt, final byte[] inputBuffer, final int inputStart, final int inputLen)
    '''
def detectEncoding():
    '''public JsonEncoding detectEncoding()
    '''
def skipUTF8BOM():
    '''public static int skipUTF8BOM(final DataInput input)
    '''
def constructReader():
    '''public Reader constructReader()
    '''
def constructParser():
    '''public JsonParser constructParser(final int parserFeatures, final ObjectCodec codec, final ByteQuadsCanonicalizer rootByteSymbols, final CharsToNameCanonicalizer rootCharSymbols, final int factoryFeatures)
    '''
def hasJSONFormat():
    '''public static MatchStrength hasJSONFormat(final InputAccessor acc)
    '''
