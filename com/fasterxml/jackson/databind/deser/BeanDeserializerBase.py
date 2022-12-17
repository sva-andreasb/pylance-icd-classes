def ():
    '''returns BeanDeserializerBase\n\n
    (final BeanDeserializerBase src, final ObjectIdReader oir)\n
    (final BeanDeserializerBase src, final Set<String> ignorableProps)\n
    '''
def withBeanProperties():
    '''returns BeanDeserializerBase\n\n
    withBeanProperties(final BeanPropertyMap props)\n
    '''
def resolve():
    '''returns None\n\n
    resolve(final DeserializationContext ctxt)\n
    '''
def getNullAccessPattern():
    '''returns AccessPattern\n\n
    getNullAccessPattern()\n
    '''
def getEmptyAccessPattern():
    '''returns AccessPattern\n\n
    getEmptyAccessPattern()\n
    '''
def getEmptyValue():
    '''returns Object\n\n
    getEmptyValue(final DeserializationContext ctxt)\n
    '''
def isCachable():
    '''returns boolean\n\n
    isCachable()\n
    '''
def supportsUpdate():
    '''returns Boolean\n\n
    supportsUpdate(final DeserializationConfig config)\n
    '''
def getObjectIdReader():
    '''returns ObjectIdReader\n\n
    getObjectIdReader()\n
    '''
def hasProperty():
    '''returns boolean\n\n
    hasProperty(final String propertyName)\n
    '''
def hasViews():
    '''returns boolean\n\n
    hasViews()\n
    '''
def getPropertyCount():
    '''returns int\n\n
    getPropertyCount()\n
    '''
def getKnownPropertyNames():
    '''returns Collection<Object>\n\n
    getKnownPropertyNames()\n
    '''
def getValueType():
    '''returns JavaType\n\n
    getValueType()\n
    '''
def properties():
    '''returns Iterator<SettableBeanProperty>\n\n
    properties()\n
    '''
def creatorProperties():
    '''returns Iterator<SettableBeanProperty>\n\n
    creatorProperties()\n
    '''
def findProperty():
    '''returns SettableBeanProperty\n\n
    findProperty(final PropertyName propertyName)\n
    findProperty(final String propertyName)\n
    findProperty(final int propertyIndex)\n
    '''
def findBackReference():
    '''returns SettableBeanProperty\n\n
    findBackReference(final String logicalName)\n
    '''
def getValueInstantiator():
    '''returns ValueInstantiator\n\n
    getValueInstantiator()\n
    '''
def replaceProperty():
    '''returns None\n\n
    replaceProperty(final SettableBeanProperty original, final SettableBeanProperty replacement)\n
    '''
def deserializeWithType():
    '''returns Object\n\n
    deserializeWithType(final JsonParser p, final DeserializationContext ctxt, final TypeDeserializer typeDeserializer)\n
    '''
def deserializeFromNumber():
    '''returns Object\n\n
    deserializeFromNumber(final JsonParser p, final DeserializationContext ctxt)\n
    '''
def deserializeFromString():
    '''returns Object\n\n
    deserializeFromString(final JsonParser p, final DeserializationContext ctxt)\n
    '''
def deserializeFromDouble():
    '''returns Object\n\n
    deserializeFromDouble(final JsonParser p, final DeserializationContext ctxt)\n
    '''
def deserializeFromBoolean():
    '''returns Object\n\n
    deserializeFromBoolean(final JsonParser p, final DeserializationContext ctxt)\n
    '''
def deserializeFromArray():
    '''returns Object\n\n
    deserializeFromArray(final JsonParser p, final DeserializationContext ctxt)\n
    '''
def deserializeFromEmbedded():
    '''returns Object\n\n
    deserializeFromEmbedded(final JsonParser p, final DeserializationContext ctxt)\n
    '''
def wrapAndThrow():
    '''returns None\n\n
    wrapAndThrow(final Throwable t, final Object bean, final String fieldName, final DeserializationContext ctxt)\n
    '''
