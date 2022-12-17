def ():
    '''returns EnumSetSerializer\n\n
    (final JavaType elemType)\n
    (final EnumSetSerializer src, final BeanProperty property, final TypeSerializer vts, final JsonSerializer<?> valueSerializer, final Boolean unwrapSingle)\n
    '''
def _withValueTypeSerializer():
    '''returns EnumSetSerializer\n\n
    _withValueTypeSerializer(final TypeSerializer vts)\n
    '''
def withResolved():
    '''returns EnumSetSerializer\n\n
    withResolved(final BeanProperty property, final TypeSerializer vts, final JsonSerializer<?> elementSerializer, final Boolean unwrapSingle)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty(final SerializerProvider prov, final EnumSet<? extends Enum<?>> value)\n
    '''
def hasSingleElement():
    '''returns boolean\n\n
    hasSingleElement(final EnumSet<? extends Enum<?>> value)\n
    '''
def serializeContents():
    '''returns None\n\n
    serializeContents(final EnumSet<? extends Enum<?>> value, final JsonGenerator gen, final SerializerProvider provider)\n
    '''
