def is():
    '''public static <T extends Comparable<T>> Range<T> is(final T element)
    public static <T> Range<T> is(final T element, final Comparator<T> comparator)
    '''
def between():
    '''public static <T extends Comparable<T>> Range<T> between(final T fromInclusive, final T toInclusive)
    public static <T> Range<T> between(final T fromInclusive, final T toInclusive, final Comparator<T> comparator)
    '''
def getMinimum():
    '''public T getMinimum()
    '''
def getMaximum():
    '''public T getMaximum()
    '''
def getComparator():
    '''public Comparator<T> getComparator()
    '''
def isNaturalOrdering():
    '''public boolean isNaturalOrdering()
    '''
def contains():
    '''public boolean contains(final T element)
    '''
def isAfter():
    '''public boolean isAfter(final T element)
    '''
def isStartedBy():
    '''public boolean isStartedBy(final T element)
    '''
def isEndedBy():
    '''public boolean isEndedBy(final T element)
    '''
def isBefore():
    '''public boolean isBefore(final T element)
    '''
def elementCompareTo():
    '''public int elementCompareTo(final T element)
    '''
def containsRange():
    '''public boolean containsRange(final Range<T> otherRange)
    '''
def isAfterRange():
    '''public boolean isAfterRange(final Range<T> otherRange)
    '''
def isOverlappedBy():
    '''public boolean isOverlappedBy(final Range<T> otherRange)
    '''
def isBeforeRange():
    '''public boolean isBeforeRange(final Range<T> otherRange)
    '''
def intersectionWith():
    '''public Range<T> intersectionWith(final Range<T> other)
    '''
def equals():
    '''public boolean equals(final Object obj)
    '''
def hashCode():
    '''public int hashCode()
    '''
def toString():
    '''public String toString()
    public String toString(final String format)
    '''
def compare():
    '''public int compare(final Object obj1, final Object obj2)
    '''
