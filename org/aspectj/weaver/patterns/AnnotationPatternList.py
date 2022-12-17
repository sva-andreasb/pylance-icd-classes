def ():
    '''returns AnnotationPatternList\n\n
    ()\n
    (final AnnotationTypePattern[] arguments)\n
    (final List l)\n
    '''
def parameterizeWith():
    '''returns AnnotationPatternList\n\n
    parameterizeWith(final Map typeVariableMap, final World w)\n
    '''
def resolve():
    '''returns None\n\n
    resolve(final World inWorld)\n
    '''
def matches():
    '''returns FuzzyBoolean\n\n
    matches(final ResolvedType[] someArgs)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def get():
    '''returns AnnotationTypePattern\n\n
    get(final int index)\n
    '''
def resolveBindings():
    '''returns AnnotationPatternList\n\n
    resolveBindings(final IScope scope, final Bindings bindings, final boolean allowBinding)\n
    '''
def resolveReferences():
    '''returns AnnotationPatternList\n\n
    resolveReferences(final IntMap bindings)\n
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
def traverse():
    '''returns Object\n\n
    traverse(final PatternNodeVisitor visitor, final Object data)\n
    '''
