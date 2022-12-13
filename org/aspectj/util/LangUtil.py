def is13VMOrGreater():
    '''    public static boolean is13VMOrGreater()
    '''
def is14VMOrGreater():
    '''    public static boolean is14VMOrGreater()
    '''
def is15VMOrGreater():
    '''    public static boolean is15VMOrGreater()
    '''
def is16VMOrGreater():
    '''    public static boolean is16VMOrGreater()
    '''
def is17VMOrGreater():
    '''    public static boolean is17VMOrGreater()
    '''
def throwIaxIfNull():
    '''    public static final void throwIaxIfNull(final Object o, final String name)
    '''
def throwIaxIfNotAssignable():
    '''    public static final void throwIaxIfNotAssignable(final Object[] ra, final Class<?> c, final String name)
    public static final void throwIaxIfNotAssignable(final Object o, final Class<?> c, final String name)
    '''
def throwIaxIfFalse():
    '''    public static final void throwIaxIfFalse(final boolean test, final String message)
    '''
def isEmpty():
    '''    public static boolean isEmpty(final String s)
    public static boolean isEmpty(final Object[] ra)
    public static boolean isEmpty(final byte[] ra)
    public static boolean isEmpty(final Collection<?> collection)
    public static boolean isEmpty(final Map<?, ?> map)
    '''
def split():
    '''    public static String[] split(final String text)
    '''
def commaSplit():
    '''    public static List<String> commaSplit(final String input)
    '''
def splitClasspath():
    '''    public static String[] splitClasspath(final String classpath)
    '''
def getBoolean():
    '''    public static boolean getBoolean(final String propertyName, final boolean defaultValue)
    '''
def anySplit():
    '''    public static List<String> anySplit(final String input, final String delim)
    '''
def strings():
    '''    public static List<String> strings(final String text)
    '''
def safeList():
    '''    public static <T> List<T> safeList(final List<T> list)
    '''
def copyStrings():
    '''    public static String[][] copyStrings(final String[][] in)
    '''
def extractOptions():
    '''    public static String[] extractOptions(String[] args, final String[][] options)
    '''
def safeCopy():
    '''    public static Object[] safeCopy(final Object[] source, Object[] sink)
    '''
def unqualifiedClassName():
    '''    public static String unqualifiedClassName(final Class<?> c)
    public static String unqualifiedClassName(final Object o)
    '''
def replace():
    '''    public static String replace(final String in, final String sought, final String replace)
    '''
def toSizedString():
    '''    public static String toSizedString(final long i, int width)
    '''
def renderExceptionShort():
    '''    public static String renderExceptionShort(final Throwable e)
    '''
def renderException():
    '''    public static String renderException(final Throwable t)
    public static String renderException(Throwable t, final boolean elide)
    '''
def stackToString():
    '''    public static StringBuffer stackToString(final Throwable throwable, final boolean skipMessage)
    '''
def unwrapException():
    '''    public static Throwable unwrapException(final Throwable t)
    '''
def arrayAsList():
    '''    public static List<Object> arrayAsList(final Object[] array)
    '''
def makeClasspath():
    '''    public static String makeClasspath(final String bootclasspath, final String classpath, final String classesDir, final String outputJar)
    '''
def makeProcess():
    '''    public static ProcessController makeProcess(ProcessController controller, final String classpath, final String mainClass, final String[] args)
    '''
def getJavaExecutable():
    '''    public static File getJavaExecutable()
    '''
def sleepUntil():
    '''    public static boolean sleepUntil(final long time)
    '''
def acceptString():
    '''    public boolean acceptString(final String input)
    '''
def reinit():
    '''    public final void reinit()
    '''
def init():
    '''    public final void init(final String classpath, final String mainClass, final String[] args)
    public final void init(final File java, final String classpath, final String mainClass, final String[] args)
    public final void init(final String[] command, final String label)
    '''
def setEnvp():
    '''    public final void setEnvp(final String[] envp)
    '''
def setErrSnoop():
    '''    public final void setErrSnoop(final ByteArrayOutputStream snoop)
    '''
def setOutSnoop():
    '''    public final void setOutSnoop(final ByteArrayOutputStream snoop)
    '''
def start():
    '''    public final Thread start()
    '''
def run():
    '''    public void run()
    '''
def stop():
    '''    public final synchronized void stop()
    '''
def getCommand():
    '''    public final String[] getCommand()
    '''
def completed():
    '''    public final boolean completed()
    '''
def started():
    '''    public final boolean started()
    '''
def userStopped():
    '''    public final boolean userStopped()
    '''
def getThrown():
    '''    public final Thrown getThrown()
    '''
def getResult():
    '''    public final int getResult()
    '''
def toString():
    '''    public String toString()
    '''
