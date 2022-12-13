def ObjectIdReferenceProperty():
    '''public ObjectIdReferenceProperty(final SettableBeanProperty forward, final ObjectIdInfo objectIdInfo)
    public ObjectIdReferenceProperty(final ObjectIdReferenceProperty src, final JsonDeserializer<?> deser, final NullValueProvider nva)
    public ObjectIdReferenceProperty(final ObjectIdReferenceProperty src, final PropertyName newName)
    '''
def withName():
    '''public SettableBeanProperty withName(final PropertyName newName)
    '''
def withValueDeserializer():
    '''public SettableBeanProperty withValueDeserializer(final JsonDeserializer<?> deser)
    '''
def withNullProvider():
    '''public SettableBeanProperty withNullProvider(final NullValueProvider nva)
    '''
def fixAccess():
    '''public void fixAccess(final DeserializationConfig config)
    '''
def getAnnotation():
    '''public <A extends Annotation> A getAnnotation(final Class<A> acls)
    '''
def getMember():
    '''public AnnotatedMember getMember()
    '''
def getCreatorIndex():
    '''public int getCreatorIndex()
    '''
def deserializeAndSet():
    '''public void deserializeAndSet(final JsonParser p, final DeserializationContext ctxt, final Object instance)
    '''
def deserializeSetAndReturn():
    '''public Object deserializeSetAndReturn(final JsonParser p, final DeserializationContext ctxt, final Object instance)
    '''
def set():
    '''public void set(final Object instance, final Object value)
    '''
def setAndReturn():
    '''public Object setAndReturn(final Object instance, final Object value)
    '''
def PropertyReferring():
    '''public PropertyReferring(final ObjectIdReferenceProperty parent, final UnresolvedForwardReference ref, final Class<?> type, final Object ob)
    '''
def handleResolvedForwardReference():
    '''public void handleResolvedForwardReference(final Object id, final Object value)
    '''
