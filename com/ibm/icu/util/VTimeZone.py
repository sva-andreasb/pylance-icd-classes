def create():
    '''    public static VTimeZone create(final String tzid)
    public static VTimeZone create(final Reader reader)
    '''
def getOffset():
    '''    public int getOffset(final int era, final int year, final int month, final int day, final int dayOfWeek, final int milliseconds)
    public void getOffset(final long date, final boolean local, final int[] offsets)
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
def getTZURL():
    '''    public String getTZURL()
    '''
def setTZURL():
    '''    public void setTZURL(final String url)
    '''
def getLastModified():
    '''    public Date getLastModified()
    '''
def setLastModified():
    '''    public void setLastModified(final Date date)
    '''
def write():
    '''    public void write(final Writer writer)
    public void write(final Writer writer, final long start)
    '''
def writeSimple():
    '''    public void writeSimple(final Writer writer, final long time)
    '''
def getNextTransition():
    '''    public TimeZoneTransition getNextTransition(final long base, final boolean inclusive)
    '''
def getPreviousTransition():
    '''    public TimeZoneTransition getPreviousTransition(final long base, final boolean inclusive)
    '''
def hasEquivalentTransitions():
    '''    public boolean hasEquivalentTransitions(final TimeZone other, final long start, final long end)
    '''
def getTimeZoneRules():
    '''    public TimeZoneRule[] getTimeZoneRules()
    public TimeZoneRule[] getTimeZoneRules(final long start)
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
