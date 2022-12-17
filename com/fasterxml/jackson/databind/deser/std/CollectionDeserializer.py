def ():
    '''returns CollectionReferringAccumulator\n\n
    (final JavaType collectionType, final JsonDeserializer<Object> valueDeser, final TypeDeserializer valueTypeDeser, final ValueInstantiator valueInstantiator)\n
    (final Class<?> elementType, final Collection<Object> result)\n
    '''
def isCachable():
    '''returns boolean\n\n
    isCachable()\n
    '''
def createContextual():
    '''returns CollectionDeserializer\n\n
    createContextual(final DeserializationContext ctxt, final BeanProperty property)\n
    '''
def getContentDeserializer():
    '''returns JsonDeserializer<Object>\n\n
    getContentDeserializer()\n
    '''
def getValueInstantiator():
    '''returns ValueInstantiator\n\n
    getValueInstantiator()\n
    '''
def deserialize():
    '''returns Collection<Object>\n\n
    deserialize(final JsonParser p, final DeserializationContext ctxt)\n
    deserialize(final JsonParser p, final DeserializationContext ctxt, final Collection<Object> result)\n
    '''
def deserializeWithType():
    '''returns Object\n\n
    deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)\n
    '''
def add():
    '''returns None\n\n
    add(final Object value)\n
    '''
def resolveForwardReference():
    '''returns None\n\n
    resolveForwardReference(final Object id, final Object value)\n
    '''
def handleResolvedForwardReference():
    '''returns None\n\n
    handleResolvedForwardReference(final Object id, final Object value)\n
    '''
