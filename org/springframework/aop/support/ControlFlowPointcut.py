def ():
    '''returns ControlFlowPointcut\n\n
    (final Class clazz)\n
    (final Class clazz, final String methodName)\n
    '''
def matches():
    '''returns boolean\n\n
    matches(final Class clazz)\n
    matches(final Method method, final Class targetClass)\n
    matches(final Method method, final Class targetClass, final Object[] args)\n
    '''
def isRuntime():
    '''returns boolean\n\n
    isRuntime()\n
    '''
def getEvaluations():
    '''returns int\n\n
    getEvaluations()\n
    '''
def getClassFilter():
    '''returns ClassFilter\n\n
    getClassFilter()\n
    '''
def getMethodMatcher():
    '''returns MethodMatcher\n\n
    getMethodMatcher()\n
    '''
