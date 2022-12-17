def ():
    '''returns ReflectionBasedReferenceTypeDelegate\n\n
    (final Class forClass, final ClassLoader aClassLoader, final World inWorld, final ReferenceType resolvedType)\n
    ()\n
    '''
def initialize():
    '''returns None\n\n
    initialize(final ReferenceType aType, final Class aClass, final ClassLoader aClassLoader, final World aWorld)\n
    '''
def buildGenericType():
    '''returns ReferenceType\n\n
    buildGenericType()\n
    '''
def isAspect():
    '''returns boolean\n\n
    isAspect()\n
    '''
def isAnnotationStyleAspect():
    '''returns boolean\n\n
    isAnnotationStyleAspect()\n
    '''
def isInterface():
    '''returns boolean\n\n
    isInterface()\n
    '''
def isEnum():
    '''returns boolean\n\n
    isEnum()\n
    '''
def isAnnotationWithRuntimeRetention():
    '''returns boolean\n\n
    isAnnotationWithRuntimeRetention()\n
    '''
def isAnnotation():
    '''returns boolean\n\n
    isAnnotation()\n
    '''
def getRetentionPolicy():
    '''returns String\n\n
    getRetentionPolicy()\n
    '''
def canAnnotationTargetType():
    '''returns boolean\n\n
    canAnnotationTargetType()\n
    '''
def getAnnotationTargetKinds():
    '''returns AnnotationTargetKind[]\n\n
    getAnnotationTargetKinds()\n
    '''
def isClass():
    '''returns boolean\n\n
    isClass()\n
    '''
def isGeneric():
    '''returns boolean\n\n
    isGeneric()\n
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
def isExposedToWeaver():
    '''returns boolean\n\n
    isExposedToWeaver()\n
    '''
def hasAnnotation():
    '''returns boolean\n\n
    hasAnnotation(final UnresolvedType ofType)\n
    '''
def getAnnotations():
    '''returns AnnotationAJ[]\n\n
    getAnnotations()\n
    '''
def getAnnotationTypes():
    '''returns ResolvedType[]\n\n
    getAnnotationTypes()\n
    '''
def getDeclaredFields():
    '''returns ResolvedMember[]\n\n
    getDeclaredFields()\n
    '''
def getDeclaredInterfaces():
    '''returns ResolvedType[]\n\n
    getDeclaredInterfaces()\n
    '''
def isCacheable():
    '''returns boolean\n\n
    isCacheable()\n
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
    '''returns Collection\n\n
    getDeclares()\n
    '''
def getTypeMungers():
    '''returns Collection\n\n
    getTypeMungers()\n
    '''
def getPrivilegedAccesses():
    '''returns Collection\n\n
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
def getWeaverState():
    '''returns WeaverStateInfo\n\n
    getWeaverState()\n
    '''
def getResolvedTypeX():
    '''returns ReferenceType\n\n
    getResolvedTypeX()\n
    '''
def doesNotExposeShadowMungers():
    '''returns boolean\n\n
    doesNotExposeShadowMungers()\n
    '''
def getDeclaredGenericSignature():
    '''returns String\n\n
    getDeclaredGenericSignature()\n
    '''
def createResolvedMemberFor():
    '''returns ReflectionBasedResolvedMemberImpl\n\n
    createResolvedMemberFor(final Member aMember)\n
    '''
def getSourcefilename():
    '''returns String\n\n
    getSourcefilename()\n
    '''
def getSourceContext():
    '''returns ISourceContext\n\n
    getSourceContext()\n
    '''
def copySourceContext():
    '''returns boolean\n\n
    copySourceContext()\n
    '''
def getCompilerVersion():
    '''returns int\n\n
    getCompilerVersion()\n
    '''
def ensureConsistent():
    '''returns None\n\n
    ensureConsistent()\n
    '''
def isWeavable():
    '''returns boolean\n\n
    isWeavable()\n
    '''
def hasBeenWoven():
    '''returns boolean\n\n
    hasBeenWoven()\n
    '''
