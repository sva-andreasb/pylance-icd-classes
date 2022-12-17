def ():
    '''returns BeanDeserializer\n\n
    (final BeanDeserializerBuilder builder, final BeanDescription beanDesc, final BeanPropertyMap properties, final Map<String, SettableBeanProperty> backRefs, final HashSet<String> ignorableProps, final boolean ignoreAllUnknown, final boolean hasViews)\n
    (final BeanDeserializerBase src, final ObjectIdReader oir)\n
    (final BeanDeserializerBase src, final Set<String> ignorableProps)\n
    (final BeanDeserializerBase src, final BeanPropertyMap props)\n
    '''
def unwrappingDeserializer():
    '''returns JsonDeserializer<Object>\n\n
    unwrappingDeserializer(final NameTransformer transformer)\n
    '''
def withObjectIdReader():
    '''returns BeanDeserializer\n\n
    withObjectIdReader(final ObjectIdReader oir)\n
    '''
def withIgnorableProperties():
    '''returns BeanDeserializer\n\n
    withIgnorableProperties(final Set<String> ignorableProps)\n
    '''
def withBeanProperties():
    '''returns BeanDeserializerBase\n\n
    withBeanProperties(final BeanPropertyMap props)\n
    '''
def deserialize():
    '''returns Object\n\n
    deserialize(final JsonParser p, final DeserializationContext ctxt)\n
    deserialize(final JsonParser p, final DeserializationContext ctxt, final Object bean)\n
    '''
def deserializeFromObject():
    '''returns Object\n\n
    deserializeFromObject(final JsonParser p, final DeserializationContext ctxt)\n
    '''
def setBean():
    '''returns None\n\n
    setBean(final Object bean)\n
    '''
def handleResolvedForwardReference():
    '''returns None\n\n
    handleResolvedForwardReference(final Object id, final Object value)\n
    '''
