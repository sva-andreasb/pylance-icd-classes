def ():
    '''returns MapReferringAccumulator\n\n
    (final JavaType mapType, final ValueInstantiator valueInstantiator, final KeyDeserializer keyDeser, final JsonDeserializer<Object> valueDeser, final TypeDeserializer valueTypeDeser)\n
    (final Class<?> valueType, final Map<Object, Object> result)\n
    '''
def setIgnorableProperties():
    '''returns None\n\n
    setIgnorableProperties(final String[] ignorable)\n
    setIgnorableProperties(final Set<String> ignorable)\n
    '''
def resolve():
    '''returns None\n\n
    resolve(final DeserializationContext ctxt)\n
    '''
def getContentDeserializer():
    '''returns JsonDeserializer<Object>\n\n
    getContentDeserializer()\n
    '''
def getValueInstantiator():
    '''returns ValueInstantiator\n\n
    getValueInstantiator()\n
    '''
def isCachable():
    '''returns boolean\n\n
    isCachable()\n
    '''
def deserializeWithType():
    '''returns Object\n\n
    deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)\n
    '''
def getValueType():
    '''returns JavaType\n\n
    getValueType()\n
    '''
def put():
    '''returns None\n\n
    put(final Object key, final Object value)\n
    '''
def resolveForwardReference():
    '''returns None\n\n
    resolveForwardReference(final Object id, final Object value)\n
    '''
def handleResolvedForwardReference():
    '''returns None\n\n
    handleResolvedForwardReference(final Object id, final Object value)\n
    '''
