def ():
    '''returns NotSignaturePattern\n\n
    (final ISignaturePattern negatedSp)\n
    '''
def couldEverMatch():
    '''returns boolean\n\n
    couldEverMatch(final ResolvedType type)\n
    '''
def getExactDeclaringTypes():
    '''returns List<ExactTypePattern>\n\n
    getExactDeclaringTypes()\n
    '''
def isMatchOnAnyName():
    '''returns boolean\n\n
    isMatchOnAnyName()\n
    '''
def isStarAnnotation():
    '''returns boolean\n\n
    isStarAnnotation()\n
    '''
def matches():
    '''returns boolean\n\n
    matches(final Member member, final World world, final boolean b)\n
    '''
def parameterizeWith():
    '''returns ISignaturePattern\n\n
    parameterizeWith(final Map<String, UnresolvedType> typeVariableBindingMap, final World world)\n
    '''
def resolveBindings():
    '''returns ISignaturePattern\n\n
    resolveBindings(final IScope scope, final Bindings bindings)\n
    '''
def getNegated():
    '''returns ISignaturePattern\n\n
    getNegated()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
