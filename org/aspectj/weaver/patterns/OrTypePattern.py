def ():
    '''returns OrTypePattern\n\n
    (final TypePattern left, final TypePattern right)\n
    '''
def getRight():
    '''returns TypePattern\n\n
    getRight()\n
    '''
def getLeft():
    '''returns TypePattern\n\n
    getLeft()\n
    '''
def matchesInstanceof():
    '''returns FuzzyBoolean\n\n
    matchesInstanceof(final ResolvedType type)\n
    '''
def matchesStatically():
    '''returns boolean\n\n
    matchesStatically(final ResolvedType type)\n
    '''
def setIsVarArgs():
    '''returns None\n\n
    setIsVarArgs(final boolean isVarArgs)\n
    '''
def setAnnotationTypePattern():
    '''returns None\n\n
    setAnnotationTypePattern(final AnnotationTypePattern annPatt)\n
    '''
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream s)\n
    '''
def resolveBindings():
    '''returns TypePattern\n\n
    resolveBindings(final IScope scope, final Bindings bindings, final boolean allowBinding, final boolean requireExactType)\n
    '''
def parameterizeWith():
    '''returns TypePattern\n\n
    parameterizeWith(final Map<String, UnresolvedType> typeVariableMap, final World w)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def isStarAnnotation():
    '''returns boolean\n\n
    isStarAnnotation()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def accept():
    '''returns Object\n\n
    accept(final PatternNodeVisitor visitor, final Object data)\n
    '''
def traverse():
    '''returns Object\n\n
    traverse(final PatternNodeVisitor visitor, final Object data)\n
    '''
