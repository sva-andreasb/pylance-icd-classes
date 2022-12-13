def BeanDeserializerBase():
'''public BeanDeserializerBase(final BeanDeserializerBase src, final ObjectIdReader oir)
public BeanDeserializerBase(final BeanDeserializerBase src, final Set<String> ignorableProps)
'''
pass
def withBeanProperties():
'''public BeanDeserializerBase withBeanProperties(final BeanPropertyMap props)
'''
pass
def resolve():
'''public void resolve(final DeserializationContext ctxt)
'''
pass
def getNullAccessPattern():
'''public AccessPattern getNullAccessPattern()
'''
pass
def getEmptyAccessPattern():
'''public AccessPattern getEmptyAccessPattern()
'''
pass
def getEmptyValue():
'''public Object getEmptyValue(final DeserializationContext ctxt)
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
def hasProperty():
'''public boolean hasProperty(final String propertyName)
'''
pass
def hasViews():
'''public boolean hasViews()
'''
pass
def getPropertyCount():
'''public int getPropertyCount()
'''
pass
def getKnownPropertyNames():
'''public Collection<Object> getKnownPropertyNames()
'''
pass
def getValueType():
'''public JavaType getValueType()
'''
pass
def properties():
'''public Iterator<SettableBeanProperty> properties()
'''
pass
def creatorProperties():
'''public Iterator<SettableBeanProperty> creatorProperties()
'''
pass
def findProperty():
'''public SettableBeanProperty findProperty(final PropertyName propertyName)
public SettableBeanProperty findProperty(final String propertyName)
public SettableBeanProperty findProperty(final int propertyIndex)
'''
pass
def findBackReference():
'''public SettableBeanProperty findBackReference(final String logicalName)
'''
pass
def getValueInstantiator():
'''public ValueInstantiator getValueInstantiator()
'''
pass
def replaceProperty():
'''public void replaceProperty(final SettableBeanProperty original, final SettableBeanProperty replacement)
'''
pass
def deserializeWithType():
'''public Object deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)
'''
pass
def deserializeFromNumber():
'''public Object deserializeFromNumber(final JsonParser p, final DeserializationContext ctxt)
'''
pass
def deserializeFromString():
'''public Object deserializeFromString(final JsonParser p, final DeserializationContext ctxt)
'''
pass
def deserializeFromDouble():
'''public Object deserializeFromDouble(final JsonParser p, final DeserializationContext ctxt)
'''
pass
def deserializeFromBoolean():
'''public Object deserializeFromBoolean(final JsonParser p, final DeserializationContext ctxt)
'''
pass
def deserializeFromArray():
'''public Object deserializeFromArray(final JsonParser p, final DeserializationContext ctxt)
'''
pass
def deserializeFromEmbedded():
'''public Object deserializeFromEmbedded(final JsonParser p, final DeserializationContext ctxt)
'''
pass
def wrapAndThrow():
'''public void wrapAndThrow(final Throwable t, final Object bean, final String fieldName, final DeserializationContext ctxt)
'''
pass
