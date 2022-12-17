def ():
    '''returns PropertyReferring\n\n
    (final SettableBeanProperty forward, final ObjectIdInfo objectIdInfo)\n
    (final ObjectIdReferenceProperty src, final JsonDeserializer<?> deser, final NullValueProvider nva)\n
    (final ObjectIdReferenceProperty src, final PropertyName newName)\n
    (final ObjectIdReferenceProperty parent, final UnresolvedForwardReference ref, final Class<?> type, final Object ob)\n
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
def getCreatorIndex():
    '''returns int\n\n
    getCreatorIndex()\n
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
def handleResolvedForwardReference():
    '''returns None\n\n
    handleResolvedForwardReference(final Object id, final Object value)\n
    '''
