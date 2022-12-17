def ():
    '''returns EnumSetDeserializer\n\n
    (final JavaType enumType, final JsonDeserializer<?> deser)\n
    '''
def withDeserializer():
    '''returns EnumSetDeserializer\n\n
    withDeserializer(final JsonDeserializer<?> deser)\n
    '''
def withResolved():
    '''returns EnumSetDeserializer\n\n
    withResolved(final JsonDeserializer<?> deser, final Boolean unwrapSingle)\n
    '''
def isCachable():
    '''returns boolean\n\n
    isCachable()\n
    '''
def supportsUpdate():
    '''returns Boolean\n\n
    supportsUpdate(final DeserializationConfig config)\n
    '''
def deserializeWithType():
    '''returns Object\n\n
    deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)\n
    '''
