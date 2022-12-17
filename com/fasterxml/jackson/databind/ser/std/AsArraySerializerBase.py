def getContentType():
    '''returns JavaType\n\n
    getContentType()\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final T value, final JsonGenerator gen, final SerializerProvider provider)\n
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
