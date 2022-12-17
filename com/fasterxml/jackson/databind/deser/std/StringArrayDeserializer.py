def ():
    '''returns StringArrayDeserializer\n\n
    ()\n
    '''
def supportsUpdate():
    '''returns Boolean\n\n
    supportsUpdate(final DeserializationConfig config)\n
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
    '''returns String[]\n\n
    deserialize(final JsonParser p, final DeserializationContext ctxt)\n
    deserialize(final JsonParser p, final DeserializationContext ctxt, final String[] intoValue)\n
    '''
def deserializeWithType():
    '''returns Object\n\n
    deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)\n
    '''
