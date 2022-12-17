def ():
    '''returns VerifyBoundsForTypePattern\n\n
    (final List<NamePattern> names, final boolean includeSubtypes, final int dim)\n
    (final List<NamePattern> names, final boolean includeSubtypes, final int dim, final int endPos)\n
    (final List<NamePattern> names, final boolean includeSubtypes, final int dim, final int endPos, final boolean isVarArg)\n
    (final List<NamePattern> names, final boolean includeSubtypes, final int dim, final int endPos, final boolean isVarArg, final TypePatternList typeParams, final TypePattern upperBound, final TypePattern[] additionalInterfaceBounds, final TypePattern lowerBound)\n
    (final List<NamePattern> names, final boolean includeSubtypes, final int dim, final int endPos, final boolean isVarArg, final TypePatternList typeParams)\n
    (final IScope scope, final ResolvedType genericType, final boolean requireExactType, final TypePatternList typeParameters, final ISourceLocation sLoc)\n
    '''
def getNamePatterns():
    '''returns NamePattern[]\n\n
    getNamePatterns()\n
    '''
def getUpperBound():
    '''returns TypePattern\n\n
    getUpperBound()\n
    '''
def getLowerBound():
    '''returns TypePattern\n\n
    getLowerBound()\n
    '''
def getAdditionalIntefaceBounds():
    '''returns TypePattern[]\n\n
    getAdditionalIntefaceBounds()\n
    '''
def setIsVarArgs():
    '''returns None\n\n
    setIsVarArgs(final boolean isVarArgs)\n
    '''
def getDimensions():
    '''returns int\n\n
    getDimensions()\n
    '''
def isArray():
    '''returns boolean\n\n
    isArray()\n
    '''
def matchesInstanceof():
    '''returns FuzzyBoolean\n\n
    matchesInstanceof(final ResolvedType type)\n
    '''
def extractName():
    '''returns NamePattern\n\n
    extractName()\n
    '''
def maybeExtractName():
    '''returns boolean\n\n
    maybeExtractName(final String string)\n
    '''
def maybeGetSimpleName():
    '''returns String\n\n
    maybeGetSimpleName()\n
    '''
def maybeGetCleanName():
    '''returns String\n\n
    maybeGetCleanName()\n
    '''
def parameterizeWith():
    '''returns TypePattern\n\n
    parameterizeWith(final Map<String, UnresolvedType> typeVariableMap, final World w)\n
    '''
def resolveBindings():
    '''returns TypePattern\n\n
    resolveBindings(final IScope scope, final Bindings bindings, final boolean allowBinding, final boolean requireExactType)\n
    '''
def isStar():
    '''returns boolean\n\n
    isStar()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream s)\n
    '''
def accept():
    '''returns Object\n\n
    accept(final PatternNodeVisitor visitor, final Object data)\n
    '''
def hasFailedResolution():
    '''returns boolean\n\n
    hasFailedResolution()\n
    '''
def verify():
    '''returns None\n\n
    verify()\n
    '''
