LEVEL_NONE = "int  11"
LEVEL_FATAL = "int  10"
LEVEL_SEVERE = "int  9"
LEVEL_WARNING = "int  8"
LEVEL_AUDIT = "int  7"
LEVEL_INFO = "int  6"
LEVEL_CONFIG = "int  5"
LEVEL_DETAIL = "int  4"
LEVEL_FINE = "int  3"
LEVEL_FINER = "int  2"
LEVEL_FINEST = "int  1"
LEVEL_ALL = "int  0"
def logp():
    '''returns None\n\n
    logp(final int n, final String s, final String s2, final String s3)\n
    logp(final int n, final String s, final String s2, final String s3, final Object o)\n
    logp(final int n, final String s, final String s2, final String s3, final Object[] array)\n
    logp(final int n, final String s, final String s2, final String s3, final Throwable t)\n
    '''
def entering():
    '''returns None\n\n
    entering(final String s, final String s2)\n
    entering(final String s, final String s2, final Object o)\n
    entering(final String s, final String s2, final Object[] array)\n
    '''
def exiting():
    '''returns None\n\n
    exiting(final String s, final String s2)\n
    exiting(final String s, final String s2, final Object o)\n
    '''
def throwing():
    '''returns None\n\n
    throwing(final String s, final String s2, final Throwable t)\n
    '''
def isLoggable():
    '''returns boolean\n\n
    isLoggable(final int n)\n
    '''
