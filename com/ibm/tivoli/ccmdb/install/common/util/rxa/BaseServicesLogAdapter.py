def ():
    '''returns BaseServicesLogAdapter\n\n
    ()\n
    '''
def entry():
    '''returns None\n\n
    entry(final com.ibm.tivoli.remoteaccess.log.Level level, final Object loggingClass, final String loggingMethod)\n
    entry(final com.ibm.tivoli.remoteaccess.log.Level level, final Object loggingClass, final String loggingMethod, final Object parm1)\n
    entry(final com.ibm.tivoli.remoteaccess.log.Level level, final Object loggingClass, final String loggingMethod, final Object[] parms)\n
    entry(final com.ibm.tivoli.remoteaccess.log.Level level, final Object loggingClass, final String loggingMethod, final Object parm1, final Object parm2)\n
    '''
def exception():
    '''returns None\n\n
    exception(final com.ibm.tivoli.remoteaccess.log.Level level, final Object loggingClass, final String loggingMethod, final Throwable throwable)\n
    exception(final com.ibm.tivoli.remoteaccess.log.Level level, final Object loggingClass, final String loggingMethod, final Throwable throwable, final String text)\n
    '''
def exit():
    '''returns None\n\n
    exit(final com.ibm.tivoli.remoteaccess.log.Level level, final Object loggingClass, final String loggingMethod)\n
    exit(final com.ibm.tivoli.remoteaccess.log.Level level, final Object loggingClass, final String loggingMethod, final boolean retValue)\n
    exit(final com.ibm.tivoli.remoteaccess.log.Level level, final Object loggingClass, final String loggingMethod, final int retValue)\n
    exit(final com.ibm.tivoli.remoteaccess.log.Level level, final Object loggingClass, final String loggingMethod, final long retValue)\n
    exit(final com.ibm.tivoli.remoteaccess.log.Level level, final Object loggingClass, final String loggingMethod, final Object retValue)\n
    '''
def text():
    '''returns None\n\n
    text(final com.ibm.tivoli.remoteaccess.log.Level level, final Object loggingClass, final String loggingMethod, final String text)\n
    text(final com.ibm.tivoli.remoteaccess.log.Level level, final Object loggingClass, final String loggingMethod, final String text, final Object insert1)\n
    text(final com.ibm.tivoli.remoteaccess.log.Level level, final Object loggingClass, final String loggingMethod, final String text, final Object[] inserts)\n
    text(final com.ibm.tivoli.remoteaccess.log.Level level, final Object loggingClass, final String loggingMethod, final String text, final Object insert1, final Object insert2)\n
    '''
def isLoggable():
    '''returns boolean\n\n
    isLoggable(final com.ibm.tivoli.remoteaccess.log.Level level)\n
    '''
