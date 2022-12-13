def getDefaultCauseMethodNames():
    '''public static String[] getDefaultCauseMethodNames()
    '''
def getCause():
    '''public static Throwable getCause(final Throwable throwable)
    public static Throwable getCause(final Throwable throwable, String[] methodNames)
    '''
def getRootCause():
    '''public static Throwable getRootCause(final Throwable throwable)
    '''
def getThrowableCount():
    '''public static int getThrowableCount(final Throwable throwable)
    '''
def getThrowables():
    '''public static Throwable[] getThrowables(final Throwable throwable)
    '''
def getThrowableList():
    '''public static List<Throwable> getThrowableList(Throwable throwable)
    '''
def indexOfThrowable():
    '''public static int indexOfThrowable(final Throwable throwable, final Class<?> clazz)
    public static int indexOfThrowable(final Throwable throwable, final Class<?> clazz, final int fromIndex)
    '''
def indexOfType():
    '''public static int indexOfType(final Throwable throwable, final Class<?> type)
    public static int indexOfType(final Throwable throwable, final Class<?> type, final int fromIndex)
    '''
def printRootCauseStackTrace():
    '''public static void printRootCauseStackTrace(final Throwable throwable)
    public static void printRootCauseStackTrace(final Throwable throwable, final PrintStream stream)
    public static void printRootCauseStackTrace(final Throwable throwable, final PrintWriter writer)
    '''
def getRootCauseStackTrace():
    '''public static String[] getRootCauseStackTrace(final Throwable throwable)
    '''
def removeCommonFrames():
    '''public static void removeCommonFrames(final List<String> causeFrames, final List<String> wrapperFrames)
    '''
def getStackTrace():
    '''public static String getStackTrace(final Throwable throwable)
    '''
def getStackFrames():
    '''public static String[] getStackFrames(final Throwable throwable)
    '''
def getMessage():
    '''public static String getMessage(final Throwable th)
    '''
def getRootCauseMessage():
    '''public static String getRootCauseMessage(final Throwable th)
    '''
