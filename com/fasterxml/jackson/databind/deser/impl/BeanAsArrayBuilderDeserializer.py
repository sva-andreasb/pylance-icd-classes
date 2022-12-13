def BeanAsArrayBuilderDeserializer():
    '''public BeanAsArrayBuilderDeserializer(final BeanDeserializerBase delegate, final JavaType targetType, final SettableBeanProperty[] ordered, final AnnotatedMethod buildMethod)
    '''
def unwrappingDeserializer():
    '''public JsonDeserializer<Object> unwrappingDeserializer(final NameTransformer unwrapper)
    '''
def withObjectIdReader():
    '''public BeanDeserializerBase withObjectIdReader(final ObjectIdReader oir)
    '''
def withIgnorableProperties():
    '''public BeanDeserializerBase withIgnorableProperties(final Set<String> ignorableProps)
    '''
def withBeanProperties():
    '''public BeanDeserializerBase withBeanProperties(final BeanPropertyMap props)
    '''
def supportsUpdate():
    '''public Boolean supportsUpdate(final DeserializationConfig config)
    '''
def deserialize():
    '''public Object deserialize(final JsonParser p, final DeserializationContext ctxt)
    public Object deserialize(final JsonParser p, final DeserializationContext ctxt, final Object value)
    '''
def deserializeFromObject():
    '''public Object deserializeFromObject(final JsonParser p, final DeserializationContext ctxt)
    '''
