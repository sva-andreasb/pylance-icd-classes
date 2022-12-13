def isValueNode():
    '''public boolean isValueNode()
    '''
def isContainerNode():
    '''public boolean isContainerNode()
    '''
def isMissingNode():
    '''public boolean isMissingNode()
    '''
def isArray():
    '''public boolean isArray()
    '''
def isObject():
    '''public boolean isObject()
    '''
def isPojo():
    '''public boolean isPojo()
    '''
def isNumber():
    '''public boolean isNumber()
    '''
def isIntegralNumber():
    '''public boolean isIntegralNumber()
    '''
def isFloatingPointNumber():
    '''public boolean isFloatingPointNumber()
    '''
def isInt():
    '''public boolean isInt()
    '''
def isLong():
    '''public boolean isLong()
    '''
def isDouble():
    '''public boolean isDouble()
    '''
def isBigDecimal():
    '''public boolean isBigDecimal()
    '''
def isBigInteger():
    '''public boolean isBigInteger()
    '''
def isTextual():
    '''public boolean isTextual()
    '''
def isBoolean():
    '''public boolean isBoolean()
    '''
def isNull():
    '''public boolean isNull()
    '''
def isBinary():
    '''public boolean isBinary()
    '''
def getTextValue():
    '''public String getTextValue()
    '''
def getBinaryValue():
    '''public byte[] getBinaryValue()
    '''
def getBooleanValue():
    '''public boolean getBooleanValue()
    '''
def getNumberValue():
    '''public Number getNumberValue()
    '''
def getIntValue():
    '''public int getIntValue()
    '''
def getLongValue():
    '''public long getLongValue()
    '''
def getDoubleValue():
    '''public double getDoubleValue()
    '''
def getDecimalValue():
    '''public BigDecimal getDecimalValue()
    '''
def getBigIntegerValue():
    '''public BigInteger getBigIntegerValue()
    '''
def get():
    '''public JsonNode get(final int index)
    public JsonNode get(final String fieldName)
    '''
def asInt():
    '''public int asInt()
    public int asInt(final int defaultValue)
    '''
def asLong():
    '''public long asLong()
    public long asLong(final long defaultValue)
    '''
def asDouble():
    '''public double asDouble()
    public double asDouble(final double defaultValue)
    '''
def asBoolean():
    '''public boolean asBoolean()
    public boolean asBoolean(final boolean defaultValue)
    '''
def getValueAsText():
    '''public String getValueAsText()
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
def has():
    '''public boolean has(final String fieldName)
    public boolean has(final int index)
    '''
def findValues():
    '''public final List<JsonNode> findValues(final String fieldName)
    '''
def findValuesAsText():
    '''public final List<String> findValuesAsText(final String fieldName)
    '''
def findParents():
    '''public final List<JsonNode> findParents(final String fieldName)
    '''
def size():
    '''public int size()
    '''
def iterator():
    '''public final Iterator<JsonNode> iterator()
    '''
def getElements():
    '''public Iterator<JsonNode> getElements()
    '''
def getFieldNames():
    '''public Iterator<String> getFieldNames()
    '''
def getPath():
    '''public final JsonNode getPath(final String fieldName)
    public final JsonNode getPath(final int index)
    '''
def with():
    '''public JsonNode with(final String propertyName)
    '''
