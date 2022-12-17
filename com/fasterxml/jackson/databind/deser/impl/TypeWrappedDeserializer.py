def ():
    '''returns TypeWrappedDeserializer\n\n
    (final TypeDeserializer typeDeser, final JsonDeserializer<?> deser)\n
    '''
def supportsUpdate():
    '''returns Boolean\n\n
    supportsUpdate(final DeserializationConfig config)\n
    '''
def getKnownPropertyNames():
    '''returns Collection<Object>\n\n
    getKnownPropertyNames()\n
    '''
def getNullValue():
    '''returns Object\n\n
    getNullValue(final DeserializationContext ctxt)\n
    '''
def getEmptyValue():
    '''returns Object\n\n
    getEmptyValue(final DeserializationContext ctxt)\n
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
