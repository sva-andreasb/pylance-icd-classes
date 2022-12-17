def ():
    '''returns IteratorSerializer\n\n
    (final JavaType elemType, final boolean staticTyping, final TypeSerializer vts)\n
    (final IteratorSerializer src, final BeanProperty property, final TypeSerializer vts, final JsonSerializer<?> valueSerializer, final Boolean unwrapSingle)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty(final SerializerProvider prov, final Iterator<?> value)\n
    '''
def hasSingleElement():
    '''returns boolean\n\n
    hasSingleElement(final Iterator<?> value)\n
    '''
def withResolved():
    '''returns IteratorSerializer\n\n
    withResolved(final BeanProperty property, final TypeSerializer vts, final JsonSerializer<?> elementSerializer, final Boolean unwrapSingle)\n
    '''
def serializeContents():
    '''returns None\n\n
    serializeContents(final Iterator<?> value, final JsonGenerator g, final SerializerProvider provider)\n
    '''
