def ():
    '''returns StringCollectionDeserializer\n\n
    (final JavaType collectionType, final JsonDeserializer<?> valueDeser, final ValueInstantiator valueInstantiator)\n
    '''
def isCachable():
    '''returns boolean\n\n
    isCachable()\n
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
    '''returns Collection<String>\n\n
    deserialize(final JsonParser p, final DeserializationContext ctxt)\n
    deserialize(final JsonParser p, final DeserializationContext ctxt, final Collection<String> result)\n
    '''
def deserializeWithType():
    '''returns Object\n\n
    deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)\n
    '''
