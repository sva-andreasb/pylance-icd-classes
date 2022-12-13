def getDefaultCauseMethodNames():
'''public static String[] getDefaultCauseMethodNames()
'''
pass
def getCause():
'''public static Throwable getCause(final Throwable throwable)
public static Throwable getCause(final Throwable throwable, String[] methodNames)
'''
pass
def getRootCause():
'''public static Throwable getRootCause(final Throwable throwable)
'''
pass
def getThrowableCount():
'''public static int getThrowableCount(final Throwable throwable)
'''
pass
def getThrowables():
'''public static Throwable[] getThrowables(final Throwable throwable)
'''
pass
def getThrowableList():
'''public static List<Throwable> getThrowableList(Throwable throwable)
'''
pass
def indexOfThrowable():
'''public static int indexOfThrowable(final Throwable throwable, final Class<?> clazz)
public static int indexOfThrowable(final Throwable throwable, final Class<?> clazz, final int fromIndex)
'''
pass
def indexOfType():
'''public static int indexOfType(final Throwable throwable, final Class<?> type)
public static int indexOfType(final Throwable throwable, final Class<?> type, final int fromIndex)
'''
pass
def printRootCauseStackTrace():
'''public static void printRootCauseStackTrace(final Throwable throwable)
public static void printRootCauseStackTrace(final Throwable throwable, final PrintStream stream)
public static void printRootCauseStackTrace(final Throwable throwable, final PrintWriter writer)
'''
pass
def getRootCauseStackTrace():
'''public static String[] getRootCauseStackTrace(final Throwable throwable)
'''
pass
def removeCommonFrames():
'''public static void removeCommonFrames(final List<String> causeFrames, final List<String> wrapperFrames)
'''
pass
def getStackTrace():
'''public static String getStackTrace(final Throwable throwable)
'''
pass
def getStackFrames():
'''public static String[] getStackFrames(final Throwable throwable)
'''
pass
def getMessage():
'''public static String getMessage(final Throwable th)
'''
pass
def getRootCauseMessage():
'''public static String getRootCauseMessage(final Throwable th)
'''
pass
