def StdDelegatingDeserializer():
    '''    public StdDelegatingDeserializer(final Converter<?, T> converter)
    public StdDelegatingDeserializer(final Converter<Object, T> converter, final JavaType delegateType, final JsonDeserializer<?> delegateDeserializer)
    '''
def resolve():
    '''    public void resolve(final DeserializationContext ctxt)
    '''
def supportsUpdate():
    '''    public Boolean supportsUpdate(final DeserializationConfig config)
    '''
def deserialize():
    '''    public T deserialize(final JsonParser p, final DeserializationContext ctxt)
    public T deserialize(final JsonParser p, final DeserializationContext ctxt, final Object intoValue)
    '''
def deserializeWithType():
    '''    public Object deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)
    '''
