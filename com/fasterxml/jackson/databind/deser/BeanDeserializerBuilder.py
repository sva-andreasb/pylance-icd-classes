def ():
    '''returns BeanDeserializerBuilder\n\n
    (final BeanDescription beanDesc, final DeserializationContext ctxt)\n
    '''
def addOrReplaceProperty():
    '''returns None\n\n
    addOrReplaceProperty(final SettableBeanProperty prop, final boolean allowOverride)\n
    '''
def addProperty():
    '''returns None\n\n
    addProperty(final SettableBeanProperty prop)\n
    '''
def addBackReferenceProperty():
    '''returns None\n\n
    addBackReferenceProperty(final String referenceName, final SettableBeanProperty prop)\n
    '''
def addInjectable():
    '''returns None\n\n
    addInjectable(final PropertyName propName, final JavaType propType, final Annotations contextAnnotations, final AnnotatedMember member, final Object valueId)\n
    '''
def addIgnorable():
    '''returns None\n\n
    addIgnorable(final String propName)\n
    '''
def addCreatorProperty():
    '''returns None\n\n
    addCreatorProperty(final SettableBeanProperty prop)\n
    '''
def setAnySetter():
    '''returns None\n\n
    setAnySetter(final SettableAnyProperty s)\n
    '''
def setIgnoreUnknownProperties():
    '''returns None\n\n
    setIgnoreUnknownProperties(final boolean ignore)\n
    '''
def setValueInstantiator():
    '''returns None\n\n
    setValueInstantiator(final ValueInstantiator inst)\n
    '''
def setObjectIdReader():
    '''returns None\n\n
    setObjectIdReader(final ObjectIdReader r)\n
    '''
def setPOJOBuilder():
    '''returns None\n\n
    setPOJOBuilder(final AnnotatedMethod buildMethod, final JsonPOJOBuilder.Value config)\n
    '''
def getProperties():
    '''returns Iterator<SettableBeanProperty>\n\n
    getProperties()\n
    '''
def findProperty():
    '''returns SettableBeanProperty\n\n
    findProperty(final PropertyName propertyName)\n
    '''
def hasProperty():
    '''returns boolean\n\n
    hasProperty(final PropertyName propertyName)\n
    '''
def removeProperty():
    '''returns SettableBeanProperty\n\n
    removeProperty(final PropertyName name)\n
    '''
def getAnySetter():
    '''returns SettableAnyProperty\n\n
    getAnySetter()\n
    '''
def getValueInstantiator():
    '''returns ValueInstantiator\n\n
    getValueInstantiator()\n
    '''
def getInjectables():
    '''returns List<ValueInjector>\n\n
    getInjectables()\n
    '''
def getObjectIdReader():
    '''returns ObjectIdReader\n\n
    getObjectIdReader()\n
    '''
def getBuildMethod():
    '''returns AnnotatedMethod\n\n
    getBuildMethod()\n
    '''
def hasIgnorable():
    '''returns boolean\n\n
    hasIgnorable(final String name)\n
    '''
def buildAbstract():
    '''returns AbstractDeserializer\n\n
    buildAbstract()\n
    '''
