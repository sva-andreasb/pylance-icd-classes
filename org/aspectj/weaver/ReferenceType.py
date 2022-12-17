def ():
    '''returns ReferenceType\n\n
    (final String signature, final World world)\n
    (final String signature, final String signatureErasure, final World world)\n
    (final ResolvedType theGenericType, final ResolvedType[] theParameters, final World aWorld)\n
    (final UnresolvedType genericType, final World world)\n
    '''
def checkDuplicates():
    '''returns None\n\n
    checkDuplicates(final ReferenceType newRt)\n
    '''
def getSignatureForAttribute():
    '''returns String\n\n
    getSignatureForAttribute()\n
    '''
def isClass():
    '''returns boolean\n\n
    isClass()\n
    '''
def getCompilerVersion():
    '''returns int\n\n
    getCompilerVersion()\n
    '''
def isGenericType():
    '''returns boolean\n\n
    isGenericType()\n
    '''
def getGenericSignature():
    '''returns String\n\n
    getGenericSignature()\n
    '''
def getAnnotations():
    '''returns AnnotationAJ[]\n\n
    getAnnotations()\n
    '''
def addAnnotation():
    '''returns None\n\n
    addAnnotation(final AnnotationAJ annotationX)\n
    '''
def hasAnnotation():
    '''returns boolean\n\n
    hasAnnotation(final UnresolvedType ofType)\n
    '''
def getAnnotationTypes():
    '''returns ResolvedType[]\n\n
    getAnnotationTypes()\n
    '''
def getNameAsIdentifier():
    '''returns String\n\n
    getNameAsIdentifier()\n
    '''
def getAnnotationOfType():
    '''returns AnnotationAJ\n\n
    getAnnotationOfType(final UnresolvedType ofType)\n
    '''
def isAspect():
    '''returns boolean\n\n
    isAspect()\n
    '''
def isAnnotationStyleAspect():
    '''returns boolean\n\n
    isAnnotationStyleAspect()\n
    '''
def isEnum():
    '''returns boolean\n\n
    isEnum()\n
    '''
def isAnnotation():
    '''returns boolean\n\n
    isAnnotation()\n
    '''
def isAnonymous():
    '''returns boolean\n\n
    isAnonymous()\n
    '''
def isNested():
    '''returns boolean\n\n
    isNested()\n
    '''
def getOuterClass():
    '''returns ResolvedType\n\n
    getOuterClass()\n
    '''
def getRetentionPolicy():
    '''returns String\n\n
    getRetentionPolicy()\n
    '''
def isAnnotationWithRuntimeRetention():
    '''returns boolean\n\n
    isAnnotationWithRuntimeRetention()\n
    '''
def canAnnotationTargetType():
    '''returns boolean\n\n
    canAnnotationTargetType()\n
    '''
def getAnnotationTargetKinds():
    '''returns AnnotationTargetKind[]\n\n
    getAnnotationTargetKinds()\n
    '''
def isCoerceableFrom():
    '''returns boolean\n\n
    isCoerceableFrom(final ResolvedType o)\n
    '''
def isAssignableFrom():
    '''returns boolean\n\n
    isAssignableFrom(final ResolvedType other)\n
    isAssignableFrom(final ResolvedType other, final boolean allowMissing)\n
    '''
def getSourceContext():
    '''returns ISourceContext\n\n
    getSourceContext()\n
    '''
def getSourceLocation():
    '''returns ISourceLocation\n\n
    getSourceLocation()\n
    '''
def isExposedToWeaver():
    '''returns boolean\n\n
    isExposedToWeaver()\n
    '''
def getWeaverState():
    '''returns WeaverStateInfo\n\n
    getWeaverState()\n
    '''
def getDeclaredFields():
    '''returns ResolvedMember[]\n\n
    getDeclaredFields()\n
    '''
def getDeclaredInterfaces():
    '''returns ResolvedType[]\n\n
    getDeclaredInterfaces()\n
    '''
def getDeclaredMethods():
    '''returns ResolvedMember[]\n\n
    getDeclaredMethods()\n
    '''
def getDeclaredPointcuts():
    '''returns ResolvedMember[]\n\n
    getDeclaredPointcuts()\n
    '''
def getTypeVariables():
    '''returns TypeVariable[]\n\n
    getTypeVariables()\n
    '''
def getPerClause():
    '''returns PerClause\n\n
    getPerClause()\n
    '''
def getDeclares():
    '''returns Collection<Declare>\n\n
    getDeclares()\n
    '''
def getTypeMungers():
    '''returns Collection<ConcreteTypeMunger>\n\n
    getTypeMungers()\n
    '''
def getPrivilegedAccesses():
    '''returns Collection<ResolvedMember>\n\n
    getPrivilegedAccesses()\n
    '''
def getModifiers():
    '''returns int\n\n
    getModifiers()\n
    '''
def getSuperclass():
    '''returns ResolvedType\n\n
    getSuperclass()\n
    '''
def getDelegate():
    '''returns ReferenceTypeDelegate\n\n
    getDelegate()\n
    '''
def setDelegate():
    '''returns None\n\n
    setDelegate(final ReferenceTypeDelegate delegate)\n
    '''
def getEndPos():
    '''returns int\n\n
    getEndPos()\n
    '''
def getStartPos():
    '''returns int\n\n
    getStartPos()\n
    '''
def setEndPos():
    '''returns None\n\n
    setEndPos(final int endPos)\n
    '''
def setStartPos():
    '''returns None\n\n
    setStartPos(final int startPos)\n
    '''
def doesNotExposeShadowMungers():
    '''returns boolean\n\n
    doesNotExposeShadowMungers()\n
    '''
def getDeclaredGenericSignature():
    '''returns String\n\n
    getDeclaredGenericSignature()\n
    '''
def setGenericType():
    '''returns None\n\n
    setGenericType(final ReferenceType rt)\n
    '''
def demoteToSimpleType():
    '''returns None\n\n
    demoteToSimpleType()\n
    '''
def getGenericType():
    '''returns ReferenceType\n\n
    getGenericType()\n
    '''
def ensureConsistent():
    '''returns None\n\n
    ensureConsistent()\n
    '''
def addParent():
    '''returns None\n\n
    addParent(final ResolvedType newParent)\n
    '''
def findDerivativeType():
    '''returns ReferenceType\n\n
    findDerivativeType(final ResolvedType[] typeParameters)\n
    '''
def hasNewInterfaces():
    '''returns boolean\n\n
    hasNewInterfaces()\n
    '''
