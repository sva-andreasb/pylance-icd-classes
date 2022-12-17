def ():
    '''returns ArrayBlockingQueueWithShutdown\n\n
    (final int capacity)\n
    (final int capacity, final boolean fair)\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def start():
    '''returns None\n\n
    start()\n
    '''
def isShutdown():
    '''returns boolean\n\n
    isShutdown()\n
    '''
def poll():
    '''returns E\n\n
    poll()\n
    poll(final long timeout, final TimeUnit unit)\n
    '''
def peek():
    '''returns E\n\n
    peek()\n
    '''
def offer():
    '''returns boolean\n\n
    offer(final E e)\n
    offer(final E e, final long timeout, final TimeUnit unit)\n
    '''
def put():
    '''returns None\n\n
    put(final E e)\n
    '''
def take():
    '''returns E\n\n
    take()\n
    '''
def remainingCapacity():
    '''returns int\n\n
    remainingCapacity()\n
    '''
def drainTo():
    '''returns int\n\n
    drainTo(final Collection<? super E> c)\n
    drainTo(final Collection<? super E> c, final int maxElements)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def iterator():
    '''returns Iterator<E>\n\n
    iterator()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns E\n\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
