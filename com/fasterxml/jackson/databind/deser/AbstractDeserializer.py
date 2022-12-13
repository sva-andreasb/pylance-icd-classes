def AbstractDeserializer():
'''public AbstractDeserializer(final BeanDeserializerBuilder builder, final BeanDescription beanDesc, final Map<String, SettableBeanProperty> backRefProps, final Map<String, SettableBeanProperty> props)
public AbstractDeserializer(final BeanDeserializerBuilder builder, final BeanDescription beanDesc, final Map<String, SettableBeanProperty> backRefProps)
'''
pass
def constructForNonPOJO():
'''public static AbstractDeserializer constructForNonPOJO(final BeanDescription beanDesc)
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
def getObjectIdReader():
'''public ObjectIdReader getObjectIdReader()
'''
pass
def findBackReference():
'''public SettableBeanProperty findBackReference(final String logicalName)
'''
pass
def deserializeWithType():
'''public Object deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)
'''
pass
def deserialize():
'''public Object deserialize(final JsonParser p, final DeserializationContext ctxt)
'''
pass
