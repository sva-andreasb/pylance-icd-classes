def ZoneStringFormat():
    '''    public ZoneStringFormat(final String[][] zoneStrings)
    '''
def getInstance():
    '''    public static ZoneStringFormat getInstance(final ULocale locale)
    '''
def getZoneStrings():
    '''    public String[][] getZoneStrings()
    '''
def getSpecificLongString():
    '''    public String getSpecificLongString(final Calendar cal)
    '''
def getSpecificShortString():
    '''    public String getSpecificShortString(final Calendar cal, final boolean commonlyUsedOnly)
    '''
def getGenericLongString():
    '''    public String getGenericLongString(final Calendar cal)
    '''
def getGenericShortString():
    '''    public String getGenericShortString(final Calendar cal, final boolean commonlyUsedOnly)
    '''
def getGenericLocationString():
    '''    public String getGenericLocationString(final Calendar cal)
    '''
def findSpecificLong():
    '''    public ZoneStringInfo findSpecificLong(final String text, final int start)
    '''
def findSpecificShort():
    '''    public ZoneStringInfo findSpecificShort(final String text, final int start)
    '''
def findGenericLong():
    '''    public ZoneStringInfo findGenericLong(final String text, final int start)
    '''
def findGenericShort():
    '''    public ZoneStringInfo findGenericShort(final String text, final int start)
    '''
def findGenericLocation():
    '''    public ZoneStringInfo findGenericLocation(final String text, final int start)
    '''
def getLongStandard():
    '''    public String getLongStandard(final String tzid, final long date)
    '''
def getLongDaylight():
    '''    public String getLongDaylight(final String tzid, final long date)
    '''
def getLongGenericNonLocation():
    '''    public String getLongGenericNonLocation(final String tzid, final long date)
    '''
def getLongGenericPartialLocation():
    '''    public String getLongGenericPartialLocation(final String tzid, final long date)
    '''
def getShortStandard():
    '''    public String getShortStandard(final String tzid, final long date, final boolean commonlyUsedOnly)
    '''
def getShortDaylight():
    '''    public String getShortDaylight(final String tzid, final long date, final boolean commonlyUsedOnly)
    '''
def getShortGenericNonLocation():
    '''    public String getShortGenericNonLocation(final String tzid, final long date, final boolean commonlyUsedOnly)
    '''
def getShortGenericPartialLocation():
    '''    public String getShortGenericPartialLocation(final String tzid, final long date, final boolean commonlyUsedOnly)
    '''
def getGenericLocation():
    '''    public String getGenericLocation(final String tzid)
    '''
def getID():
    '''    public String getID()
    '''
def getString():
    '''    public String getString()
    '''
def isStandard():
    '''    public boolean isStandard()
    '''
def isDaylight():
    '''    public boolean isDaylight()
    '''
def isGeneric():
    '''    public boolean isGeneric()
    '''
def handlePrefixMatch():
    '''    public boolean handlePrefixMatch(final int matchLength, final Iterator<ZoneStringInfo> values)
    '''
