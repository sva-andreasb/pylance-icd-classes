ALL_EMPTY = "int 0"
NOT_A_SUPERSET_B = "int 1"
NOT_A_DISJOINT_B = "int 2"
NOT_A_SUBSET_B = "int 4"
NOT_A_EQUALS_B = "int 5"
A_PROPER_SUBSET_OF_B = "int 3"
A_PROPER_SUPERSET_B = "int 6"
A_PROPER_OVERLAPS_B = "int 7"
def join():
'''public static String join(final Object[] array, final String separator)
public static String join(final Collection collection, final String separator)
'''
pass
def asMap():
'''public static Map asMap(final Object[][] source, final Map target, final boolean reverse)
public static Map asMap(final Object[][] source)
'''
pass
def addAll():
'''public static Collection addAll(final Iterator source, final Collection target)
'''
pass
def size():
'''public static int size(final Iterator source)
'''
pass
def removeAll():
'''public static Map removeAll(final Map m, final Collection itemsToRemove)
public static Collection removeAll(final Collection c, final ObjectMatcher f)
'''
pass
def getFirst():
'''public Object getFirst(final Collection c)
'''
pass
def getBest():
'''public static Object getBest(final Collection c, final Comparator comp, final int direction)
'''
pass
def retainAll():
'''public static Collection retainAll(final Collection c, final ObjectMatcher f)
'''
pass
def containsSome():
'''public static boolean containsSome(final Collection a, final Collection b)
'''
pass
def containsAll():
'''public static boolean containsAll(final Collection a, final Collection b)
'''
pass
def containsNone():
'''public static boolean containsNone(final Collection a, final Collection b)
'''
pass
def getContainmentRelation():
'''public static int getContainmentRelation(final Collection a, final Collection b)
'''
pass
def remove():
'''public static String remove(final String source, final UnicodeSet removals)
public void remove()
'''
pass
def matchesAt():
'''public static int matchesAt(final CharSequence text, final int offset, final CharSequence other)
'''
pass
def span():
'''public int span(final CharSequence string, final int offset, final UnicodeSet testSet)
'''
pass
def spanNot():
'''public int spanNot(final CharSequence string, int offset, final UnicodeSet testSet)
'''
pass
def prettyPrint():
'''public static String prettyPrint(final UnicodeSet uset, final boolean compressRanges, final UnicodeSet toQuote, final Transliterator quoter, final Comparator ordering, final Comparator spaceComparator)
'''
pass
def flatten():
'''public static UnicodeSet flatten(final UnicodeSet exemplar1)
'''
pass
def set():
'''public ObjectMatcher set(final ObjectMatcher toInverse)
public FilteredIterator set(final Iterator baseIterator)
public PrefixIterator set(final Iterator baseIterator, final String prefix)
public RegexIterator set(final Iterator baseIterator, final Matcher matcher)
'''
pass
def matches():
'''public boolean matches(final Object value)
'''
pass
def MultiComparator():
'''public MultiComparator(final Comparator[] comparators)
'''
pass
def compare():
'''public int compare(final Object arg0, final Object arg1)
'''
pass
def FilteredIterator():
'''public FilteredIterator()
'''
pass
def next():
'''public Object next()
'''
pass
def hasNext():
'''public boolean hasNext()
'''
pass
def isIncluded():
'''public boolean isIncluded(final Object item)
public boolean isIncluded(final Object item)
'''
pass
