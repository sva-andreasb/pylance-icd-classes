def empty():
    '''public static <T> FluentIterable<T> empty()
    '''
def of():
    '''public static <T> FluentIterable<T> of(final T singleton)
    public static <T> FluentIterable<T> of(final T... elements)
    public static <T> FluentIterable<T> of(final Iterable<T> iterable)
    '''
def append():
    '''public FluentIterable<E> append(final E... elements)
    public FluentIterable<E> append(final Iterable<? extends E> other)
    '''
def collate():
    '''public FluentIterable<E> collate(final Iterable<? extends E> other)
    public FluentIterable<E> collate(final Iterable<? extends E> other, final Comparator<? super E> comparator)
    '''
def eval():
    '''public FluentIterable<E> eval()
    '''
def filter():
    '''public FluentIterable<E> filter(final Predicate<? super E> predicate)
    '''
def limit():
    '''public FluentIterable<E> limit(final long maxSize)
    '''
def loop():
    '''public FluentIterable<E> loop()
    '''
def reverse():
    '''public FluentIterable<E> reverse()
    '''
def skip():
    '''public FluentIterable<E> skip(final long elementsToSkip)
    '''
def transform():
    '''public <O> FluentIterable<O> transform(final Transformer<? super E, ? extends O> transformer)
    '''
def unique():
    '''public FluentIterable<E> unique()
    '''
def unmodifiable():
    '''public FluentIterable<E> unmodifiable()
    '''
def zip():
    '''public FluentIterable<E> zip(final Iterable<? extends E> other)
    public FluentIterable<E> zip(final Iterable<? extends E>... others)
    '''
def iterator():
    '''public Iterator<E> iterator()
    '''
def asEnumeration():
    '''public Enumeration<E> asEnumeration()
    '''
def allMatch():
    '''public boolean allMatch(final Predicate<? super E> predicate)
    '''
def anyMatch():
    '''public boolean anyMatch(final Predicate<? super E> predicate)
    '''
def isEmpty():
    '''public boolean isEmpty()
    '''
def contains():
    '''public boolean contains(final Object object)
    '''
def forEach():
    '''public void forEach(final Closure<? super E> closure)
    '''
def get():
    '''public E get(final int position)
    '''
def size():
    '''public int size()
    '''
def copyInto():
    '''public void copyInto(final Collection<? super E> collection)
    '''
def toArray():
    '''public E[] toArray(final Class<E> arrayClass)
    '''
def toList():
    '''public List<E> toList()
    '''
def toString():
    '''public String toString()
    '''
