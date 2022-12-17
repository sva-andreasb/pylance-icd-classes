def ():
    '''returns AnyGetterWriter\n\n
    (final BeanProperty property, final AnnotatedMember accessor, final JsonSerializer<?> serializer)\n
    '''
def fixAccess():
    '''returns None\n\n
    fixAccess(final SerializationConfig config)\n
    '''
def getAndSerialize():
    '''returns None\n\n
    getAndSerialize(final Object bean, final JsonGenerator gen, final SerializerProvider provider)\n
    '''
def getAndFilter():
    '''returns None\n\n
    getAndFilter(final Object bean, final JsonGenerator gen, final SerializerProvider provider, final PropertyFilter filter)\n
    '''
def resolve():
    '''returns None\n\n
    resolve(final SerializerProvider provider)\n
    '''
