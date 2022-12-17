def ():
    '''returns NativeMemoryManager\n\n
    (final NativeRuntime runtime)\n
    '''
def allocate():
    '''returns Pointer\n\n
    allocate(final int size)\n
    '''
def allocateDirect():
    '''returns Pointer\n\n
    allocateDirect(final int size)\n
    allocateDirect(final int size, final boolean clear)\n
    '''
def allocateTemporary():
    '''returns Pointer\n\n
    allocateTemporary(final int size)\n
    allocateTemporary(final int size, final boolean clear)\n
    '''
def newPointer():
    '''returns Pointer\n\n
    newPointer(final ByteBuffer buffer)\n
    newPointer(final long address)\n
    newPointer(final long address, final long size)\n
    '''
def newOpaquePointer():
    '''returns Pointer\n\n
    newOpaquePointer(final long address)\n
    '''
