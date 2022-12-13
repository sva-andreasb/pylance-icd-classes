def uniqueIndexedCollection():
    '''public static <K, C> IndexedCollection<K, C> uniqueIndexedCollection(final Collection<C> coll, final Transformer<C, K> keyTransformer)
    '''
def nonUniqueIndexedCollection():
    '''public static <K, C> IndexedCollection<K, C> nonUniqueIndexedCollection(final Collection<C> coll, final Transformer<C, K> keyTransformer)
    '''
def IndexedCollection():
    '''public IndexedCollection(final Collection<C> coll, final Transformer<C, K> keyTransformer, final MultiMap<K, C> map, final boolean uniqueIndex)
    '''
def add():
    '''public boolean add(final C object)
    '''
def addAll():
    '''public boolean addAll(final Collection<? extends C> coll)
    '''
def clear():
    '''public void clear()
    '''
def contains():
    '''public boolean contains(final Object object)
    '''
def containsAll():
    '''public boolean containsAll(final Collection<?> coll)
    '''
def get():
    '''public C get(final K key)
    '''
def values():
    '''public Collection<C> values(final K key)
    '''
def reindex():
    '''public void reindex()
    '''
def remove():
    '''public boolean remove(final Object object)
    '''
def removeAll():
    '''public boolean removeAll(final Collection<?> coll)
    '''
def retainAll():
    '''public boolean retainAll(final Collection<?> coll)
    '''
