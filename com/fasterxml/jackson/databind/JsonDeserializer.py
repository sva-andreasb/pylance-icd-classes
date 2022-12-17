def deserialize():
    '''returns T\n\n
    deserialize(final JsonParser p, final DeserializationContext ctxt, final T intoValue)\n
    '''
def deserializeWithType():
    '''returns Object\n\n
    deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)\n
    '''
def unwrappingDeserializer():
    '''returns JsonDeserializer<T>\n\n
    unwrappingDeserializer(final NameTransformer unwrapper)\n
    '''
def isCachable():
    '''returns boolean\n\n
    isCachable()\n
    '''
def getKnownPropertyNames():
    '''returns Collection<Object>\n\n
    getKnownPropertyNames()\n
    '''
def getNullValue():
    '''returns T\n\n
    getNullValue(final DeserializationContext ctxt)\n
    getNullValue()\n
    '''
def getNullAccessPattern():
    '''returns AccessPattern\n\n
    getNullAccessPattern()\n
    '''
def getEmptyAccessPattern():
    '''returns AccessPattern\n\n
    getEmptyAccessPattern()\n
    '''
def getEmptyValue():
    '''returns Object\n\n
    getEmptyValue(final DeserializationContext ctxt)\n
    getEmptyValue()\n
    '''
def getObjectIdReader():
    '''returns ObjectIdReader\n\n
    getObjectIdReader()\n
    '''
def findBackReference():
    '''returns SettableBeanProperty\n\n
    findBackReference(final String refName)\n
    '''
def supportsUpdate():
    '''returns Boolean\n\n
    supportsUpdate(final DeserializationConfig config)\n
    '''
