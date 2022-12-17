def ():
    '''returns StringSerializer\n\n
    ()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty(final SerializerProvider prov, final Object value)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final Object value, final JsonGenerator gen, final SerializerProvider provider)\n
    '''
def getSchema():
    '''returns JsonNode\n\n
    getSchema(final SerializerProvider provider, final Type typeHint)\n
    '''
def acceptJsonFormatVisitor():
    '''returns None\n\n
    acceptJsonFormatVisitor(final JsonFormatVisitorWrapper visitor, final JavaType typeHint)\n
    '''
