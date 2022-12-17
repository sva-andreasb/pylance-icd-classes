def ():
    '''returns IterableSerializer\n\n
    (final JavaType elemType, final boolean staticTyping, final TypeSerializer vts)\n
    (final IterableSerializer src, final BeanProperty property, final TypeSerializer vts, final JsonSerializer<?> valueSerializer, final Boolean unwrapSingle)\n
    '''
def withResolved():
    '''returns IterableSerializer\n\n
    withResolved(final BeanProperty property, final TypeSerializer vts, final JsonSerializer<?> elementSerializer, final Boolean unwrapSingle)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty(final SerializerProvider prov, final Iterable<?> value)\n
    '''
def hasSingleElement():
    '''returns boolean\n\n
    hasSingleElement(final Iterable<?> value)\n
    '''
def serializeContents():
    '''returns None\n\n
    serializeContents(final Iterable<?> value, final JsonGenerator jgen, final SerializerProvider provider)\n
    '''
