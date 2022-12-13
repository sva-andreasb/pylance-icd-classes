def on():
    '''    public static Splitter on(final char separator)
    public static Splitter on(final CharMatcher separatorMatcher)
    public static Splitter on(final String separator)
    public static Splitter on(final Pattern separatorPattern)
    '''
def iterator():
    '''    public SplittingIterator iterator(final Splitter splitter, final CharSequence toSplit)
    public SplittingIterator iterator(final Splitter splitter, final CharSequence toSplit)
    public SplittingIterator iterator(final Splitter splitter, final CharSequence toSplit)
    public SplittingIterator iterator(final Splitter splitter, final CharSequence toSplit)
    public Iterator<String> iterator()
    '''
def separatorStart():
    '''    public int separatorStart(final int start)
    public int separatorStart(final int start)
    public int separatorStart(final int start)
    '''
def separatorEnd():
    '''    public int separatorEnd(final int separatorPosition)
    public int separatorEnd(final int separatorPosition)
    public int separatorEnd(final int separatorPosition)
    '''
def onPattern():
    '''    public static Splitter onPattern(final String separatorPattern)
    '''
def fixedLength():
    '''    public static Splitter fixedLength(final int length)
    '''
def omitEmptyStrings():
    '''    public Splitter omitEmptyStrings()
    '''
def limit():
    '''    public Splitter limit(final int limit)
    '''
def trimResults():
    '''    public Splitter trimResults()
    public Splitter trimResults(final CharMatcher trimmer)
    '''
def split():
    '''    public Iterable<String> split(final CharSequence sequence)
    public Map<String, String> split(final CharSequence sequence)
    '''
def toString():
    '''    public String toString()
    '''
def splitToList():
    '''    public List<String> splitToList(final CharSequence sequence)
    '''
def withKeyValueSeparator():
    '''    public MapSplitter withKeyValueSeparator(final String separator)
    public MapSplitter withKeyValueSeparator(final char separator)
    public MapSplitter withKeyValueSeparator(final Splitter keyValueSplitter)
    '''
