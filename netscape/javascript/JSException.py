EXCEPTION_TYPE_EMPTY = "int  -1"
EXCEPTION_TYPE_VOID = "int  0"
EXCEPTION_TYPE_OBJECT = "int  1"
EXCEPTION_TYPE_FUNCTION = "int  2"
EXCEPTION_TYPE_STRING = "int  3"
EXCEPTION_TYPE_NUMBER = "int  4"
EXCEPTION_TYPE_BOOLEAN = "int  5"
EXCEPTION_TYPE_ERROR = "int  6"
def JSException():
    '''public JSException()
    public JSException(final String s)
    public JSException(final String s, final String filename, final int lineno, final String source, final int tokenIndex)
    public JSException(final int wrappedExceptionType, final Object wrappedException)
    '''
def getWrappedExceptionType():
    '''public int getWrappedExceptionType()
    '''
def getWrappedException():
    '''public Object getWrappedException()
    '''
