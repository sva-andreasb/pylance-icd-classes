def ():
    '''returns LazyIterator\n\n
    ()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns T\n\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
def andThen():
    '''returns ExtendedIterator<T>\n\n
    andThen(final ClosableIterator<? extends T> other)\n
    '''
def filterKeep():
    '''returns ExtendedIterator<T>\n\n
    filterKeep(final Filter<T> f)\n
    '''
def filterDrop():
    '''returns ExtendedIterator<T>\n\n
    filterDrop(final Filter<T> f)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
