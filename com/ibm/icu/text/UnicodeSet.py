MIN_VALUE = "int  0"
MAX_VALUE = "int  1114111"
IGNORE_SPACE = "int  1"
CASE = "int  2"
CASE_INSENSITIVE = "int  2"
ADD_CASE_MAPPINGS = "int  4"
def UnicodeSet():
    '''public UnicodeSet()
    public UnicodeSet(final UnicodeSet other)
    public UnicodeSet(final int start, final int end)
    public UnicodeSet(final int... pairs)
    public UnicodeSet(final String pattern)
    public UnicodeSet(final String pattern, final boolean ignoreWhitespace)
    public UnicodeSet(final String pattern, final int options)
    public UnicodeSet(final String pattern, final ParsePosition pos, final SymbolTable symbols)
    public UnicodeSet(final String pattern, final ParsePosition pos, final SymbolTable symbols, final int options)
    '''
def clone():
    '''public Object clone()
    '''
def set():
    '''public UnicodeSet set(final int start, final int end)
    public UnicodeSet set(final UnicodeSet other)
    '''
def applyPattern():
    '''public final UnicodeSet applyPattern(final String pattern)
    public UnicodeSet applyPattern(final String pattern, final boolean ignoreWhitespace)
    public UnicodeSet applyPattern(final String pattern, final int options)
    public UnicodeSet applyPattern(final String pattern, ParsePosition pos, final SymbolTable symbols, final int options)
    '''
def resemblesPattern():
    '''public static boolean resemblesPattern(final String pattern, final int pos)
    '''
def toPattern():
    '''public String toPattern(final boolean escapeUnprintable)
    '''
def _generatePattern():
    '''public StringBuffer _generatePattern(final StringBuffer result, final boolean escapeUnprintable)
    public StringBuffer _generatePattern(final StringBuffer result, final boolean escapeUnprintable, final boolean includeStrings)
    '''
def size():
    '''public int size()
    '''
def isEmpty():
    '''public boolean isEmpty()
    '''
def matchesIndexValue():
    '''public boolean matchesIndexValue(final int v)
    '''
def matches():
    '''public int matches(final Replaceable text, final int[] offset, final int limit, final boolean incremental)
    '''
def matchesAt():
    '''public int matchesAt(final CharSequence text, final int offset)
    '''
def addMatchSetTo():
    '''public void addMatchSetTo(final UnicodeSet toUnionTo)
    '''
def indexOf():
    '''public int indexOf(final int c)
    '''
def charAt():
    '''public int charAt(int index)
    '''
def add():
    '''public UnicodeSet add(final int start, final int end)
    public final UnicodeSet add(final int c)
    public final UnicodeSet add(final CharSequence s)
    public UnicodeSet add(final Iterable<?> source)
    '''
def addAll():
    '''public UnicodeSet addAll(final int start, final int end)
    public final UnicodeSet addAll(final CharSequence s)
    public UnicodeSet addAll(final UnicodeSet c)
    public UnicodeSet addAll(final Iterable<?> source)
    public <T extends CharSequence> UnicodeSet addAll(final T... collection)
    '''
def retainAll():
    '''public final UnicodeSet retainAll(final CharSequence s)
    public UnicodeSet retainAll(final UnicodeSet c)
    public <T extends CharSequence> UnicodeSet retainAll(final Iterable<T> collection)
    '''
def complementAll():
    '''public final UnicodeSet complementAll(final CharSequence s)
    public UnicodeSet complementAll(final UnicodeSet c)
    '''
def removeAll():
    '''public final UnicodeSet removeAll(final CharSequence s)
    public UnicodeSet removeAll(final UnicodeSet c)
    public <T extends CharSequence> UnicodeSet removeAll(final Iterable<T> collection)
    '''
def removeAllStrings():
    '''public final UnicodeSet removeAllStrings()
    '''
def from():
    '''public static UnicodeSet from(final CharSequence s)
    '''
def fromAll():
    '''public static UnicodeSet fromAll(final CharSequence s)
    '''
def retain():
    '''public UnicodeSet retain(final int start, final int end)
    public final UnicodeSet retain(final int c)
    public final UnicodeSet retain(final CharSequence cs)
    '''
def remove():
    '''public UnicodeSet remove(final int start, final int end)
    public final UnicodeSet remove(final int c)
    public final UnicodeSet remove(final CharSequence s)
    public void remove()
    public void remove()
    '''
def complement():
    '''public UnicodeSet complement(final int start, final int end)
    public final UnicodeSet complement(final int c)
    public UnicodeSet complement()
    public final UnicodeSet complement(final CharSequence s)
    '''
def contains():
    '''public boolean contains(final int c)
    public boolean contains(final int start, final int end)
    public final boolean contains(final CharSequence s)
    public boolean contains(final int ch)
    public boolean contains(final int ch)
    public boolean contains(final int ch)
    public boolean contains(final int c)
    public boolean contains(final int ch)
    '''
