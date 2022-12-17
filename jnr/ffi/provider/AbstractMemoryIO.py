def indexOf():
    '''returns int\n\n
    indexOf(final long offset, final byte value)\n
    '''
def getAddress():
    '''returns long\n\n
    getAddress(final long offset)\n
    '''
def putAddress():
    '''returns None\n\n
    putAddress(final long offset, final long value)\n
    putAddress(final long offset, final Address value)\n
    '''
def checkBounds():
    '''returns None\n\n
    checkBounds(final long offset, final long size)\n
    '''
def putNativeLong():
    '''returns None\n\n
    putNativeLong(final long offset, final long value)\n
    '''
def getLong():
    '''returns long\n\n
    getLong(final long offset)\n
    '''
def putLong():
    '''returns None\n\n
    putLong(final long offset, final long value)\n
    '''
def putInt():
    '''returns None\n\n
    putInt(final Type type, final long offset, final long value)\n
    '''
def getInt():
    '''returns long\n\n
    getInt(final Type type, final long offset)\n
    '''
def slice():
    '''returns AbstractMemoryIO\n\n
    slice(final long offset)\n
    slice(final long offset, final long size)\n
    '''
def transferTo():
    '''returns None\n\n
    transferTo(final long offset, final Pointer other, final long otherOffset, final long count)\n
    '''
def transferFrom():
    '''returns None\n\n
    transferFrom(final long offset, final Pointer other, final long otherOffset, final long count)\n
    '''
