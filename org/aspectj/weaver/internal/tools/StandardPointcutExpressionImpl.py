def ():
    '''returns Handler\n\n
    (final Pointcut pointcut, final String expression, final PointcutParameter[] params, final World inWorld)\n
    (final Class decClass, final Class exType)\n
    '''
def getUnderlyingPointcut():
    '''returns Pointcut\n\n
    getUnderlyingPointcut()\n
    '''
def setMatchingContext():
    '''returns None\n\n
    setMatchingContext(final MatchingContext aMatchContext)\n
    '''
def couldMatchJoinPointsInType():
    '''returns boolean\n\n
    couldMatchJoinPointsInType(final Class aClass)\n
    '''
def mayNeedDynamicTest():
    '''returns boolean\n\n
    mayNeedDynamicTest()\n
    '''
def matchesMethodExecution():
    '''returns ShadowMatch\n\n
    matchesMethodExecution(final ResolvedMember aMethod)\n
    '''
def matchesConstructorExecution():
    '''returns ShadowMatch\n\n
    matchesConstructorExecution(final Constructor aConstructor)\n
    '''
def matchesStaticInitialization():
    '''returns ShadowMatch\n\n
    matchesStaticInitialization(final ResolvedType aType)\n
    '''
def matchesMethodCall():
    '''returns ShadowMatch\n\n
    matchesMethodCall(final ResolvedMember aMethod, final ResolvedMember withinCode)\n
    '''
def getPointcutExpression():
    '''returns String\n\n
    getPointcutExpression()\n
    '''
def hasDynamicContent():
    '''returns boolean\n\n
    hasDynamicContent()\n
    '''
def visit():
    '''returns Object\n\n
    visit(final WithinAnnotationPointcut node, final Object data)\n
    visit(final WithinCodeAnnotationPointcut node, final Object data)\n
    visit(final AnnotationPointcut node, final Object data)\n
    visit(final ArgsAnnotationPointcut node, final Object data)\n
    visit(final ArgsPointcut node, final Object data)\n
    visit(final CflowPointcut node, final Object data)\n
    visit(final IfPointcut node, final Object data)\n
    visit(final NotAnnotationTypePattern node, final Object data)\n
    visit(final NotPointcut node, final Object data)\n
    visit(final ThisOrTargetAnnotationPointcut node, final Object data)\n
    visit(final ThisOrTargetPointcut node, final Object data)\n
    '''
def getModifiers():
    '''returns int\n\n
    getModifiers()\n
    '''
def getDeclaringClass():
    '''returns Class\n\n
    getDeclaringClass()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getHandledExceptionType():
    '''returns Class\n\n
    getHandledExceptionType()\n
    '''
def isSynthetic():
    '''returns boolean\n\n
    isSynthetic()\n
    '''
