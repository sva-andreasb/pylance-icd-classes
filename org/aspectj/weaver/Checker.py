def ():
    '''returns Checker\n\n
    (final DeclareErrorOrWarning deow)\n
    '''
def isError():
    '''returns boolean\n\n
    isError()\n
    '''
def getMessage():
    '''returns String\n\n
    getMessage(final Shadow shadow)\n
    '''
def specializeOn():
    '''returns None\n\n
    specializeOn(final Shadow shadow)\n
    '''
def implementOn():
    '''returns boolean\n\n
    implementOn(final Shadow shadow)\n
    '''
def match():
    '''returns boolean\n\n
    match(final Shadow shadow, final World world)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Object other)\n
    '''
def mustCheckExceptions():
    '''returns boolean\n\n
    mustCheckExceptions()\n
    '''
def getThrownExceptions():
    '''returns Collection<ResolvedType>\n\n
    getThrownExceptions()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def parameterizeWith():
    '''returns ShadowMunger\n\n
    parameterizeWith(final ResolvedType declaringType, final Map<String, UnresolvedType> typeVariableMap)\n
    '''
def concretize():
    '''returns ShadowMunger\n\n
    concretize(final ResolvedType theAspect, final World world, final PerClause clause)\n
    '''
def getConcreteAspect():
    '''returns ResolvedType\n\n
    getConcreteAspect()\n
    '''
