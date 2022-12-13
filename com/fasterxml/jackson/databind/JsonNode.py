def size():
    '''public int size()
    '''
def isValueNode():
    '''public final boolean isValueNode()
    '''
def isContainerNode():
    '''public final boolean isContainerNode()
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
def get():
    '''public JsonNode get(final String fieldName)
    '''
def fieldNames():
    '''public Iterator<String> fieldNames()
    '''
def at():
    '''public final JsonNode at(final JsonPointer ptr)
    public final JsonNode at(final String jsonPtrExpr)
    '''
def isPojo():
    '''public final boolean isPojo()
    '''
def isNumber():
    '''public final boolean isNumber()
    '''
def isIntegralNumber():
    '''public boolean isIntegralNumber()
    '''
def isFloatingPointNumber():
    '''public boolean isFloatingPointNumber()
    '''
def isShort():
    '''public boolean isShort()
    '''
def isInt():
    '''public boolean isInt()
    '''
def isLong():
    '''public boolean isLong()
    '''
def isFloat():
    '''public boolean isFloat()
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
    '''public final boolean isTextual()
    '''
def isBoolean():
    '''public final boolean isBoolean()
    '''
def isNull():
    '''public final boolean isNull()
    '''
def isBinary():
    '''public final boolean isBinary()
    '''
def canConvertToInt():
    '''public boolean canConvertToInt()
    '''
def canConvertToLong():
    '''public boolean canConvertToLong()
    '''
def textValue():
    '''public String textValue()
    '''
def binaryValue():
    '''public byte[] binaryValue()
    '''
def booleanValue():
    '''public boolean booleanValue()
    '''
def numberValue():
    '''public Number numberValue()
    '''
def shortValue():
    '''public short shortValue()
    '''
def intValue():
    '''public int intValue()
    '''
def longValue():
    '''public long longValue()
    '''
def floatValue():
    '''public float floatValue()
    '''
def doubleValue():
    '''public double doubleValue()
    '''
def decimalValue():
    '''public BigDecimal decimalValue()
    '''
def bigIntegerValue():
    '''public BigInteger bigIntegerValue()
    '''
def asText():
    '''public String asText(final String defaultValue)
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
def has():
    '''public boolean has(final String fieldName)
    public boolean has(final int index)
    '''
def hasNonNull():
    '''public boolean hasNonNull(final String fieldName)
    public boolean hasNonNull(final int index)
    '''
def iterator():
    '''public final Iterator<JsonNode> iterator()
    '''
def elements():
    '''public Iterator<JsonNode> elements()
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
def with():
    '''public JsonNode with(final String propertyName)
    '''
def withArray():
    '''public JsonNode withArray(final String propertyName)
    '''
def equals():
    '''public boolean equals(final Comparator<JsonNode> comparator, final JsonNode other)
    '''
