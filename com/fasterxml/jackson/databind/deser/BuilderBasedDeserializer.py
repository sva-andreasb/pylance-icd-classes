def ():
    '''returns BuilderBasedDeserializer\n\n
    (final BeanDeserializerBuilder builder, final BeanDescription beanDesc, final JavaType targetType, final BeanPropertyMap properties, final Map<String, SettableBeanProperty> backRefs, final Set<String> ignorableProps, final boolean ignoreAllUnknown, final boolean hasViews)\n
    (final BeanDeserializerBuilder builder, final BeanDescription beanDesc, final BeanPropertyMap properties, final Map<String, SettableBeanProperty> backRefs, final Set<String> ignorableProps, final boolean ignoreAllUnknown, final boolean hasViews)\n
    (final BuilderBasedDeserializer src, final ObjectIdReader oir)\n
    (final BuilderBasedDeserializer src, final Set<String> ignorableProps)\n
    (final BuilderBasedDeserializer src, final BeanPropertyMap props)\n
    '''
def unwrappingDeserializer():
    '''returns JsonDeserializer<Object>\n\n
    unwrappingDeserializer(final NameTransformer unwrapper)\n
    '''
def withObjectIdReader():
    '''returns BeanDeserializerBase\n\n
    withObjectIdReader(final ObjectIdReader oir)\n
    '''
def withIgnorableProperties():
    '''returns BeanDeserializerBase\n\n
    withIgnorableProperties(final Set<String> ignorableProps)\n
    '''
def withBeanProperties():
    '''returns BeanDeserializerBase\n\n
    withBeanProperties(final BeanPropertyMap props)\n
    '''
def supportsUpdate():
    '''returns Boolean\n\n
    supportsUpdate(final DeserializationConfig config)\n
    '''
def deserialize():
    '''returns Object\n\n
    deserialize(final JsonParser p, final DeserializationContext ctxt)\n
    deserialize(final JsonParser p, final DeserializationContext ctxt, final Object value)\n
    '''
def deserializeFromObject():
    '''returns Object\n\n
    deserializeFromObject(final JsonParser p, final DeserializationContext ctxt)\n
    '''
