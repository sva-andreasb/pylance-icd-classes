WILD = "byte  1"
EXACT = "byte  2"
BINDING = "byte  3"
ELLIPSIS_KEY = "byte  4"
ANY_KEY = "byte  5"
NOT = "byte  6"
OR = "byte  7"
AND = "byte  8"
NO_KEY = "byte  9"
ANY_WITH_ANNO = "byte  10"
HAS_MEMBER = "byte  11"
TYPE_CATEGORY = "byte  12"
def getAnnotationPattern():
    '''returns AnnotationTypePattern\n\n
    getAnnotationPattern()\n
    '''
def isVarArgs():
    '''returns boolean\n\n
    isVarArgs()\n
    '''
def isStarAnnotation():
    '''returns boolean\n\n
    isStarAnnotation()\n
    '''
def isArray():
    '''returns boolean\n\n
    isArray()\n
    '''
def setAnnotationTypePattern():
    '''returns None\n\n
    setAnnotationTypePattern(final AnnotationTypePattern annPatt)\n
    '''
def setTypeParameters():
    '''returns None\n\n
    setTypeParameters(final TypePatternList typeParams)\n
    '''
def getTypeParameters():
    '''returns TypePatternList\n\n
    getTypeParameters()\n
    '''
def setIsVarArgs():
    '''returns None\n\n
    setIsVarArgs(final boolean isVarArgs)\n
    '''
def matchesStatically():
    '''returns boolean\n\n
    matchesStatically(final ResolvedType type)\n
    '''
def resolveExactType():
    '''returns UnresolvedType\n\n
    resolveExactType(final IScope scope, final Bindings bindings)\n
    '''
def getExactType():
    '''returns UnresolvedType\n\n
    getExactType()\n
    '''
def resolveBindings():
    '''returns TypePattern\n\n
    resolveBindings(final IScope scope, final Bindings bindings, final boolean allowBinding, final boolean requireExactType)\n
    '''
def resolve():
    '''returns None\n\n
    resolve(final World world)\n
    '''
def postRead():
    '''returns None\n\n
    postRead(final ResolvedType enclosingType)\n
    '''
def isEllipsis():
    '''returns boolean\n\n
    isEllipsis()\n
    '''
def isStar():
    '''returns boolean\n\n
    isStar()\n
    '''
def remapAdviceFormals():
    '''returns TypePattern\n\n
    remapAdviceFormals(final IntMap bindings)\n
    '''
def isIncludeSubtypes():
    '''returns boolean\n\n
    isIncludeSubtypes()\n
    '''
def isBangVoid():
    '''returns boolean\n\n
    isBangVoid()\n
    '''
def isVoid():
    '''returns boolean\n\n
    isVoid()\n
    '''
def hasFailedResolution():
    '''returns boolean\n\n
    hasFailedResolution()\n
    '''
def ():
    '''returns MatchKind\n\n
    (final String name)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
