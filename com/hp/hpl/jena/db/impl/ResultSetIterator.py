def ():
    '''returns ResultSetIterator\n\n
    ()\n
    (final ResultSet resultSet, final PreparedStatement sourceStatement, final SQLCache cache, final String opname)\n
    (final ResultSet resultSet, final PreparedStatement sourceStatement)\n
    '''
def reset():
    '''returns None\n\n
    reset(final ResultSet resultSet, final PreparedStatement sourceStatement, final SQLCache cache, final String opname)\n
    reset(final ResultSet resultSet, final PreparedStatement sourceStatement)\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def removeNext():
    '''returns T\n\n
    removeNext()\n
    '''
def next():
    '''returns T\n\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getSingleton():
    '''returns Object\n\n
    getSingleton()\n
    '''
def toSet():
    '''returns Set<T>\n\n
    toSet()\n
    '''
def toList():
    '''returns List<T>\n\n
    toList()\n
    '''
def filterKeep():
    '''returns ExtendedIterator<T>\n\n
    filterKeep(final Filter<T> f)\n
    '''
def filterDrop():
    '''returns ExtendedIterator<T>\n\n
    filterDrop(final Filter<T> f)\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final T x)\n
    '''
