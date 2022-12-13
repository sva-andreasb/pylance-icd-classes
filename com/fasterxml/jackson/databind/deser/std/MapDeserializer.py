def MapDeserializer():
'''public MapDeserializer(final JavaType mapType, final ValueInstantiator valueInstantiator, final KeyDeserializer keyDeser, final JsonDeserializer<Object> valueDeser, final TypeDeserializer valueTypeDeser)
'''
pass
def setIgnorableProperties():
'''public void setIgnorableProperties(final String[] ignorable)
public void setIgnorableProperties(final Set<String> ignorable)
'''
pass
def resolve():
'''public void resolve(final DeserializationContext ctxt)
'''
pass
def getContentDeserializer():
'''public JsonDeserializer<Object> getContentDeserializer()
'''
pass
def getValueInstantiator():
'''public ValueInstantiator getValueInstantiator()
'''
pass
def isCachable():
'''public boolean isCachable()
'''
pass
def deserialize():
'''public Map<Object, Object> deserialize(final JsonParser p, final DeserializationContext ctxt)
public Map<Object, Object> deserialize(final JsonParser p, final DeserializationContext ctxt, final Map<Object, Object> result)
'''
pass
def deserializeWithType():
'''public Object deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)
'''
pass
def getValueType():
'''public JavaType getValueType()
'''
pass
def _deserializeUsingCreator():
'''public Map<Object, Object> _deserializeUsingCreator(final JsonParser p, final DeserializationContext ctxt)
'''
pass
def MapReferringAccumulator():
'''public MapReferringAccumulator(final Class<?> valueType, final Map<Object, Object> result)
'''
pass
def put():
'''public void put(final Object key, final Object value)
'''
pass
def resolveForwardReference():
'''public void resolveForwardReference(final Object id, final Object value)
'''
pass
def handleResolvedForwardReference():
'''public void handleResolvedForwardReference(final Object id, final Object value)
'''
pass
