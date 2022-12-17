def withConfig():
    '''returns SerializerFactory\n\n
    withConfig(final SerializerFactoryConfig config)\n
    '''
def createSerializer():
    '''returns JsonSerializer<Object>\n\n
    createSerializer(final SerializerProvider prov, final JavaType origType)\n
    '''
def findBeanSerializer():
    '''returns JsonSerializer<Object>\n\n
    findBeanSerializer(final SerializerProvider prov, final JavaType type, final BeanDescription beanDesc)\n
    '''
def findPropertyTypeSerializer():
    '''returns TypeSerializer\n\n
    findPropertyTypeSerializer(final JavaType baseType, final SerializationConfig config, final AnnotatedMember accessor)\n
    '''
def findPropertyContentTypeSerializer():
    '''returns TypeSerializer\n\n
    findPropertyContentTypeSerializer(final JavaType containerType, final SerializationConfig config, final AnnotatedMember accessor)\n
    '''
