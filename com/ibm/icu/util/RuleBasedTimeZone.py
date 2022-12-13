def RuleBasedTimeZone():
    '''    public RuleBasedTimeZone(final String id, final InitialTimeZoneRule initialRule)
    '''
def addTransitionRule():
    '''    public void addTransitionRule(final TimeZoneRule rule)
    '''
def getOffset():
    '''    public int getOffset(final int era, int year, final int month, final int day, final int dayOfWeek, final int milliseconds)
    public void getOffset(final long time, final boolean local, final int[] offsets)
    '''
def getOffsetFromLocal():
    '''    public void getOffsetFromLocal(final long date, final int nonExistingTimeOpt, final int duplicatedTimeOpt, final int[] offsets)
    '''
def getRawOffset():
    '''    public int getRawOffset()
    '''
def inDaylightTime():
    '''    public boolean inDaylightTime(final Date date)
    '''
def setRawOffset():
    '''    public void setRawOffset(final int offsetMillis)
    '''
def useDaylightTime():
    '''    public boolean useDaylightTime()
    '''
def observesDaylightTime():
    '''    public boolean observesDaylightTime()
    '''
def hasSameRules():
    '''    public boolean hasSameRules(final TimeZone other)
    '''
def getTimeZoneRules():
    '''    public TimeZoneRule[] getTimeZoneRules()
    '''
def getNextTransition():
    '''    public TimeZoneTransition getNextTransition(final long base, final boolean inclusive)
    '''
def getPreviousTransition():
    '''    public TimeZoneTransition getPreviousTransition(final long base, final boolean inclusive)
    '''
def clone():
    '''    public Object clone()
    '''
def isFrozen():
    '''    public boolean isFrozen()
    '''
def freeze():
    '''    public TimeZone freeze()
    '''
def cloneAsThawed():
    '''    public TimeZone cloneAsThawed()
    '''
