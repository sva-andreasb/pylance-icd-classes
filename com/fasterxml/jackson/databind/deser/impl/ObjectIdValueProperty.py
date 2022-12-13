def ObjectIdValueProperty():
    '''public ObjectIdValueProperty(final ObjectIdReader objectIdReader, final PropertyMetadata metadata)
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
def getAnnotation():
    '''public <A extends Annotation> A getAnnotation(final Class<A> acls)
    '''
def getMember():
    '''public AnnotatedMember getMember()
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
