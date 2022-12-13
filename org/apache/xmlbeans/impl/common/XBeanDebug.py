TRACE_SCHEMA_LOADING = "int  1"
traceProp = "String  \"org.apache.xmlbeans.impl.debug\""
defaultProp = "String  \"\""
def enable():
    '''public static void enable(final int bits)
    '''
def disable():
    '''public static void disable(final int bits)
    '''
def trace():
    '''public static void trace(final int bits, final String message, final int indent)
    '''
def test():
    '''public static boolean test(final int bits)
    '''
def log():
    '''public static String log(final String message)
    '''
def logStackTrace():
    '''public static String logStackTrace(final String message)
    '''
def logException():
    '''public static Throwable logException(final Throwable t)
    '''
