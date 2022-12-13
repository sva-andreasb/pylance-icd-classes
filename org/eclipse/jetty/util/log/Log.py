EXCEPTION = "String  \"EXCEPTION \""
IGNORED = "String  \"IGNORED \""
def initialized():
    '''public static boolean initialized()
    '''
def setLog():
    '''public static void setLog(final Logger log)
    '''
def getLog():
    '''public static Logger getLog()
    '''
def getRootLogger():
    '''public static Logger getRootLogger()
    '''
def setLogToParent():
    '''public static void setLogToParent(final String name)
    '''
def debug():
    '''public static void debug(final Throwable th)
    public static void debug(final String msg)
    public static void debug(final String msg, final Object arg)
    public static void debug(final String msg, final Object arg0, final Object arg1)
    '''
def ignore():
    '''public static void ignore(final Throwable thrown)
    '''
def info():
    '''public static void info(final String msg)
    public static void info(final String msg, final Object arg)
    public static void info(final String msg, final Object arg0, final Object arg1)
    '''
def isDebugEnabled():
    '''public static boolean isDebugEnabled()
    '''
def warn():
    '''public static void warn(final String msg)
    public static void warn(final String msg, final Object arg)
    public static void warn(final String msg, final Object arg0, final Object arg1)
    public static void warn(final String msg, final Throwable th)
    public static void warn(final Throwable th)
    '''
def getLogger():
    '''public static Logger getLogger(final Class<?> clazz)
    public static Logger getLogger(final String name)
    '''
def getLoggers():
    '''public static Map<String, Logger> getLoggers()
    '''
def run():
    '''public Object run()
    '''
