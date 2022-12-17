def ():
    '''returns KindedPointcut\n\n
    (final Shadow.Kind kind, final SignaturePattern signature)\n
    (final Shadow.Kind kind, final SignaturePattern signature, final ShadowMunger munger)\n
    '''
def getSignature():
    '''returns SignaturePattern\n\n
    getSignature()\n
    '''
def couldMatchKinds():
    '''returns int\n\n
    couldMatchKinds()\n
    '''
def couldEverMatchSameJoinPointsAs():
    '''returns boolean\n\n
    couldEverMatchSameJoinPointsAs(final KindedPointcut other)\n
    '''
def fastMatch():
    '''returns FuzzyBoolean\n\n
    fastMatch(final FastMatchInfo info)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def postRead():
    '''returns None\n\n
    postRead(final ResolvedType enclosingType)\n
    '''
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream s)\n
    '''
def resolveBindings():
    '''returns None\n\n
    resolveBindings(final IScope scope, final Bindings bindings)\n
    '''
def concretize1():
    '''returns Pointcut\n\n
    concretize1(final ResolvedType inAspect, final ResolvedType declaringType, final IntMap bindings)\n
    '''
def parameterizeWith():
    '''returns Pointcut\n\n
    parameterizeWith(final Map typeVariableMap, final World w)\n
    '''
def accept():
    '''returns Object\n\n
    accept(final PatternNodeVisitor visitor, final Object data)\n
    '''