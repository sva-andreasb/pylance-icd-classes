def registerExceptionAdapter():
    '''    public static synchronized void registerExceptionAdapter(final Class<? extends Exception> exceptionClass, final MXExceptionAdapter exceptionAdapter)
    '''
def unregisterExceptionAdapter():
    '''    public static synchronized void unregisterExceptionAdapter(final Class<? extends Exception> exceptionClass)
    '''
def getMessage():
    '''    public static synchronized String getMessage(final Throwable throwable, final String langCode)
    '''
def toMXException():
    '''    public static synchronized MXException toMXException(final Throwable throwable)
    '''
