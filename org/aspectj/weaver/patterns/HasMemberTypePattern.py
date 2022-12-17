def ():
    '''returns HasMemberTypePattern\n\n
    (final SignaturePattern aSignaturePattern)\n
    '''
def getSignaturePattern():
    '''returns ISignaturePattern\n\n
    getSignaturePattern()\n
    '''
def matchesInstanceof():
    '''returns FuzzyBoolean\n\n
    matchesInstanceof(final ResolvedType type)\n
    '''
def parameterizeWith():
    '''returns TypePattern\n\n
    parameterizeWith(final Map typeVariableMap, final World w)\n
    '''
def resolveBindings():
    '''returns TypePattern\n\n
    resolveBindings(final IScope scope, final Bindings bindings, final boolean allowBinding, final boolean requireExactType)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream s)\n
    '''
def accept():
    '''returns Object\n\n
    accept(final PatternNodeVisitor visitor, final Object data)\n
    '''
