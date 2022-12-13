def BeanDeserializerBuilder():
    '''public BeanDeserializerBuilder(final BeanDescription beanDesc, final DeserializationContext ctxt)
    '''
def addOrReplaceProperty():
    '''public void addOrReplaceProperty(final SettableBeanProperty prop, final boolean allowOverride)
    '''
def addProperty():
    '''public void addProperty(final SettableBeanProperty prop)
    '''
def addBackReferenceProperty():
    '''public void addBackReferenceProperty(final String referenceName, final SettableBeanProperty prop)
    '''
def addInjectable():
    '''public void addInjectable(final PropertyName propName, final JavaType propType, final Annotations contextAnnotations, final AnnotatedMember member, final Object valueId)
    '''
def addIgnorable():
    '''public void addIgnorable(final String propName)
    '''
def addCreatorProperty():
    '''public void addCreatorProperty(final SettableBeanProperty prop)
    '''
def setAnySetter():
    '''public void setAnySetter(final SettableAnyProperty s)
    '''
def setIgnoreUnknownProperties():
    '''public void setIgnoreUnknownProperties(final boolean ignore)
    '''
def setValueInstantiator():
    '''public void setValueInstantiator(final ValueInstantiator inst)
    '''
def setObjectIdReader():
    '''public void setObjectIdReader(final ObjectIdReader r)
    '''
def setPOJOBuilder():
    '''public void setPOJOBuilder(final AnnotatedMethod buildMethod, final JsonPOJOBuilder.Value config)
    '''
def getProperties():
    '''public Iterator<SettableBeanProperty> getProperties()
    '''
def findProperty():
    '''public SettableBeanProperty findProperty(final PropertyName propertyName)
    '''
def hasProperty():
    '''public boolean hasProperty(final PropertyName propertyName)
    '''
def removeProperty():
    '''public SettableBeanProperty removeProperty(final PropertyName name)
    '''
def getAnySetter():
    '''public SettableAnyProperty getAnySetter()
    '''
def getValueInstantiator():
    '''public ValueInstantiator getValueInstantiator()
    '''
def getInjectables():
    '''public List<ValueInjector> getInjectables()
    '''
def getObjectIdReader():
    '''public ObjectIdReader getObjectIdReader()
    '''
def getBuildMethod():
    '''public AnnotatedMethod getBuildMethod()
    '''
def hasIgnorable():
    '''public boolean hasIgnorable(final String name)
    '''
def buildAbstract():
    '''public AbstractDeserializer buildAbstract()
    '''
