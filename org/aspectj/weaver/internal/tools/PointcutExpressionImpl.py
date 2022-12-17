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
    matchesMethodExecution(final Method aMethod)\n
    '''
def matchesConstructorExecution():
    '''returns ShadowMatch\n\n
    matchesConstructorExecution(final Constructor aConstructor)\n
    '''
def matchesStaticInitialization():
    '''returns ShadowMatch\n\n
    matchesStaticInitialization(final Class aClass)\n
    '''
def matchesAdviceExecution():
    '''returns ShadowMatch\n\n
    matchesAdviceExecution(final Method aMethod)\n
    '''
def matchesInitialization():
    '''returns ShadowMatch\n\n
    matchesInitialization(final Constructor aConstructor)\n
    '''
def matchesPreInitialization():
    '''returns ShadowMatch\n\n
    matchesPreInitialization(final Constructor aConstructor)\n
    '''
def matchesMethodCall():
    '''returns ShadowMatch\n\n
    matchesMethodCall(final Method aMethod, final Member withinCode)\n
    matchesMethodCall(final Method aMethod, final Class callerType)\n
    '''
def matchesConstructorCall():
    '''returns ShadowMatch\n\n
    matchesConstructorCall(final Constructor aConstructor, final Class callerType)\n
    matchesConstructorCall(final Constructor aConstructor, final Member withinCode)\n
    '''
def matchesHandler():
    '''returns ShadowMatch\n\n
    matchesHandler(final Class exceptionType, final Class handlingType)\n
    matchesHandler(final Class exceptionType, final Member withinCode)\n
    '''
def matchesFieldGet():
    '''returns ShadowMatch\n\n
    matchesFieldGet(final Field aField, final Class withinType)\n
    matchesFieldGet(final Field aField, final Member withinCode)\n
    '''
def matchesFieldSet():
    '''returns ShadowMatch\n\n
    matchesFieldSet(final Field aField, final Class withinType)\n
    matchesFieldSet(final Field aField, final Member withinCode)\n
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
