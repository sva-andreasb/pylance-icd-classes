def getFactoryConfig():
    '''    public DeserializerFactoryConfig getFactoryConfig()
    '''
def withAdditionalDeserializers():
    '''    public final DeserializerFactory withAdditionalDeserializers(final Deserializers additional)
    '''
def withAdditionalKeyDeserializers():
    '''    public final DeserializerFactory withAdditionalKeyDeserializers(final KeyDeserializers additional)
    '''
def withDeserializerModifier():
    '''    public final DeserializerFactory withDeserializerModifier(final BeanDeserializerModifier modifier)
    '''
def withAbstractTypeResolver():
    '''    public final DeserializerFactory withAbstractTypeResolver(final AbstractTypeResolver resolver)
    '''
def withValueInstantiators():
    '''    public final DeserializerFactory withValueInstantiators(final ValueInstantiators instantiators)
    '''
def mapAbstractType():
    '''    public JavaType mapAbstractType(final DeserializationConfig config, JavaType type)
    '''
def findValueInstantiator():
    '''    public ValueInstantiator findValueInstantiator(final DeserializationContext ctxt, final BeanDescription beanDesc)
    '''
def _valueInstantiatorInstance():
    '''    public ValueInstantiator _valueInstantiatorInstance(final DeserializationConfig config, final Annotated annotated, final Object instDef)
    '''
def findTypeDeserializer():
    '''    public TypeDeserializer findTypeDeserializer(final DeserializationConfig config, final JavaType baseType)
    '''
def createKeyDeserializer():
    '''    public KeyDeserializer createKeyDeserializer(final DeserializationContext ctxt, final JavaType type)
    '''
def findPropertyTypeDeserializer():
    '''    public TypeDeserializer findPropertyTypeDeserializer(final DeserializationConfig config, final JavaType baseType, final AnnotatedMember annotated)
    '''
def findPropertyContentTypeDeserializer():
    '''    public TypeDeserializer findPropertyContentTypeDeserializer(final DeserializationConfig config, final JavaType containerType, final AnnotatedMember propertyEntity)
    '''
