def JsonParserDelegate():
'''public JsonParserDelegate(final JsonParser d)
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
def setCodec():
'''public void setCodec(final ObjectCodec c)
'''
pass
def getCodec():
'''public ObjectCodec getCodec()
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
def overrideFormatFeatures():
'''public JsonParser overrideFormatFeatures(final int values, final int mask)
'''
pass
def getSchema():
'''public FormatSchema getSchema()
'''
pass
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
def requiresCustomCodec():
'''public boolean requiresCustomCodec()
'''
pass
def close():
'''public void close()
'''
pass
def isClosed():
'''public boolean isClosed()
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
def getCurrentToken():
'''public JsonToken getCurrentToken()
'''
pass
def getCurrentTokenId():
'''public int getCurrentTokenId()
'''
pass
def hasCurrentToken():
'''public boolean hasCurrentToken()
'''
pass
def hasTokenId():
'''public boolean hasTokenId(final int id)
'''
pass
def hasToken():
'''public boolean hasToken(final JsonToken t)
'''
pass
def getCurrentName():
'''public String getCurrentName()
'''
pass
def getCurrentLocation():
'''public JsonLocation getCurrentLocation()
'''
pass
def getParsingContext():
'''public JsonStreamContext getParsingContext()
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
def clearCurrentToken():
'''public void clearCurrentToken()
'''
pass
def getLastClearedToken():
'''public JsonToken getLastClearedToken()
'''
pass
def overrideCurrentName():
'''public void overrideCurrentName(final String name)
'''
pass
def getText():
'''public String getText()
public int getText(final Writer writer)
'''
pass
def hasTextCharacters():
'''public boolean hasTextCharacters()
'''
pass
def getTextCharacters():
'''public char[] getTextCharacters()
'''
pass
def getTextLength():
'''public int getTextLength()
'''
pass
def getTextOffset():
'''public int getTextOffset()
'''
pass
def getBigIntegerValue():
'''public BigInteger getBigIntegerValue()
'''
pass
def getBooleanValue():
'''public boolean getBooleanValue()
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
def getDecimalValue():
'''public BigDecimal getDecimalValue()
'''
pass
def getDoubleValue():
'''public double getDoubleValue()
'''
pass
def getFloatValue():
'''public float getFloatValue()
'''
pass
def getIntValue():
'''public int getIntValue()
'''
pass
def getLongValue():
'''public long getLongValue()
'''
pass
def getNumberType():
'''public NumberType getNumberType()
'''
pass
def getNumberValue():
'''public Number getNumberValue()
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
def getValueAsString():
'''public String getValueAsString()
public String getValueAsString(final String defaultValue)
'''
pass
def getEmbeddedObject():
'''public Object getEmbeddedObject()
'''
pass
def getBinaryValue():
'''public byte[] getBinaryValue(final Base64Variant b64variant)
'''
pass
def readBinaryValue():
'''public int readBinaryValue(final Base64Variant b64variant, final OutputStream out)
'''
pass
def getTokenLocation():
'''public JsonLocation getTokenLocation()
'''
pass
def nextToken():
'''public JsonToken nextToken()
'''
pass
def nextValue():
'''public JsonToken nextValue()
'''
pass
def finishToken():
'''public void finishToken()
'''
pass
def skipChildren():
'''public JsonParser skipChildren()
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
