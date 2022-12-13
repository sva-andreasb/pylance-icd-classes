def construct():
    '''public static PropertyBasedCreator construct(final DeserializationContext ctxt, final ValueInstantiator valueInstantiator, final SettableBeanProperty[] srcCreatorProps, final BeanPropertyMap allProperties)
    public static PropertyBasedCreator construct(final DeserializationContext ctxt, final ValueInstantiator valueInstantiator, final SettableBeanProperty[] srcCreatorProps, final boolean caseInsensitive)
    public static PropertyBasedCreator construct(final DeserializationContext ctxt, final ValueInstantiator valueInstantiator, final SettableBeanProperty[] srcCreatorProps)
    '''
def properties():
    '''public Collection<SettableBeanProperty> properties()
    '''
def findCreatorProperty():
    '''public SettableBeanProperty findCreatorProperty(final String name)
    public SettableBeanProperty findCreatorProperty(final int propertyIndex)
    '''
def startBuilding():
    '''public PropertyValueBuffer startBuilding(final JsonParser p, final DeserializationContext ctxt, final ObjectIdReader oir)
    '''
def build():
    '''public Object build(final DeserializationContext ctxt, final PropertyValueBuffer buffer)
    '''
def get():
    '''public SettableBeanProperty get(final Object key0)
    '''
def put():
    '''public SettableBeanProperty put(String key, final SettableBeanProperty value)
    '''
