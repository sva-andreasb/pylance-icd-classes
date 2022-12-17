def ():
    '''returns BlockingArrayQueue\n\n
    ()\n
    (final int limit)\n
    (final int capacity, final int growBy)\n
    (final int capacity, final int growBy, final int limit)\n
    '''
def getCapacity():
    '''returns int\n\n
    getCapacity()\n
    '''
def getLimit():
    '''returns int\n\n
    getLimit()\n
    '''
def add():
    '''returns None\n\n
    add(final E e)\n
    add(final int index, final E e)\n
    '''
def element():
    '''returns E\n\n
    element()\n
    '''
def peek():
    '''returns E\n\n
    peek()\n
    '''
def offer():
    '''returns boolean\n\n
    offer(final E e)\n
    offer(final E o, final long timeout, final TimeUnit unit)\n
    '''
def poll():
    '''returns E\n\n
    poll()\n
    poll(final long time, final TimeUnit unit)\n
    '''
def take():
    '''returns E\n\n
    take()\n
    '''
def remove():
    '''returns E\n\n
    remove()\n
    remove(final int index)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def get():
    '''returns E\n\n
    get(final int index)\n
    '''
def set():
    '''returns E\n\n
    set(final int index, final E e)\n
    '''
def drainTo():
    '''returns int\n\n
    drainTo(final Collection<? super E> c)\n
    drainTo(final Collection<? super E> c, final int maxElements)\n
    '''
def put():
    '''returns None\n\n
    put(final E o)\n
    '''
def remainingCapacity():
    '''returns int\n\n
    remainingCapacity()\n
    '''
