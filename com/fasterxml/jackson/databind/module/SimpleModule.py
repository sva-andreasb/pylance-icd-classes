def ():
    '''returns SimpleModule\n\n
    ()\n
    (final String name)\n
    (final Version version)\n
    (final String name, final Version version)\n
    (final String name, final Version version, final Map<Class<?>, JsonDeserializer<?>> deserializers)\n
    (final String name, final Version version, final List<JsonSerializer<?>> serializers)\n
    (final String name, final Version version, final Map<Class<?>, JsonDeserializer<?>> deserializers, final List<JsonSerializer<?>> serializers)\n
    '''
def getTypeId():
    '''returns Object\n\n
    getTypeId()\n
    '''
def setSerializers():
    '''returns None\n\n
    setSerializers(final SimpleSerializers s)\n
    '''
def setDeserializers():
    '''returns None\n\n
    setDeserializers(final SimpleDeserializers d)\n
    '''
def setKeySerializers():
    '''returns None\n\n
    setKeySerializers(final SimpleSerializers ks)\n
    '''
def setKeyDeserializers():
    '''returns None\n\n
    setKeyDeserializers(final SimpleKeyDeserializers kd)\n
    '''
def setAbstractTypes():
    '''returns None\n\n
    setAbstractTypes(final SimpleAbstractTypeResolver atr)\n
    '''
def setValueInstantiators():
    '''returns None\n\n
    setValueInstantiators(final SimpleValueInstantiators svi)\n
    '''
def setDeserializerModifier():
    '''returns SimpleModule\n\n
    setDeserializerModifier(final BeanDeserializerModifier mod)\n
    '''
def setSerializerModifier():
    '''returns SimpleModule\n\n
    setSerializerModifier(final BeanSerializerModifier mod)\n
    '''
def addSerializer():
    '''returns SimpleModule\n\n
    addSerializer(final JsonSerializer<?> ser)\n
    '''
def addKeyDeserializer():
    '''returns SimpleModule\n\n
    addKeyDeserializer(final Class<?> type, final KeyDeserializer deser)\n
    '''
def registerSubtypes():
    '''returns SimpleModule\n\n
    registerSubtypes(final Class<?>... subtypes)\n
    registerSubtypes(final NamedType... subtypes)\n
    registerSubtypes(final Collection<Class<?>> subtypes)\n
    '''
def addValueInstantiator():
    '''returns SimpleModule\n\n
    addValueInstantiator(final Class<?> beanType, final ValueInstantiator inst)\n
    '''
def setMixInAnnotation():
    '''returns SimpleModule\n\n
    setMixInAnnotation(final Class<?> targetType, final Class<?> mixinClass)\n
    '''
def getModuleName():
    '''returns String\n\n
    getModuleName()\n
    '''
def setupModule():
    '''returns None\n\n
    setupModule(final SetupContext context)\n
    '''
def version():
    '''returns Version\n\n
    version()\n
    '''
