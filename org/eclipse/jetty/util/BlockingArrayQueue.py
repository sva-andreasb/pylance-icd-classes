def BlockingArrayQueue():
'''public BlockingArrayQueue()
public BlockingArrayQueue(final int limit)
public BlockingArrayQueue(final int capacity, final int growBy)
public BlockingArrayQueue(final int capacity, final int growBy, final int limit)
'''
pass
def getCapacity():
'''public int getCapacity()
'''
pass
def getLimit():
'''public int getLimit()
'''
pass
def add():
'''public boolean add(final E e)
public void add(final int index, final E e)
'''
pass
def element():
'''public E element()
'''
pass
def peek():
'''public E peek()
'''
pass
def offer():
'''public boolean offer(final E e)
public boolean offer(final E o, final long timeout, final TimeUnit unit)
'''
pass
def poll():
'''public E poll()
public E poll(final long time, final TimeUnit unit)
'''
pass
def take():
'''public E take()
'''
pass
def remove():
'''public E remove()
public E remove(final int index)
'''
pass
def clear():
'''public void clear()
'''
pass
def isEmpty():
'''public boolean isEmpty()
'''
pass
def size():
'''public int size()
'''
pass
def get():
'''public E get(final int index)
'''
pass
def set():
'''public E set(final int index, final E e)
'''
pass
def drainTo():
'''public int drainTo(final Collection<? super E> c)
public int drainTo(final Collection<? super E> c, final int maxElements)
'''
pass
def put():
'''public void put(final E o)
'''
pass
def remainingCapacity():
'''public int remainingCapacity()
'''
pass
