def ():
    '''returns ByteArraySerializer\n\n
    ()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty(final SerializerProvider prov, final byte[] value)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final byte[] value, final JsonGenerator g, final SerializerProvider provider)\n
    '''
def serializeWithType():
    '''returns None\n\n
    serializeWithType(final byte[] value, final JsonGenerator g, final SerializerProvider provider, final TypeSerializer typeSer)\n
    '''
def getSchema():
    '''returns JsonNode\n\n
    getSchema(final SerializerProvider provider, final Type typeHint)\n
    '''
def acceptJsonFormatVisitor():
    '''returns None\n\n
    acceptJsonFormatVisitor(final JsonFormatVisitorWrapper visitor, final JavaType typeHint)\n
    '''
