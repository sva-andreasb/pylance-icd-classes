def on():
'''public static Splitter on(final char separator)
public static Splitter on(final CharMatcher separatorMatcher)
public static Splitter on(final String separator)
public static Splitter on(final Pattern separatorPattern)
'''
pass
def iterator():
'''public SplittingIterator iterator(final Splitter splitter, final CharSequence toSplit)
public SplittingIterator iterator(final Splitter splitter, final CharSequence toSplit)
public SplittingIterator iterator(final Splitter splitter, final CharSequence toSplit)
public SplittingIterator iterator(final Splitter splitter, final CharSequence toSplit)
public Iterator<String> iterator()
'''
pass
def separatorStart():
'''public int separatorStart(final int start)
public int separatorStart(final int start)
public int separatorStart(final int start)
'''
pass
def separatorEnd():
'''public int separatorEnd(final int separatorPosition)
public int separatorEnd(final int separatorPosition)
public int separatorEnd(final int separatorPosition)
'''
pass
def onPattern():
'''public static Splitter onPattern(final String separatorPattern)
'''
pass
def fixedLength():
'''public static Splitter fixedLength(final int length)
'''
pass
def omitEmptyStrings():
'''public Splitter omitEmptyStrings()
'''
pass
def limit():
'''public Splitter limit(final int limit)
'''
pass
def trimResults():
'''public Splitter trimResults()
public Splitter trimResults(final CharMatcher trimmer)
'''
pass
def split():
'''public Iterable<String> split(final CharSequence sequence)
public Map<String, String> split(final CharSequence sequence)
'''
pass
def toString():
'''public String toString()
'''
pass
def splitToList():
'''public List<String> splitToList(final CharSequence sequence)
'''
pass
def withKeyValueSeparator():
'''public MapSplitter withKeyValueSeparator(final String separator)
public MapSplitter withKeyValueSeparator(final char separator)
public MapSplitter withKeyValueSeparator(final Splitter keyValueSplitter)
'''
pass
