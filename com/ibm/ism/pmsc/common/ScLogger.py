COPYRIGHT = "String IBM Confidential OCO Source Material\n5725-E24 (C) COPYRIGHT International Business Machines Corp. 2007, 2017\nThe source code for this program is not published or otherwise divested\nof its trade secrets, irrespective of what has been deposited with the\nU.S. Copyright Office.""
def ScLogger():
'''public ScLogger(final MXLogger logger)
'''
pass
def getInstance():
'''public static ScLogger getInstance(final Type loggerType)
'''
pass
def debugEntry():
'''public void debugEntry(final Class className, final String method, final Object[] params)
public void debugEntry(final Class className, final String method)
public void debugEntry(final Class className, final String method, final String msg)
public void debugEntry(final Class className, final String method, final Object param1)
public void debugEntry(final Class className, final String method, final Object param1, final Object param2)
public void debugEntry(final Class className, final String method, final Object param1, final Object param2, final Object param3)
public void debugEntry(final Class className, final String method, final Object param1, final Object param2, final Object param3, final Object param4)
public void debugEntry(final String className, final String method, final Object[] params)
public void debugEntry(final String className, final String method)
public void debugEntry(final String className, final String method, final Object param1)
public void debugEntry(final String className, final String method, final Object param1, final Object param2)
public void debugEntry(final String className, final String method, final Object param1, final Object param2, final Object param3)
public void debugEntry(final String className, final String method, final Object param1, final Object param2, final Object param3, final Object param4)
'''
pass
def debugExit():
'''public void debugExit(final Class className, final String method, final Object returnValue)
public void debugExit(final Class className, final String method)
public void debugExit(final Class className, final String methodName, final String msg)
public void debugExit(final String className, final String method, final Object returnValue)
public void debugExit(final String className, final String method)
'''
pass
def debugNote():
'''public void debugNote(final Class className, final String methodName, final String msg)
'''
pass
def infoNote():
'''public void infoNote(final Class className, final String methodName, final String msg)
'''
pass
def warnNote():
'''public void warnNote(final Class className, final String methodName, final String msg)
'''
pass
def errorNote():
'''public void errorNote(final Class className, final String methodName, final String msg)
'''
pass
def fatalNote():
'''public void fatalNote(final Class className, final String methodName, final String msg)
'''
pass
def logException():
'''public void logException(final Class className, final String methodName, final Throwable thrown)
'''
pass
def isFatalEnabled():
'''public boolean isFatalEnabled()
'''
pass
def isErrorEnabled():
'''public boolean isErrorEnabled()
'''
pass
def isWarnEnabled():
'''public boolean isWarnEnabled()
'''
pass
def isInfoEnabled():
'''public boolean isInfoEnabled()
'''
pass
def isDebugEnabled():
'''public boolean isDebugEnabled()
'''
pass
def isEnabled():
'''public boolean isEnabled(final int level)
'''
pass
def getErrorMessageForThrowable():
'''public static final String getErrorMessageForThrowable(final Throwable t)
'''
pass
def main():
'''public static void main()
'''
pass
def isDebug():
'''public boolean isDebug()
'''
pass
def isInfo():
'''public boolean isInfo()
'''
pass
def isWarn():
'''public boolean isWarn()
'''
pass
def isError():
'''public boolean isError()
'''
pass
def debug():
'''public void debug(final String className, final String method, final String msg)
public void debug(final String className, final String method, final String msg, final Throwable t)
'''
pass
def info():
'''public void info(final String className, final String method, final String msg)
public void info(final String className, final String method, final String msg, final Throwable t)
'''
pass
def warn():
'''public void warn(final String className, final String method, final String msg)
public void warn(final String className, final String method, final String msg, final Throwable t)
'''
pass
def error():
'''public void error(final String className, final String method, final String msg)
public void error(final String className, final String method, final String msg, final Throwable t)
'''
pass
def fatal():
'''public void fatal(final String className, final String method, final String msg)
public void fatal(final String className, final String method, final String msg, final Throwable t)
'''
pass
