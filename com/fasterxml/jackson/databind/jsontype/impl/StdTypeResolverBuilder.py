def ():
    '''returns StdTypeResolverBuilder\n\n
    ()\n
    '''
def init():
    '''returns StdTypeResolverBuilder\n\n
    init(final JsonTypeInfo.Id idType, final TypeIdResolver idRes)\n
    '''
def buildTypeSerializer():
    '''returns TypeSerializer\n\n
    buildTypeSerializer(final SerializationConfig config, final JavaType baseType, final Collection<NamedType> subtypes)\n
    '''
def buildTypeDeserializer():
    '''returns TypeDeserializer\n\n
    buildTypeDeserializer(final DeserializationConfig config, final JavaType baseType, final Collection<NamedType> subtypes)\n
    '''
def inclusion():
    '''returns StdTypeResolverBuilder\n\n
    inclusion(final JsonTypeInfo.As includeAs)\n
    '''
def typeProperty():
    '''returns StdTypeResolverBuilder\n\n
    typeProperty(String typeIdPropName)\n
    '''
def defaultImpl():
    '''returns StdTypeResolverBuilder\n\n
    defaultImpl(final Class<?> defaultImpl)\n
    '''
def typeIdVisibility():
    '''returns StdTypeResolverBuilder\n\n
    typeIdVisibility(final boolean isVisible)\n
    '''
def getTypeProperty():
    '''returns String\n\n
    getTypeProperty()\n
    '''
def isTypeIdVisible():
    '''returns boolean\n\n
    isTypeIdVisible()\n
    '''
