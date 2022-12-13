def CompositeCollection():
    '''public CompositeCollection()
    public CompositeCollection(final Collection<E> compositeCollection)
    public CompositeCollection(final Collection<E> compositeCollection1, final Collection<E> compositeCollection2)
    public CompositeCollection(final Collection<E>... compositeCollections)
    '''
def size():
    '''public int size()
    '''
def isEmpty():
    '''public boolean isEmpty()
    '''
def contains():
    '''public boolean contains(final Object obj)
    '''
def iterator():
    '''public Iterator<E> iterator()
    '''
def toArray():
    '''public Object[] toArray()
    public <T> T[] toArray(final T[] array)
    '''
def add():
    '''public boolean add(final E obj)
    '''
def remove():
    '''public boolean remove(final Object obj)
    '''
def containsAll():
    '''public boolean containsAll(final Collection<?> coll)
    '''
def addAll():
    '''public boolean addAll(final Collection<? extends E> coll)
    '''
def removeAll():
    '''public boolean removeAll(final Collection<?> coll)
    '''
def retainAll():
    '''public boolean retainAll(final Collection<?> coll)
    '''
def clear():
    '''public void clear()
    '''
def setMutator():
    '''public void setMutator(final CollectionMutator<E> mutator)
    '''
def addComposited():
    '''public void addComposited(final Collection<E> compositeCollection)
    public void addComposited(final Collection<E> compositeCollection1, final Collection<E> compositeCollection2)
    public void addComposited(final Collection<E>... compositeCollections)
    '''
def removeComposited():
    '''public void removeComposited(final Collection<E> coll)
    '''
def toCollection():
    '''public Collection<E> toCollection()
    '''
def getCollections():
    '''public List<Collection<E>> getCollections()
    '''
