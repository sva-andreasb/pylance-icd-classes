def BeanDeserializerBase():
    '''    public BeanDeserializerBase(final BeanDeserializerBase src, final ObjectIdReader oir)
    public BeanDeserializerBase(final BeanDeserializerBase src, final Set<String> ignorableProps)
    '''
def withBeanProperties():
    '''    public BeanDeserializerBase withBeanProperties(final BeanPropertyMap props)
    '''
def resolve():
    '''    public void resolve(final DeserializationContext ctxt)
    '''
def getNullAccessPattern():
    '''    public AccessPattern getNullAccessPattern()
    '''
def getEmptyAccessPattern():
    '''    public AccessPattern getEmptyAccessPattern()
    '''
def getEmptyValue():
    '''    public Object getEmptyValue(final DeserializationContext ctxt)
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
def hasProperty():
    '''    public boolean hasProperty(final String propertyName)
    '''
def hasViews():
    '''    public boolean hasViews()
    '''
def getPropertyCount():
    '''    public int getPropertyCount()
    '''
def getKnownPropertyNames():
    '''    public Collection<Object> getKnownPropertyNames()
    '''
def getValueType():
    '''    public JavaType getValueType()
    '''
def properties():
    '''    public Iterator<SettableBeanProperty> properties()
    '''
def creatorProperties():
    '''    public Iterator<SettableBeanProperty> creatorProperties()
    '''
def findProperty():
    '''    public SettableBeanProperty findProperty(final PropertyName propertyName)
    public SettableBeanProperty findProperty(final String propertyName)
    public SettableBeanProperty findProperty(final int propertyIndex)
    '''
def findBackReference():
    '''    public SettableBeanProperty findBackReference(final String logicalName)
    '''
def getValueInstantiator():
    '''    public ValueInstantiator getValueInstantiator()
    '''
def replaceProperty():
    '''    public void replaceProperty(final SettableBeanProperty original, final SettableBeanProperty replacement)
    '''
def deserializeWithType():
    '''    public Object deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)
    '''
def deserializeFromNumber():
    '''    public Object deserializeFromNumber(final JsonParser p, final DeserializationContext ctxt)
    '''
def deserializeFromString():
    '''    public Object deserializeFromString(final JsonParser p, final DeserializationContext ctxt)
    '''
def deserializeFromDouble():
    '''    public Object deserializeFromDouble(final JsonParser p, final DeserializationContext ctxt)
    '''
def deserializeFromBoolean():
    '''    public Object deserializeFromBoolean(final JsonParser p, final DeserializationContext ctxt)
    '''
def deserializeFromArray():
    '''    public Object deserializeFromArray(final JsonParser p, final DeserializationContext ctxt)
    '''
def deserializeFromEmbedded():
    '''    public Object deserializeFromEmbedded(final JsonParser p, final DeserializationContext ctxt)
    '''
def wrapAndThrow():
    '''    public void wrapAndThrow(final Throwable t, final Object bean, final String fieldName, final DeserializationContext ctxt)
    '''
