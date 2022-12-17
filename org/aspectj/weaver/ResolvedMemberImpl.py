def ():
    '''returns ResolvedMemberImpl\n\n
    (final MemberKind kind, final UnresolvedType declaringType, final int modifiers, final UnresolvedType returnType, final String name, final UnresolvedType[] parameterTypes)\n
    (final MemberKind kind, final UnresolvedType declaringType, final int modifiers, final UnresolvedType returnType, final String name, final UnresolvedType[] parameterTypes, final UnresolvedType[] checkedExceptions)\n
    (final MemberKind kind, final UnresolvedType declaringType, final int modifiers, final UnresolvedType returnType, final String name, final UnresolvedType[] parameterTypes, final UnresolvedType[] checkedExceptions, final ResolvedMember backingGenericMember)\n
    (final MemberKind kind, final UnresolvedType declaringType, final int modifiers, final String name, final String signature)\n
    '''
def getExceptions():
    '''returns UnresolvedType[]\n\n
    getExceptions()\n
    '''
def getAssociatedShadowMunger():
    '''returns ShadowMunger\n\n
    getAssociatedShadowMunger()\n
    '''
def isAjSynthetic():
    '''returns boolean\n\n
    isAjSynthetic()\n
    '''
def hasAnnotations():
    '''returns boolean\n\n
    hasAnnotations()\n
    '''
def hasAnnotation():
    '''returns boolean\n\n
    hasAnnotation(final UnresolvedType ofType)\n
    '''
def getAnnotationTypes():
    '''returns ResolvedType[]\n\n
    getAnnotationTypes()\n
    '''
def getAnnotationDefaultValue():
    '''returns String\n\n
    getAnnotationDefaultValue()\n
    '''
def getAnnotations():
    '''returns AnnotationAJ[]\n\n
    getAnnotations()\n
    '''
def getAnnotationOfType():
    '''returns AnnotationAJ\n\n
    getAnnotationOfType(final UnresolvedType ofType)\n
    '''
def setAnnotations():
    '''returns None\n\n
    setAnnotations(final AnnotationAJ[] annotations)\n
    '''
def setAnnotationTypes():
    '''returns None\n\n
    setAnnotationTypes(final ResolvedType[] annotationTypes)\n
    '''
def getParameterAnnotationTypes():
    '''returns ResolvedType[][]\n\n
    getParameterAnnotationTypes()\n
    '''
def getParameterAnnotations():
    '''returns AnnotationAJ[][]\n\n
    getParameterAnnotations()\n
    '''
def addAnnotation():
    '''returns None\n\n
    addAnnotation(final AnnotationAJ annotation)\n
    '''
def isBridgeMethod():
    '''returns boolean\n\n
    isBridgeMethod()\n
    '''
def isVarargsMethod():
    '''returns boolean\n\n
    isVarargsMethod()\n
    '''
def setVarargsMethod():
    '''returns None\n\n
    setVarargsMethod()\n
    '''
def isSynthetic():
    '''returns boolean\n\n
    isSynthetic()\n
    '''
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream s)\n
    '''
def getSignatureForAttribute():
    '''returns String\n\n
    getSignatureForAttribute()\n
    '''
def getGenericSignature():
    '''returns String\n\n
    getGenericSignature()\n
    '''
def resolve():
    '''returns ResolvedMember\n\n
    resolve(final World world)\n
    '''
def getSourceContext():
    '''returns ISourceContext\n\n
    getSourceContext(final World world)\n
    getSourceContext()\n
    '''
def getParameterNames():
    '''returns String[]\n\n
    getParameterNames()\n
    '''
def getSourceLocation():
    '''returns ISourceLocation\n\n
    getSourceLocation()\n
    '''
def getEnd():
    '''returns int\n\n
    getEnd()\n
    '''
def getStart():
    '''returns int\n\n
    getStart()\n
    '''
def setPosition():
    '''returns None\n\n
    setPosition(final int sourceStart, final int sourceEnd)\n
    '''
def setDeclaringType():
    '''returns None\n\n
    setDeclaringType(final ReferenceType rt)\n
    '''
def setSourceContext():
    '''returns None\n\n
    setSourceContext(final ISourceContext sourceContext)\n
    '''
def isAbstract():
    '''returns boolean\n\n
    isAbstract()\n
    '''
def isPublic():
    '''returns boolean\n\n
    isPublic()\n
    '''
def isDefault():
    '''returns boolean\n\n
    isDefault()\n
    '''
def isVisible():
    '''returns boolean\n\n
    isVisible(final ResolvedType fromType)\n
    '''
def setCheckedExceptions():
    '''returns None\n\n
    setCheckedExceptions(final UnresolvedType[] checkedExceptions)\n
    '''
def setAnnotatedElsewhere():
    '''returns None\n\n
    setAnnotatedElsewhere(final boolean b)\n
    '''
def isAnnotatedElsewhere():
    '''returns boolean\n\n
    isAnnotatedElsewhere()\n
    '''
def getGenericReturnType():
    '''returns UnresolvedType\n\n
    getGenericReturnType()\n
    '''
def getGenericParameterTypes():
    '''returns UnresolvedType[]\n\n
    getGenericParameterTypes()\n
    '''
def parameterizedWith():
    '''returns ResolvedMember\n\n
    parameterizedWith(final UnresolvedType[] typeParameters, final ResolvedType newDeclaringType, final boolean isParameterized)\n
    parameterizedWith(final UnresolvedType[] typeParameters, final ResolvedType newDeclaringType, final boolean isParameterized, final List<String> aliases)\n
    parameterizedWith(final Map<String, UnresolvedType> m, final World w)\n
    '''
def setTypeVariables():
    '''returns None\n\n
    setTypeVariables(final TypeVariable[] tvars)\n
    '''
def getTypeVariables():
    '''returns TypeVariable[]\n\n
    getTypeVariables()\n
    '''
def hasBackingGenericMember():
    '''returns boolean\n\n
    hasBackingGenericMember()\n
    '''
def getBackingGenericMember():
    '''returns ResolvedMember\n\n
    getBackingGenericMember()\n
    '''
def resetName():
    '''returns None\n\n
    resetName(final String newName)\n
    '''
def resetKind():
    '''returns None\n\n
    resetKind(final MemberKind newKind)\n
    '''
def resetModifiers():
    '''returns None\n\n
    resetModifiers(final int newModifiers)\n
    '''
def resetReturnTypeToObjectArray():
    '''returns None\n\n
    resetReturnTypeToObjectArray()\n
    '''
def matches():
    '''returns boolean\n\n
    matches(final ResolvedMember aCandidateMatch, final boolean ignoreGenerics)\n
    '''
def getParameterSignatureErased():
    '''returns String\n\n
    getParameterSignatureErased()\n
    '''
def getSignatureErased():
    '''returns String\n\n
    getSignatureErased()\n
    '''
def toDebugString():
    '''returns String\n\n
    toDebugString()\n
    '''
def toGenericString():
    '''returns String\n\n
    toGenericString()\n
    '''
def isCompatibleWith():
    '''returns boolean\n\n
    isCompatibleWith(final Member am)\n
    '''
def getTypeVariableNamed():
    '''returns TypeVariable\n\n
    getTypeVariableNamed(final String name)\n
    '''
def evictWeavingState():
    '''returns None\n\n
    evictWeavingState()\n
    '''
def isEquivalentTo():
    '''returns boolean\n\n
    isEquivalentTo(final Object other)\n
    '''
def isDefaultConstructor():
    '''returns boolean\n\n
    isDefaultConstructor()\n
    '''
