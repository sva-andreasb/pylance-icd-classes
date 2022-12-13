def SetterlessProperty():
    '''    public SetterlessProperty(final BeanPropertyDefinition propDef, final JavaType type, final TypeDeserializer typeDeser, final Annotations contextAnnotations, final AnnotatedMethod method)
    '''
def withName():
    '''    public SettableBeanProperty withName(final PropertyName newName)
    '''
def withValueDeserializer():
    '''    public SettableBeanProperty withValueDeserializer(final JsonDeserializer<?> deser)
    '''
def withNullProvider():
    '''    public SettableBeanProperty withNullProvider(final NullValueProvider nva)
    '''
def fixAccess():
    '''    public void fixAccess(final DeserializationConfig config)
    '''
def getAnnotation():
    '''    public <A extends Annotation> A getAnnotation(final Class<A> acls)
    '''
def getMember():
    '''    public AnnotatedMember getMember()
    '''
def deserializeAndSet():
    '''    public final void deserializeAndSet(final JsonParser p, final DeserializationContext ctxt, final Object instance)
    '''
def deserializeSetAndReturn():
    '''    public Object deserializeSetAndReturn(final JsonParser p, final DeserializationContext ctxt, final Object instance)
    '''
def set():
    '''    public final void set(final Object instance, final Object value)
    '''
def setAndReturn():
    '''    public Object setAndReturn(final Object instance, final Object value)
    '''
