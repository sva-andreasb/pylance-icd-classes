def ():
    '''returns StringArraySerializer\n\n
    (final StringArraySerializer src, final BeanProperty prop, final JsonSerializer<?> ser, final Boolean unwrapSingle)\n
    '''
def getContentType():
    '''returns JavaType\n\n
    getContentType()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty(final SerializerProvider prov, final String[] value)\n
    '''
def hasSingleElement():
    '''returns boolean\n\n
    hasSingleElement(final String[] value)\n
    '''
def serializeContents():
    '''returns None\n\n
    serializeContents(final String[] value, final JsonGenerator gen, final SerializerProvider provider)\n
    '''
def getSchema():
    '''returns JsonNode\n\n
    getSchema(final SerializerProvider provider, final Type typeHint)\n
    '''
def acceptJsonFormatVisitor():
    '''returns None\n\n
    acceptJsonFormatVisitor(final JsonFormatVisitorWrapper visitor, final JavaType typeHint)\n
    '''
