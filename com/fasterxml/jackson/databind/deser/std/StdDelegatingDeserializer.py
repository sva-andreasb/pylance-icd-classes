def ():
    '''returns StdDelegatingDeserializer\n\n
    (final Converter<?, T> converter)\n
    (final Converter<Object, T> converter, final JavaType delegateType, final JsonDeserializer<?> delegateDeserializer)\n
    '''
def resolve():
    '''returns None\n\n
    resolve(final DeserializationContext ctxt)\n
    '''
def supportsUpdate():
    '''returns Boolean\n\n
    supportsUpdate(final DeserializationConfig config)\n
    '''
def deserialize():
    '''returns T\n\n
    deserialize(final JsonParser p, final DeserializationContext ctxt)\n
    deserialize(final JsonParser p, final DeserializationContext ctxt, final Object intoValue)\n
    '''
def deserializeWithType():
    '''returns Object\n\n
    deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)\n
    '''
