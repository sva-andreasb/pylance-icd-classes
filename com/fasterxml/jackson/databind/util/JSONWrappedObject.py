def ():
    '''returns JSONWrappedObject\n\n
    (final String prefix, final String suffix, final Object value)\n
    (final String prefix, final String suffix, final Object value, final JavaType asType)\n
    '''
def serializeWithType():
    '''returns None\n\n
    serializeWithType(final JsonGenerator jgen, final SerializerProvider provider, final TypeSerializer typeSer)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final JsonGenerator jgen, final SerializerProvider provider)\n
    '''
def getPrefix():
    '''returns String\n\n
    getPrefix()\n
    '''
def getSuffix():
    '''returns String\n\n
    getSuffix()\n
    '''
def getValue():
    '''returns Object\n\n
    getValue()\n
    '''
def getSerializationType():
    '''returns JavaType\n\n
    getSerializationType()\n
    '''
