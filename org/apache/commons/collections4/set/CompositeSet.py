def CompositeSet():
    '''public CompositeSet()
    public CompositeSet(final Set<E> set)
    public CompositeSet(final Set<E>... sets)
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
    '''public void setMutator(final SetMutator<E> mutator)
    '''
def addComposited():
    '''public synchronized void addComposited(final Set<E> set)
    public void addComposited(final Set<E> set1, final Set<E> set2)
    public void addComposited(final Set<E>... sets)
    '''
def removeComposited():
    '''public void removeComposited(final Set<E> set)
    '''
def toSet():
    '''public Set<E> toSet()
    '''
def getSets():
    '''public List<Set<E>> getSets()
    '''
def equals():
    '''public boolean equals(final Object obj)
    '''
def hashCode():
    '''public int hashCode()
    '''
