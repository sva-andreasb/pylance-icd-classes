def ():
    '''returns BeanDeserializerFactory\n\n
    (final DeserializerFactoryConfig config)\n
    '''
def withConfig():
    '''returns DeserializerFactory\n\n
    withConfig(final DeserializerFactoryConfig config)\n
    '''
def createBeanDeserializer():
    '''returns JsonDeserializer<Object>\n\n
    createBeanDeserializer(final DeserializationContext ctxt, final JavaType type, BeanDescription beanDesc)\n
    '''
def createBuilderBasedDeserializer():
    '''returns JsonDeserializer<Object>\n\n
    createBuilderBasedDeserializer(final DeserializationContext ctxt, final JavaType valueType, final BeanDescription beanDesc, final Class<?> builderClass)\n
    '''
def buildBeanDeserializer():
    '''returns JsonDeserializer<Object>\n\n
    buildBeanDeserializer(final DeserializationContext ctxt, final JavaType type, final BeanDescription beanDesc)\n
    '''
def buildThrowableDeserializer():
    '''returns JsonDeserializer<Object>\n\n
    buildThrowableDeserializer(final DeserializationContext ctxt, final JavaType type, final BeanDescription beanDesc)\n
    '''
