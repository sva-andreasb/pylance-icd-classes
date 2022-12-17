def ():
    '''returns ExactTypePattern\n\n
    (final UnresolvedType type, final boolean includeSubtypes, final boolean isVarArgs)\n
    '''
def isArray():
    '''returns boolean\n\n
    isArray()\n
    '''
def getType():
    '''returns UnresolvedType\n\n
    getType()\n
    '''
def getResolvedExactType():
    '''returns ResolvedType\n\n
    getResolvedExactType(final World world)\n
    '''
def isVoid():
    '''returns boolean\n\n
    isVoid()\n
    '''
def matchesInstanceof():
    '''returns FuzzyBoolean\n\n
    matchesInstanceof(final ResolvedType matchType)\n
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
    write(final CompressingDataOutputStream out)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def resolveBindings():
    '''returns TypePattern\n\n
    resolveBindings(final IScope scope, final Bindings bindings, final boolean allowBinding, final boolean requireExactType)\n
    '''
def parameterizeWith():
    '''returns TypePattern\n\n
    parameterizeWith(final Map<String, UnresolvedType> typeVariableMap, final World w)\n
    '''
def accept():
    '''returns Object\n\n
    accept(final PatternNodeVisitor visitor, final Object data)\n
    '''
