def emptyIterable():
    '''public static <E> Iterable<E> emptyIterable()
    '''
def chainedIterable():
    '''public static <E> Iterable<E> chainedIterable(final Iterable<? extends E> a, final Iterable<? extends E> b)
    public static <E> Iterable<E> chainedIterable(final Iterable<? extends E> a, final Iterable<? extends E> b, final Iterable<? extends E> c)
    public static <E> Iterable<E> chainedIterable(final Iterable<? extends E> a, final Iterable<? extends E> b, final Iterable<? extends E> c, final Iterable<? extends E> d)
    public static <E> Iterable<E> chainedIterable(final Iterable<? extends E>... iterables)
    '''
def iterator():
    '''public Iterator<E> iterator()
    public Iterator<E> iterator()
    public Iterator<E> iterator()
    public Iterator<E> iterator()
    public Iterator<E> iterator()
    public Iterator<E> iterator()
    public Iterator<E> iterator()
    public Iterator<E> iterator()
    public Iterator<O> iterator()
    public Iterator<E> iterator()
    public Iterator<E> iterator()
    public Iterator<E> iterator()
    public Iterator<Object> iterator()
    public Iterator<E> iterator()
    '''
def collatedIterable():
    '''public static <E> Iterable<E> collatedIterable(final Iterable<? extends E> a, final Iterable<? extends E> b)
    public static <E> Iterable<E> collatedIterable(final Comparator<? super E> comparator, final Iterable<? extends E> a, final Iterable<? extends E> b)
    '''
def filteredIterable():
    '''public static <E> Iterable<E> filteredIterable(final Iterable<E> iterable, final Predicate<? super E> predicate)
    '''
def boundedIterable():
    '''public static <E> Iterable<E> boundedIterable(final Iterable<E> iterable, final long maxSize)
    '''
def loopingIterable():
    '''public static <E> Iterable<E> loopingIterable(final Iterable<E> iterable)
    '''
def reversedIterable():
    '''public static <E> Iterable<E> reversedIterable(final Iterable<E> iterable)
    '''
def skippingIterable():
    '''public static <E> Iterable<E> skippingIterable(final Iterable<E> iterable, final long elementsToSkip)
    '''
def transformedIterable():
    '''public static <I, O> Iterable<O> transformedIterable(final Iterable<I> iterable, final Transformer<? super I, ? extends O> transformer)
    '''
def uniqueIterable():
    '''public static <E> Iterable<E> uniqueIterable(final Iterable<E> iterable)
    '''
def unmodifiableIterable():
    '''public static <E> Iterable<E> unmodifiableIterable(final Iterable<E> iterable)
    '''
def zippingIterable():
    '''public static <E> Iterable<E> zippingIterable(final Iterable<? extends E> a, final Iterable<? extends E> b)
    public static <E> Iterable<E> zippingIterable(final Iterable<? extends E> first, final Iterable<? extends E>... others)
    '''
def emptyIfNull():
    '''public static <E> Iterable<E> emptyIfNull(final Iterable<E> iterable)
    '''
def forEach():
    '''public static <E> void forEach(final Iterable<E> iterable, final Closure<? super E> closure)
    '''
def forEachButLast():
    '''public static <E> E forEachButLast(final Iterable<E> iterable, final Closure<? super E> closure)
    '''
def find():
    '''public static <E> E find(final Iterable<E> iterable, final Predicate<? super E> predicate)
    '''
def indexOf():
    '''public static <E> int indexOf(final Iterable<E> iterable, final Predicate<? super E> predicate)
    '''
def matchesAll():
    '''public static <E> boolean matchesAll(final Iterable<E> iterable, final Predicate<? super E> predicate)
    '''
def matchesAny():
    '''public static <E> boolean matchesAny(final Iterable<E> iterable, final Predicate<? super E> predicate)
    '''
def countMatches():
    '''public static <E> long countMatches(final Iterable<E> input, final Predicate<? super E> predicate)
    '''
def isEmpty():
    '''public static boolean isEmpty(final Iterable<?> iterable)
    '''
def contains():
    '''public static <E> boolean contains(final Iterable<E> iterable, final Object object)
    public static <E> boolean contains(final Iterable<? extends E> iterable, final E object, final Equator<? super E> equator)
    '''
def frequency():
    '''public static <E, T extends E> int frequency(final Iterable<E> iterable, final T obj)
    '''
def get():
    '''public static <T> T get(final Iterable<T> iterable, final int index)
    '''
def size():
    '''public static int size(final Iterable<?> iterable)
    '''
def partition():
    '''public static <O> List<List<O>> partition(final Iterable<? extends O> iterable, final Predicate<? super O> predicate)
    public static <O> List<List<O>> partition(final Iterable<? extends O> iterable, final Predicate<? super O>... predicates)
    public static <O, R extends Collection<O>> List<R> partition(final Iterable<? extends O> iterable, final Factory<R> partitionFactory, final Predicate<? super O>... predicates)
    '''
def toList():
    '''public static <E> List<E> toList(final Iterable<E> iterable)
    '''
def toString():
    '''public static <E> String toString(final Iterable<E> iterable)
    public static <E> String toString(final Iterable<E> iterable, final Transformer<? super E, String> transformer)
    public static <E> String toString(final Iterable<E> iterable, final Transformer<? super E, String> transformer, final String delimiter, final String prefix, final String suffix)
    '''
def UnmodifiableIterable():
    '''public UnmodifiableIterable(final Iterable<E> iterable)
    '''
