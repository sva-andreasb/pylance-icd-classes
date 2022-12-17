LEVEL_ALL = "int  0"
LEVEL_DEBUG = "int  1"
LEVEL_INFO = "int  2"
LEVEL_WARN = "int  3"
def ():
    '''returns StdErrLog\n\n
    ()\n
    (final String name)\n
    (final String name, final Properties props)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setPrintLongNames():
    '''returns None\n\n
    setPrintLongNames(final boolean printLongNames)\n
    '''
def isPrintLongNames():
    '''returns boolean\n\n
    isPrintLongNames()\n
    '''
def isHideStacks():
    '''returns boolean\n\n
    isHideStacks()\n
    '''
def setHideStacks():
    '''returns None\n\n
    setHideStacks(final boolean hideStacks)\n
    '''
def isSource():
    '''returns boolean\n\n
    isSource()\n
    '''
def setSource():
    '''returns None\n\n
    setSource(final boolean source)\n
    '''
def warn():
    '''returns None\n\n
    warn(final String msg, final Object... args)\n
    warn(final Throwable thrown)\n
    warn(final String msg, final Throwable thrown)\n
    '''
def info():
    '''returns None\n\n
    info(final String msg, final Object... args)\n
    info(final Throwable thrown)\n
    info(final String msg, final Throwable thrown)\n
    '''
def isDebugEnabled():
    '''returns boolean\n\n
    isDebugEnabled()\n
    '''
def setDebugEnabled():
    '''returns None\n\n
    setDebugEnabled(final boolean enabled)\n
    '''
def getLevel():
    '''returns int\n\n
    getLevel()\n
    '''
def setLevel():
    '''returns None\n\n
    setLevel(final int level)\n
    '''
def setStdErrStream():
    '''returns None\n\n
    setStdErrStream(final PrintStream stream)\n
    '''
def debug():
    '''returns None\n\n
    debug(final String msg, final Object... args)\n
    debug(final Throwable thrown)\n
    debug(final String msg, final Throwable thrown)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def ignore():
    '''returns None\n\n
    ignore(final Throwable ignored)\n
    '''
