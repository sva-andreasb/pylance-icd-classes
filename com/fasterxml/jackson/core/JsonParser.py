def getInputSource():
'''public Object getInputSource()
'''
pass
def getCurrentValue():
'''public Object getCurrentValue()
'''
pass
def setCurrentValue():
'''public void setCurrentValue(final Object v)
'''
pass
def setRequestPayloadOnError():
'''public void setRequestPayloadOnError(final RequestPayload payload)
public void setRequestPayloadOnError(final byte[] payload, final String charset)
public void setRequestPayloadOnError(final String payload)
'''
pass
def setSchema():
'''public void setSchema(final FormatSchema schema)
'''
pass
def getSchema():
'''public FormatSchema getSchema()
'''
pass
def canUseSchema():
'''public boolean canUseSchema(final FormatSchema schema)
'''
pass
def requiresCustomCodec():
'''public boolean requiresCustomCodec()
'''
pass
def canParseAsync():
'''public boolean canParseAsync()
'''
pass
def getNonBlockingInputFeeder():
'''public NonBlockingInputFeeder getNonBlockingInputFeeder()
'''
pass
def releaseBuffered():
'''public int releaseBuffered(final OutputStream out)
public int releaseBuffered(final Writer w)
'''
pass
def enable():
'''public JsonParser enable(final Feature f)
'''
pass
def disable():
'''public JsonParser disable(final Feature f)
'''
pass
def configure():
'''public JsonParser configure(final Feature f, final boolean state)
'''
pass
def isEnabled():
'''public boolean isEnabled(final Feature f)
'''
pass
def getFeatureMask():
'''public int getFeatureMask()
'''
pass
def setFeatureMask():
'''public JsonParser setFeatureMask(final int mask)
'''
pass
def overrideStdFeatures():
'''public JsonParser overrideStdFeatures(final int values, final int mask)
'''
pass
def getFormatFeatures():
'''public int getFormatFeatures()
'''
pass
def overrideFormatFeatures():
'''public JsonParser overrideFormatFeatures(final int values, final int mask)
'''
pass
def nextFieldName():
'''public boolean nextFieldName(final SerializableString str)
public String nextFieldName()
'''
pass
def nextTextValue():
'''public String nextTextValue()
'''
pass
def nextIntValue():
'''public int nextIntValue(final int defaultValue)
'''
pass
def nextLongValue():
'''public long nextLongValue(final long defaultValue)
'''
pass
def nextBooleanValue():
'''public Boolean nextBooleanValue()
'''
pass
def finishToken():
'''public void finishToken()
'''
pass
def currentToken():
'''public JsonToken currentToken()
'''
pass
def currentTokenId():
'''public int currentTokenId()
'''
pass
def isExpectedStartArrayToken():
'''public boolean isExpectedStartArrayToken()
'''
pass
def isExpectedStartObjectToken():
'''public boolean isExpectedStartObjectToken()
'''
pass
def isNaN():
'''public boolean isNaN()
'''
pass
def currentName():
'''public String currentName()
'''
pass
def getText():
'''public int getText(final Writer writer)
'''
pass
def getByteValue():
'''public byte getByteValue()
'''
pass
def getShortValue():
'''public short getShortValue()
'''
pass
def getBooleanValue():
'''public boolean getBooleanValue()
'''
pass
def getEmbeddedObject():
'''public Object getEmbeddedObject()
'''
pass
def getBinaryValue():
'''public byte[] getBinaryValue()
'''
pass
def readBinaryValue():
'''public int readBinaryValue(final OutputStream out)
public int readBinaryValue(final Base64Variant bv, final OutputStream out)
'''
pass
def getValueAsInt():
'''public int getValueAsInt()
public int getValueAsInt(final int def)
'''
pass
def getValueAsLong():
'''public long getValueAsLong()
public long getValueAsLong(final long def)
'''
pass
def getValueAsDouble():
'''public double getValueAsDouble()
public double getValueAsDouble(final double def)
'''
pass
def getValueAsBoolean():
'''public boolean getValueAsBoolean()
public boolean getValueAsBoolean(final boolean def)
'''
pass
def getValueAsString():
'''public String getValueAsString()
'''
pass
def canReadObjectId():
'''public boolean canReadObjectId()
'''
pass
def canReadTypeId():
'''public boolean canReadTypeId()
'''
pass
def getObjectId():
'''public Object getObjectId()
'''
pass
def getTypeId():
'''public Object getTypeId()
'''
pass
def readValueAs():
'''public <T> T readValueAs(final Class<T> valueType)
public <T> T readValueAs(final TypeReference<?> valueTypeRef)
'''
pass
def readValuesAs():
'''public <T> Iterator<T> readValuesAs(final Class<T> valueType)
public <T> Iterator<T> readValuesAs(final TypeReference<?> valueTypeRef)
'''
pass
def readValueAsTree():
'''public <T extends TreeNode> T readValueAsTree()
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
