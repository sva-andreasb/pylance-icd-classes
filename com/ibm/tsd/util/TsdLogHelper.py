COPYRIGHT = "String  \"IBM Confidential OCO Source Material\n5725-E24 (C) COPYRIGHT International Business Machines Corp. 2007, 2017\nThe source code for this program is not published or otherwise divested\nof its trade secrets, irrespective of what has been deposited with the\nU.S. Copyright Office.\""
def getInstance():
    '''public static TsdLogHelper getInstance(final Type loggerType)
    '''
def debugEntry():
    '''public void debugEntry(final Class className, final String method, final Object[] params)
    public void debugEntry(final Class className, final String method)
    public void debugEntry(final Class className, final String method, final String msg)
    public void debugEntry(final Class className, final String method, final Object param1)
    public void debugEntry(final Class className, final String method, final Object param1, final Object param2)
    public void debugEntry(final Class className, final String method, final Object param1, final Object param2, final Object param3)
    public void debugEntry(final Class className, final String method, final Object param1, final Object param2, final Object param3, final Object param4)
    '''
def debugExit():
    '''public void debugExit(final Class className, final String method, final Object returnValue)
    public void debugExit(final Class className, final String method)
    public void debugExit(final Class className, final String methodName, final String msg)
    '''
def debugNote():
    '''public void debugNote(final Class className, final String methodName, final String msg)
    '''
def infoNote():
    '''public void infoNote(final Class className, final String methodName, final String msg)
    '''
def warnNote():
    '''public void warnNote(final Class className, final String methodName, final String msg)
    '''
def errorNote():
    '''public void errorNote(final Class className, final String methodName, final String msg)
    '''
def fatalNote():
    '''public void fatalNote(final Class className, final String methodName, final String msg)
    '''
def logException():
    '''public void logException(final Class className, final String methodName, final Throwable thrown)
    '''
def isFatalEnabled():
    '''public boolean isFatalEnabled()
    '''
def isErrorEnabled():
    '''public boolean isErrorEnabled()
    '''
def isWarnEnabled():
    '''public boolean isWarnEnabled()
    '''
def isInfoEnabled():
    '''public boolean isInfoEnabled()
    '''
def isDebugEnabled():
    '''public boolean isDebugEnabled()
    '''
def isEnabled():
    '''public boolean isEnabled(final int level)
    '''
def getErrorMessageForThrowable():
    '''public static final String getErrorMessageForThrowable(final Throwable t)
    '''
def main():
    '''public static void main()
    '''
