def emptyIterator():
'''public static <E> ResettableIterator<E> emptyIterator()
'''
pass
def emptyListIterator():
'''public static <E> ResettableListIterator<E> emptyListIterator()
'''
pass
def emptyOrderedIterator():
'''public static <E> OrderedIterator<E> emptyOrderedIterator()
'''
pass
def emptyMapIterator():
'''public static <K, V> MapIterator<K, V> emptyMapIterator()
'''
pass
def emptyOrderedMapIterator():
'''public static <K, V> OrderedMapIterator<K, V> emptyOrderedMapIterator()
'''
pass
def singletonIterator():
'''public static <E> ResettableIterator<E> singletonIterator(final E object)
'''
pass
def singletonListIterator():
'''public static <E> ListIterator<E> singletonListIterator(final E object)
'''
pass
def arrayIterator():
'''public static <E> ResettableIterator<E> arrayIterator(final E... array)
public static <E> ResettableIterator<E> arrayIterator(final Object array)
public static <E> ResettableIterator<E> arrayIterator(final E[] array, final int start)
public static <E> ResettableIterator<E> arrayIterator(final Object array, final int start)
public static <E> ResettableIterator<E> arrayIterator(final E[] array, final int start, final int end)
public static <E> ResettableIterator<E> arrayIterator(final Object array, final int start, final int end)
'''
pass
def arrayListIterator():
'''public static <E> ResettableListIterator<E> arrayListIterator(final E... array)
public static <E> ResettableListIterator<E> arrayListIterator(final Object array)
public static <E> ResettableListIterator<E> arrayListIterator(final E[] array, final int start)
public static <E> ResettableListIterator<E> arrayListIterator(final Object array, final int start)
public static <E> ResettableListIterator<E> arrayListIterator(final E[] array, final int start, final int end)
public static <E> ResettableListIterator<E> arrayListIterator(final Object array, final int start, final int end)
'''
pass
def boundedIterator():
'''public static <E> BoundedIterator<E> boundedIterator(final Iterator<? extends E> iterator, final long max)
public static <E> BoundedIterator<E> boundedIterator(final Iterator<? extends E> iterator, final long offset, final long max)
'''
pass
def unmodifiableIterator():
'''public static <E> Iterator<E> unmodifiableIterator(final Iterator<E> iterator)
'''
pass
def unmodifiableListIterator():
'''public static <E> ListIterator<E> unmodifiableListIterator(final ListIterator<E> listIterator)
'''
pass
def unmodifiableMapIterator():
'''public static <K, V> MapIterator<K, V> unmodifiableMapIterator(final MapIterator<K, V> mapIterator)
'''
pass
def chainedIterator():
'''public static <E> Iterator<E> chainedIterator(final Iterator<? extends E> iterator1, final Iterator<? extends E> iterator2)
public static <E> Iterator<E> chainedIterator(final Iterator<? extends E>... iterators)
public static <E> Iterator<E> chainedIterator(final Collection<Iterator<? extends E>> iterators)
'''
pass
def collatedIterator():
'''public static <E> Iterator<E> collatedIterator(final Comparator<? super E> comparator, final Iterator<? extends E> iterator1, final Iterator<? extends E> iterator2)
public static <E> Iterator<E> collatedIterator(final Comparator<? super E> comparator, final Iterator<? extends E>... iterators)
public static <E> Iterator<E> collatedIterator(final Comparator<? super E> comparator, final Collection<Iterator<? extends E>> iterators)
'''
pass
def objectGraphIterator():
'''public static <E> Iterator<E> objectGraphIterator(final E root, final Transformer<? super E, ? extends E> transformer)
'''
pass
def transformedIterator():
'''public static <I, O> Iterator<O> transformedIterator(final Iterator<? extends I> iterator, final Transformer<? super I, ? extends O> transform)
'''
pass
def filteredIterator():
'''public static <E> Iterator<E> filteredIterator(final Iterator<? extends E> iterator, final Predicate<? super E> predicate)
'''
pass
def filteredListIterator():
'''public static <E> ListIterator<E> filteredListIterator(final ListIterator<? extends E> listIterator, final Predicate<? super E> predicate)
'''
pass
def loopingIterator():
'''public static <E> ResettableIterator<E> loopingIterator(final Collection<? extends E> coll)
'''
pass
def loopingListIterator():
'''public static <E> ResettableListIterator<E> loopingListIterator(final List<E> list)
'''
pass
def nodeListIterator():
'''public static NodeListIterator nodeListIterator(final NodeList nodeList)
public static NodeListIterator nodeListIterator(final Node node)
'''
pass
def peekingIterator():
'''public static <E> Iterator<E> peekingIterator(final Iterator<? extends E> iterator)
'''
pass
def pushbackIterator():
'''public static <E> Iterator<E> pushbackIterator(final Iterator<? extends E> iterator)
'''
pass
def skippingIterator():
'''public static <E> SkippingIterator<E> skippingIterator(final Iterator<E> iterator, final long offset)
'''
pass
def zippingIterator():
'''public static <E> ZippingIterator<E> zippingIterator(final Iterator<? extends E> a, final Iterator<? extends E> b)
public static <E> ZippingIterator<E> zippingIterator(final Iterator<? extends E> a, final Iterator<? extends E> b, final Iterator<? extends E> c)
public static <E> ZippingIterator<E> zippingIterator(final Iterator<? extends E>... iterators)
'''
pass
def asIterator():
'''public static <E> Iterator<E> asIterator(final Enumeration<? extends E> enumeration)
public static <E> Iterator<E> asIterator(final Enumeration<? extends E> enumeration, final Collection<? super E> removeCollection)
'''
pass
def asEnumeration():
'''public static <E> Enumeration<E> asEnumeration(final Iterator<? extends E> iterator)
'''
pass
def asIterable():
'''public static <E> Iterable<E> asIterable(final Iterator<? extends E> iterator)
'''
pass
def asMultipleUseIterable():
'''public static <E> Iterable<E> asMultipleUseIterable(final Iterator<? extends E> iterator)
'''
pass
def toListIterator():
'''public static <E> ListIterator<E> toListIterator(final Iterator<? extends E> iterator)
'''
pass
def toArray():
'''public static Object[] toArray(final Iterator<?> iterator)
public static <E> E[] toArray(final Iterator<? extends E> iterator, final Class<E> arrayClass)
'''
pass
def toList():
'''public static <E> List<E> toList(final Iterator<? extends E> iterator)
public static <E> List<E> toList(final Iterator<? extends E> iterator, final int estimatedSize)
'''
pass
def forEach():
'''public static <E> void forEach(final Iterator<E> iterator, final Closure<? super E> closure)
'''
pass
def forEachButLast():
'''public static <E> E forEachButLast(final Iterator<E> iterator, final Closure<? super E> closure)
'''
pass
def find():
'''public static <E> E find(final Iterator<E> iterator, final Predicate<? super E> predicate)
'''
pass
def indexOf():
'''public static <E> int indexOf(final Iterator<E> iterator, final Predicate<? super E> predicate)
'''
pass
def matchesAny():
'''public static <E> boolean matchesAny(final Iterator<E> iterator, final Predicate<? super E> predicate)
'''
pass
def matchesAll():
'''public static <E> boolean matchesAll(final Iterator<E> iterator, final Predicate<? super E> predicate)
'''
pass
def isEmpty():
'''public static boolean isEmpty(final Iterator<?> iterator)
'''
pass
def contains():
'''public static <E> boolean contains(final Iterator<E> iterator, final Object object)
'''
pass
def get():
'''public static <E> E get(final Iterator<E> iterator, final int index)
'''
pass
def size():
'''public static int size(final Iterator<?> iterator)
'''
pass
def toString():
'''public static <E> String toString(final Iterator<E> iterator)
public static <E> String toString(final Iterator<E> iterator, final Transformer<? super E, String> transformer)
public static <E> String toString(final Iterator<E> iterator, final Transformer<? super E, String> transformer, final String delimiter, final String prefix, final String suffix)
'''
pass
