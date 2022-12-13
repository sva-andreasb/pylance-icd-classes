def SettableAnyProperty():
    '''    public SettableAnyProperty(final BeanProperty property, final AnnotatedMember setter, final JavaType type, final KeyDeserializer keyDeser, final JsonDeserializer<Object> valueDeser, final TypeDeserializer typeDeser)
    public SettableAnyProperty(final BeanProperty property, final AnnotatedMember setter, final JavaType type, final JsonDeserializer<Object> valueDeser, final TypeDeserializer typeDeser)
    '''
def withValueDeserializer():
    '''    public SettableAnyProperty withValueDeserializer(final JsonDeserializer<Object> deser)
    '''
def fixAccess():
    '''    public void fixAccess(final DeserializationConfig config)
    '''
def getProperty():
    '''    public BeanProperty getProperty()
    '''
def hasValueDeserializer():
    '''    public boolean hasValueDeserializer()
    '''
def getType():
    '''    public JavaType getType()
    '''
def deserializeAndSet():
    '''    public final void deserializeAndSet(final JsonParser p, final DeserializationContext ctxt, final Object instance, final String propName)
    '''
def deserialize():
    '''    public Object deserialize(final JsonParser p, final DeserializationContext ctxt)
    '''
def set():
    '''    public void set(final Object instance, final Object propName, final Object value)
    '''
def toString():
    '''    public String toString()
    '''
def AnySetterReferring():
    '''    public AnySetterReferring(final SettableAnyProperty parent, final UnresolvedForwardReference reference, final Class<?> type, final Object instance, final String propName)
    '''
def handleResolvedForwardReference():
    '''    public void handleResolvedForwardReference(final Object id, final Object value)
    '''
