def ():
    '''returns ReferenceTypeSerializer\n\n
    (final ReferenceType fullType, final boolean staticTyping, final TypeSerializer vts, final JsonSerializer<Object> ser)\n
    '''
def unwrappingSerializer():
    '''returns JsonSerializer<T>\n\n
    unwrappingSerializer(final NameTransformer transformer)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty(final SerializerProvider provider, final T value)\n
    '''
def isUnwrappingSerializer():
    '''returns boolean\n\n
    isUnwrappingSerializer()\n
    '''
def getReferredType():
    '''returns JavaType\n\n
    getReferredType()\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final T ref, final JsonGenerator g, final SerializerProvider provider)\n
    '''
def serializeWithType():
    '''returns None\n\n
    serializeWithType(final T ref, final JsonGenerator g, final SerializerProvider provider, final TypeSerializer typeSer)\n
    '''
def acceptJsonFormatVisitor():
    '''returns None\n\n
    acceptJsonFormatVisitor(final JsonFormatVisitorWrapper visitor, final JavaType typeHint)\n
    '''
