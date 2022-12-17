def ():
    '''returns DeclareAnnotation\n\n
    (final Kind kind, final TypePattern typePattern)\n
    (final Kind kind, final ISignaturePattern sigPattern)\n
    '''
def getAnnotationString():
    '''returns String\n\n
    getAnnotationString()\n
    '''
def isExactPattern():
    '''returns boolean\n\n
    isExactPattern()\n
    '''
def getAnnotationMethod():
    '''returns String\n\n
    getAnnotationMethod()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def accept():
    '''returns Object\n\n
    accept(final PatternNodeVisitor visitor, final Object data)\n
    '''
def resolve():
    '''returns None\n\n
    resolve(final IScope scope)\n
    '''
def parameterizeWith():
    '''returns Declare\n\n
    parameterizeWith(final Map<String, UnresolvedType> typeVariableBindingMap, final World w)\n
    '''
def isAdviceLike():
    '''returns boolean\n\n
    isAdviceLike()\n
    '''
def setAnnotationString():
    '''returns None\n\n
    setAnnotationString(final String annotationString)\n
    '''
def setAnnotationLocation():
    '''returns None\n\n
    setAnnotationLocation(final int start, final int end)\n
    '''
def getAnnotationSourceStart():
    '''returns int\n\n
    getAnnotationSourceStart()\n
    '''
def getAnnotationSourceEnd():
    '''returns int\n\n
    getAnnotationSourceEnd()\n
    '''
def setAnnotationMethod():
    '''returns None\n\n
    setAnnotationMethod(final String methodName)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    hashCode()\n
    '''
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream s)\n
    '''
def matches():
    '''returns boolean\n\n
    matches(final ResolvedMember resolvedmember, final World world)\n
    matches(final ResolvedType type)\n
    '''
def setAspect():
    '''returns None\n\n
    setAspect(final ResolvedType typeX)\n
    '''
def getAspect():
    '''returns UnresolvedType\n\n
    getAspect()\n
    '''
def copyAnnotationTo():
    '''returns None\n\n
    copyAnnotationTo(final ResolvedType onType)\n
    '''
def getAnnotation():
    '''returns AnnotationAJ\n\n
    getAnnotation()\n
    '''
def getTypePattern():
    '''returns TypePattern\n\n
    getTypePattern()\n
    '''
def getSignaturePattern():
    '''returns ISignaturePattern\n\n
    getSignaturePattern()\n
    '''
def isStarredAnnotationPattern():
    '''returns boolean\n\n
    isStarredAnnotationPattern()\n
    '''
def getKind():
    '''returns Kind\n\n
    getKind()\n
    '''
def isDeclareAtConstuctor():
    '''returns boolean\n\n
    isDeclareAtConstuctor()\n
    '''
def isDeclareAtMethod():
    '''returns boolean\n\n
    isDeclareAtMethod()\n
    '''
def isDeclareAtType():
    '''returns boolean\n\n
    isDeclareAtType()\n
    '''
def isDeclareAtField():
    '''returns boolean\n\n
    isDeclareAtField()\n
    '''
def getAnnotationType():
    '''returns ResolvedType\n\n
    getAnnotationType()\n
    '''
def isAnnotationAllowedOnField():
    '''returns boolean\n\n
    isAnnotationAllowedOnField()\n
    '''
def getPatternAsString():
    '''returns String\n\n
    getPatternAsString()\n
    '''
def couldEverMatch():
    '''returns boolean\n\n
    couldEverMatch(final ResolvedType type)\n
    '''
def getNameSuffix():
    '''returns String\n\n
    getNameSuffix()\n
    '''
def setRemover():
    '''returns None\n\n
    setRemover(final boolean b)\n
    '''
def isRemover():
    '''returns boolean\n\n
    isRemover()\n
    '''
