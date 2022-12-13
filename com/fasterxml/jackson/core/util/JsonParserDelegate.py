def JsonParserDelegate():
    '''public JsonParserDelegate(final JsonParser d)
    '''
def getCurrentValue():
    '''public Object getCurrentValue()
    '''
def setCurrentValue():
    '''public void setCurrentValue(final Object v)
    '''
def setCodec():
    '''public void setCodec(final ObjectCodec c)
    '''
def getCodec():
    '''public ObjectCodec getCodec()
    '''
def enable():
    '''public JsonParser enable(final Feature f)
    '''
def disable():
    '''public JsonParser disable(final Feature f)
    '''
def isEnabled():
    '''public boolean isEnabled(final Feature f)
    '''
def getFeatureMask():
    '''public int getFeatureMask()
    '''
def setFeatureMask():
    '''public JsonParser setFeatureMask(final int mask)
    '''
def overrideStdFeatures():
    '''public JsonParser overrideStdFeatures(final int values, final int mask)
    '''
def overrideFormatFeatures():
    '''public JsonParser overrideFormatFeatures(final int values, final int mask)
    '''
def getSchema():
    '''public FormatSchema getSchema()
    '''
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
def requiresCustomCodec():
    '''public boolean requiresCustomCodec()
    '''
def close():
    '''public void close()
    '''
def isClosed():
    '''public boolean isClosed()
    '''
def currentToken():
    '''public JsonToken currentToken()
    '''
def currentTokenId():
    '''public int currentTokenId()
    '''
def getCurrentToken():
    '''public JsonToken getCurrentToken()
    '''
def getCurrentTokenId():
    '''public int getCurrentTokenId()
    '''
def hasCurrentToken():
    '''public boolean hasCurrentToken()
    '''
def hasTokenId():
    '''public boolean hasTokenId(final int id)
    '''
def hasToken():
    '''public boolean hasToken(final JsonToken t)
    '''
def getCurrentName():
    '''public String getCurrentName()
    '''
def getCurrentLocation():
    '''public JsonLocation getCurrentLocation()
    '''
def getParsingContext():
    '''public JsonStreamContext getParsingContext()
    '''
def isExpectedStartArrayToken():
    '''public boolean isExpectedStartArrayToken()
    '''
def isExpectedStartObjectToken():
    '''public boolean isExpectedStartObjectToken()
    '''
def isNaN():
    '''public boolean isNaN()
    '''
def clearCurrentToken():
    '''public void clearCurrentToken()
    '''
def getLastClearedToken():
    '''public JsonToken getLastClearedToken()
    '''
def overrideCurrentName():
    '''public void overrideCurrentName(final String name)
    '''
def getText():
    '''public String getText()
    public int getText(final Writer writer)
    '''
def hasTextCharacters():
    '''public boolean hasTextCharacters()
    '''
def getTextCharacters():
    '''public char[] getTextCharacters()
    '''
def getTextLength():
    '''public int getTextLength()
    '''
def getTextOffset():
    '''public int getTextOffset()
    '''
def getBigIntegerValue():
    '''public BigInteger getBigIntegerValue()
    '''
def getBooleanValue():
    '''public boolean getBooleanValue()
    '''
def getByteValue():
    '''public byte getByteValue()
    '''
def getShortValue():
    '''public short getShortValue()
    '''
def getDecimalValue():
    '''public BigDecimal getDecimalValue()
    '''
def getDoubleValue():
    '''public double getDoubleValue()
    '''
def getFloatValue():
    '''public float getFloatValue()
    '''
def getIntValue():
    '''public int getIntValue()
    '''
def getLongValue():
    '''public long getLongValue()
    '''
def getNumberType():
    '''public NumberType getNumberType()
    '''
def getNumberValue():
    '''public Number getNumberValue()
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
def getValueAsString():
    '''public String getValueAsString()
    public String getValueAsString(final String defaultValue)
    '''
def getEmbeddedObject():
    '''public Object getEmbeddedObject()
    '''
def getBinaryValue():
    '''public byte[] getBinaryValue(final Base64Variant b64variant)
    '''
def readBinaryValue():
    '''public int readBinaryValue(final Base64Variant b64variant, final OutputStream out)
    '''
def getTokenLocation():
    '''public JsonLocation getTokenLocation()
    '''
def nextToken():
    '''public JsonToken nextToken()
    '''
def nextValue():
    '''public JsonToken nextValue()
    '''
def finishToken():
    '''public void finishToken()
    '''
def skipChildren():
    '''public JsonParser skipChildren()
    '''
def canReadObjectId():
    '''public boolean canReadObjectId()
    '''
def canReadTypeId():
    '''public boolean canReadTypeId()
    '''
def getObjectId():
    '''public Object getObjectId()
    '''
def getTypeId():
    '''public Object getTypeId()
    '''
