def ():
    '''returns IndexedListSerializer\n\n
    (final JavaType elemType, final boolean staticTyping, final TypeSerializer vts, final JsonSerializer<Object> valueSerializer)\n
    (final IndexedListSerializer src, final BeanProperty property, final TypeSerializer vts, final JsonSerializer<?> valueSerializer, final Boolean unwrapSingle)\n
    '''
def withResolved():
    '''returns IndexedListSerializer\n\n
    withResolved(final BeanProperty property, final TypeSerializer vts, final JsonSerializer<?> elementSerializer, final Boolean unwrapSingle)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty(final SerializerProvider prov, final List<?> value)\n
    '''
def hasSingleElement():
    '''returns boolean\n\n
    hasSingleElement(final List<?> value)\n
    '''
def serializeContents():
    '''returns None\n\n
    serializeContents(final List<?> value, final JsonGenerator g, final SerializerProvider provider)\n
    '''
def serializeContentsUsing():
    '''returns None\n\n
    serializeContentsUsing(final List<?> value, final JsonGenerator jgen, final SerializerProvider provider, final JsonSerializer<Object> ser)\n
    '''
def serializeTypedContents():
    '''returns None\n\n
    serializeTypedContents(final List<?> value, final JsonGenerator jgen, final SerializerProvider provider)\n
    '''
