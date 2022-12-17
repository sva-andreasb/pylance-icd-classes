def ():
    '''returns Vanilla\n\n
    ()\n
    (final JavaType listType, final JavaType mapType)\n
    (final UntypedObjectDeserializer base, final JsonDeserializer<?> mapDeser, final JsonDeserializer<?> listDeser, final JsonDeserializer<?> stringDeser, final JsonDeserializer<?> numberDeser)\n
    ()\n
    '''
def resolve():
    '''returns None\n\n
    resolve(final DeserializationContext ctxt)\n
    '''
def isCachable():
    '''returns boolean\n\n
    isCachable()\n
    '''
def supportsUpdate():
    '''returns Boolean\n\n
    supportsUpdate(final DeserializationConfig config)\n
    supportsUpdate(final DeserializationConfig config)\n
    '''
def deserialize():
    '''returns Object\n\n
    deserialize(final JsonParser p, final DeserializationContext ctxt)\n
    deserialize(final JsonParser p, final DeserializationContext ctxt, final Object intoValue)\n
    deserialize(final JsonParser p, final DeserializationContext ctxt)\n
    deserialize(final JsonParser p, final DeserializationContext ctxt, final Object intoValue)\n
    '''
def deserializeWithType():
    '''returns Object\n\n
    deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)\n
    deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)\n
    '''
