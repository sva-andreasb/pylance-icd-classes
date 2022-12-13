def ObjectArrayDeserializer():
    '''public ObjectArrayDeserializer(final JavaType arrayType, final JsonDeserializer<Object> elemDeser, final TypeDeserializer elemTypeDeser)
    '''
def withDeserializer():
    '''public ObjectArrayDeserializer withDeserializer(final TypeDeserializer elemTypeDeser, final JsonDeserializer<?> elemDeser)
    '''
def withResolved():
    '''public ObjectArrayDeserializer withResolved(final TypeDeserializer elemTypeDeser, final JsonDeserializer<?> elemDeser, final NullValueProvider nuller, final Boolean unwrapSingle)
    '''
def isCachable():
    '''public boolean isCachable()
    '''
def getContentDeserializer():
    '''public JsonDeserializer<Object> getContentDeserializer()
    '''
def getEmptyAccessPattern():
    '''public AccessPattern getEmptyAccessPattern()
    '''
def getEmptyValue():
    '''public Object getEmptyValue(final DeserializationContext ctxt)
    '''
def deserialize():
    '''public Object[] deserialize(final JsonParser p, final DeserializationContext ctxt)
    public Object[] deserialize(final JsonParser p, final DeserializationContext ctxt, final Object[] intoValue)
    '''
def deserializeWithType():
    '''public Object[] deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)
    '''
