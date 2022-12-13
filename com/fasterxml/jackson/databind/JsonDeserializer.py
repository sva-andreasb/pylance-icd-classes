def deserialize():
'''public T deserialize(final JsonParser p, final DeserializationContext ctxt, final T intoValue)
'''
pass
def deserializeWithType():
'''public Object deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)
'''
pass
def unwrappingDeserializer():
'''public JsonDeserializer<T> unwrappingDeserializer(final NameTransformer unwrapper)
'''
pass
def isCachable():
'''public boolean isCachable()
'''
pass
def getKnownPropertyNames():
'''public Collection<Object> getKnownPropertyNames()
'''
pass
def getNullValue():
'''public T getNullValue(final DeserializationContext ctxt)
public T getNullValue()
'''
pass
def getNullAccessPattern():
'''public AccessPattern getNullAccessPattern()
'''
pass
def getEmptyAccessPattern():
'''public AccessPattern getEmptyAccessPattern()
'''
pass
def getEmptyValue():
'''public Object getEmptyValue(final DeserializationContext ctxt)
public Object getEmptyValue()
'''
pass
def getObjectIdReader():
'''public ObjectIdReader getObjectIdReader()
'''
pass
def findBackReference():
'''public SettableBeanProperty findBackReference(final String refName)
'''
pass
def supportsUpdate():
'''public Boolean supportsUpdate(final DeserializationConfig config)
'''
pass
