def ():
    '''returns CollatingIterator\n\n
    ()\n
    (final Comparator<? super E> comp)\n
    (final Comparator<? super E> comp, final int initIterCapacity)\n
    (final Comparator<? super E> comp, final Iterator<? extends E> a, final Iterator<? extends E> b)\n
    (final Comparator<? super E> comp, final Iterator<? extends E>[] iterators)\n
    (final Comparator<? super E> comp, final Collection<Iterator<? extends E>> iterators)\n
    '''
def addIterator():
    '''returns None\n\n
    addIterator(final Iterator<? extends E> iterator)\n
    '''
def setIterator():
    '''returns None\n\n
    setIterator(final int index, final Iterator<? extends E> iterator)\n
    '''
def setComparator():
    '''returns None\n\n
    setComparator(final Comparator<? super E> comp)\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns E\n\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
def getIteratorIndex():
    '''returns int\n\n
    getIteratorIndex()\n
    '''
