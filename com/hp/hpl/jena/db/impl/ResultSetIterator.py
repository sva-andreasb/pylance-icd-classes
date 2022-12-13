def ResultSetIterator():
    '''public ResultSetIterator()
    public ResultSetIterator(final ResultSet resultSet, final PreparedStatement sourceStatement, final SQLCache cache, final String opname)
    public ResultSetIterator(final ResultSet resultSet, final PreparedStatement sourceStatement)
    '''
def reset():
    '''public void reset(final ResultSet resultSet, final PreparedStatement sourceStatement, final SQLCache cache, final String opname)
    public void reset(final ResultSet resultSet, final PreparedStatement sourceStatement)
    '''
def hasNext():
    '''public boolean hasNext()
    '''
def removeNext():
    '''public T removeNext()
    '''
def next():
    '''public T next()
    '''
def remove():
    '''public void remove()
    '''
def close():
    '''public void close()
    '''
def getSingleton():
    '''public Object getSingleton()
    '''
def andThen():
    '''public <X extends T> ExtendedIterator<T> andThen(final Iterator<X> other)
    '''
def toSet():
    '''public Set<T> toSet()
    '''
def toList():
    '''public List<T> toList()
    '''
def filterKeep():
    '''public ExtendedIterator<T> filterKeep(final Filter<T> f)
    '''
def filterDrop():
    '''public ExtendedIterator<T> filterDrop(final Filter<T> f)
    '''
def accept():
    '''public boolean accept(final T x)
    '''
def mapWith():
    '''public <X> ExtendedIterator<X> mapWith(final Map1<T, X> map1)
    '''
