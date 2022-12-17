def ():
    '''returns ObjectArraySerializer\n\n
    (final JavaType elemType, final boolean staticTyping, final TypeSerializer vts, final JsonSerializer<Object> elementSerializer)\n
    (final ObjectArraySerializer src, final TypeSerializer vts)\n
    (final ObjectArraySerializer src, final BeanProperty property, final TypeSerializer vts, final JsonSerializer<?> elementSerializer, final Boolean unwrapSingle)\n
    '''
def withResolved():
    '''returns ObjectArraySerializer\n\n
    withResolved(final BeanProperty prop, final TypeSerializer vts, final JsonSerializer<?> ser, final Boolean unwrapSingle)\n
    '''
def getContentType():
    '''returns JavaType\n\n
    getContentType()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty(final SerializerProvider prov, final Object[] value)\n
    '''
def hasSingleElement():
    '''returns boolean\n\n
    hasSingleElement(final Object[] value)\n
    '''
def serializeContents():
    '''returns None\n\n
    serializeContents(final Object[] value, final JsonGenerator gen, final SerializerProvider provider)\n
    '''
def serializeContentsUsing():
    '''returns None\n\n
    serializeContentsUsing(final Object[] value, final JsonGenerator jgen, final SerializerProvider provider, final JsonSerializer<Object> ser)\n
    '''
def serializeTypedContents():
    '''returns None\n\n
    serializeTypedContents(final Object[] value, final JsonGenerator jgen, final SerializerProvider provider)\n
    '''
def acceptJsonFormatVisitor():
    '''returns None\n\n
    acceptJsonFormatVisitor(final JsonFormatVisitorWrapper visitor, final JavaType typeHint)\n
    '''
