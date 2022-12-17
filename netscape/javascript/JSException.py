EXCEPTION_TYPE_EMPTY = "int  -1"
EXCEPTION_TYPE_VOID = "int  0"
EXCEPTION_TYPE_OBJECT = "int  1"
EXCEPTION_TYPE_FUNCTION = "int  2"
EXCEPTION_TYPE_STRING = "int  3"
EXCEPTION_TYPE_NUMBER = "int  4"
EXCEPTION_TYPE_BOOLEAN = "int  5"
EXCEPTION_TYPE_ERROR = "int  6"
def ():
    '''returns JSException\n\n
    ()\n
    (final String s)\n
    (final String s, final String filename, final int lineno, final String source, final int tokenIndex)\n
    (final int wrappedExceptionType, final Object wrappedException)\n
    '''
def getWrappedExceptionType():
    '''returns int\n\n
    getWrappedExceptionType()\n
    '''
def getWrappedException():
    '''returns Object\n\n
    getWrappedException()\n
    '''
