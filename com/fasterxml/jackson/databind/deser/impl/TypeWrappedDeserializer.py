def TypeWrappedDeserializer():
    '''public TypeWrappedDeserializer(final TypeDeserializer typeDeser, final JsonDeserializer<?> deser)
    '''
def supportsUpdate():
    '''public Boolean supportsUpdate(final DeserializationConfig config)
    '''
def getKnownPropertyNames():
    '''public Collection<Object> getKnownPropertyNames()
    '''
def getNullValue():
    '''public Object getNullValue(final DeserializationContext ctxt)
    '''
def getEmptyValue():
    '''public Object getEmptyValue(final DeserializationContext ctxt)
    '''
def deserialize():
    '''public Object deserialize(final JsonParser p, final DeserializationContext ctxt)
    public Object deserialize(final JsonParser p, final DeserializationContext ctxt, final Object intoValue)
    '''
def deserializeWithType():
    '''public Object deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)
    '''
