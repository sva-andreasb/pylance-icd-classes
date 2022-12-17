def create():
    '''returns BlockingQueue<E>\n\n
    create(final int capacity)\n
    '''
def drainTo():
    '''returns int\n\n
    drainTo(final Collection<? super E> c)\n
    drainTo(final Collection<? super E> c, final int maxElements)\n
    '''
def offer():
    '''returns boolean\n\n
    offer(final E e, final long timeout, final TimeUnit unit)\n
    offer(final E e)\n
    '''
def poll():
    '''returns E\n\n
    poll(final long timeout, final TimeUnit unit)\n
    '''
def put():
    '''returns None\n\n
    put(final E e)\n
    '''
def remainingCapacity():
    '''returns int\n\n
    remainingCapacity()\n
    '''
def take():
    '''returns E\n\n
    take()\n
    '''
