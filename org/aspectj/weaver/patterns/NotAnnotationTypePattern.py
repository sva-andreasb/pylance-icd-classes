def ():
    '''returns NotAnnotationTypePattern\n\n
    (final AnnotationTypePattern pattern)\n
    '''
def matches():
    '''returns FuzzyBoolean\n\n
    matches(final AnnotatedElement annotated)\n
    matches(final AnnotatedElement annotated, final ResolvedType[] parameterAnnotations)\n
    '''
def resolve():
    '''returns None\n\n
    resolve(final World world)\n
    '''
def resolveBindings():
    '''returns AnnotationTypePattern\n\n
    resolveBindings(final IScope scope, final Bindings bindings, final boolean allowBinding)\n
    '''
def parameterizeWith():
    '''returns AnnotationTypePattern\n\n
    parameterizeWith(final Map typeVariableMap, final World w)\n
    '''
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream s)\n
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
def getNegatedPattern():
    '''returns AnnotationTypePattern\n\n
    getNegatedPattern()\n
    '''
def accept():
    '''returns Object\n\n
    accept(final PatternNodeVisitor visitor, final Object data)\n
    '''
def traverse():
    '''returns Object\n\n
    traverse(final PatternNodeVisitor visitor, final Object data)\n
    '''
def setForParameterAnnotationMatch():
    '''returns None\n\n
    setForParameterAnnotationMatch()\n
    '''
