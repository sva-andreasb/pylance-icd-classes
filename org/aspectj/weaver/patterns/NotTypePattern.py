def ():
    '''returns NotTypePattern\n\n
    (final TypePattern pattern)\n
    '''
def getNegatedPattern():
    '''returns TypePattern\n\n
    getNegatedPattern()\n
    '''
def matchesInstanceof():
    '''returns FuzzyBoolean\n\n
    matchesInstanceof(final ResolvedType type)\n
    '''
def matchesStatically():
    '''returns boolean\n\n
    matchesStatically(final ResolvedType type)\n
    '''
def setAnnotationTypePattern():
    '''returns None\n\n
    setAnnotationTypePattern(final AnnotationTypePattern annPatt)\n
    '''
def setIsVarArgs():
    '''returns None\n\n
    setIsVarArgs(final boolean isVarArgs)\n
    '''
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream s)\n
    '''
def resolveBindings():
    '''returns TypePattern\n\n
    resolveBindings(final IScope scope, final Bindings bindings, final boolean allowBinding, final boolean requireExactType)\n
    '''
def isBangVoid():
    '''returns boolean\n\n
    isBangVoid()\n
    '''
def parameterizeWith():
    '''returns TypePattern\n\n
    parameterizeWith(final Map typeVariableMap, final World w)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
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
