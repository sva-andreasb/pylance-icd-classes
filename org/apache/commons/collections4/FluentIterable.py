def empty():
'''public static <T> FluentIterable<T> empty()
'''
pass
def of():
'''public static <T> FluentIterable<T> of(final T singleton)
public static <T> FluentIterable<T> of(final T... elements)
public static <T> FluentIterable<T> of(final Iterable<T> iterable)
'''
pass
def append():
'''public FluentIterable<E> append(final E... elements)
public FluentIterable<E> append(final Iterable<? extends E> other)
'''
pass
def collate():
'''public FluentIterable<E> collate(final Iterable<? extends E> other)
public FluentIterable<E> collate(final Iterable<? extends E> other, final Comparator<? super E> comparator)
'''
pass
def eval():
'''public FluentIterable<E> eval()
'''
pass
def filter():
'''public FluentIterable<E> filter(final Predicate<? super E> predicate)
'''
pass
def limit():
'''public FluentIterable<E> limit(final long maxSize)
'''
pass
def loop():
'''public FluentIterable<E> loop()
'''
pass
def reverse():
'''public FluentIterable<E> reverse()
'''
pass
def skip():
'''public FluentIterable<E> skip(final long elementsToSkip)
'''
pass
def transform():
'''public <O> FluentIterable<O> transform(final Transformer<? super E, ? extends O> transformer)
'''
pass
def unique():
'''public FluentIterable<E> unique()
'''
pass
def unmodifiable():
'''public FluentIterable<E> unmodifiable()
'''
pass
def zip():
'''public FluentIterable<E> zip(final Iterable<? extends E> other)
public FluentIterable<E> zip(final Iterable<? extends E>... others)
'''
pass
def iterator():
'''public Iterator<E> iterator()
'''
pass
def asEnumeration():
'''public Enumeration<E> asEnumeration()
'''
pass
def allMatch():
'''public boolean allMatch(final Predicate<? super E> predicate)
'''
pass
def anyMatch():
'''public boolean anyMatch(final Predicate<? super E> predicate)
'''
pass
def isEmpty():
'''public boolean isEmpty()
'''
pass
def contains():
'''public boolean contains(final Object object)
'''
pass
def forEach():
'''public void forEach(final Closure<? super E> closure)
'''
pass
def get():
'''public E get(final int position)
'''
pass
def size():
'''public int size()
'''
pass
def copyInto():
'''public void copyInto(final Collection<? super E> collection)
'''
pass
def toArray():
'''public E[] toArray(final Class<E> arrayClass)
'''
pass
def toList():
'''public List<E> toList()
'''
pass
def toString():
'''public String toString()
'''
pass
