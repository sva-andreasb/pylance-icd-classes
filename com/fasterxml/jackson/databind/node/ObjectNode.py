def ():
    '''returns ObjectNode\n\n
    (final JsonNodeFactory nc)\n
    (final JsonNodeFactory nc, final Map<String, JsonNode> kids)\n
    '''
def deepCopy():
    '''returns ObjectNode\n\n
    deepCopy()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty(final SerializerProvider serializers)\n
    '''
def getNodeType():
    '''returns JsonNodeType\n\n
    getNodeType()\n
    '''
def asToken():
    '''returns JsonToken\n\n
    asToken()\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def elements():
    '''returns Iterator<JsonNode>\n\n
    elements()\n
    '''
def get():
    '''returns JsonNode\n\n
    get(final int index)\n
    get(final String fieldName)\n
    '''
def fieldNames():
    '''returns Iterator<String>\n\n
    fieldNames()\n
    '''
def path():
    '''returns JsonNode\n\n
    path(final int index)\n
    path(final String fieldName)\n
    '''
def with():
    '''returns ObjectNode\n\n
    with(final String propertyName)\n
    '''
def withArray():
    '''returns ArrayNode\n\n
    withArray(final String propertyName)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Comparator<JsonNode> comparator, final JsonNode o)\n
    equals(final Object o)\n
    '''
def findValue():
    '''returns JsonNode\n\n
    findValue(final String fieldName)\n
    '''
def findValues():
    '''returns List<JsonNode>\n\n
    findValues(final String fieldName, List<JsonNode> foundSoFar)\n
    '''
def findValuesAsText():
    '''returns List<String>\n\n
    findValuesAsText(final String fieldName, List<String> foundSoFar)\n
    '''
def findParent():
    '''returns ObjectNode\n\n
    findParent(final String fieldName)\n
    '''
def findParents():
    '''returns List<JsonNode>\n\n
    findParents(final String fieldName, List<JsonNode> foundSoFar)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final JsonGenerator g, final SerializerProvider provider)\n
    '''
def serializeWithType():
    '''returns None\n\n
    serializeWithType(final JsonGenerator g, final SerializerProvider provider, final TypeSerializer typeSer)\n
    '''
def set():
    '''returns JsonNode\n\n
    set(final String fieldName, JsonNode value)\n
    '''
def setAll():
    '''returns JsonNode\n\n
    setAll(final Map<String, ? extends JsonNode> properties)\n
    setAll(final ObjectNode other)\n
    '''
def replace():
    '''returns JsonNode\n\n
    replace(final String fieldName, JsonNode value)\n
    '''
def without():
    '''returns ObjectNode\n\n
    without(final String fieldName)\n
    without(final Collection<String> fieldNames)\n
    '''
def put():
    '''returns ObjectNode\n\n
    put(final String fieldName, JsonNode value)\n
    put(final String fieldName, final short v)\n
    put(final String fieldName, final Short v)\n
    put(final String fieldName, final int v)\n
    put(final String fieldName, final Integer v)\n
    put(final String fieldName, final long v)\n
    put(final String fieldName, final Long v)\n
    put(final String fieldName, final float v)\n
    put(final String fieldName, final Float v)\n
    put(final String fieldName, final double v)\n
    put(final String fieldName, final Double v)\n
    put(final String fieldName, final BigDecimal v)\n
    put(final String fieldName, final BigInteger v)\n
    put(final String fieldName, final String v)\n
    put(final String fieldName, final boolean v)\n
    put(final String fieldName, final Boolean v)\n
    put(final String fieldName, final byte[] v)\n
    '''
def remove():
    '''returns ObjectNode\n\n
    remove(final String fieldName)\n
    remove(final Collection<String> fieldNames)\n
    '''
def removeAll():
    '''returns ObjectNode\n\n
    removeAll()\n
    '''
def putAll():
    '''returns JsonNode\n\n
    putAll(final Map<String, ? extends JsonNode> properties)\n
    putAll(final ObjectNode other)\n
    '''
def retain():
    '''returns ObjectNode\n\n
    retain(final Collection<String> fieldNames)\n
    retain(final String... fieldNames)\n
    '''
def putArray():
    '''returns ArrayNode\n\n
    putArray(final String fieldName)\n
    '''
def putObject():
    '''returns ObjectNode\n\n
    putObject(final String fieldName)\n
    '''
def putPOJO():
    '''returns ObjectNode\n\n
    putPOJO(final String fieldName, final Object pojo)\n
    '''
def putRawValue():
    '''returns ObjectNode\n\n
    putRawValue(final String fieldName, final RawValue raw)\n
    '''
def putNull():
    '''returns ObjectNode\n\n
    putNull(final String fieldName)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
