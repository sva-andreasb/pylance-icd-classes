def getInputSource():
    '''    public Object getInputSource()
    '''
def getCurrentValue():
    '''    public Object getCurrentValue()
    '''
def setCurrentValue():
    '''    public void setCurrentValue(final Object v)
    '''
def setRequestPayloadOnError():
    '''    public void setRequestPayloadOnError(final RequestPayload payload)
    public void setRequestPayloadOnError(final byte[] payload, final String charset)
    public void setRequestPayloadOnError(final String payload)
    '''
def setSchema():
    '''    public void setSchema(final FormatSchema schema)
    '''
def getSchema():
    '''    public FormatSchema getSchema()
    '''
def canUseSchema():
    '''    public boolean canUseSchema(final FormatSchema schema)
    '''
def requiresCustomCodec():
    '''    public boolean requiresCustomCodec()
    '''
def canParseAsync():
    '''    public boolean canParseAsync()
    '''
def getNonBlockingInputFeeder():
    '''    public NonBlockingInputFeeder getNonBlockingInputFeeder()
    '''
def releaseBuffered():
    '''    public int releaseBuffered(final OutputStream out)
    public int releaseBuffered(final Writer w)
    '''
def enable():
    '''    public JsonParser enable(final Feature f)
    '''
def disable():
    '''    public JsonParser disable(final Feature f)
    '''
def configure():
    '''    public JsonParser configure(final Feature f, final boolean state)
    '''
def isEnabled():
    '''    public boolean isEnabled(final Feature f)
    '''
def getFeatureMask():
    '''    public int getFeatureMask()
    '''
def setFeatureMask():
    '''    public JsonParser setFeatureMask(final int mask)
    '''
def overrideStdFeatures():
    '''    public JsonParser overrideStdFeatures(final int values, final int mask)
    '''
def getFormatFeatures():
    '''    public int getFormatFeatures()
    '''
def overrideFormatFeatures():
    '''    public JsonParser overrideFormatFeatures(final int values, final int mask)
    '''
def nextFieldName():
    '''    public boolean nextFieldName(final SerializableString str)
    public String nextFieldName()
    '''
def nextTextValue():
    '''    public String nextTextValue()
    '''
def nextIntValue():
    '''    public int nextIntValue(final int defaultValue)
    '''
def nextLongValue():
    '''    public long nextLongValue(final long defaultValue)
    '''
def nextBooleanValue():
    '''    public Boolean nextBooleanValue()
    '''
def finishToken():
    '''    public void finishToken()
    '''
def currentToken():
    '''    public JsonToken currentToken()
    '''
def currentTokenId():
    '''    public int currentTokenId()
    '''
def isExpectedStartArrayToken():
    '''    public boolean isExpectedStartArrayToken()
    '''
def isExpectedStartObjectToken():
    '''    public boolean isExpectedStartObjectToken()
    '''
def isNaN():
    '''    public boolean isNaN()
    '''
def currentName():
    '''    public String currentName()
    '''
def getText():
    '''    public int getText(final Writer writer)
    '''
def getByteValue():
    '''    public byte getByteValue()
    '''
def getShortValue():
    '''    public short getShortValue()
    '''
def getBooleanValue():
    '''    public boolean getBooleanValue()
    '''
def getEmbeddedObject():
    '''    public Object getEmbeddedObject()
    '''
def getBinaryValue():
    '''    public byte[] getBinaryValue()
    '''
def readBinaryValue():
    '''    public int readBinaryValue(final OutputStream out)
    public int readBinaryValue(final Base64Variant bv, final OutputStream out)
    '''
def getValueAsInt():
    '''    public int getValueAsInt()
    public int getValueAsInt(final int def)
    '''
def getValueAsLong():
    '''    public long getValueAsLong()
    public long getValueAsLong(final long def)
    '''
def getValueAsDouble():
    '''    public double getValueAsDouble()
    public double getValueAsDouble(final double def)
    '''
def getValueAsBoolean():
    '''    public boolean getValueAsBoolean()
    public boolean getValueAsBoolean(final boolean def)
    '''
def getValueAsString():
    '''    public String getValueAsString()
    '''
def canReadObjectId():
    '''    public boolean canReadObjectId()
    '''
def canReadTypeId():
    '''    public boolean canReadTypeId()
    '''
def getObjectId():
    '''    public Object getObjectId()
    '''
def getTypeId():
    '''    public Object getTypeId()
    '''
def readValueAs():
    '''    public <T> T readValueAs(final Class<T> valueType)
    public <T> T readValueAs(final TypeReference<?> valueTypeRef)
    '''
def readValuesAs():
    '''    public <T> Iterator<T> readValuesAs(final Class<T> valueType)
    public <T> Iterator<T> readValuesAs(final TypeReference<?> valueTypeRef)
    '''
def readValueAsTree():
    '''    public <T extends TreeNode> T readValueAsTree()
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
