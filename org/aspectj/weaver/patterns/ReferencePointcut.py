def ():
    '''returns ReferencePointcut\n\n
    (final TypePattern onTypeSymbolic, final String name, final TypePatternList arguments)\n
    (final UnresolvedType onType, final String name, final TypePatternList arguments)\n
    '''
def couldMatchKinds():
    '''returns int\n\n
    couldMatchKinds()\n
    '''
def fastMatch():
    '''returns FuzzyBoolean\n\n
    fastMatch(final FastMatchInfo type)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream s)\n
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
    concretize1(ResolvedType searchStart, ResolvedType declaringType, final IntMap bindings)\n
    '''
def parameterizeWith():
    '''returns Pointcut\n\n
    parameterizeWith(final Map<String, UnresolvedType> typeVariableMap, final World w)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def accept():
    '''returns Object\n\n
    accept(final PatternNodeVisitor visitor, final Object data)\n
    '''
