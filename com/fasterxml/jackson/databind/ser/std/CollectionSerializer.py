def ():
    '''returns CollectionSerializer\n\n
    (final JavaType elemType, final boolean staticTyping, final TypeSerializer vts, final JsonSerializer<Object> valueSerializer)\n
    (final JavaType elemType, final boolean staticTyping, final TypeSerializer vts, final BeanProperty property, final JsonSerializer<Object> valueSerializer)\n
    (final CollectionSerializer src, final BeanProperty property, final TypeSerializer vts, final JsonSerializer<?> valueSerializer, final Boolean unwrapSingle)\n
    '''
def withResolved():
    '''returns CollectionSerializer\n\n
    withResolved(final BeanProperty property, final TypeSerializer vts, final JsonSerializer<?> elementSerializer, final Boolean unwrapSingle)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty(final SerializerProvider prov, final Collection<?> value)\n
    '''
def hasSingleElement():
    '''returns boolean\n\n
    hasSingleElement(final Collection<?> value)\n
    '''
def serializeContents():
    '''returns None\n\n
    serializeContents(final Collection<?> value, final JsonGenerator g, final SerializerProvider provider)\n
    '''
def serializeContentsUsing():
    '''returns None\n\n
    serializeContentsUsing(final Collection<?> value, final JsonGenerator g, final SerializerProvider provider, final JsonSerializer<Object> ser)\n
    '''
