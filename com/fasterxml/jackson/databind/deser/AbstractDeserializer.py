def AbstractDeserializer():
    '''    public AbstractDeserializer(final BeanDeserializerBuilder builder, final BeanDescription beanDesc, final Map<String, SettableBeanProperty> backRefProps, final Map<String, SettableBeanProperty> props)
    public AbstractDeserializer(final BeanDeserializerBuilder builder, final BeanDescription beanDesc, final Map<String, SettableBeanProperty> backRefProps)
    '''
def constructForNonPOJO():
    '''    public static AbstractDeserializer constructForNonPOJO(final BeanDescription beanDesc)
    '''
def isCachable():
    '''    public boolean isCachable()
    '''
def supportsUpdate():
    '''    public Boolean supportsUpdate(final DeserializationConfig config)
    '''
def getObjectIdReader():
    '''    public ObjectIdReader getObjectIdReader()
    '''
def findBackReference():
    '''    public SettableBeanProperty findBackReference(final String logicalName)
    '''
def deserializeWithType():
    '''    public Object deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)
    '''
def deserialize():
    '''    public Object deserialize(final JsonParser p, final DeserializationContext ctxt)
    '''
