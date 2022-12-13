DEFAULT_LOG_NAME = "String  \"maximo.service.PMCFGLCSVC\""
def getIdString():
    '''    public String getIdString()
    '''
def setIdString():
    '''    public void setIdString(final String idString)
    '''
def PmCfgLogger():
    '''    public PmCfgLogger(final Class cls, final String logName)
    public PmCfgLogger(final Class cls)
    public PmCfgLogger(final Class cls, final MXLogger logger)
    '''
def isDebugEnabled():
    '''    public final boolean isDebugEnabled()
    '''
def isInfoEnabled():
    '''    public final boolean isInfoEnabled()
    '''
def isWarnEnabled():
    '''    public final boolean isWarnEnabled()
    '''
def isErrorEnabled():
    '''    public final boolean isErrorEnabled()
    '''
def isFatalEnabled():
    '''    public final boolean isFatalEnabled()
    '''
def logException():
    '''    public void logException(final Throwable exc)
    '''
def debug():
    '''    public void debug(final Object... msgs)
    '''
def debugExc():
    '''    public void debugExc(String msg, final Throwable exc)
    '''
def enter():
    '''    public void enter(final String method, final Object... args)
    '''
def argsToString():
    '''    public String argsToString(final Object[] args)
    '''
def exit():
    '''    public <T> T exit(final T returnVal)
    public void exit()
    '''
def throwExc():
    '''    public <T extends Throwable> void throwExc(final T exc)
    '''
def warn():
    '''    public void warn(String msg)
    public void warn(final String msg, final Throwable exc)
    '''
def error():
    '''    public void error(String msg)
    public void error(final String msg, final Throwable exc)
    '''
def fatal():
    '''    public void fatal(String msg)
    public void fatal(final String msg, final Throwable exc)
    '''
def info():
    '''    public void info(String msg)
    public void info(String msg, final Throwable exc)
    '''
def getLogClass():
    '''    public Class getLogClass()
    '''
def setLogger():
    '''    public void setLogger(final String logName)
    public void setLogger(final MXLogger logger)
    '''
def getLogger():
    '''    public MXLogger getLogger()
    '''
def getMethod():
    '''    public String getMethod()
    '''
def setMethod():
    '''    public void setMethod(final String method)
    '''
