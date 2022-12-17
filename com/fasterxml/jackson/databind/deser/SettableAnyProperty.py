def ():
    '''returns AnySetterReferring\n\n
    (final BeanProperty property, final AnnotatedMember setter, final JavaType type, final KeyDeserializer keyDeser, final JsonDeserializer<Object> valueDeser, final TypeDeserializer typeDeser)\n
    (final BeanProperty property, final AnnotatedMember setter, final JavaType type, final JsonDeserializer<Object> valueDeser, final TypeDeserializer typeDeser)\n
    (final SettableAnyProperty parent, final UnresolvedForwardReference reference, final Class<?> type, final Object instance, final String propName)\n
    '''
def withValueDeserializer():
    '''returns SettableAnyProperty\n\n
    withValueDeserializer(final JsonDeserializer<Object> deser)\n
    '''
def fixAccess():
    '''returns None\n\n
    fixAccess(final DeserializationConfig config)\n
    '''
def getProperty():
    '''returns BeanProperty\n\n
    getProperty()\n
    '''
def hasValueDeserializer():
    '''returns boolean\n\n
    hasValueDeserializer()\n
    '''
def getType():
    '''returns JavaType\n\n
    getType()\n
    '''
def deserialize():
    '''returns Object\n\n
    deserialize(final JsonParser p, final DeserializationContext ctxt)\n
    '''
def set():
    '''returns None\n\n
    set(final Object instance, final Object propName, final Object value)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def handleResolvedForwardReference():
    '''returns None\n\n
    handleResolvedForwardReference(final Object id, final Object value)\n
    '''
