def ():
    '''returns JoinPointSignature\n\n
    (final ResolvedMember backing, final ResolvedType aType)\n
    '''
def getDeclaringType():
    '''returns UnresolvedType\n\n
    getDeclaringType()\n
    '''
def getModifiers():
    '''returns int\n\n
    getModifiers(final World world)\n
    getModifiers()\n
    '''
def getExceptions():
    '''returns UnresolvedType[]\n\n
    getExceptions(final World world)\n
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
def hasAnnotation():
    '''returns boolean\n\n
    hasAnnotation(final UnresolvedType ofType)\n
    '''
def getAnnotationTypes():
    '''returns ResolvedType[]\n\n
    getAnnotationTypes()\n
    '''
def getAnnotationOfType():
    '''returns AnnotationAJ\n\n
    getAnnotationOfType(final UnresolvedType ofType)\n
    '''
def setAnnotationTypes():
    '''returns None\n\n
    setAnnotationTypes(final ResolvedType[] annotationtypes)\n
    '''
def setAnnotations():
    '''returns None\n\n
    setAnnotations(final AnnotationAJ[] annotations)\n
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
def isSynthetic():
    '''returns boolean\n\n
    isSynthetic()\n
    '''
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream s)\n
    '''
def getSourceContext():
    '''returns ISourceContext\n\n
    getSourceContext(final World world)\n
    getSourceContext()\n
    '''
def getParameterNames():
    '''returns String[]\n\n
    getParameterNames()\n
    getParameterNames(final World world)\n
    '''
def setParameterNames():
    '''returns None\n\n
    setParameterNames(final String[] names)\n
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
    parameterizedWith(final Map m, final World w)\n
    '''
def setTypeVariables():
    '''returns None\n\n
    setTypeVariables(final TypeVariable[] types)\n
    '''
def getTypeVariables():
    '''returns TypeVariable[]\n\n
    getTypeVariables()\n
    '''
def getTypeVariableNamed():
    '''returns TypeVariable\n\n
    getTypeVariableNamed(final String name)\n
    '''
def matches():
    '''returns boolean\n\n
    matches(final ResolvedMember aCandidateMatch, final boolean ignoreGenerics)\n
    '''
def resolve():
    '''returns ResolvedMember\n\n
    resolve(final World world)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Member other)\n
    '''
def getKind():
    '''returns MemberKind\n\n
    getKind()\n
    '''
def getReturnType():
    '''returns UnresolvedType\n\n
    getReturnType()\n
    '''
def getType():
    '''returns UnresolvedType\n\n
    getType()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getParameterTypes():
    '''returns UnresolvedType[]\n\n
    getParameterTypes()\n
    '''
def getParameterAnnotations():
    '''returns AnnotationAJ[][]\n\n
    getParameterAnnotations()\n
    '''
def getParameterAnnotationTypes():
    '''returns ResolvedType[][]\n\n
    getParameterAnnotationTypes()\n
    '''
def getSignature():
    '''returns String\n\n
    getSignature()\n
    '''
def getArity():
    '''returns int\n\n
    getArity()\n
    '''
def getParameterSignature():
    '''returns String\n\n
    getParameterSignature()\n
    '''
def isCompatibleWith():
    '''returns boolean\n\n
    isCompatibleWith(final Member am)\n
    '''
def canBeParameterized():
    '''returns boolean\n\n
    canBeParameterized()\n
    '''
def getAnnotations():
    '''returns AnnotationAJ[]\n\n
    getAnnotations()\n
    '''
def getDeclaringTypes():
    '''returns Collection<ResolvedType>\n\n
    getDeclaringTypes(final World world)\n
    '''
def getJoinPointSignatures():
    '''returns JoinPointSignatureIterator\n\n
    getJoinPointSignatures(final World world)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def toGenericString():
    '''returns String\n\n
    toGenericString()\n
    '''
def toDebugString():
    '''returns String\n\n
    toDebugString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def hasBackingGenericMember():
    '''returns boolean\n\n
    hasBackingGenericMember()\n
    '''
def getBackingGenericMember():
    '''returns ResolvedMember\n\n
    getBackingGenericMember()\n
    '''
def evictWeavingState():
    '''returns None\n\n
    evictWeavingState()\n
    '''
def getAnnotationDefaultValue():
    '''returns String\n\n
    getAnnotationDefaultValue()\n
    '''
def getParameterSignatureErased():
    '''returns String\n\n
    getParameterSignatureErased()\n
    '''
def getSignatureErased():
    '''returns String\n\n
    getSignatureErased()\n
    '''
def isDefaultConstructor():
    '''returns boolean\n\n
    isDefaultConstructor()\n
    '''
def equalsApartFromDeclaringType():
    '''returns boolean\n\n
    equalsApartFromDeclaringType(final Object other)\n
    '''
