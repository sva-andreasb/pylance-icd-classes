def ProgressLoggerBase():
'''public ProgressLoggerBase(final String messageBundleName)
'''
pass
def getErrorCount():
'''public int getErrorCount()
'''
pass
def getWarningCount():
'''public int getWarningCount()
'''
pass
def getPercentCompelete():
'''public int getPercentCompelete()
'''
pass
def setItemCount():
'''public void setItemCount(final long count)
'''
pass
def error():
'''public void error(final String msg)
public void error(final String msg, final String[] params)
'''
pass
def exception():
'''public void exception(final Throwable t)
public void exception(final String pageName, final String itemName, final Throwable t)
public void exception(final String pageName, final String itemName, final String fieldName, final Throwable t)
'''
pass
def message():
'''public void message(final String msg)
public void message(final String msg, final String[] params)
'''
pass
def progressMsg():
'''public void progressMsg(final String msg)
public void progressMsg(final String msg, final String[] params)
'''
pass
def start():
'''public void start(final int startStatus)
'''
pass
def warning():
'''public void warning(final String msg)
public void warning(final String msg, final String[] params)
'''
pass
def flush():
'''public void flush()
'''
pass
def dataIntegrityMessage():
'''public void dataIntegrityMessage(final String msg)
public void dataIntegrityMessage(String msg, final String[] params)
'''
pass
def setLoader():
'''public void setLoader(final ModelLoaderBase loader)
'''
pass
def cleanup():
'''public void cleanup()
'''
pass
def loadComplete():
'''public void loadComplete()
'''
pass
def itemProcessed():
'''public void itemProcessed(final long count)
public void itemProcessed()
'''
pass
def setLogLevel():
'''public void setLogLevel(final long level)
'''
pass
def setMaxLogSize():
'''public void setMaxLogSize(final int maxLogSize)
'''
pass
def formatMessage():
'''public static String formatMessage(String msg, final String[] params)
'''
pass
def messageFromException():
'''public static String messageFromException(final Throwable t)
'''
pass
