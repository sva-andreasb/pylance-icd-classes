def ():
    '''returns TypeWrappedSerializer\n\n
    (final TypeSerializer typeSer, final JsonSerializer<?> ser)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final Object value, final JsonGenerator g, final SerializerProvider provider)\n
    '''
def serializeWithType():
    '''returns None\n\n
    serializeWithType(final Object value, final JsonGenerator g, final SerializerProvider provider, final TypeSerializer typeSer)\n
    '''
def handledType():
    '''returns Class<Object>\n\n
    handledType()\n
    '''
def valueSerializer():
    '''returns JsonSerializer<Object>\n\n
    valueSerializer()\n
    '''
def typeSerializer():
    '''returns TypeSerializer\n\n
    typeSerializer()\n
    '''
