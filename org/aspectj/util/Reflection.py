def invokestaticN():
    '''public static Object invokestaticN(final Class<?> class_, final String name, final Object[] args)
    '''
def invoke():
    '''public static Object invoke(final Class<?> class_, final Object target, final String name, final Object arg1, final Object arg2)
    public static Object invoke(final Class<?> class_, final Object target, final String name, final Object arg1, final Object arg2, final Object arg3)
    '''
def invokeN():
    '''public static Object invokeN(final Class<?> class_, final String name, final Object target, final Object[] args)
    '''
def getMatchingMethod():
    '''public static Method getMatchingMethod(final Class<?> class_, final String name, final Object[] args)
    '''
def getStaticField():
    '''public static Object getStaticField(final Class<?> class_, final String name)
    '''
def runMainInSameVM():
    '''public static void runMainInSameVM(final String classpath, final String className, final String[] args)
    public static void runMainInSameVM(URL[] urls, final File[] libs, final File[] dirs, final String className, final String[] args)
    public static void runMainInSameVM(final Class<?> mainClass, final String[] args)
    '''
