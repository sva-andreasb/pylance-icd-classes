def EnumMapDeserializer():
    '''public EnumMapDeserializer(final JavaType mapType, final ValueInstantiator valueInst, final KeyDeserializer keyDeser, final JsonDeserializer<?> valueDeser, final TypeDeserializer vtd, final NullValueProvider nuller)
    public EnumMapDeserializer(final JavaType mapType, final KeyDeserializer keyDeser, final JsonDeserializer<?> valueDeser, final TypeDeserializer vtd)
    '''
def withResolved():
    '''public EnumMapDeserializer withResolved(final KeyDeserializer keyDeserializer, final JsonDeserializer<?> valueDeserializer, final TypeDeserializer valueTypeDeser, final NullValueProvider nuller)
    '''
def resolve():
    '''public void resolve(final DeserializationContext ctxt)
    '''
def isCachable():
    '''public boolean isCachable()
    '''
def getContentDeserializer():
    '''public JsonDeserializer<Object> getContentDeserializer()
    '''
def getEmptyValue():
    '''public Object getEmptyValue(final DeserializationContext ctxt)
    '''
def deserializeWithType():
    '''public Object deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)
    '''
