def getFactoryConfig():
'''public DeserializerFactoryConfig getFactoryConfig()
'''
pass
def withAdditionalDeserializers():
'''public final DeserializerFactory withAdditionalDeserializers(final Deserializers additional)
'''
pass
def withAdditionalKeyDeserializers():
'''public final DeserializerFactory withAdditionalKeyDeserializers(final KeyDeserializers additional)
'''
pass
def withDeserializerModifier():
'''public final DeserializerFactory withDeserializerModifier(final BeanDeserializerModifier modifier)
'''
pass
def withAbstractTypeResolver():
'''public final DeserializerFactory withAbstractTypeResolver(final AbstractTypeResolver resolver)
'''
pass
def withValueInstantiators():
'''public final DeserializerFactory withValueInstantiators(final ValueInstantiators instantiators)
'''
pass
def mapAbstractType():
'''public JavaType mapAbstractType(final DeserializationConfig config, JavaType type)
'''
pass
def findValueInstantiator():
'''public ValueInstantiator findValueInstantiator(final DeserializationContext ctxt, final BeanDescription beanDesc)
'''
pass
def _valueInstantiatorInstance():
'''public ValueInstantiator _valueInstantiatorInstance(final DeserializationConfig config, final Annotated annotated, final Object instDef)
'''
pass
def findTypeDeserializer():
'''public TypeDeserializer findTypeDeserializer(final DeserializationConfig config, final JavaType baseType)
'''
pass
def createKeyDeserializer():
'''public KeyDeserializer createKeyDeserializer(final DeserializationContext ctxt, final JavaType type)
'''
pass
def findPropertyTypeDeserializer():
'''public TypeDeserializer findPropertyTypeDeserializer(final DeserializationConfig config, final JavaType baseType, final AnnotatedMember annotated)
'''
pass
def findPropertyContentTypeDeserializer():
'''public TypeDeserializer findPropertyContentTypeDeserializer(final DeserializationConfig config, final JavaType containerType, final AnnotatedMember propertyEntity)
'''
pass
