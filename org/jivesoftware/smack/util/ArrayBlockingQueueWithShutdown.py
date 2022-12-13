def ArrayBlockingQueueWithShutdown():
    '''    public ArrayBlockingQueueWithShutdown(final int capacity)
    public ArrayBlockingQueueWithShutdown(final int capacity, final boolean fair)
    '''
def shutdown():
    '''    public void shutdown()
    '''
def start():
    '''    public void start()
    '''
def isShutdown():
    '''    public boolean isShutdown()
    '''
def poll():
    '''    public E poll()
    public E poll(final long timeout, final TimeUnit unit)
    '''
def peek():
    '''    public E peek()
    '''
def offer():
    '''    public boolean offer(final E e)
    public boolean offer(final E e, final long timeout, final TimeUnit unit)
    '''
def put():
    '''    public void put(final E e)
    '''
def take():
    '''    public E take()
    '''
def remainingCapacity():
    '''    public int remainingCapacity()
    '''
def drainTo():
    '''    public int drainTo(final Collection<? super E> c)
    public int drainTo(final Collection<? super E> c, final int maxElements)
    '''
def size():
    '''    public int size()
    '''
def iterator():
    '''    public Iterator<E> iterator()
    '''
def hasNext():
    '''    public boolean hasNext()
    '''
def next():
    '''    public E next()
    '''
def remove():
    '''    public void remove()
    '''
