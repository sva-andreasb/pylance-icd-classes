INVALID_HANDLE_VALUE = "long  -1L"
def ():
    '''returns HANDLE\n\n
    (final Pointer pointer)\n
    '''
def toNative():
    '''returns Pointer\n\n
    toNative(final HANDLE value, final ToNativeContext context)\n
    '''
def fromNative():
    '''returns HANDLE\n\n
    fromNative(final Pointer nativeValue, final FromNativeContext context)\n
    '''
def nativeType():
    '''returns Class<Pointer>\n\n
    nativeType()\n
    '''
