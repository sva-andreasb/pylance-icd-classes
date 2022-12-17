def ():
    '''returns DelegatingDeserializer\n\n
    (final JsonDeserializer<?> d)\n
    '''
def resolve():
    '''returns None\n\n
    resolve(final DeserializationContext ctxt)\n
    '''
def deserialize():
    '''returns Object\n\n
    deserialize(final JsonParser p, final DeserializationContext ctxt)\n
    deserialize(final JsonParser p, final DeserializationContext ctxt, final Object intoValue)\n
    '''
def deserializeWithType():
    '''returns Object\n\n
    deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)\n
    '''
def isCachable():
    '''returns boolean\n\n
    isCachable()\n
    '''
def supportsUpdate():
    '''returns Boolean\n\n
    supportsUpdate(final DeserializationConfig config)\n
    '''
def findBackReference():
    '''returns SettableBeanProperty\n\n
    findBackReference(final String logicalName)\n
    '''
def getNullAccessPattern():
    '''returns AccessPattern\n\n
    getNullAccessPattern()\n
    '''
def getNullValue():
    '''returns Object\n\n
    getNullValue(final DeserializationContext ctxt)\n
    '''
def getEmptyValue():
    '''returns Object\n\n
    getEmptyValue(final DeserializationContext ctxt)\n
    '''
def getKnownPropertyNames():
    '''returns Collection<Object>\n\n
    getKnownPropertyNames()\n
    '''
def getObjectIdReader():
    '''returns ObjectIdReader\n\n
    getObjectIdReader()\n
    '''