def containsAll():
    '''public boolean containsAll(final UnicodeSet b)
    public boolean containsAll(final String s)
    public <T extends CharSequence> boolean containsAll(final Iterable<T> collection)
    '''
def getRegexEquivalent():
    '''public String getRegexEquivalent()
    '''
def containsNone():
    '''public boolean containsNone(final int start, final int end)
    public boolean containsNone(final UnicodeSet b)
    public boolean containsNone(final CharSequence s)
    public <T extends CharSequence> boolean containsNone(final Iterable<T> collection)
    '''
def containsSome():
    '''public final boolean containsSome(final int start, final int end)
    public final boolean containsSome(final UnicodeSet s)
    public final boolean containsSome(final CharSequence s)
    public final <T extends CharSequence> boolean containsSome(final Iterable<T> collection)
    '''
def clear():
    '''public UnicodeSet clear()
    '''
def getRangeCount():
    '''public int getRangeCount()
    '''
def getRangeStart():
    '''public int getRangeStart(final int index)
    '''
def getRangeEnd():
    '''public int getRangeEnd(final int index)
    '''
def compact():
    '''public UnicodeSet compact()
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
def hashCode():
    '''public int hashCode()
    '''
def toString():
    '''public String toString()
    public String toString()
    '''
def addAllTo():
    '''public <T extends Collection<String>> T addAllTo(final T target)
    public String[] addAllTo(final String[] target)
    public static <T, U extends Collection<T>> U addAllTo(final Iterable<T> source, final U target)
    public static <T> T[] addAllTo(final Iterable<T> source, final T[] target)
    '''
def toArray():
    '''public static String[] toArray(final UnicodeSet set)
    '''
def applyIntPropertyValue():
    '''public UnicodeSet applyIntPropertyValue(final int prop, final int value)
    '''
def applyPropertyAlias():
    '''public UnicodeSet applyPropertyAlias(final String propertyAlias, final String valueAlias)
    public UnicodeSet applyPropertyAlias(final String propertyAlias, final String valueAlias, final SymbolTable symbols)
    public boolean applyPropertyAlias(final String propertyName, final String propertyValue, final UnicodeSet result)
    '''
def closeOver():
    '''public UnicodeSet closeOver(final int attribute)
    '''
def isFrozen():
    '''public boolean isFrozen()
    '''
def freeze():
    '''public UnicodeSet freeze()
    '''
def span():
    '''public int span(final CharSequence s, final SpanCondition spanCondition)
    public int span(final CharSequence s, int start, final SpanCondition spanCondition)
    '''
def spanAndCount():
    '''public int spanAndCount(final CharSequence s, int start, final SpanCondition spanCondition, final OutputInt outCount)
    '''
def spanBack():
    '''public int spanBack(final CharSequence s, final SpanCondition spanCondition)
    public int spanBack(final CharSequence s, int fromIndex, final SpanCondition spanCondition)
    '''
def cloneAsThawed():
    '''public UnicodeSet cloneAsThawed()
    '''
def ranges():
    '''public Iterable<EntryRange> ranges()
    '''
def iterator():
    '''public Iterator<String> iterator()
    public Iterator<EntryRange> iterator()
    '''
def compareTo():
    '''public int compareTo(final UnicodeSet o)
    public int compareTo(final UnicodeSet o, final ComparisonStyle style)
    public int compareTo(final Iterable<String> other)
    '''
def compare():
    '''public static int compare(final CharSequence string, final int codePoint)
    public static int compare(final int codePoint, final CharSequence string)
    public static <T extends Comparable<T>> int compare(final Iterable<T> collection1, final Iterable<T> collection2)
    public static <T extends Comparable<T>> int compare(final Iterator<T> first, final Iterator<T> other)
    public static <T extends Comparable<T>> int compare(final Collection<T> collection1, final Collection<T> collection2, final ComparisonStyle style)
    '''
def strings():
    '''public Collection<String> strings()
    '''
def getSingleCodePoint():
    '''public static int getSingleCodePoint(final CharSequence s)
    '''
def addBridges():
    '''public UnicodeSet addBridges(final UnicodeSet dontCare)
    '''
def findIn():
    '''public int findIn(final CharSequence value, int fromIndex, final boolean findNot)
    '''
def findLastIn():
    '''public int findLastIn(final CharSequence value, int fromIndex, final boolean findNot)
    '''
def stripFrom():
    '''public String stripFrom(final CharSequence source, final boolean matches)
    '''
def getDefaultXSymbolTable():
    '''public static XSymbolTable getDefaultXSymbolTable()
    '''
def setDefaultXSymbolTable():
    '''public static void setDefaultXSymbolTable(final XSymbolTable xSymbolTable)
    '''
def lookupMatcher():
    '''public UnicodeMatcher lookupMatcher(final int i)
    '''
def lookup():
    '''public char[] lookup(final String s)
    '''
def parseReference():
    '''public String parseReference(final String text, final ParsePosition pos, final int limit)
    '''
def hasNext():
    '''public boolean hasNext()
    public boolean hasNext()
    '''
def next():
    '''public EntryRange next()
    public String next()
    '''
