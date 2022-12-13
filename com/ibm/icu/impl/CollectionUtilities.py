ALL_EMPTY = "int  0"
NOT_A_SUPERSET_B = "int  1"
NOT_A_DISJOINT_B = "int  2"
NOT_A_SUBSET_B = "int  4"
NOT_A_EQUALS_B = "int  5"
A_PROPER_SUBSET_OF_B = "int  3"
A_PROPER_SUPERSET_B = "int  6"
A_PROPER_OVERLAPS_B = "int  7"
def join():
    '''    public static String join(final Object[] array, final String separator)
    public static String join(final Collection collection, final String separator)
    '''
def asMap():
    '''    public static Map asMap(final Object[][] source, final Map target, final boolean reverse)
    public static Map asMap(final Object[][] source)
    '''
def addAll():
    '''    public static Collection addAll(final Iterator source, final Collection target)
    '''
def size():
    '''    public static int size(final Iterator source)
    '''
def removeAll():
    '''    public static Map removeAll(final Map m, final Collection itemsToRemove)
    public static Collection removeAll(final Collection c, final ObjectMatcher f)
    '''
def getFirst():
    '''    public Object getFirst(final Collection c)
    '''
def getBest():
    '''    public static Object getBest(final Collection c, final Comparator comp, final int direction)
    '''
def retainAll():
    '''    public static Collection retainAll(final Collection c, final ObjectMatcher f)
    '''
def containsSome():
    '''    public static boolean containsSome(final Collection a, final Collection b)
    '''
def containsAll():
    '''    public static boolean containsAll(final Collection a, final Collection b)
    '''
def containsNone():
    '''    public static boolean containsNone(final Collection a, final Collection b)
    '''
def getContainmentRelation():
    '''    public static int getContainmentRelation(final Collection a, final Collection b)
    '''
def remove():
    '''    public static String remove(final String source, final UnicodeSet removals)
    public void remove()
    '''
def matchesAt():
    '''    public static int matchesAt(final CharSequence text, final int offset, final CharSequence other)
    '''
def span():
    '''    public int span(final CharSequence string, final int offset, final UnicodeSet testSet)
    '''
def spanNot():
    '''    public int spanNot(final CharSequence string, int offset, final UnicodeSet testSet)
    '''
def prettyPrint():
    '''    public static String prettyPrint(final UnicodeSet uset, final boolean compressRanges, final UnicodeSet toQuote, final Transliterator quoter, final Comparator ordering, final Comparator spaceComparator)
    '''
def flatten():
    '''    public static UnicodeSet flatten(final UnicodeSet exemplar1)
    '''
def set():
    '''    public ObjectMatcher set(final ObjectMatcher toInverse)
    public FilteredIterator set(final Iterator baseIterator)
    public PrefixIterator set(final Iterator baseIterator, final String prefix)
    public RegexIterator set(final Iterator baseIterator, final Matcher matcher)
    '''
def matches():
    '''    public boolean matches(final Object value)
    '''
def MultiComparator():
    '''    public MultiComparator(final Comparator[] comparators)
    '''
def compare():
    '''    public int compare(final Object arg0, final Object arg1)
    '''
def FilteredIterator():
    '''    public FilteredIterator()
    '''
def next():
    '''    public Object next()
    '''
def hasNext():
    '''    public boolean hasNext()
    '''
def isIncluded():
    '''    public boolean isIncluded(final Object item)
    public boolean isIncluded(final Object item)
    '''
