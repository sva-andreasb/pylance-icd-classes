def deserialize():
    '''    public T deserialize(final JsonParser p, final DeserializationContext ctxt, final T intoValue)
    '''
def deserializeWithType():
    '''    public Object deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)
    '''
def unwrappingDeserializer():
    '''    public JsonDeserializer<T> unwrappingDeserializer(final NameTransformer unwrapper)
    '''
def isCachable():
    '''    public boolean isCachable()
    '''
def getKnownPropertyNames():
    '''    public Collection<Object> getKnownPropertyNames()
    '''
def getNullValue():
    '''    public T getNullValue(final DeserializationContext ctxt)
    public T getNullValue()
    '''
def getNullAccessPattern():
    '''    public AccessPattern getNullAccessPattern()
    '''
def getEmptyAccessPattern():
    '''    public AccessPattern getEmptyAccessPattern()
    '''
def getEmptyValue():
    '''    public Object getEmptyValue(final DeserializationContext ctxt)
    public Object getEmptyValue()
    '''
def getObjectIdReader():
    '''    public ObjectIdReader getObjectIdReader()
    '''
def findBackReference():
    '''    public SettableBeanProperty findBackReference(final String refName)
    '''
def supportsUpdate():
    '''    public Boolean supportsUpdate(final DeserializationConfig config)
    '''
