def ():
    '''returns ReflectionBasedResolvedMemberImpl\n\n
    (final MemberKind kind, final UnresolvedType declaringType, final int modifiers, final UnresolvedType returnType, final String name, final UnresolvedType[] parameterTypes, final java.lang.reflect.Member reflectMember)\n
    (final MemberKind kind, final UnresolvedType declaringType, final int modifiers, final UnresolvedType returnType, final String name, final UnresolvedType[] parameterTypes, final UnresolvedType[] checkedExceptions, final java.lang.reflect.Member reflectMember)\n
    (final MemberKind kind, final UnresolvedType declaringType, final int modifiers, final UnresolvedType returnType, final String name, final UnresolvedType[] parameterTypes, final UnresolvedType[] checkedExceptions, final ResolvedMember backingGenericMember, final java.lang.reflect.Member reflectMember)\n
    (final MemberKind kind, final UnresolvedType declaringType, final int modifiers, final String name, final String signature, final java.lang.reflect.Member reflectMember)\n
    '''
def setGenericSignatureInformationProvider():
    '''returns None\n\n
    setGenericSignatureInformationProvider(final GenericSignatureInformationProvider gsigProvider)\n
    '''
def getGenericParameterTypes():
    '''returns UnresolvedType[]\n\n
    getGenericParameterTypes()\n
    '''
def getGenericReturnType():
    '''returns UnresolvedType\n\n
    getGenericReturnType()\n
    '''
def isSynthetic():
    '''returns boolean\n\n
    isSynthetic()\n
    '''
def isVarargsMethod():
    '''returns boolean\n\n
    isVarargsMethod()\n
    '''
def isBridgeMethod():
    '''returns boolean\n\n
    isBridgeMethod()\n
    '''
def setAnnotationFinder():
    '''returns None\n\n
    setAnnotationFinder(final AnnotationFinder finder)\n
    '''
def hasAnnotation():
    '''returns boolean\n\n
    hasAnnotation(final UnresolvedType ofType)\n
    '''
def hasAnnotations():
    '''returns boolean\n\n
    hasAnnotations()\n
    '''
def getAnnotationTypes():
    '''returns ResolvedType[]\n\n
    getAnnotationTypes()\n
    '''
def getAnnotationOfType():
    '''returns AnnotationAJ\n\n
    getAnnotationOfType(final UnresolvedType ofType)\n
    '''
def getAnnotationDefaultValue():
    '''returns String\n\n
    getAnnotationDefaultValue()\n
    '''
def getParameterAnnotationTypes():
    '''returns ResolvedType[][]\n\n
    getParameterAnnotationTypes()\n
    '''
