def serialize():
    '''returns None\n\n
    serialize(final Object value, final JsonGenerator gen, final SerializerProvider provider)\n
    '''
def serializeWithType():
    '''returns None\n\n
    serializeWithType(final Object value, final JsonGenerator gen, final SerializerProvider serializers, final TypeSerializer typeSer)\n
    '''
def getSchema():
    '''returns JsonNode\n\n
    getSchema(final SerializerProvider provider, final Type typeHint)\n
    '''
def acceptJsonFormatVisitor():
    '''returns None\n\n
    acceptJsonFormatVisitor(final JsonFormatVisitorWrapper visitor, final JavaType typeHint)\n
    '''
