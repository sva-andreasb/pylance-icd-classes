def ():
    '''returns ObjectArrayDeserializer\n\n
    (final JavaType arrayType, final JsonDeserializer<Object> elemDeser, final TypeDeserializer elemTypeDeser)\n
    '''
def withDeserializer():
    '''returns ObjectArrayDeserializer\n\n
    withDeserializer(final TypeDeserializer elemTypeDeser, final JsonDeserializer<?> elemDeser)\n
    '''
def withResolved():
    '''returns ObjectArrayDeserializer\n\n
    withResolved(final TypeDeserializer elemTypeDeser, final JsonDeserializer<?> elemDeser, final NullValueProvider nuller, final Boolean unwrapSingle)\n
    '''
def isCachable():
    '''returns boolean\n\n
    isCachable()\n
    '''
def getContentDeserializer():
    '''returns JsonDeserializer<Object>\n\n
    getContentDeserializer()\n
    '''
def getEmptyAccessPattern():
    '''returns AccessPattern\n\n
    getEmptyAccessPattern()\n
    '''
def getEmptyValue():
    '''returns Object\n\n
    getEmptyValue(final DeserializationContext ctxt)\n
    '''
def deserialize():
    '''returns Object[]\n\n
    deserialize(final JsonParser p, final DeserializationContext ctxt)\n
    deserialize(final JsonParser p, final DeserializationContext ctxt, final Object[] intoValue)\n
    '''
def deserializeWithType():
    '''returns Object[]\n\n
    deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)\n
    '''
