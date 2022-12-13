MIN_VALUE = "int 0"
MAX_VALUE = "int 1114111"
IGNORE_SPACE = "int 1"
CASE = "int 2"
CASE_INSENSITIVE = "int 2"
ADD_CASE_MAPPINGS = "int 4"
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
pass
def clone():
'''public Object clone()
'''
pass
def set():
'''public UnicodeSet set(final int start, final int end)
public UnicodeSet set(final UnicodeSet other)
'''
pass
def applyPattern():
'''public final UnicodeSet applyPattern(final String pattern)
public UnicodeSet applyPattern(final String pattern, final boolean ignoreWhitespace)
public UnicodeSet applyPattern(final String pattern, final int options)
public UnicodeSet applyPattern(final String pattern, ParsePosition pos, final SymbolTable symbols, final int options)
'''
pass
def resemblesPattern():
'''public static boolean resemblesPattern(final String pattern, final int pos)
'''
pass
def toPattern():
'''public String toPattern(final boolean escapeUnprintable)
'''
pass
def _generatePattern():
'''public StringBuffer _generatePattern(final StringBuffer result, final boolean escapeUnprintable)
public StringBuffer _generatePattern(final StringBuffer result, final boolean escapeUnprintable, final boolean includeStrings)
'''
pass
def size():
'''public int size()
'''
pass
def isEmpty():
'''public boolean isEmpty()
'''
pass
def matchesIndexValue():
'''public boolean matchesIndexValue(final int v)
'''
pass
def matches():
'''public int matches(final Replaceable text, final int[] offset, final int limit, final boolean incremental)
'''
pass
def matchesAt():
'''public int matchesAt(final CharSequence text, final int offset)
'''
pass
def addMatchSetTo():
'''public void addMatchSetTo(final UnicodeSet toUnionTo)
'''
pass
def indexOf():
'''public int indexOf(final int c)
'''
pass
def charAt():
'''public int charAt(int index)
'''
pass
def add():
'''public UnicodeSet add(final int start, final int end)
public final UnicodeSet add(final int c)
public final UnicodeSet add(final CharSequence s)
public UnicodeSet add(final Iterable<?> source)
'''
pass
def addAll():
'''public UnicodeSet addAll(final int start, final int end)
public final UnicodeSet addAll(final CharSequence s)
public UnicodeSet addAll(final UnicodeSet c)
public UnicodeSet addAll(final Iterable<?> source)
public <T extends CharSequence> UnicodeSet addAll(final T... collection)
'''
pass
def retainAll():
'''public final UnicodeSet retainAll(final CharSequence s)
public UnicodeSet retainAll(final UnicodeSet c)
public <T extends CharSequence> UnicodeSet retainAll(final Iterable<T> collection)
'''
pass
def complementAll():
'''public final UnicodeSet complementAll(final CharSequence s)
public UnicodeSet complementAll(final UnicodeSet c)
'''
pass
def removeAll():
'''public final UnicodeSet removeAll(final CharSequence s)
public UnicodeSet removeAll(final UnicodeSet c)
public <T extends CharSequence> UnicodeSet removeAll(final Iterable<T> collection)
'''
pass
def removeAllStrings():
'''public final UnicodeSet removeAllStrings()
'''
pass
def from():
'''public static UnicodeSet from(final CharSequence s)
'''
pass
def fromAll():
'''public static UnicodeSet fromAll(final CharSequence s)
'''
pass
def retain():
'''public UnicodeSet retain(final int start, final int end)
public final UnicodeSet retain(final int c)
public final UnicodeSet retain(final CharSequence cs)
'''
pass
def remove():
'''public UnicodeSet remove(final int start, final int end)
public final UnicodeSet remove(final int c)
public final UnicodeSet remove(final CharSequence s)
public void remove()
public void remove()
'''
pass
def complement():
'''public UnicodeSet complement(final int start, final int end)
public final UnicodeSet complement(final int c)
public UnicodeSet complement()
public final UnicodeSet complement(final CharSequence s)
'''
pass
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
pass
def containsAll():
'''public boolean containsAll(final UnicodeSet b)
public boolean containsAll(final String s)
public <T extends CharSequence> boolean containsAll(final Iterable<T> collection)
'''
pass
def getRegexEquivalent():
'''public String getRegexEquivalent()
'''
pass
def containsNone():
'''public boolean containsNone(final int start, final int end)
public boolean containsNone(final UnicodeSet b)
public boolean containsNone(final CharSequence s)
public <T extends CharSequence> boolean containsNone(final Iterable<T> collection)
'''
pass
def containsSome():
'''public final boolean containsSome(final int start, final int end)
public final boolean containsSome(final UnicodeSet s)
public final boolean containsSome(final CharSequence s)
public final <T extends CharSequence> boolean containsSome(final Iterable<T> collection)
'''
pass
def clear():
'''public UnicodeSet clear()
'''
pass
def getRangeCount():
'''public int getRangeCount()
'''
pass
def getRangeStart():
'''public int getRangeStart(final int index)
'''
pass
def getRangeEnd():
'''public int getRangeEnd(final int index)
'''
pass
def compact():
'''public UnicodeSet compact()
'''
pass
def equals():
'''public boolean equals(final Object o)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def addAllTo():
'''public <T extends Collection<String>> T addAllTo(final T target)
public String[] addAllTo(final String[] target)
public static <T, U extends Collection<T>> U addAllTo(final Iterable<T> source, final U target)
public static <T> T[] addAllTo(final Iterable<T> source, final T[] target)
'''
pass
def toArray():
'''public static String[] toArray(final UnicodeSet set)
'''
pass
def applyIntPropertyValue():
'''public UnicodeSet applyIntPropertyValue(final int prop, final int value)
'''
pass
def applyPropertyAlias():
'''public UnicodeSet applyPropertyAlias(final String propertyAlias, final String valueAlias)
public UnicodeSet applyPropertyAlias(final String propertyAlias, final String valueAlias, final SymbolTable symbols)
public boolean applyPropertyAlias(final String propertyName, final String propertyValue, final UnicodeSet result)
'''
pass
def closeOver():
'''public UnicodeSet closeOver(final int attribute)
'''
pass
def isFrozen():
'''public boolean isFrozen()
'''
pass
def freeze():
'''public UnicodeSet freeze()
'''
pass
def span():
'''public int span(final CharSequence s, final SpanCondition spanCondition)
public int span(final CharSequence s, int start, final SpanCondition spanCondition)
'''
pass
def spanAndCount():
'''public int spanAndCount(final CharSequence s, int start, final SpanCondition spanCondition, final OutputInt outCount)
'''
pass
def spanBack():
'''public int spanBack(final CharSequence s, final SpanCondition spanCondition)
public int spanBack(final CharSequence s, int fromIndex, final SpanCondition spanCondition)
'''
pass
def cloneAsThawed():
'''public UnicodeSet cloneAsThawed()
'''
pass
def ranges():
'''public Iterable<EntryRange> ranges()
'''
pass
def iterator():
'''public Iterator<String> iterator()
public Iterator<EntryRange> iterator()
'''
pass
def compareTo():
'''public int compareTo(final UnicodeSet o)
public int compareTo(final UnicodeSet o, final ComparisonStyle style)
public int compareTo(final Iterable<String> other)
'''
pass
def compare():
'''public static int compare(final CharSequence string, final int codePoint)
public static int compare(final int codePoint, final CharSequence string)
public static <T extends Comparable<T>> int compare(final Iterable<T> collection1, final Iterable<T> collection2)
public static <T extends Comparable<T>> int compare(final Iterator<T> first, final Iterator<T> other)
public static <T extends Comparable<T>> int compare(final Collection<T> collection1, final Collection<T> collection2, final ComparisonStyle style)
'''
pass
def strings():
'''public Collection<String> strings()
'''
pass
def getSingleCodePoint():
'''public static int getSingleCodePoint(final CharSequence s)
'''
pass
def addBridges():
'''public UnicodeSet addBridges(final UnicodeSet dontCare)
'''
pass
def findIn():
'''public int findIn(final CharSequence value, int fromIndex, final boolean findNot)
'''
pass
def findLastIn():
'''public int findLastIn(final CharSequence value, int fromIndex, final boolean findNot)
'''
pass
def stripFrom():
'''public String stripFrom(final CharSequence source, final boolean matches)
'''
pass
def getDefaultXSymbolTable():
'''public static XSymbolTable getDefaultXSymbolTable()
'''
pass
def setDefaultXSymbolTable():
'''public static void setDefaultXSymbolTable(final XSymbolTable xSymbolTable)
'''
pass
def lookupMatcher():
'''public UnicodeMatcher lookupMatcher(final int i)
'''
pass
def lookup():
'''public char[] lookup(final String s)
'''
pass
def parseReference():
'''public String parseReference(final String text, final ParsePosition pos, final int limit)
'''
pass
def hasNext():
'''public boolean hasNext()
public boolean hasNext()
'''
pass
def next():
'''public EntryRange next()
public String next()
'''
pass
