def setSchema():
    '''public void setSchema(final FormatSchema schema)
    '''
def canUseSchema():
    '''public boolean canUseSchema(final FormatSchema schema)
    '''
def version():
    '''public Version version()
    '''
def getInputSource():
    '''public Object getInputSource()
    '''
def releaseBuffered():
    '''public int releaseBuffered(final OutputStream out)
    public int releaseBuffered(final Writer w)
    '''
def enable():
    '''public JsonParser enable(final Feature f)
    '''
def disable():
    '''public JsonParser disable(final Feature f)
    '''
def configure():
    '''public JsonParser configure(final Feature f, final boolean state)
    '''
def isEnabled():
    '''public boolean isEnabled(final Feature f)
    '''
def setFeature():
    '''public void setFeature(final Feature f, final boolean state)
    '''
def enableFeature():
    '''public void enableFeature(final Feature f)
    '''
def disableFeature():
    '''public void disableFeature(final Feature f)
    '''
def isFeatureEnabled():
    '''public final boolean isFeatureEnabled(final Feature f)
    '''
def nextValue():
    '''public JsonToken nextValue()
    '''
def nextFieldName():
    '''public boolean nextFieldName(final SerializableString str)
    '''
def nextTextValue():
    '''public String nextTextValue()
    '''
def nextIntValue():
    '''public int nextIntValue(final int defaultValue)
    '''
def nextLongValue():
    '''public long nextLongValue(final long defaultValue)
    '''
def nextBooleanValue():
    '''public Boolean nextBooleanValue()
    '''
def getCurrentToken():
    '''public JsonToken getCurrentToken()
    '''
def hasCurrentToken():
    '''public boolean hasCurrentToken()
    '''
def clearCurrentToken():
    '''public void clearCurrentToken()
    '''
def getLastClearedToken():
    '''public JsonToken getLastClearedToken()
    '''
def isExpectedStartArrayToken():
    '''public boolean isExpectedStartArrayToken()
    '''
def hasTextCharacters():
    '''public boolean hasTextCharacters()
    '''
def getByteValue():
    '''public byte getByteValue()
    '''
def getShortValue():
    '''public short getShortValue()
    '''
def getBooleanValue():
    '''public boolean getBooleanValue()
    '''
def getEmbeddedObject():
    '''public Object getEmbeddedObject()
    '''
def getBinaryValue():
    '''public byte[] getBinaryValue()
    '''
def getValueAsInt():
    '''public int getValueAsInt()
    public int getValueAsInt(final int defaultValue)
    '''
def getValueAsLong():
    '''public long getValueAsLong()
    public long getValueAsLong(final long defaultValue)
    '''
def getValueAsDouble():
    '''public double getValueAsDouble()
    public double getValueAsDouble(final double defaultValue)
    '''
def getValueAsBoolean():
    '''public boolean getValueAsBoolean()
    public boolean getValueAsBoolean(final boolean defaultValue)
    '''
def readValueAs():
    '''public <T> T readValueAs(final Class<T> valueType)
    public <T> T readValueAs(final TypeReference<?> valueTypeRef)
    '''
def readValuesAs():
    '''public <T> Iterator<T> readValuesAs(final Class<T> valueType)
    public <T> Iterator<T> readValuesAs(final TypeReference<?> valueTypeRef)
    '''
def readValueAsTree():
    '''public JsonNode readValueAsTree()
    '''
def collectDefaults():
    '''public static int collectDefaults()
    '''
def enabledByDefault():
    '''public boolean enabledByDefault()
    '''
def enabledIn():
    '''public boolean enabledIn(final int flags)
    '''
def getMask():
    '''public int getMask()
    '''
