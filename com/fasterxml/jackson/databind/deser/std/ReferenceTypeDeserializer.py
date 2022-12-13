def ReferenceTypeDeserializer():
    '''public ReferenceTypeDeserializer(final JavaType fullType, final ValueInstantiator vi, final TypeDeserializer typeDeser, final JsonDeserializer<?> deser)
    public ReferenceTypeDeserializer(final JavaType fullType, final TypeDeserializer typeDeser, final JsonDeserializer<?> deser)
    '''
def getNullAccessPattern():
    '''public AccessPattern getNullAccessPattern()
    '''
def getEmptyAccessPattern():
    '''public AccessPattern getEmptyAccessPattern()
    '''
def getEmptyValue():
    '''public Object getEmptyValue(final DeserializationContext ctxt)
    '''
def getValueType():
    '''public JavaType getValueType()
    '''
def supportsUpdate():
    '''public Boolean supportsUpdate(final DeserializationConfig config)
    '''
def deserialize():
    '''public T deserialize(final JsonParser p, final DeserializationContext ctxt)
    public T deserialize(final JsonParser p, final DeserializationContext ctxt, final T reference)
    '''
def deserializeWithType():
    '''public Object deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)
    '''
