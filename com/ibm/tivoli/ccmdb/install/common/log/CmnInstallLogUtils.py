PRISM_INSTALL_MESSAGE_LOGGER_NAME = "String  \"com.ibm.tivoli.ccmdb.install.message.logger\""
PRISM_INSTALL_TRACE_LOGGER_NAME = "String  \"com.ibm.tivoli.ccmdb.install.trace.logger\""
CMS_TRACE_LOGGER_PREFIX = "String  \"com.ibm.tivoli.contextmenuservice\""
def getTraceLogger():
    '''returns Logger\n\n
    getTraceLogger()\n
    '''
def getMessageLogger():
    '''returns Logger\n\n
    getMessageLogger()\n
    '''
def logMessage():
    '''returns None\n\n
    logMessage(final Level msgLevel, final Class<?> loggingClass, final String loggingMethod, final String key, final Object[] inserts)\n
    '''
def getAndLogMessage():
    '''returns String\n\n
    getAndLogMessage(final Locale aLocale, final Level msgLevel, final Class<?> loggingClass, final String loggingMethod, final String key, final Object[] inserts)\n
    '''
def getMessage():
    '''returns String\n\n
    getMessage(final Locale aLocale, final String key, final Object[] inserts, final String bundle)\n
    getMessage(final Locale aLocale, final String key, final Object[] inserts)\n
    '''
def getStackTrace():
    '''returns String\n\n
    getStackTrace(final Throwable aThrowable)\n
    '''
def handleUnexpectedException():
    '''returns String\n\n
    handleUnexpectedException(final Throwable t, final boolean logMessage)\n
    handleUnexpectedException(final Throwable t)\n
    '''
