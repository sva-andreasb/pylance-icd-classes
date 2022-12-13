def BuilderBasedDeserializer():
'''public BuilderBasedDeserializer(final BeanDeserializerBuilder builder, final BeanDescription beanDesc, final JavaType targetType, final BeanPropertyMap properties, final Map<String, SettableBeanProperty> backRefs, final Set<String> ignorableProps, final boolean ignoreAllUnknown, final boolean hasViews)
public BuilderBasedDeserializer(final BeanDeserializerBuilder builder, final BeanDescription beanDesc, final BeanPropertyMap properties, final Map<String, SettableBeanProperty> backRefs, final Set<String> ignorableProps, final boolean ignoreAllUnknown, final boolean hasViews)
public BuilderBasedDeserializer(final BuilderBasedDeserializer src, final ObjectIdReader oir)
public BuilderBasedDeserializer(final BuilderBasedDeserializer src, final Set<String> ignorableProps)
public BuilderBasedDeserializer(final BuilderBasedDeserializer src, final BeanPropertyMap props)
'''
pass
def unwrappingDeserializer():
'''public JsonDeserializer<Object> unwrappingDeserializer(final NameTransformer unwrapper)
'''
pass
def withObjectIdReader():
'''public BeanDeserializerBase withObjectIdReader(final ObjectIdReader oir)
'''
pass
def withIgnorableProperties():
'''public BeanDeserializerBase withIgnorableProperties(final Set<String> ignorableProps)
'''
pass
def withBeanProperties():
'''public BeanDeserializerBase withBeanProperties(final BeanPropertyMap props)
'''
pass
def supportsUpdate():
'''public Boolean supportsUpdate(final DeserializationConfig config)
'''
pass
def deserialize():
'''public Object deserialize(final JsonParser p, final DeserializationContext ctxt)
public Object deserialize(final JsonParser p, final DeserializationContext ctxt, final Object value)
'''
pass
def deserializeFromObject():
'''public Object deserializeFromObject(final JsonParser p, final DeserializationContext ctxt)
'''
pass
