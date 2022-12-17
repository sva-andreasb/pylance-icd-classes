def ():
    '''returns ArrayNode\n\n
    (final JsonNodeFactory nf)\n
    (final JsonNodeFactory nf, final int capacity)\n
    (final JsonNodeFactory nf, final List<JsonNode> children)\n
    '''
def deepCopy():
    '''returns ArrayNode\n\n
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
def isArray():
    '''returns boolean\n\n
    isArray()\n
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
def path():
    '''returns JsonNode\n\n
    path(final String fieldName)\n
    path(final int index)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Comparator<JsonNode> comparator, final JsonNode o)\n
    equals(final Object o)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final JsonGenerator f, final SerializerProvider provider)\n
    '''
def serializeWithType():
    '''returns None\n\n
    serializeWithType(final JsonGenerator g, final SerializerProvider provider, final TypeSerializer typeSer)\n
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
def set():
    '''returns JsonNode\n\n
    set(final int index, JsonNode value)\n
    '''
def add():
    '''returns ArrayNode\n\n
    add(JsonNode value)\n
    add(final int v)\n
    add(final Integer value)\n
    add(final long v)\n
    add(final Long value)\n
    add(final float v)\n
    add(final Float value)\n
    add(final double v)\n
    add(final Double value)\n
    add(final BigDecimal v)\n
    add(final BigInteger v)\n
    add(final String v)\n
    add(final boolean v)\n
    add(final Boolean value)\n
    add(final byte[] v)\n
    '''
def addAll():
    '''returns ArrayNode\n\n
    addAll(final ArrayNode other)\n
    addAll(final Collection<? extends JsonNode> nodes)\n
    '''
def insert():
    '''returns ArrayNode\n\n
    insert(final int index, JsonNode value)\n
    insert(final int index, final int v)\n
    insert(final int index, final Integer value)\n
    insert(final int index, final long v)\n
    insert(final int index, final Long value)\n
    insert(final int index, final float v)\n
    insert(final int index, final Float value)\n
    insert(final int index, final double v)\n
    insert(final int index, final Double value)\n
    insert(final int index, final BigDecimal v)\n
    insert(final int index, final BigInteger v)\n
    insert(final int index, final String v)\n
    insert(final int index, final boolean v)\n
    insert(final int index, final Boolean value)\n
    insert(final int index, final byte[] v)\n
    '''
def remove():
    '''returns JsonNode\n\n
    remove(final int index)\n
    '''
def removeAll():
    '''returns ArrayNode\n\n
    removeAll()\n
    '''
def addArray():
    '''returns ArrayNode\n\n
    addArray()\n
    '''
def addObject():
    '''returns ObjectNode\n\n
    addObject()\n
    '''
def addPOJO():
    '''returns ArrayNode\n\n
    addPOJO(final Object value)\n
    '''
def addRawValue():
    '''returns ArrayNode\n\n
    addRawValue(final RawValue raw)\n
    '''
def addNull():
    '''returns ArrayNode\n\n
    addNull()\n
    '''
def insertArray():
    '''returns ArrayNode\n\n
    insertArray(final int index)\n
    '''
def insertObject():
    '''returns ObjectNode\n\n
    insertObject(final int index)\n
    '''
def insertPOJO():
    '''returns ArrayNode\n\n
    insertPOJO(final int index, final Object value)\n
    '''
def insertNull():
    '''returns ArrayNode\n\n
    insertNull(final int index)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
