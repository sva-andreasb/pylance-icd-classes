def ():
    '''returns ExactAnnotationFieldTypePattern\n\n
    (final ExactAnnotationTypePattern p, final String formalName)\n
    (final UnresolvedType annotationType, final String formalName)\n
    '''
def resolveBindings():
    '''returns AnnotationTypePattern\n\n
    resolveBindings(final IScope scope, final Bindings bindings, final boolean allowBinding)\n
    '''
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream s)\n
    '''
def accept():
    '''returns Object\n\n
    accept(final PatternNodeVisitor visitor, final Object data)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def fastMatches():
    '''returns FuzzyBoolean\n\n
    fastMatches(final AnnotatedElement annotated)\n
    '''
def getAnnotationType():
    '''returns UnresolvedType\n\n
    getAnnotationType()\n
    '''
def getAnnotationValues():
    '''returns Map\n\n
    getAnnotationValues()\n
    '''
def getResolvedAnnotationType():
    '''returns ResolvedType\n\n
    getResolvedAnnotationType()\n
    '''
def matches():
    '''returns FuzzyBoolean\n\n
    matches(final AnnotatedElement annotated, final ResolvedType[] parameterAnnotations)\n
    matches(final AnnotatedElement annotated)\n
    '''
def matchesRuntimeType():
    '''returns FuzzyBoolean\n\n
    matchesRuntimeType(final AnnotatedElement annotated)\n
    '''
def parameterizeWith():
    '''returns AnnotationTypePattern\n\n
    parameterizeWith(final Map typeVariableMap, final World w)\n
    '''
def resolve():
    '''returns None\n\n
    resolve(final World world)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
