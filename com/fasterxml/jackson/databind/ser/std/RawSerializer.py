def ():
    '''returns RawSerializer\n\n
    (final Class<?> cls)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final T value, final JsonGenerator jgen, final SerializerProvider provider)\n
    '''
def serializeWithType():
    '''returns None\n\n
    serializeWithType(final T value, final JsonGenerator g, final SerializerProvider provider, final TypeSerializer typeSer)\n
    '''
def getSchema():
    '''returns JsonNode\n\n
    getSchema(final SerializerProvider provider, final Type typeHint)\n
    '''
def acceptJsonFormatVisitor():
    '''returns None\n\n
    acceptJsonFormatVisitor(final JsonFormatVisitorWrapper visitor, final JavaType typeHint)\n
    '''
