def ():
    '''returns MissingResolvedTypeWithKnownSignature\n\n
    (final String signature, final World world)\n
    (final String signature, final String signatureErasure, final World world)\n
    '''
def isMissing():
    '''returns boolean\n\n
    isMissing()\n
    '''
def getDeclaredFields():
    '''returns ResolvedMember[]\n\n
    getDeclaredFields()\n
    '''
def getDeclaredMethods():
    '''returns ResolvedMember[]\n\n
    getDeclaredMethods()\n
    '''
def getAnnotations():
    '''returns AnnotationAJ[]\n\n
    getAnnotations()\n
    '''
def getDeclaredInterfaces():
    '''returns ResolvedType[]\n\n
    getDeclaredInterfaces()\n
    '''
def getDeclaredPointcuts():
    '''returns ResolvedMember[]\n\n
    getDeclaredPointcuts()\n
    '''
def getSuperclass():
    '''returns ResolvedType\n\n
    getSuperclass()\n
    '''
def getModifiers():
    '''returns int\n\n
    getModifiers()\n
    '''
def getSourceContext():
    '''returns ISourceContext\n\n
    getSourceContext()\n
    '''
def makeSourceLocation():
    '''returns ISourceLocation\n\n
    makeSourceLocation(final IHasPosition position)\n
    makeSourceLocation(final int line, final int offset)\n
    '''
def getOffset():
    '''returns int\n\n
    getOffset()\n
    '''
def tidy():
    '''returns None\n\n
    tidy()\n
    '''
def isAssignableFrom():
    '''returns boolean\n\n
    isAssignableFrom(final ResolvedType other)\n
    isAssignableFrom(final ResolvedType other, final boolean allowMissing)\n
    '''
def isCoerceableFrom():
    '''returns boolean\n\n
    isCoerceableFrom(final ResolvedType other)\n
    '''
def hasAnnotation():
    '''returns boolean\n\n
    hasAnnotation(final UnresolvedType ofType)\n
    '''
def getInterTypeMungers():
    '''returns List\n\n
    getInterTypeMungers()\n
    '''
def getInterTypeMungersIncludingSupers():
    '''returns List\n\n
    getInterTypeMungersIncludingSupers()\n
    '''
def getInterTypeParentMungers():
    '''returns List\n\n
    getInterTypeParentMungers()\n
    '''
def getInterTypeParentMungersIncludingSupers():
    '''returns List\n\n
    getInterTypeParentMungersIncludingSupers()\n
    '''
def raiseWarningOnJoinPointSignature():
    '''returns None\n\n
    raiseWarningOnJoinPointSignature(final String signature)\n
    '''
def raiseWarningOnMissingInterfaceWhilstFindingMethods():
    '''returns None\n\n
    raiseWarningOnMissingInterfaceWhilstFindingMethods()\n
    '''
