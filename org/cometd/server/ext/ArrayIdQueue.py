def ():
    '''returns ArrayIdQueue\n\n
    ()\n
    (final int capacity)\n
    (final int initCapacity, final int growBy)\n
    (final int initCapacity, final int growBy, final Object lock)\n
    '''
def getCurrentId():
    '''returns int\n\n
    getCurrentId()\n
    '''
def setCurrentId():
    '''returns None\n\n
    setCurrentId(final int currentId)\n
    '''
def incrementCurrentId():
    '''returns None\n\n
    incrementCurrentId()\n
    '''
def add():
    '''returns None\n\n
    add(final E e)\n
    add(final int index, final E element)\n
    '''
def addUnsafe():
    '''returns None\n\n
    addUnsafe(final E e)\n
    '''
def offer():
    '''returns boolean\n\n
    offer(final E e)\n
    '''
def getAssociatedId():
    '''returns int\n\n
    getAssociatedId(final int index)\n
    '''
def getAssociatedIdUnsafe():
    '''returns int\n\n
    getAssociatedIdUnsafe(final int index)\n
    '''
def remove():
    '''returns E\n\n
    remove(final int index)\n
    '''
def set():
    '''returns E\n\n
    set(final int index, final E element)\n
    '''
