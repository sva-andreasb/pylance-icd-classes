def ():
    '''returns FieldProperty\n\n
    (final BeanPropertyDefinition propDef, final JavaType type, final TypeDeserializer typeDeser, final Annotations contextAnnotations, final AnnotatedField field)\n
    '''
def withName():
    '''returns SettableBeanProperty\n\n
    withName(final PropertyName newName)\n
    '''
def withValueDeserializer():
    '''returns SettableBeanProperty\n\n
    withValueDeserializer(final JsonDeserializer<?> deser)\n
    '''
def withNullProvider():
    '''returns SettableBeanProperty\n\n
    withNullProvider(final NullValueProvider nva)\n
    '''
def fixAccess():
    '''returns None\n\n
    fixAccess(final DeserializationConfig config)\n
    '''
def getMember():
    '''returns AnnotatedMember\n\n
    getMember()\n
    '''
def deserializeAndSet():
    '''returns None\n\n
    deserializeAndSet(final JsonParser p, final DeserializationContext ctxt, final Object instance)\n
    '''
def deserializeSetAndReturn():
    '''returns Object\n\n
    deserializeSetAndReturn(final JsonParser p, final DeserializationContext ctxt, final Object instance)\n
    '''
def set():
    '''returns None\n\n
    set(final Object instance, final Object value)\n
    '''
def setAndReturn():
    '''returns Object\n\n
    setAndReturn(final Object instance, final Object value)\n
    '''
