def emptyCollection():
'''public static <T> Collection<T> emptyCollection()
'''
pass
def emptyIfNull():
'''public static <T> Collection<T> emptyIfNull(final Collection<T> collection)
'''
pass
def union():
'''public static <O> Collection<O> union(final Iterable<? extends O> a, final Iterable<? extends O> b)
'''
pass
def intersection():
'''public static <O> Collection<O> intersection(final Iterable<? extends O> a, final Iterable<? extends O> b)
'''
pass
def disjunction():
'''public static <O> Collection<O> disjunction(final Iterable<? extends O> a, final Iterable<? extends O> b)
'''
pass
def subtract():
'''public static <O> Collection<O> subtract(final Iterable<? extends O> a, final Iterable<? extends O> b)
public static <O> Collection<O> subtract(final Iterable<? extends O> a, final Iterable<? extends O> b, final Predicate<O> p)
'''
pass
def containsAll():
'''public static boolean containsAll(final Collection<?> coll1, final Collection<?> coll2)
'''
pass
def containsAny():
'''public static boolean containsAny(final Collection<?> coll1, final Collection<?> coll2)
'''
pass
def getCardinalityMap():
'''public static <O> Map<O, Integer> getCardinalityMap(final Iterable<? extends O> coll)
'''
pass
def isSubCollection():
'''public static boolean isSubCollection(final Collection<?> a, final Collection<?> b)
'''
pass
def isProperSubCollection():
'''public static boolean isProperSubCollection(final Collection<?> a, final Collection<?> b)
'''
pass
def isEqualCollection():
'''public static boolean isEqualCollection(final Collection<?> a, final Collection<?> b)
public static <E> boolean isEqualCollection(final Collection<? extends E> a, final Collection<? extends E> b, final Equator<? super E> equator)
'''
pass
def cardinality():
'''public static <O> int cardinality(final O obj, final Iterable<? super O> coll)
'''
pass
def find():
'''public static <T> T find(final Iterable<T> collection, final Predicate<? super T> predicate)
'''
pass
def filter():
'''public static <T> boolean filter(final Iterable<T> collection, final Predicate<? super T> predicate)
'''
pass
def filterInverse():
'''public static <T> boolean filterInverse(final Iterable<T> collection, final Predicate<? super T> predicate)
'''
pass
def transform():
'''public static <C> void transform(final Collection<C> collection, final Transformer<? super C, ? extends C> transformer)
public EquatorWrapper<E> transform(final E input)
public EquatorWrapper<E> transform(final E input)
'''
pass
def countMatches():
'''public static <C> int countMatches(final Iterable<C> input, final Predicate<? super C> predicate)
'''
pass
def exists():
'''public static <C> boolean exists(final Iterable<C> input, final Predicate<? super C> predicate)
'''
pass
def matchesAll():
'''public static <C> boolean matchesAll(final Iterable<C> input, final Predicate<? super C> predicate)
'''
pass
def select():
'''public static <O> Collection<O> select(final Iterable<? extends O> inputCollection, final Predicate<? super O> predicate)
'''
pass
def selectRejected():
'''public static <O> Collection<O> selectRejected(final Iterable<? extends O> inputCollection, final Predicate<? super O> predicate)
'''
pass
def collect():
'''public static <I, O> Collection<O> collect(final Iterable<I> inputCollection, final Transformer<? super I, ? extends O> transformer)
public static <I, O> Collection<O> collect(final Iterator<I> inputIterator, final Transformer<? super I, ? extends O> transformer)
'''
pass
def addIgnoreNull():
'''public static <T> boolean addIgnoreNull(final Collection<T> collection, final T object)
'''
pass
def addAll():
'''public static <C> boolean addAll(final Collection<C> collection, final Iterable<? extends C> iterable)
public static <C> boolean addAll(final Collection<C> collection, final Iterator<? extends C> iterator)
public static <C> boolean addAll(final Collection<C> collection, final Enumeration<? extends C> enumeration)
public static <C> boolean addAll(final Collection<C> collection, final C[] elements)
'''
pass
def get():
'''public static <T> T get(final Iterator<T> iterator, final int index)
public static <T> T get(final Iterable<T> iterable, final int index)
public static Object get(final Object object, final int index)
'''
pass
def size():
'''public static int size(final Object object)
'''
pass
def sizeIsEmpty():
'''public static boolean sizeIsEmpty(final Object object)
'''
pass
def isEmpty():
'''public static boolean isEmpty(final Collection<?> coll)
'''
pass
def isNotEmpty():
'''public static boolean isNotEmpty(final Collection<?> coll)
'''
pass
def reverseArray():
'''public static void reverseArray(final Object[] array)
'''
pass
def isFull():
'''public static boolean isFull(final Collection<?> coll)
'''
pass
def maxSize():
'''public static int maxSize(final Collection<?> coll)
'''
pass
def collate():
'''public static <O> List<O> collate(final Iterable<? extends O> a, final Iterable<? extends O> b, final Comparator<? super O> c)
public static <O> List<O> collate(final Iterable<? extends O> a, final Iterable<? extends O> b, final Comparator<? super O> c, final boolean includeDuplicates)
'''
pass
def permutations():
'''public static <E> Collection<List<E>> permutations(final Collection<E> collection)
'''
pass
def retainAll():
'''public static <C> Collection<C> retainAll(final Collection<C> collection, final Collection<?> retain)
public static <E> Collection<E> retainAll(final Iterable<E> collection, final Iterable<? extends E> retain, final Equator<? super E> equator)
'''
pass
def removeAll():
'''public static <E> Collection<E> removeAll(final Collection<E> collection, final Collection<?> remove)
public static <E> Collection<E> removeAll(final Iterable<E> collection, final Iterable<? extends E> remove, final Equator<? super E> equator)
'''
pass
def synchronizedCollection():
'''public static <C> Collection<C> synchronizedCollection(final Collection<C> collection)
'''
pass
def unmodifiableCollection():
'''public static <C> Collection<C> unmodifiableCollection(final Collection<? extends C> collection)
'''
pass
def predicatedCollection():
'''public static <C> Collection<C> predicatedCollection(final Collection<C> collection, final Predicate<? super C> predicate)
'''
pass
def transformingCollection():
'''public static <E> Collection<E> transformingCollection(final Collection<E> collection, final Transformer<? super E, ? extends E> transformer)
'''
pass
def extractSingleton():
'''public static <E> E extractSingleton(final Collection<E> collection)
'''
pass
def CardinalityHelper():
'''public CardinalityHelper(final Iterable<? extends O> a, final Iterable<? extends O> b)
'''
pass
def max():
'''public final int max(final Object obj)
'''
pass
def min():
'''public final int min(final Object obj)
'''
pass
def freqA():
'''public int freqA(final Object obj)
'''
pass
def freqB():
'''public int freqB(final Object obj)
'''
pass
def SetOperationCardinalityHelper():
'''public SetOperationCardinalityHelper(final Iterable<? extends O> a, final Iterable<? extends O> b)
'''
pass
def iterator():
'''public Iterator<O> iterator()
'''
pass
def setCardinality():
'''public void setCardinality(final O obj, final int count)
'''
pass
def list():
'''public Collection<O> list()
'''
pass
def EquatorWrapper():
'''public EquatorWrapper(final Equator<? super O> equator, final O object)
'''
pass
def getObject():
'''public O getObject()
'''
pass
def equals():
'''public boolean equals(final Object obj)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
