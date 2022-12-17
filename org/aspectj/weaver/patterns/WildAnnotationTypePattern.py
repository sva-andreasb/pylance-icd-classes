def ():
    '''returns WildAnnotationTypePattern\n\n
    (final TypePattern typePattern)\n
    (final TypePattern typePattern, final Map<String, String> annotationValues)\n
    '''
def getTypePattern():
    '''returns TypePattern\n\n
    getTypePattern()\n
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
def accept():
    '''returns Object\n\n
    accept(final PatternNodeVisitor visitor, final Object data)\n
    '''
