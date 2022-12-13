def CreatorProperty():
    '''    public CreatorProperty(final PropertyName name, final JavaType type, final PropertyName wrapperName, final TypeDeserializer typeDeser, final Annotations contextAnnotations, final AnnotatedParameter param, final int index, final Object injectableValueId, final PropertyMetadata metadata)
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
def setFallbackSetter():
    '''    public void setFallbackSetter(final SettableBeanProperty fallbackSetter)
    '''
def markAsIgnorable():
    '''    public void markAsIgnorable()
    '''
def isIgnorable():
    '''    public boolean isIgnorable()
    '''
def findInjectableValue():
    '''    public Object findInjectableValue(final DeserializationContext context, final Object beanInstance)
    '''
def inject():
    '''    public void inject(final DeserializationContext context, final Object beanInstance)
    '''
def getAnnotation():
    '''    public <A extends Annotation> A getAnnotation(final Class<A> acls)
    '''
def getMember():
    '''    public AnnotatedMember getMember()
    '''
def getCreatorIndex():
    '''    public int getCreatorIndex()
    '''
def deserializeAndSet():
    '''    public void deserializeAndSet(final JsonParser p, final DeserializationContext ctxt, final Object instance)
    '''
def deserializeSetAndReturn():
    '''    public Object deserializeSetAndReturn(final JsonParser p, final DeserializationContext ctxt, final Object instance)
    '''
def set():
    '''    public void set(final Object instance, final Object value)
    '''
def setAndReturn():
    '''    public Object setAndReturn(final Object instance, final Object value)
    '''
def getInjectableValueId():
    '''    public Object getInjectableValueId()
    '''
def toString():
    '''    public String toString()
    '''
