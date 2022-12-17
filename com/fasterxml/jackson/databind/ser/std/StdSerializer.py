def handledType():
    '''returns Class<T>\n\n
    handledType()\n
    '''
def acceptJsonFormatVisitor():
    '''returns None\n\n
    acceptJsonFormatVisitor(final JsonFormatVisitorWrapper visitor, final JavaType typeHint)\n
    '''
def getSchema():
    '''returns JsonNode\n\n
    getSchema(final SerializerProvider provider, final Type typeHint)\n
    getSchema(final SerializerProvider provider, final Type typeHint, final boolean isOptional)\n
    '''
def wrapAndThrow():
    '''returns None\n\n
    wrapAndThrow(final SerializerProvider provider, Throwable t, final Object bean, final String fieldName)\n
    wrapAndThrow(final SerializerProvider provider, Throwable t, final Object bean, final int index)\n
    '''
