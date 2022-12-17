COPYRIGHT = "String  \"IBM Confidential OCO Source Material\n5725-E24 (C) COPYRIGHT International Business Machines Corp. 2007, 2017\nThe source code for this program is not published or otherwise divested\nof its trade secrets, irrespective of what has been deposited with the\nU.S. Copyright Office.\""
def debugEntry():
    '''returns None\n\n
    debugEntry(final Class className, final String method, final Object[] params)\n
    debugEntry(final Class className, final String method)\n
    debugEntry(final Class className, final String method, final String msg)\n
    debugEntry(final Class className, final String method, final Object param1)\n
    debugEntry(final Class className, final String method, final Object param1, final Object param2)\n
    debugEntry(final Class className, final String method, final Object param1, final Object param2, final Object param3)\n
    debugEntry(final Class className, final String method, final Object param1, final Object param2, final Object param3, final Object param4)\n
    '''
def debugExit():
    '''returns None\n\n
    debugExit(final Class className, final String method, final Object returnValue)\n
    debugExit(final Class className, final String method)\n
    debugExit(final Class className, final String methodName, final String msg)\n
    '''
def debugNote():
    '''returns None\n\n
    debugNote(final Class className, final String methodName, final String msg)\n
    '''
def infoNote():
    '''returns None\n\n
    infoNote(final Class className, final String methodName, final String msg)\n
    '''
def warnNote():
    '''returns None\n\n
    warnNote(final Class className, final String methodName, final String msg)\n
    '''
def errorNote():
    '''returns None\n\n
    errorNote(final Class className, final String methodName, final String msg)\n
    '''
def fatalNote():
    '''returns None\n\n
    fatalNote(final Class className, final String methodName, final String msg)\n
    '''
def logException():
    '''returns None\n\n
    logException(final Class className, final String methodName, final Throwable thrown)\n
    '''
def isFatalEnabled():
    '''returns boolean\n\n
    isFatalEnabled()\n
    '''
def isErrorEnabled():
    '''returns boolean\n\n
    isErrorEnabled()\n
    '''
def isWarnEnabled():
    '''returns boolean\n\n
    isWarnEnabled()\n
    '''
def isInfoEnabled():
    '''returns boolean\n\n
    isInfoEnabled()\n
    '''
def isDebugEnabled():
    '''returns boolean\n\n
    isDebugEnabled()\n
    '''
def isEnabled():
    '''returns boolean\n\n
    isEnabled(final int level)\n
    '''
