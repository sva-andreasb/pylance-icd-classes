def DateIntervalInfo():
'''public DateIntervalInfo()
public DateIntervalInfo(final ULocale locale)
public DateIntervalInfo(final Locale locale)
'''
pass
def setIntervalPattern():
'''public void setIntervalPattern(final String skeleton, final int lrgDiffCalUnit, final String intervalPattern)
'''
pass
def genPatternInfo():
'''public static PatternInfo genPatternInfo(final String intervalPattern, final boolean laterDateFirst)
'''
pass
def getIntervalPattern():
'''public PatternInfo getIntervalPattern(final String skeleton, final int field)
'''
pass
def getFallbackIntervalPattern():
'''public String getFallbackIntervalPattern()
'''
pass
def setFallbackIntervalPattern():
'''public void setFallbackIntervalPattern(final String fallbackPattern)
'''
pass
def getDefaultOrder():
'''public boolean getDefaultOrder()
'''
pass
def clone():
'''public Object clone()
'''
pass
def isFrozen():
'''public boolean isFrozen()
'''
pass
def freeze():
'''public DateIntervalInfo freeze()
'''
pass
def cloneAsThawed():
'''public DateIntervalInfo cloneAsThawed()
'''
pass
def equals():
'''public boolean equals(final Object a)
public boolean equals(final Object a)
'''
pass
def hashCode():
'''public int hashCode()
public int hashCode()
'''
pass
def getPatterns():
'''public Map<String, Set<String>> getPatterns()
'''
pass
def getRawPatterns():
'''public Map<String, Map<String, PatternInfo>> getRawPatterns()
'''
pass
def PatternInfo():
'''public PatternInfo(final String firstPart, final String secondPart, final boolean firstDateInPtnIsLaterDate)
'''
pass
def getFirstPart():
'''public String getFirstPart()
'''
pass
def getSecondPart():
'''public String getSecondPart()
'''
pass
def firstDateInPtnIsLaterDate():
'''public boolean firstDateInPtnIsLaterDate()
'''
pass
def toString():
'''public String toString()
'''
pass
def DateIntervalSink():
'''public DateIntervalSink(final DateIntervalInfo dateIntervalInfo)
'''
pass
def put():
'''public void put(final UResource.Key key, final UResource.Value value, final boolean noFallback)
'''
pass
def processSkeletonTable():
'''public void processSkeletonTable(final UResource.Key key, final UResource.Value value)
'''
pass
def getAndResetNextCalendarType():
'''public String getAndResetNextCalendarType()
'''
pass
