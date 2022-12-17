def withModifier():
    '''returns TypeFactory\n\n
    withModifier(final TypeModifier mod)\n
    '''
def withClassLoader():
    '''returns TypeFactory\n\n
    withClassLoader(final ClassLoader classLoader)\n
    '''
def withCache():
    '''returns TypeFactory\n\n
    withCache(final LRUMap<Object, JavaType> cache)\n
    '''
def clearCache():
    '''returns None\n\n
    clearCache()\n
    '''
def getClassLoader():
    '''returns ClassLoader\n\n
    getClassLoader()\n
    '''
def constructSpecializedType():
    '''returns JavaType\n\n
    constructSpecializedType(final JavaType baseType, final Class<?> subclass)\n
    '''
def constructGeneralizedType():
    '''returns JavaType\n\n
    constructGeneralizedType(final JavaType baseType, final Class<?> superClass)\n
    '''
def constructFromCanonical():
    '''returns JavaType\n\n
    constructFromCanonical(final String canonical)\n
    '''
def findTypeParameters():
    '''returns JavaType[]\n\n
    findTypeParameters(final JavaType type, final Class<?> expType)\n
    findTypeParameters(final Class<?> clz, final Class<?> expType, final TypeBindings bindings)\n
    findTypeParameters(final Class<?> clz, final Class<?> expType)\n
    '''
def moreSpecificType():
    '''returns JavaType\n\n
    moreSpecificType(final JavaType type1, final JavaType type2)\n
    '''
def constructType():
    '''returns JavaType\n\n
    constructType(final Type type)\n
    constructType(final Type type, final TypeBindings bindings)\n
    constructType(final TypeReference<?> typeRef)\n
    constructType(final Type type, final Class<?> contextClass)\n
    constructType(final Type type, JavaType contextType)\n
    '''
def constructArrayType():
    '''returns ArrayType\n\n
    constructArrayType(final Class<?> elementType)\n
    constructArrayType(final JavaType elementType)\n
    '''
def constructCollectionType():
    '''returns CollectionType\n\n
    constructCollectionType(final Class<? extends Collection> collectionClass, final Class<?> elementClass)\n
    constructCollectionType(final Class<? extends Collection> collectionClass, final JavaType elementType)\n
    '''
def constructCollectionLikeType():
    '''returns CollectionLikeType\n\n
    constructCollectionLikeType(final Class<?> collectionClass, final Class<?> elementClass)\n
    constructCollectionLikeType(final Class<?> collectionClass, final JavaType elementType)\n
    '''
def constructMapType():
    '''returns MapType\n\n
    constructMapType(final Class<? extends Map> mapClass, final Class<?> keyClass, final Class<?> valueClass)\n
    constructMapType(final Class<? extends Map> mapClass, final JavaType keyType, final JavaType valueType)\n
    '''
def constructMapLikeType():
    '''returns MapLikeType\n\n
    constructMapLikeType(final Class<?> mapClass, final Class<?> keyClass, final Class<?> valueClass)\n
    constructMapLikeType(final Class<?> mapClass, final JavaType keyType, final JavaType valueType)\n
    '''
def constructSimpleType():
    '''returns JavaType\n\n
    constructSimpleType(final Class<?> rawType, final JavaType[] parameterTypes)\n
    constructSimpleType(final Class<?> rawType, final Class<?> parameterTarget, final JavaType[] parameterTypes)\n
    '''
def constructReferenceType():
    '''returns JavaType\n\n
    constructReferenceType(final Class<?> rawType, final JavaType referredType)\n
    '''
def uncheckedSimpleType():
    '''returns JavaType\n\n
    uncheckedSimpleType(final Class<?> cls)\n
    '''
def constructParametricType():
    '''returns JavaType\n\n
    constructParametricType(final Class<?> parametrized, final Class<?>... parameterClasses)\n
    constructParametricType(final Class<?> rawType, final JavaType... parameterTypes)\n
    '''
def constructParametrizedType():
    '''returns JavaType\n\n
    constructParametrizedType(final Class<?> parametrized, final Class<?> parametersFor, final JavaType... parameterTypes)\n
    constructParametrizedType(final Class<?> parametrized, final Class<?> parametersFor, final Class<?>... parameterClasses)\n
    '''
def constructRawCollectionType():
    '''returns CollectionType\n\n
    constructRawCollectionType(final Class<? extends Collection> collectionClass)\n
    '''
def constructRawCollectionLikeType():
    '''returns CollectionLikeType\n\n
    constructRawCollectionLikeType(final Class<?> collectionClass)\n
    '''
def constructRawMapType():
    '''returns MapType\n\n
    constructRawMapType(final Class<? extends Map> mapClass)\n
    '''
def constructRawMapLikeType():
    '''returns MapLikeType\n\n
    constructRawMapLikeType(final Class<?> mapClass)\n
    '''
