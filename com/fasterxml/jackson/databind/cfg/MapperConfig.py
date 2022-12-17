def compileString():
    '''returns SerializableString\n\n
    compileString(final String src)\n
    '''
def getClassIntrospector():
    '''returns ClassIntrospector\n\n
    getClassIntrospector()\n
    '''
def getAnnotationIntrospector():
    '''returns AnnotationIntrospector\n\n
    getAnnotationIntrospector()\n
    '''
def constructSpecializedType():
    '''returns JavaType\n\n
    constructSpecializedType(final JavaType baseType, final Class<?> subclass)\n
    '''
def introspectClassAnnotations():
    '''returns BeanDescription\n\n
    introspectClassAnnotations(final Class<?> cls)\n
    introspectClassAnnotations(final JavaType type)\n
    '''
def introspectDirectClassAnnotations():
    '''returns BeanDescription\n\n
    introspectDirectClassAnnotations(final Class<?> cls)\n
    '''
def getBase64Variant():
    '''returns Base64Variant\n\n
    getBase64Variant()\n
    '''
def typeIdResolverInstance():
    '''returns TypeIdResolver\n\n
    typeIdResolverInstance(final Annotated annotated, final Class<? extends TypeIdResolver> resolverClass)\n
    '''
