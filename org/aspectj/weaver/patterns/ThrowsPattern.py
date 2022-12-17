def ():
    '''returns ThrowsPattern\n\n
    (final TypePatternList required, final TypePatternList forbidden)\n
    '''
def getRequired():
    '''returns TypePatternList\n\n
    getRequired()\n
    '''
def getForbidden():
    '''returns TypePatternList\n\n
    getForbidden()\n
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
    '''returns ThrowsPattern\n\n
    resolveBindings(final IScope scope, final Bindings bindings)\n
    '''
def parameterizeWith():
    '''returns ThrowsPattern\n\n
    parameterizeWith(final Map typeVariableMap, final World w)\n
    '''
def matches():
    '''returns boolean\n\n
    matches(final UnresolvedType[] tys, final World world)\n
    '''
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream s)\n
    '''
def accept():
    '''returns Object\n\n
    accept(final PatternNodeVisitor visitor, final Object data)\n
    '''
def traverse():
    '''returns Object\n\n
    traverse(final PatternNodeVisitor visitor, final Object data)\n
    '''
