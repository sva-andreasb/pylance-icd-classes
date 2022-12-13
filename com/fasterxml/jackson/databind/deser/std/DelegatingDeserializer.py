def DelegatingDeserializer():
'''public DelegatingDeserializer(final JsonDeserializer<?> d)
'''
pass
def resolve():
'''public void resolve(final DeserializationContext ctxt)
'''
pass
def deserialize():
'''public Object deserialize(final JsonParser p, final DeserializationContext ctxt)
public Object deserialize(final JsonParser p, final DeserializationContext ctxt, final Object intoValue)
'''
pass
def deserializeWithType():
'''public Object deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)
'''
pass
def isCachable():
'''public boolean isCachable()
'''
pass
def supportsUpdate():
'''public Boolean supportsUpdate(final DeserializationConfig config)
'''
pass
def findBackReference():
'''public SettableBeanProperty findBackReference(final String logicalName)
'''
pass
def getNullAccessPattern():
'''public AccessPattern getNullAccessPattern()
'''
pass
def getNullValue():
'''public Object getNullValue(final DeserializationContext ctxt)
'''
pass
def getEmptyValue():
'''public Object getEmptyValue(final DeserializationContext ctxt)
'''
pass
def getKnownPropertyNames():
'''public Collection<Object> getKnownPropertyNames()
'''
pass
def getObjectIdReader():
'''public ObjectIdReader getObjectIdReader()
'''
pass
