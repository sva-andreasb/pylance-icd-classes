def emptyIfNull():
    '''public static <T> List<T> emptyIfNull(final List<T> list)
    '''
def defaultIfNull():
    '''public static <T> List<T> defaultIfNull(final List<T> list, final List<T> defaultList)
    '''
def intersection():
    '''public static <E> List<E> intersection(final List<? extends E> list1, final List<? extends E> list2)
    '''
def subtract():
    '''public static <E> List<E> subtract(final List<E> list1, final List<? extends E> list2)
    '''
def sum():
    '''public static <E> List<E> sum(final List<? extends E> list1, final List<? extends E> list2)
    '''
def union():
    '''public static <E> List<E> union(final List<? extends E> list1, final List<? extends E> list2)
    '''
def select():
    '''public static <E> List<E> select(final Collection<? extends E> inputCollection, final Predicate<? super E> predicate)
    '''
def selectRejected():
    '''public static <E> List<E> selectRejected(final Collection<? extends E> inputCollection, final Predicate<? super E> predicate)
    '''
def isEqualList():
    '''public static boolean isEqualList(final Collection<?> list1, final Collection<?> list2)
    '''
def hashCodeForList():
    '''public static int hashCodeForList(final Collection<?> list)
    '''
def retainAll():
    '''public static <E> List<E> retainAll(final Collection<E> collection, final Collection<?> retain)
    '''
def removeAll():
    '''public static <E> List<E> removeAll(final Collection<E> collection, final Collection<?> remove)
    '''
def synchronizedList():
    '''public static <E> List<E> synchronizedList(final List<E> list)
    '''
def unmodifiableList():
    '''public static <E> List<E> unmodifiableList(final List<? extends E> list)
    '''
def predicatedList():
    '''public static <E> List<E> predicatedList(final List<E> list, final Predicate<E> predicate)
    '''
def transformedList():
    '''public static <E> List<E> transformedList(final List<E> list, final Transformer<? super E, ? extends E> transformer)
    '''
def lazyList():
    '''public static <E> List<E> lazyList(final List<E> list, final Factory<? extends E> factory)
    '''
def fixedSizeList():
    '''public static <E> List<E> fixedSizeList(final List<E> list)
    '''
def indexOf():
    '''public static <E> int indexOf(final List<E> list, final Predicate<E> predicate)
    '''
def longestCommonSubsequence():
    '''public static <E> List<E> longestCommonSubsequence(final List<E> a, final List<E> b)
    public static <E> List<E> longestCommonSubsequence(final List<E> a, final List<E> b, final Equator<? super E> equator)
    public static String longestCommonSubsequence(final CharSequence a, final CharSequence b)
    '''
def partition():
    '''public static <T> List<List<T>> partition(final List<T> list, final int size)
    '''
def LcsVisitor():
    '''public LcsVisitor()
    '''
def visitInsertCommand():
    '''public void visitInsertCommand(final E object)
    '''
def visitDeleteCommand():
    '''public void visitDeleteCommand(final E object)
    '''
def visitKeepCommand():
    '''public void visitKeepCommand(final E object)
    '''
def getSubSequence():
    '''public List<E> getSubSequence()
    '''
def CharSequenceAsList():
    '''public CharSequenceAsList(final CharSequence sequence)
    '''
def get():
    '''public Character get(final int index)
    public List<T> get(final int index)
    '''
def size():
    '''public int size()
    public int size()
    '''
def isEmpty():
    '''public boolean isEmpty()
    '''
