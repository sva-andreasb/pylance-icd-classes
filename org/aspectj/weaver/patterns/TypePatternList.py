def ():
    '''returns TypePatternList\n\n
    ()\n
    (final TypePattern[] arguments)\n
    (final List l)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def get():
    '''returns TypePattern\n\n
    get(final int index)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def canMatchSignatureWithNParameters():
    '''returns boolean\n\n
    canMatchSignatureWithNParameters(final int numParams)\n
    '''
def matches():
    '''returns FuzzyBoolean\n\n
    matches(final ResolvedType[] types, final TypePattern.MatchKind kind)\n
    matches(final ResolvedType[] types, final TypePattern.MatchKind kind, final ResolvedType[][] parameterAnnotations)\n
    matches(final ResolvableTypeList types, final TypePattern.MatchKind kind, final ResolvedType[][] parameterAnnotations)\n
    '''
def parameterizeWith():
    '''returns TypePatternList\n\n
    parameterizeWith(final Map typeVariableMap, final World w)\n
    '''
def resolveBindings():
    '''returns TypePatternList\n\n
    resolveBindings(final IScope scope, final Bindings bindings, final boolean allowBinding, final boolean requireExactType)\n
    '''
def resolveReferences():
    '''returns TypePatternList\n\n
    resolveReferences(final IntMap bindings)\n
    '''
def postRead():
    '''returns None\n\n
    postRead(final ResolvedType enclosingType)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def getEnd():
    '''returns int\n\n
    getEnd()\n
    '''
def getSourceContext():
    '''returns ISourceContext\n\n
    getSourceContext()\n
    '''
def getSourceLocation():
    '''returns ISourceLocation\n\n
    getSourceLocation()\n
    '''
def getStart():
    '''returns int\n\n
    getStart()\n
    '''
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream s)\n
    '''
def getTypePatterns():
    '''returns TypePattern[]\n\n
    getTypePatterns()\n
    '''
def getExactTypes():
    '''returns List<UnresolvedType>\n\n
    getExactTypes()\n
    '''
def accept():
    '''returns Object\n\n
    accept(final PatternNodeVisitor visitor, final Object data)\n
    '''
def traverse():
    '''returns Object\n\n
    traverse(final PatternNodeVisitor visitor, final Object data)\n
    '''
def areAllExactWithNoSubtypesAllowed():
    '''returns boolean\n\n
    areAllExactWithNoSubtypesAllowed()\n
    '''
def maybeGetCleanNames():
    '''returns String[]\n\n
    maybeGetCleanNames()\n
    '''
