def ():
    '''returns LoggerUtil\n\n
    (final Class<?> clazz)\n
    '''
def traceExitError():
    '''returns None\n\n
    traceExitError(final String sourceMethod, final String msg, final Throwable cause)\n
    '''
def traceNoteError():
    '''returns None\n\n
    traceNoteError(final String sourceMethod, final String msg, final Throwable cause)\n
    '''
def traceInfo():
    '''returns None\n\n
    traceInfo(final String sourceMethod, final String msg)\n
    '''
def traceEnterMethod():
    '''returns None\n\n
    traceEnterMethod(final String sourceMethod)\n
    traceEnterMethod(final String sourceMethod, final String... arguments)\n
    '''
def traceExitMethod():
    '''returns None\n\n
    traceExitMethod(final String sourceMethod)\n
    traceExitMethod(final String sourceMethod, final String output)\n
    '''
def isEnabled():
    '''returns boolean\n\n
    isEnabled(final Level level)\n
    '''
