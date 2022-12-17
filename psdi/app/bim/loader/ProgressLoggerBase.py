def ():
    '''returns ProgressLoggerBase\n\n
    (final String messageBundleName)\n
    '''
def getErrorCount():
    '''returns int\n\n
    getErrorCount()\n
    '''
def getWarningCount():
    '''returns int\n\n
    getWarningCount()\n
    '''
def getPercentCompelete():
    '''returns int\n\n
    getPercentCompelete()\n
    '''
def setItemCount():
    '''returns None\n\n
    setItemCount(final long count)\n
    '''
def error():
    '''returns None\n\n
    error(final String msg)\n
    error(final String msg, final String[] params)\n
    '''
def exception():
    '''returns None\n\n
    exception(final Throwable t)\n
    exception(final String pageName, final String itemName, final Throwable t)\n
    exception(final String pageName, final String itemName, final String fieldName, final Throwable t)\n
    '''
def message():
    '''returns None\n\n
    message(final String msg)\n
    message(final String msg, final String[] params)\n
    '''
def progressMsg():
    '''returns None\n\n
    progressMsg(final String msg)\n
    progressMsg(final String msg, final String[] params)\n
    '''
def start():
    '''returns None\n\n
    start(final int startStatus)\n
    '''
def warning():
    '''returns None\n\n
    warning(final String msg)\n
    warning(final String msg, final String[] params)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def dataIntegrityMessage():
    '''returns None\n\n
    dataIntegrityMessage(final String msg)\n
    dataIntegrityMessage(String msg, final String[] params)\n
    '''
def setLoader():
    '''returns None\n\n
    setLoader(final ModelLoaderBase loader)\n
    '''
def cleanup():
    '''returns None\n\n
    cleanup()\n
    '''
def loadComplete():
    '''returns None\n\n
    loadComplete()\n
    '''
def itemProcessed():
    '''returns None\n\n
    itemProcessed(final long count)\n
    itemProcessed()\n
    '''
def setLogLevel():
    '''returns None\n\n
    setLogLevel(final long level)\n
    '''
def setMaxLogSize():
    '''returns None\n\n
    setMaxLogSize(final int maxLogSize)\n
    '''
