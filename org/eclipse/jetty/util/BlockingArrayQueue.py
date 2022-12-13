def BlockingArrayQueue():
    '''    public BlockingArrayQueue()
    public BlockingArrayQueue(final int limit)
    public BlockingArrayQueue(final int capacity, final int growBy)
    public BlockingArrayQueue(final int capacity, final int growBy, final int limit)
    '''
def getCapacity():
    '''    public int getCapacity()
    '''
def getLimit():
    '''    public int getLimit()
    '''
def add():
    '''    public boolean add(final E e)
    public void add(final int index, final E e)
    '''
def element():
    '''    public E element()
    '''
def peek():
    '''    public E peek()
    '''
def offer():
    '''    public boolean offer(final E e)
    public boolean offer(final E o, final long timeout, final TimeUnit unit)
    '''
def poll():
    '''    public E poll()
    public E poll(final long time, final TimeUnit unit)
    '''
def take():
    '''    public E take()
    '''
def remove():
    '''    public E remove()
    public E remove(final int index)
    '''
def clear():
    '''    public void clear()
    '''
def isEmpty():
    '''    public boolean isEmpty()
    '''
def size():
    '''    public int size()
    '''
def get():
    '''    public E get(final int index)
    '''
def set():
    '''    public E set(final int index, final E e)
    '''
def drainTo():
    '''    public int drainTo(final Collection<? super E> c)
    public int drainTo(final Collection<? super E> c, final int maxElements)
    '''
def put():
    '''    public void put(final E o)
    '''
def remainingCapacity():
    '''    public int remainingCapacity()
    '''
