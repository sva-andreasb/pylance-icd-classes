DEBUG = "int  0"
INFO = "int  1"
WARN = "int  2"
ERROR = "int  3"
def debug():
    '''public static final void debug(final String msg, final Object... args)
    '''
def warn():
    '''public static final void warn(final String msg, final Object... args)
    '''
def info():
    '''public static final void info(final String msg, final Object... args)
    '''
def error():
    '''public static void error(final String string, final Throwable e)
    '''
def printf():
    '''public static void printf(final String msg, final Object... args)
    public static void printf(final int level, String msg, final Object... args)
    '''
def isDebug():
    '''public static boolean isDebug()
    '''
def isInfo():
    '''public static boolean isInfo()
    '''
def isWarn():
    '''public static boolean isWarn()
    '''
def isError():
    '''public static boolean isError()
    '''
