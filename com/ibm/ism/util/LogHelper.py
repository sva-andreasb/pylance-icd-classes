IBM_COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
DEBUG_LEVEL = "int  0"
INFO_LEVEL = "int  1"
WARN_LEVEL = "int  2"
ERROR_LEVEL = "int  3"
FATAL_LEVEL = "int  4"
def isNull():
    '''public static boolean isNull(final String t)
    '''
def debugEntry():
    '''public static void debugEntry(final String log, final Class className, final String methodName, final String msg)
    public static void debugEntry(final MXLogger myLogger, final Class className, final String methodName, final String msg)
    public static void debugEntry(final Class className, final String methodName, final String msg)
    '''
def debugExit():
    '''public static void debugExit(final String log, final Class className, final String methodName, final String msg)
    public static void debugExit(final MXLogger myLog, final Class className, final String methodName, final String msg)
    public static void debugExit(final Class className, final String methodName, final String msg)
    '''
def debugNote():
    '''public static void debugNote(final String log, final Class className, final String methodName, final String msg)
    public static void debugNote(final MXLogger myLogger, final Class className, final String methodName, final String msg)
    public static void debugNote(final Class className, final String methodName, final String msg)
    '''
def infoNote():
    '''public static void infoNote(final String log, final Class className, final String methodName, final String msg)
    public static void infoNote(final String log, final Class className, final String method, final String group, final String key)
    public static void infoNote(final String log, final Class className, final String method, final String group, final String key, final Object[] params)
    public static void infoNote(final MXLogger log, final Class className, final String method, final String group, final String key)
    public static void infoNote(final MXLogger log, final Class className, final String method, final String group, final String key, final Object[] params)
    public static void infoNote(final Class className, final String method, final String group, final String key)
    public static void infoNote(final Class className, final String method, final String group, final String key, final Object[] params)
    public static void infoNote(final MXLogger myLogger, final Class className, final String methodName, final String msg)
    public static void infoNote(final Class className, final String methodName, final String msg)
    '''
def warnNote():
    '''public static void warnNote(final String log, final Class className, final String methodName, final String msg)
    public static void warnNote(final MXLogger myLogger, final Class className, final String methodName, final String msg)
    public static void warnNote(final Class className, final String methodName, final String msg)
    public static void warnNote(final String log, final Class className, final String method, final String group, final String key)
    public static void warnNote(final String log, final Class className, final String method, final String group, final String key, final Object[] params)
    public static void warnNote(final MXLogger log, final Class className, final String method, final String group, final String key)
    public static void warnNote(final MXLogger log, final Class className, final String method, final String group, final String key, final Object[] params)
    public static void warnNote(final Class className, final String method, final String group, final String key)
    public static void warnNote(final Class className, final String method, final String group, final String key, final Object[] params)
    '''
def errorNote():
    '''public static void errorNote(final String log, final Class className, final String methodName, final String msg)
    public static void errorNote(final MXLogger myLogger, final Class className, final String methodName, final String msg)
    public static void errorNote(final Class className, final String methodName, final String msg)
    public static void errorNote(final String log, final Class className, final String method, final String group, final String key)
    public static void errorNote(final String log, final Class className, final String method, final String group, final String key, final Object[] params)
    public static void errorNote(final MXLogger log, final Class className, final String method, final String group, final String key)
    public static void errorNote(final MXLogger log, final Class className, final String method, final String group, final String key, final Object[] params)
    public static void errorNote(final Class className, final String method, final String group, final String key)
    public static void errorNote(final Class className, final String method, final String group, final String key, final Object[] params)
    '''
def fatalNote():
    '''public static void fatalNote(final String log, final Class className, final String methodName, final String msg)
    public static void fatalNote(final MXLogger myLogger, final Class className, final String methodName, final String msg)
    public static void fatalNote(final String log, final Class className, final String method, final String group, final String key)
    public static void fatalNote(final String log, final Class className, final String method, final String group, final String key, final Object[] params)
    public static void fatalNote(final MXLogger log, final Class className, final String method, final String group, final String key)
    public static void fatalNote(final MXLogger log, final Class className, final String method, final String group, final String key, final Object[] params)
    public static void fatalNote(final Class className, final String method, final String group, final String key)
    public static void fatalNote(final Class className, final String method, final String group, final String key, final Object[] params)
    public static void fatalNote(final Class className, final String methodName, final String msg)
    '''
def logException():
    '''public static void logException(final String log, final Class className, final String methodName, final Throwable thrown)
    public static void logException(final MXLogger myLogger, final Class className, final String methodName, final Throwable thrown)
    public static void logException(final Class className, final String methodName, final Throwable thrown)
    '''
def isFatalEnabled():
    '''public static boolean isFatalEnabled()
    public static boolean isFatalEnabled(final MXLogger logger)
    public static boolean isFatalEnabled(final String log)
    '''
def isErrorEnabled():
    '''public static boolean isErrorEnabled()
    public static boolean isErrorEnabled(final MXLogger logger)
    public static boolean isErrorEnabled(final String log)
    '''
def isWarnEnabled():
    '''public static boolean isWarnEnabled()
    public static boolean isWarnEnabled(final MXLogger logger)
    public static boolean isWarnEnabled(final String log)
    '''
def isInfoEnabled():
    '''public static boolean isInfoEnabled()
    public static boolean isInfoEnabled(final MXLogger logger)
    public static boolean isInfoEnabled(final String log)
    '''
def isDebugEnabled():
    '''public static boolean isDebugEnabled()
    public static boolean isDebugEnabled(final MXLogger logger)
    public static boolean isDebugEnabled(final String log)
    '''
def isEnabled():
    '''public static boolean isEnabled(final int level)
    public static boolean isEnabled(final int level, final MXLogger log)
    public static boolean isEnabled(final int level, final String log)
    '''
def resolveMessage():
    '''public static String resolveMessage(final String group, final String key)
    public static String resolveMessage(final String group, final String key, final Object[] params)
    '''
