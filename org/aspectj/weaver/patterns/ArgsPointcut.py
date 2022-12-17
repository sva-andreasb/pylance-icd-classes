def ():
    '''returns ArgsPointcut\n\n
    (final TypePatternList arguments)\n
    '''
def getArguments():
    '''returns TypePatternList\n\n
    getArguments()\n
    '''
def parameterizeWith():
    '''returns Pointcut\n\n
    parameterizeWith(final Map typeVariableMap, final World w)\n
    '''
def couldMatchKinds():
    '''returns int\n\n
    couldMatchKinds()\n
    '''
def fastMatch():
    '''returns FuzzyBoolean\n\n
    fastMatch(final FastMatchInfo type)\n
    '''
def getBindingAnnotationTypePatterns():
    '''returns List\n\n
    getBindingAnnotationTypePatterns()\n
    '''
def getBindingTypePatterns():
    '''returns List\n\n
    getBindingTypePatterns()\n
    '''
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream s)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def resolveBindings():
    '''returns None\n\n
    resolveBindings(final IScope scope, final Bindings bindings)\n
    '''
def postRead():
    '''returns None\n\n
    postRead(final ResolvedType enclosingType)\n
    '''
def concretize1():
    '''returns Pointcut\n\n
    concretize1(final ResolvedType inAspect, final ResolvedType declaringType, final IntMap bindings)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def accept():
    '''returns Object\n\n
    accept(final PatternNodeVisitor visitor, final Object data)\n
    '''
