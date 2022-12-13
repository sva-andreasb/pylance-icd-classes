def debugEntry():
    '''    public static void debugEntry(final Class className, final String methodName, final String msg)
    '''
def debugExit():
    '''    public static void debugExit(final Class className, final String methodName, final String msg)
    '''
def debugNote():
    '''    public static void debugNote(final Class className, final String methodName, final String msg)
    '''
def infoNote():
    '''    public static void infoNote(final Class className, final String methodName, final String msg)
    '''
def warnNote():
    '''    public static void warnNote(final Class className, final String methodName, final String msg)
    '''
def errorNote():
    '''    public static void errorNote(final Class className, final String methodName, final String msg)
    public static void errorNote(final Class className, final String methodName, final String msg, final Throwable t)
    public static void errorNote(final Class className, final String methodName, final String errorgroup, final String errorkey)
    public static void errorNote(final Class className, final String methodName, final String errorgroup, final String errorkey, final Object[] params)
    '''
def fatalNote():
    '''    public static void fatalNote(final Class className, final String methodName, final String msg)
    '''
def logException():
    '''    public static void logException(final Class className, final String methodName, final Throwable thrown)
    '''
def isFatalEnabled():
    '''    public static boolean isFatalEnabled()
    '''
def isErrorEnabled():
    '''    public static boolean isErrorEnabled()
    '''
def isWarnEnabled():
    '''    public static boolean isWarnEnabled()
    '''
def isInfoEnabled():
    '''    public static boolean isInfoEnabled()
    '''
def isDebugEnabled():
    '''    public static boolean isDebugEnabled()
    '''
def isEnabled():
    '''    public static boolean isEnabled(final int level)
    '''
def getLogger():
    '''    public static MXLogger getLogger()
    '''
