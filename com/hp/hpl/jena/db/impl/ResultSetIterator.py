def ResultSetIterator():
'''public ResultSetIterator()
public ResultSetIterator(final ResultSet resultSet, final PreparedStatement sourceStatement, final SQLCache cache, final String opname)
public ResultSetIterator(final ResultSet resultSet, final PreparedStatement sourceStatement)
'''
pass
def reset():
'''public void reset(final ResultSet resultSet, final PreparedStatement sourceStatement, final SQLCache cache, final String opname)
public void reset(final ResultSet resultSet, final PreparedStatement sourceStatement)
'''
pass
def hasNext():
'''public boolean hasNext()
'''
pass
def removeNext():
'''public T removeNext()
'''
pass
def next():
'''public T next()
'''
pass
def remove():
'''public void remove()
'''
pass
def close():
'''public void close()
'''
pass
def getSingleton():
'''public Object getSingleton()
'''
pass
def andThen():
'''public <X extends T> ExtendedIterator<T> andThen(final Iterator<X> other)
'''
pass
def toSet():
'''public Set<T> toSet()
'''
pass
def toList():
'''public List<T> toList()
'''
pass
def filterKeep():
'''public ExtendedIterator<T> filterKeep(final Filter<T> f)
'''
pass
def filterDrop():
'''public ExtendedIterator<T> filterDrop(final Filter<T> f)
'''
pass
def accept():
'''public boolean accept(final T x)
'''
pass
def mapWith():
'''public <X> ExtendedIterator<X> mapWith(final Map1<T, X> map1)
'''
pass
