def StringCollectionDeserializer():
    '''    public StringCollectionDeserializer(final JavaType collectionType, final JsonDeserializer<?> valueDeser, final ValueInstantiator valueInstantiator)
    '''
def isCachable():
    '''    public boolean isCachable()
    '''
def getContentDeserializer():
    '''    public JsonDeserializer<Object> getContentDeserializer()
    '''
def getValueInstantiator():
    '''    public ValueInstantiator getValueInstantiator()
    '''
def deserialize():
    '''    public Collection<String> deserialize(final JsonParser p, final DeserializationContext ctxt)
    public Collection<String> deserialize(final JsonParser p, final DeserializationContext ctxt, final Collection<String> result)
    '''
def deserializeWithType():
    '''    public Object deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)
    '''
