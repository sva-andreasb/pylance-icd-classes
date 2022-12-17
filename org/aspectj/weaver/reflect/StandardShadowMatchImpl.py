def ():
    '''returns RuntimeTestEvaluator\n\n
    (final FuzzyBoolean match, final Test test, final ExposedState state, final PointcutParameter[] params)\n
    (final Test aTest, final Object thisObject, final Object targetObject, final Object[] args, final MatchingContext context)\n
    '''
def setWithinCode():
    '''returns None\n\n
    setWithinCode(final ResolvedMember aMember)\n
    '''
def setSubject():
    '''returns None\n\n
    setSubject(final ResolvedMember aMember)\n
    '''
def setWithinType():
    '''returns None\n\n
    setWithinType(final ResolvedType aClass)\n
    '''
def alwaysMatches():
    '''returns boolean\n\n
    alwaysMatches()\n
    '''
def maybeMatches():
    '''returns boolean\n\n
    maybeMatches()\n
    '''
def neverMatches():
    '''returns boolean\n\n
    neverMatches()\n
    '''
def matchesJoinPoint():
    '''returns JoinPointMatch\n\n
    matchesJoinPoint(final Object thisObject, final Object targetObject, final Object[] args)\n
    '''
def setMatchingContext():
    '''returns None\n\n
    setMatchingContext(final MatchingContext aMatchContext)\n
    '''
def matches():
    '''returns boolean\n\n
    matches()\n
    '''
def visit():
    '''returns None\n\n
    visit(final And e)\n
    visit(final Instanceof i)\n
    visit(final MatchingContextBasedTest matchingContextTest)\n
    visit(final Not not)\n
    visit(final Or or)\n
    visit(final Literal literal)\n
    visit(final Call call)\n
    visit(final FieldGetCall fieldGetCall)\n
    visit(final HasAnnotation hasAnnotation)\n
    '''
