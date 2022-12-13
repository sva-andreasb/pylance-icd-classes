def CollectionDeserializer():
    '''    public CollectionDeserializer(final JavaType collectionType, final JsonDeserializer<Object> valueDeser, final TypeDeserializer valueTypeDeser, final ValueInstantiator valueInstantiator)
    '''
def isCachable():
    '''    public boolean isCachable()
    '''
def createContextual():
    '''    public CollectionDeserializer createContextual(final DeserializationContext ctxt, final BeanProperty property)
    '''
def getContentDeserializer():
    '''    public JsonDeserializer<Object> getContentDeserializer()
    '''
def getValueInstantiator():
    '''    public ValueInstantiator getValueInstantiator()
    '''
def deserialize():
    '''    public Collection<Object> deserialize(final JsonParser p, final DeserializationContext ctxt)
    public Collection<Object> deserialize(final JsonParser p, final DeserializationContext ctxt, final Collection<Object> result)
    '''
def deserializeWithType():
    '''    public Object deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)
    '''
def CollectionReferringAccumulator():
    '''    public CollectionReferringAccumulator(final Class<?> elementType, final Collection<Object> result)
    '''
def add():
    '''    public void add(final Object value)
    '''
def resolveForwardReference():
    '''    public void resolveForwardReference(final Object id, final Object value)
    '''
def handleResolvedForwardReference():
    '''    public void handleResolvedForwardReference(final Object id, final Object value)
    '''
