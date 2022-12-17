def ():
    '''returns BeanAsArrayDeserializer\n\n
    (final BeanDeserializerBase delegate, final SettableBeanProperty[] ordered)\n
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
def deserialize():
    '''returns Object\n\n
    deserialize(final JsonParser p, final DeserializationContext ctxt)\n
    deserialize(final JsonParser p, final DeserializationContext ctxt, final Object bean)\n
    '''
def deserializeFromObject():
    '''returns Object\n\n
    deserializeFromObject(final JsonParser p, final DeserializationContext ctxt)\n
    '''
