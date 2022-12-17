def ():
    '''returns EnumMapDeserializer\n\n
    (final JavaType mapType, final ValueInstantiator valueInst, final KeyDeserializer keyDeser, final JsonDeserializer<?> valueDeser, final TypeDeserializer vtd, final NullValueProvider nuller)\n
    (final JavaType mapType, final KeyDeserializer keyDeser, final JsonDeserializer<?> valueDeser, final TypeDeserializer vtd)\n
    '''
def withResolved():
    '''returns EnumMapDeserializer\n\n
    withResolved(final KeyDeserializer keyDeserializer, final JsonDeserializer<?> valueDeserializer, final TypeDeserializer valueTypeDeser, final NullValueProvider nuller)\n
    '''
def resolve():
    '''returns None\n\n
    resolve(final DeserializationContext ctxt)\n
    '''
def isCachable():
    '''returns boolean\n\n
    isCachable()\n
    '''
def getContentDeserializer():
    '''returns JsonDeserializer<Object>\n\n
    getContentDeserializer()\n
    '''
def getEmptyValue():
    '''returns Object\n\n
    getEmptyValue(final DeserializationContext ctxt)\n
    '''
def deserializeWithType():
    '''returns Object\n\n
    deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)\n
    '''
