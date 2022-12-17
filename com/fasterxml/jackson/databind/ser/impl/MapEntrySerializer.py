def ():
    '''returns MapEntrySerializer\n\n
    (final JavaType type, final JavaType keyType, final JavaType valueType, final boolean staticTyping, final TypeSerializer vts, final BeanProperty property)\n
    '''
def withResolved():
    '''returns MapEntrySerializer\n\n
    withResolved(final BeanProperty property, final JsonSerializer<?> keySerializer, final JsonSerializer<?> valueSerializer, final Object suppressableValue, final boolean suppressNulls)\n
    '''
def withContentInclusion():
    '''returns MapEntrySerializer\n\n
    withContentInclusion(final Object suppressableValue, final boolean suppressNulls)\n
    '''
def getContentType():
    '''returns JavaType\n\n
    getContentType()\n
    '''
def hasSingleElement():
    '''returns boolean\n\n
    hasSingleElement(final Map.Entry<?, ?> value)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty(final SerializerProvider prov, final Map.Entry<?, ?> entry)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final Map.Entry<?, ?> value, final JsonGenerator gen, final SerializerProvider provider)\n
    '''
def serializeWithType():
    '''returns None\n\n
    serializeWithType(final Map.Entry<?, ?> value, final JsonGenerator g, final SerializerProvider provider, final TypeSerializer typeSer)\n
    '''
