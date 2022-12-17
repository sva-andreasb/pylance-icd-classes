def ():
    '''returns ReferenceTypeDeserializer\n\n
    (final JavaType fullType, final ValueInstantiator vi, final TypeDeserializer typeDeser, final JsonDeserializer<?> deser)\n
    (final JavaType fullType, final TypeDeserializer typeDeser, final JsonDeserializer<?> deser)\n
    '''
def getNullAccessPattern():
    '''returns AccessPattern\n\n
    getNullAccessPattern()\n
    '''
def getEmptyAccessPattern():
    '''returns AccessPattern\n\n
    getEmptyAccessPattern()\n
    '''
def getEmptyValue():
    '''returns Object\n\n
    getEmptyValue(final DeserializationContext ctxt)\n
    '''
def getValueType():
    '''returns JavaType\n\n
    getValueType()\n
    '''
def supportsUpdate():
    '''returns Boolean\n\n
    supportsUpdate(final DeserializationConfig config)\n
    '''
def deserialize():
    '''returns T\n\n
    deserialize(final JsonParser p, final DeserializationContext ctxt)\n
    deserialize(final JsonParser p, final DeserializationContext ctxt, final T reference)\n
    '''
def deserializeWithType():
    '''returns Object\n\n
    deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)\n
    '''
