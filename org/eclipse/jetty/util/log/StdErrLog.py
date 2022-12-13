LEVEL_ALL = "int  0"
LEVEL_DEBUG = "int  1"
LEVEL_INFO = "int  2"
LEVEL_WARN = "int  3"
def StdErrLog():
    '''    public StdErrLog()
    public StdErrLog(final String name)
    public StdErrLog(final String name, final Properties props)
    '''
def getLoggingLevel():
    '''    public static int getLoggingLevel(final Properties props, final String name)
    '''
def getName():
    '''    public String getName()
    '''
def setPrintLongNames():
    '''    public void setPrintLongNames(final boolean printLongNames)
    '''
def isPrintLongNames():
    '''    public boolean isPrintLongNames()
    '''
def isHideStacks():
    '''    public boolean isHideStacks()
    '''
def setHideStacks():
    '''    public void setHideStacks(final boolean hideStacks)
    '''
def isSource():
    '''    public boolean isSource()
    '''
def setSource():
    '''    public void setSource(final boolean source)
    '''
def warn():
    '''    public void warn(final String msg, final Object... args)
    public void warn(final Throwable thrown)
    public void warn(final String msg, final Throwable thrown)
    '''
def info():
    '''    public void info(final String msg, final Object... args)
    public void info(final Throwable thrown)
    public void info(final String msg, final Throwable thrown)
    '''
def isDebugEnabled():
    '''    public boolean isDebugEnabled()
    '''
def setDebugEnabled():
    '''    public void setDebugEnabled(final boolean enabled)
    '''
def getLevel():
    '''    public int getLevel()
    '''
def setLevel():
    '''    public void setLevel(final int level)
    '''
def setStdErrStream():
    '''    public void setStdErrStream(final PrintStream stream)
    '''
def debug():
    '''    public void debug(final String msg, final Object... args)
    public void debug(final Throwable thrown)
    public void debug(final String msg, final Throwable thrown)
    '''
def toString():
    '''    public String toString()
    '''
def setProperties():
    '''    public static void setProperties(final Properties props)
    '''
def ignore():
    '''    public void ignore(final Throwable ignored)
    '''
