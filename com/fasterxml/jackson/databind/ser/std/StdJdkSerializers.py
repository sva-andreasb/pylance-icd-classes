def ():
    '''returns AtomicLongSerializer\n\n
    ()\n
    ()\n
    ()\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final AtomicBoolean value, final JsonGenerator gen, final SerializerProvider provider)\n
    serialize(final AtomicInteger value, final JsonGenerator gen, final SerializerProvider provider)\n
    serialize(final AtomicLong value, final JsonGenerator gen, final SerializerProvider provider)\n
    '''
def getSchema():
    '''returns JsonNode\n\n
    getSchema(final SerializerProvider provider, final Type typeHint)\n
    getSchema(final SerializerProvider provider, final Type typeHint)\n
    getSchema(final SerializerProvider provider, final Type typeHint)\n
    '''
def acceptJsonFormatVisitor():
    '''returns None\n\n
    acceptJsonFormatVisitor(final JsonFormatVisitorWrapper visitor, final JavaType typeHint)\n
    acceptJsonFormatVisitor(final JsonFormatVisitorWrapper visitor, final JavaType typeHint)\n
    acceptJsonFormatVisitor(final JsonFormatVisitorWrapper visitor, final JavaType typeHint)\n
    '''
