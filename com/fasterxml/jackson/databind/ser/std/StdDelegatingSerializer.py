def ():
    '''returns StdDelegatingSerializer\n\n
    (final Converter<?, ?> converter)\n
    (final Converter<Object, ?> converter, final JavaType delegateType, final JsonSerializer<?> delegateSerializer)\n
    '''
def StdDelegatingSerializer():
    '''returns <T>\n\n
    StdDelegatingSerializer(final Class<T> cls, final Converter<T, ?> converter)\n
    '''
def resolve():
    '''returns None\n\n
    resolve(final SerializerProvider provider)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final Object value, final JsonGenerator gen, final SerializerProvider provider)\n
    '''
def serializeWithType():
    '''returns None\n\n
    serializeWithType(final Object value, final JsonGenerator gen, final SerializerProvider provider, final TypeSerializer typeSer)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty(final SerializerProvider prov, final Object value)\n
    '''
def getSchema():
    '''returns JsonNode\n\n
    getSchema(final SerializerProvider provider, final Type typeHint)\n
    getSchema(final SerializerProvider provider, final Type typeHint, final boolean isOptional)\n
    '''
def acceptJsonFormatVisitor():
    '''returns None\n\n
    acceptJsonFormatVisitor(final JsonFormatVisitorWrapper visitor, final JavaType typeHint)\n
    '''
