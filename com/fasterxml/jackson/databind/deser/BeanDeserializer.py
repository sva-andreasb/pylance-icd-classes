def BeanDeserializer():
'''public BeanDeserializer(final BeanDeserializerBuilder builder, final BeanDescription beanDesc, final BeanPropertyMap properties, final Map<String, SettableBeanProperty> backRefs, final HashSet<String> ignorableProps, final boolean ignoreAllUnknown, final boolean hasViews)
public BeanDeserializer(final BeanDeserializerBase src, final ObjectIdReader oir)
public BeanDeserializer(final BeanDeserializerBase src, final Set<String> ignorableProps)
public BeanDeserializer(final BeanDeserializerBase src, final BeanPropertyMap props)
'''
pass
def unwrappingDeserializer():
'''public JsonDeserializer<Object> unwrappingDeserializer(final NameTransformer transformer)
'''
pass
def withObjectIdReader():
'''public BeanDeserializer withObjectIdReader(final ObjectIdReader oir)
'''
pass
def withIgnorableProperties():
'''public BeanDeserializer withIgnorableProperties(final Set<String> ignorableProps)
'''
pass
def withBeanProperties():
'''public BeanDeserializerBase withBeanProperties(final BeanPropertyMap props)
'''
pass
def deserialize():
'''public Object deserialize(final JsonParser p, final DeserializationContext ctxt)
public Object deserialize(final JsonParser p, final DeserializationContext ctxt, final Object bean)
'''
pass
def deserializeFromObject():
'''public Object deserializeFromObject(final JsonParser p, final DeserializationContext ctxt)
'''
pass
def setBean():
'''public void setBean(final Object bean)
'''
pass
def handleResolvedForwardReference():
'''public void handleResolvedForwardReference(final Object id, final Object value)
'''
pass
