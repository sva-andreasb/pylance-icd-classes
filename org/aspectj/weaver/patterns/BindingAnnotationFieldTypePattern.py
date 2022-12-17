def ():
    '''returns BindingAnnotationFieldTypePattern\n\n
    (final UnresolvedType formalType, final int formalIndex, final UnresolvedType theAnnotationType)\n
    '''
def resolveBinding():
    '''returns None\n\n
    resolveBinding(final World world)\n
    '''
def parameterizeWith():
    '''returns AnnotationTypePattern\n\n
    parameterizeWith(final Map typeVariableMap, final World w)\n
    '''
def getFormalIndex():
    '''returns int\n\n
    getFormalIndex()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def remapAdviceFormals():
    '''returns AnnotationTypePattern\n\n
    remapAdviceFormals(final IntMap bindings)\n
    '''
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream s)\n
    '''
def matches():
    '''returns FuzzyBoolean\n\n
    matches(final AnnotatedElement annotated, final ResolvedType[] parameterAnnotations)\n
    '''
def getFormalType():
    '''returns UnresolvedType\n\n
    getFormalType()\n
    '''
