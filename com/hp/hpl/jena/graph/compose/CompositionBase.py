def reject():
    '''    public static <T> Filter<T> reject(final ClosableIterator<? extends T> i)
    '''
def accept():
    '''    public boolean accept(final T o)
    public boolean accept(final Triple x)
    public boolean accept(final Triple x)
    public boolean accept(final T x)
    public boolean accept(final Triple x)
    '''
def butNot():
    '''    public static <T> ClosableIterator<T> butNot(final ClosableIterator<T> a, final ClosableIterator<? extends T> b)
    '''
def recording():
    '''    public static <T> ExtendedIterator<T> recording(final ClosableIterator<T> i, final Set<T> seen)
    '''
def remove():
    '''    public void remove()
    '''
def hasNext():
    '''    public boolean hasNext()
    '''
def next():
    '''    public T next()
    '''
def close():
    '''    public void close()
    '''
def rejecting():
    '''    public static ExtendedIterator<Triple> rejecting(final ExtendedIterator<Triple> i, final Set<Triple> seen)
    public static ExtendedIterator<Triple> rejecting(final ExtendedIterator<Triple> i, final Graph seen)
    '''
def ifIn():
    '''    public static <T> Filter<T> ifIn(final ClosableIterator<T> i)
    public static Filter<Triple> ifIn(final Graph g)
    '''
