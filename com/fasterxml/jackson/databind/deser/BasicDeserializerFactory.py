def getFactoryConfig():
    '''returns DeserializerFactoryConfig\n\n
    getFactoryConfig()\n
    '''
def mapAbstractType():
    '''returns JavaType\n\n
    mapAbstractType(final DeserializationConfig config, JavaType type)\n
    '''
def findValueInstantiator():
    '''returns ValueInstantiator\n\n
    findValueInstantiator(final DeserializationContext ctxt, final BeanDescription beanDesc)\n
    '''
def _valueInstantiatorInstance():
    '''returns ValueInstantiator\n\n
    _valueInstantiatorInstance(final DeserializationConfig config, final Annotated annotated, final Object instDef)\n
    '''
def findTypeDeserializer():
    '''returns TypeDeserializer\n\n
    findTypeDeserializer(final DeserializationConfig config, final JavaType baseType)\n
    '''
def createKeyDeserializer():
    '''returns KeyDeserializer\n\n
    createKeyDeserializer(final DeserializationContext ctxt, final JavaType type)\n
    '''
def findPropertyTypeDeserializer():
    '''returns TypeDeserializer\n\n
    findPropertyTypeDeserializer(final DeserializationConfig config, final JavaType baseType, final AnnotatedMember annotated)\n
    '''
def findPropertyContentTypeDeserializer():
    '''returns TypeDeserializer\n\n
    findPropertyContentTypeDeserializer(final DeserializationConfig config, final JavaType containerType, final AnnotatedMember propertyEntity)\n
    '''
