def reject():
'''public static <T> Filter<T> reject(final ClosableIterator<? extends T> i)
'''
pass
def accept():
'''public boolean accept(final T o)
public boolean accept(final Triple x)
public boolean accept(final Triple x)
public boolean accept(final T x)
public boolean accept(final Triple x)
'''
pass
def butNot():
'''public static <T> ClosableIterator<T> butNot(final ClosableIterator<T> a, final ClosableIterator<? extends T> b)
'''
pass
def recording():
'''public static <T> ExtendedIterator<T> recording(final ClosableIterator<T> i, final Set<T> seen)
'''
pass
def remove():
'''public void remove()
'''
pass
def hasNext():
'''public boolean hasNext()
'''
pass
def next():
'''public T next()
'''
pass
def close():
'''public void close()
'''
pass
def rejecting():
'''public static ExtendedIterator<Triple> rejecting(final ExtendedIterator<Triple> i, final Set<Triple> seen)
public static ExtendedIterator<Triple> rejecting(final ExtendedIterator<Triple> i, final Graph seen)
'''
pass
def ifIn():
'''public static <T> Filter<T> ifIn(final ClosableIterator<T> i)
public static Filter<Triple> ifIn(final Graph g)
'''
pass
