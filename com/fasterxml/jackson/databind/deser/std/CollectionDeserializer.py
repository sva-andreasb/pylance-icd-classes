def CollectionDeserializer():
'''public CollectionDeserializer(final JavaType collectionType, final JsonDeserializer<Object> valueDeser, final TypeDeserializer valueTypeDeser, final ValueInstantiator valueInstantiator)
'''
pass
def isCachable():
'''public boolean isCachable()
'''
pass
def createContextual():
'''public CollectionDeserializer createContextual(final DeserializationContext ctxt, final BeanProperty property)
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
def deserialize():
'''public Collection<Object> deserialize(final JsonParser p, final DeserializationContext ctxt)
public Collection<Object> deserialize(final JsonParser p, final DeserializationContext ctxt, final Collection<Object> result)
'''
pass
def deserializeWithType():
'''public Object deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)
'''
pass
def CollectionReferringAccumulator():
'''public CollectionReferringAccumulator(final Class<?> elementType, final Collection<Object> result)
'''
pass
def add():
'''public void add(final Object value)
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
