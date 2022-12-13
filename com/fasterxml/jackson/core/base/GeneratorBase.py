SURR1_FIRST = "int  55296"
SURR1_LAST = "int  56319"
SURR2_FIRST = "int  56320"
SURR2_LAST = "int  57343"
def version():
    '''    public Version version()
    '''
def getCurrentValue():
    '''    public Object getCurrentValue()
    '''
def setCurrentValue():
    '''    public void setCurrentValue(final Object v)
    '''
def isEnabled():
    '''    public final boolean isEnabled(final Feature f)
    '''
def getFeatureMask():
    '''    public int getFeatureMask()
    '''
def enable():
    '''    public JsonGenerator enable(final Feature f)
    '''
def disable():
    '''    public JsonGenerator disable(final Feature f)
    '''
def setFeatureMask():
    '''    public JsonGenerator setFeatureMask(final int newMask)
    '''
def overrideStdFeatures():
    '''    public JsonGenerator overrideStdFeatures(final int values, final int mask)
    '''
def useDefaultPrettyPrinter():
    '''    public JsonGenerator useDefaultPrettyPrinter()
    '''
def setCodec():
    '''    public JsonGenerator setCodec(final ObjectCodec oc)
    '''
def getCodec():
    '''    public ObjectCodec getCodec()
    '''
def getOutputContext():
    '''    public JsonStreamContext getOutputContext()
    '''
def writeStartObject():
    '''    public void writeStartObject(final Object forValue)
    '''
def writeFieldName():
    '''    public void writeFieldName(final SerializableString name)
    '''
def writeString():
    '''    public void writeString(final SerializableString text)
    '''
def writeRawValue():
    '''    public void writeRawValue(final String text)
    public void writeRawValue(final String text, final int offset, final int len)
    public void writeRawValue(final char[] text, final int offset, final int len)
    public void writeRawValue(final SerializableString text)
    '''
def writeBinary():
    '''    public int writeBinary(final Base64Variant b64variant, final InputStream data, final int dataLength)
    '''
def writeObject():
    '''    public void writeObject(final Object value)
    '''
def writeTree():
    '''    public void writeTree(final TreeNode rootNode)
    '''
def close():
    '''    public void close()
    '''
def isClosed():
    '''    public boolean isClosed()
    '''
