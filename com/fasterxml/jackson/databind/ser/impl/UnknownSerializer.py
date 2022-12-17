def ():
    '''returns UnknownSerializer\n\n
    ()\n
    (final Class<?> cls)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final Object value, final JsonGenerator gen, final SerializerProvider provider)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty(final SerializerProvider provider, final Object value)\n
    '''
def getSchema():
    '''returns JsonNode\n\n
    getSchema(final SerializerProvider provider, final Type typeHint)\n
    '''
def acceptJsonFormatVisitor():
    '''returns None\n\n
    acceptJsonFormatVisitor(final JsonFormatVisitorWrapper visitor, final JavaType typeHint)\n
    '''
