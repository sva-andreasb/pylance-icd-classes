def DateIntervalInfo():
    '''public DateIntervalInfo()
    public DateIntervalInfo(final ULocale locale)
    public DateIntervalInfo(final Locale locale)
    '''
def setIntervalPattern():
    '''public void setIntervalPattern(final String skeleton, final int lrgDiffCalUnit, final String intervalPattern)
    '''
def genPatternInfo():
    '''public static PatternInfo genPatternInfo(final String intervalPattern, final boolean laterDateFirst)
    '''
def getIntervalPattern():
    '''public PatternInfo getIntervalPattern(final String skeleton, final int field)
    '''
def getFallbackIntervalPattern():
    '''public String getFallbackIntervalPattern()
    '''
def setFallbackIntervalPattern():
    '''public void setFallbackIntervalPattern(final String fallbackPattern)
    '''
def getDefaultOrder():
    '''public boolean getDefaultOrder()
    '''
def clone():
    '''public Object clone()
    '''
def isFrozen():
    '''public boolean isFrozen()
    '''
def freeze():
    '''public DateIntervalInfo freeze()
    '''
def cloneAsThawed():
    '''public DateIntervalInfo cloneAsThawed()
    '''
def equals():
    '''public boolean equals(final Object a)
    public boolean equals(final Object a)
    '''
def hashCode():
    '''public int hashCode()
    public int hashCode()
    '''
def getPatterns():
    '''public Map<String, Set<String>> getPatterns()
    '''
def getRawPatterns():
    '''public Map<String, Map<String, PatternInfo>> getRawPatterns()
    '''
def PatternInfo():
    '''public PatternInfo(final String firstPart, final String secondPart, final boolean firstDateInPtnIsLaterDate)
    '''
def getFirstPart():
    '''public String getFirstPart()
    '''
def getSecondPart():
    '''public String getSecondPart()
    '''
def firstDateInPtnIsLaterDate():
    '''public boolean firstDateInPtnIsLaterDate()
    '''
def toString():
    '''public String toString()
    '''
def DateIntervalSink():
    '''public DateIntervalSink(final DateIntervalInfo dateIntervalInfo)
    '''
def put():
    '''public void put(final UResource.Key key, final UResource.Value value, final boolean noFallback)
    '''
def processSkeletonTable():
    '''public void processSkeletonTable(final UResource.Key key, final UResource.Value value)
    '''
def getAndResetNextCalendarType():
    '''public String getAndResetNextCalendarType()
    '''
