def setJavaClass():
    '''returns None\n\n
    setJavaClass(final JavaClass newclass, final boolean artificial)\n
    '''
def isCacheable():
    '''returns boolean\n\n
    isCacheable()\n
    '''
def isInterface():
    '''returns boolean\n\n
    isInterface()\n
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
def getModifiers():
    '''returns int\n\n
    getModifiers()\n
    '''
def getSuperclass():
    '''returns ResolvedType\n\n
    getSuperclass()\n
    '''
def getWorld():
    '''returns World\n\n
    getWorld()\n
    '''
def getDeclaredInterfaces():
    '''returns ResolvedType[]\n\n
    getDeclaredInterfaces()\n
    '''
def getDeclaredMethods():
    '''returns ResolvedMember[]\n\n
    getDeclaredMethods()\n
    '''
def getDeclaredFields():
    '''returns ResolvedMember[]\n\n
    getDeclaredFields()\n
    '''
def getTypeVariables():
    '''returns TypeVariable[]\n\n
    getTypeVariables()\n
    '''
def getTypeMungers():
    '''returns Collection<ConcreteTypeMunger>\n\n
    getTypeMungers()\n
    '''
def getDeclares():
    '''returns Collection<Declare>\n\n
    getDeclares()\n
    '''
def getPrivilegedAccesses():
    '''returns Collection<ResolvedMember>\n\n
    getPrivilegedAccesses()\n
    '''
def getDeclaredPointcuts():
    '''returns ResolvedMember[]\n\n
    getDeclaredPointcuts()\n
    '''
def isAspect():
    '''returns boolean\n\n
    isAspect()\n
    '''
def isAnnotationStyleAspect():
    '''returns boolean\n\n
    isAnnotationStyleAspect()\n
    '''
def getPerClause():
    '''returns PerClause\n\n
    getPerClause()\n
    '''
def getJavaClass():
    '''returns JavaClass\n\n
    getJavaClass()\n
    '''
def isArtificial():
    '''returns boolean\n\n
    isArtificial()\n
    '''
def resetState():
    '''returns None\n\n
    resetState()\n
    '''
def finishedWith():
    '''returns None\n\n
    finishedWith()\n
    '''
def getWeaverState():
    '''returns WeaverStateInfo\n\n
    getWeaverState()\n
    '''
def printWackyStuff():
    '''returns None\n\n
    printWackyStuff(final PrintStream out)\n
    '''
def getLazyClassGen():
    '''returns LazyClassGen\n\n
    getLazyClassGen()\n
    '''
def isSynthetic():
    '''returns boolean\n\n
    isSynthetic()\n
    '''
def getAnnotationTypes():
    '''returns ResolvedType[]\n\n
    getAnnotationTypes()\n
    '''
def getAnnotations():
    '''returns AnnotationAJ[]\n\n
    getAnnotations()\n
    '''
def hasAnnotation():
    '''returns boolean\n\n
    hasAnnotation(final UnresolvedType ofType)\n
    '''
def isAnnotationWithRuntimeRetention():
    '''returns boolean\n\n
    isAnnotationWithRuntimeRetention()\n
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
def getDeclaredGenericSignature():
    '''returns String\n\n
    getDeclaredGenericSignature()\n
    '''
def getOuterClass():
    '''returns ResolvedType\n\n
    getOuterClass()\n
    '''
def isGeneric():
    '''returns boolean\n\n
    isGeneric()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def evictWeavingState():
    '''returns None\n\n
    evictWeavingState()\n
    '''
def weavingCompleted():
    '''returns None\n\n
    weavingCompleted()\n
    '''
def hasBeenWoven():
    '''returns boolean\n\n
    hasBeenWoven()\n
    '''
def copySourceContext():
    '''returns boolean\n\n
    copySourceContext()\n
    '''
def setExposedToWeaver():
    '''returns None\n\n
    setExposedToWeaver(final boolean b)\n
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
