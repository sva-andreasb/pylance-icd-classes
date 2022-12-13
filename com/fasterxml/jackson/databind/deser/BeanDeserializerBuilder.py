def BeanDeserializerBuilder():
'''public BeanDeserializerBuilder(final BeanDescription beanDesc, final DeserializationContext ctxt)
'''
pass
def addOrReplaceProperty():
'''public void addOrReplaceProperty(final SettableBeanProperty prop, final boolean allowOverride)
'''
pass
def addProperty():
'''public void addProperty(final SettableBeanProperty prop)
'''
pass
def addBackReferenceProperty():
'''public void addBackReferenceProperty(final String referenceName, final SettableBeanProperty prop)
'''
pass
def addInjectable():
'''public void addInjectable(final PropertyName propName, final JavaType propType, final Annotations contextAnnotations, final AnnotatedMember member, final Object valueId)
'''
pass
def addIgnorable():
'''public void addIgnorable(final String propName)
'''
pass
def addCreatorProperty():
'''public void addCreatorProperty(final SettableBeanProperty prop)
'''
pass
def setAnySetter():
'''public void setAnySetter(final SettableAnyProperty s)
'''
pass
def setIgnoreUnknownProperties():
'''public void setIgnoreUnknownProperties(final boolean ignore)
'''
pass
def setValueInstantiator():
'''public void setValueInstantiator(final ValueInstantiator inst)
'''
pass
def setObjectIdReader():
'''public void setObjectIdReader(final ObjectIdReader r)
'''
pass
def setPOJOBuilder():
'''public void setPOJOBuilder(final AnnotatedMethod buildMethod, final JsonPOJOBuilder.Value config)
'''
pass
def getProperties():
'''public Iterator<SettableBeanProperty> getProperties()
'''
pass
def findProperty():
'''public SettableBeanProperty findProperty(final PropertyName propertyName)
'''
pass
def hasProperty():
'''public boolean hasProperty(final PropertyName propertyName)
'''
pass
def removeProperty():
'''public SettableBeanProperty removeProperty(final PropertyName name)
'''
pass
def getAnySetter():
'''public SettableAnyProperty getAnySetter()
'''
pass
def getValueInstantiator():
'''public ValueInstantiator getValueInstantiator()
'''
pass
def getInjectables():
'''public List<ValueInjector> getInjectables()
'''
pass
def getObjectIdReader():
'''public ObjectIdReader getObjectIdReader()
'''
pass
def getBuildMethod():
'''public AnnotatedMethod getBuildMethod()
'''
pass
def hasIgnorable():
'''public boolean hasIgnorable(final String name)
'''
pass
def buildAbstract():
'''public AbstractDeserializer buildAbstract()
'''
pass
