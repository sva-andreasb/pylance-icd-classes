DISPATCH_METHOD = "int  1"
DISPATCH_PROPERTYGET = "int  2"
DISPATCH_PROPERTYPUT = "int  4"
DISPATCH_PROPERTYPUTREF = "int  8"
DISPID_OFFSET = "int  10"
def ():
    '''returns JavaClass\n\n
    (final Class wrappedClass)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getMethod():
    '''returns Method\n\n
    getMethod(final int n)\n
    '''
def getMethod1():
    '''returns Method\n\n
    getMethod1(final int n, final Object[] array)\n
    '''
def getField():
    '''returns Field\n\n
    getField(final int n)\n
    '''
def getDispatcher():
    '''returns Dispatcher\n\n
    getDispatcher(final int n, final int n2, final Object[] array)\n
    '''
