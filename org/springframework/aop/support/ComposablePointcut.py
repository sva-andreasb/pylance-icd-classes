def ():
    '''returns ComposablePointcut\n\n
    ()\n
    (final ClassFilter classFilter, final MethodMatcher methodMatcher)\n
    '''
def union():
    '''returns ComposablePointcut\n\n
    union(final ClassFilter filter)\n
    union(final MethodMatcher mm)\n
    '''
def intersection():
    '''returns ComposablePointcut\n\n
    intersection(final ClassFilter filter)\n
    intersection(final MethodMatcher mm)\n
    intersection(final Pointcut other)\n
    '''
def getClassFilter():
    '''returns ClassFilter\n\n
    getClassFilter()\n
    '''
def getMethodMatcher():
    '''returns MethodMatcher\n\n
    getMethodMatcher()\n
    '''
