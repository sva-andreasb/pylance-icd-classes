def chainedComparator():
    '''public static <E> Comparator<E> chainedComparator(final Comparator<E>... comparators)
    public static <E> Comparator<E> chainedComparator(final Collection<Comparator<E>> comparators)
    '''
def reversedComparator():
    '''public static <E> Comparator<E> reversedComparator(final Comparator<E> comparator)
    '''
def booleanComparator():
    '''public static Comparator<Boolean> booleanComparator(final boolean trueFirst)
    '''
def nullLowComparator():
    '''public static <E> Comparator<E> nullLowComparator(Comparator<E> comparator)
    '''
def nullHighComparator():
    '''public static <E> Comparator<E> nullHighComparator(Comparator<E> comparator)
    '''
def transformedComparator():
    '''public static <I, O> Comparator<I> transformedComparator(Comparator<O> comparator, final Transformer<? super I, ? extends O> transformer)
    '''
def min():
    '''public static <E> E min(final E o1, final E o2, Comparator<E> comparator)
    '''
def max():
    '''public static <E> E max(final E o1, final E o2, Comparator<E> comparator)
    '''
