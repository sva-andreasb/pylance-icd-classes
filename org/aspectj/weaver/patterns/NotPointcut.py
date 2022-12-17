def ():
    '''returns NotPointcut\n\n
    (final Pointcut negated)\n
    (final Pointcut pointcut, final int startPos)\n
    '''
def couldMatchKinds():
    '''returns int\n\n
    couldMatchKinds()\n
    '''
def getNegatedPointcut():
    '''returns Pointcut\n\n
    getNegatedPointcut()\n
    '''
def fastMatch():
    '''returns FuzzyBoolean\n\n
    fastMatch(final FastMatchInfo type)\n
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
def resolveBindings():
    '''returns None\n\n
    resolveBindings(final IScope scope, final Bindings bindings)\n
    '''
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream s)\n
    '''
def concretize1():
    '''returns Pointcut\n\n
    concretize1(final ResolvedType inAspect, final ResolvedType declaringType, final IntMap bindings)\n
    '''
def parameterizeWith():
    '''returns Pointcut\n\n
    parameterizeWith(final Map typeVariableMap, final World w)\n
    '''
def accept():
    '''returns Object\n\n
    accept(final PatternNodeVisitor visitor, final Object data)\n
    '''
def traverse():
    '''returns Object\n\n
    traverse(final PatternNodeVisitor visitor, final Object data)\n
    '''
