def setSchema():
'''public void setSchema(final FormatSchema schema)
'''
pass
def canUseSchema():
'''public boolean canUseSchema(final FormatSchema schema)
'''
pass
def version():
'''public Version version()
'''
pass
def getInputSource():
'''public Object getInputSource()
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
def setFeature():
'''public void setFeature(final Feature f, final boolean state)
'''
pass
def enableFeature():
'''public void enableFeature(final Feature f)
'''
pass
def disableFeature():
'''public void disableFeature(final Feature f)
'''
pass
def isFeatureEnabled():
'''public final boolean isFeatureEnabled(final Feature f)
'''
pass
def nextValue():
'''public JsonToken nextValue()
'''
pass
def nextFieldName():
'''public boolean nextFieldName(final SerializableString str)
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
def getCurrentToken():
'''public JsonToken getCurrentToken()
'''
pass
def hasCurrentToken():
'''public boolean hasCurrentToken()
'''
pass
def clearCurrentToken():
'''public void clearCurrentToken()
'''
pass
def getLastClearedToken():
'''public JsonToken getLastClearedToken()
'''
pass
def isExpectedStartArrayToken():
'''public boolean isExpectedStartArrayToken()
'''
pass
def hasTextCharacters():
'''public boolean hasTextCharacters()
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
def getValueAsInt():
'''public int getValueAsInt()
public int getValueAsInt(final int defaultValue)
'''
pass
def getValueAsLong():
'''public long getValueAsLong()
public long getValueAsLong(final long defaultValue)
'''
pass
def getValueAsDouble():
'''public double getValueAsDouble()
public double getValueAsDouble(final double defaultValue)
'''
pass
def getValueAsBoolean():
'''public boolean getValueAsBoolean()
public boolean getValueAsBoolean(final boolean defaultValue)
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
'''public JsonNode readValueAsTree()
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
