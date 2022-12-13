def MapDeserializer():
    '''    public MapDeserializer(final JavaType mapType, final ValueInstantiator valueInstantiator, final KeyDeserializer keyDeser, final JsonDeserializer<Object> valueDeser, final TypeDeserializer valueTypeDeser)
    '''
def setIgnorableProperties():
    '''    public void setIgnorableProperties(final String[] ignorable)
    public void setIgnorableProperties(final Set<String> ignorable)
    '''
def resolve():
    '''    public void resolve(final DeserializationContext ctxt)
    '''
def getContentDeserializer():
    '''    public JsonDeserializer<Object> getContentDeserializer()
    '''
def getValueInstantiator():
    '''    public ValueInstantiator getValueInstantiator()
    '''
def isCachable():
    '''    public boolean isCachable()
    '''
def deserialize():
    '''    public Map<Object, Object> deserialize(final JsonParser p, final DeserializationContext ctxt)
    public Map<Object, Object> deserialize(final JsonParser p, final DeserializationContext ctxt, final Map<Object, Object> result)
    '''
def deserializeWithType():
    '''    public Object deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)
    '''
def getValueType():
    '''    public JavaType getValueType()
    '''
def _deserializeUsingCreator():
    '''    public Map<Object, Object> _deserializeUsingCreator(final JsonParser p, final DeserializationContext ctxt)
    '''
def MapReferringAccumulator():
    '''    public MapReferringAccumulator(final Class<?> valueType, final Map<Object, Object> result)
    '''
def put():
    '''    public void put(final Object key, final Object value)
    '''
def resolveForwardReference():
    '''    public void resolveForwardReference(final Object id, final Object value)
    '''
def handleResolvedForwardReference():
    '''    public void handleResolvedForwardReference(final Object id, final Object value)
    '''
