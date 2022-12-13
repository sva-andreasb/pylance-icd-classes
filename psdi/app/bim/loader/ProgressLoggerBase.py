def ProgressLoggerBase():
    '''public ProgressLoggerBase(final String messageBundleName)
    '''
def getErrorCount():
    '''public int getErrorCount()
    '''
def getWarningCount():
    '''public int getWarningCount()
    '''
def getPercentCompelete():
    '''public int getPercentCompelete()
    '''
def setItemCount():
    '''public void setItemCount(final long count)
    '''
def error():
    '''public void error(final String msg)
    public void error(final String msg, final String[] params)
    '''
def exception():
    '''public void exception(final Throwable t)
    public void exception(final String pageName, final String itemName, final Throwable t)
    public void exception(final String pageName, final String itemName, final String fieldName, final Throwable t)
    '''
def message():
    '''public void message(final String msg)
    public void message(final String msg, final String[] params)
    '''
def progressMsg():
    '''public void progressMsg(final String msg)
    public void progressMsg(final String msg, final String[] params)
    '''
def start():
    '''public void start(final int startStatus)
    '''
def warning():
    '''public void warning(final String msg)
    public void warning(final String msg, final String[] params)
    '''
def flush():
    '''public void flush()
    '''
def dataIntegrityMessage():
    '''public void dataIntegrityMessage(final String msg)
    public void dataIntegrityMessage(String msg, final String[] params)
    '''
def setLoader():
    '''public void setLoader(final ModelLoaderBase loader)
    '''
def cleanup():
    '''public void cleanup()
    '''
def loadComplete():
    '''public void loadComplete()
    '''
def itemProcessed():
    '''public void itemProcessed(final long count)
    public void itemProcessed()
    '''
def setLogLevel():
    '''public void setLogLevel(final long level)
    '''
def setMaxLogSize():
    '''public void setMaxLogSize(final int maxLogSize)
    '''
def formatMessage():
    '''public static String formatMessage(String msg, final String[] params)
    '''
def messageFromException():
    '''public static String messageFromException(final Throwable t)
    '''
