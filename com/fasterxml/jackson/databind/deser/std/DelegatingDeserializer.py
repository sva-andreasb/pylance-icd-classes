def DelegatingDeserializer():
    '''    public DelegatingDeserializer(final JsonDeserializer<?> d)
    '''
def resolve():
    '''    public void resolve(final DeserializationContext ctxt)
    '''
def deserialize():
    '''    public Object deserialize(final JsonParser p, final DeserializationContext ctxt)
    public Object deserialize(final JsonParser p, final DeserializationContext ctxt, final Object intoValue)
    '''
def deserializeWithType():
    '''    public Object deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)
    '''
def isCachable():
    '''    public boolean isCachable()
    '''
def supportsUpdate():
    '''    public Boolean supportsUpdate(final DeserializationConfig config)
    '''
def findBackReference():
    '''    public SettableBeanProperty findBackReference(final String logicalName)
    '''
def getNullAccessPattern():
    '''    public AccessPattern getNullAccessPattern()
    '''
def getNullValue():
    '''    public Object getNullValue(final DeserializationContext ctxt)
    '''
def getEmptyValue():
    '''    public Object getEmptyValue(final DeserializationContext ctxt)
    '''
def getKnownPropertyNames():
    '''    public Collection<Object> getKnownPropertyNames()
    '''
def getObjectIdReader():
    '''    public ObjectIdReader getObjectIdReader()
    '''
