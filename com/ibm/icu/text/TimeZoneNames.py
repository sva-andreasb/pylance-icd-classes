def getInstance():
    '''public static TimeZoneNames getInstance(final ULocale locale)
    public static TimeZoneNames getInstance(final Locale locale)
    '''
def getTZDBInstance():
    '''public static TimeZoneNames getTZDBInstance(final ULocale locale)
    '''
def getDisplayName():
    '''public final String getDisplayName(final String tzID, final NameType type, final long date)
    '''
def getExemplarLocationName():
    '''public String getExemplarLocationName(final String tzID)
    '''
def find():
    '''public Collection<MatchInfo> find(final CharSequence text, final int start, final EnumSet<NameType> types)
    public Collection<MatchInfo> find(final CharSequence text, final int start, final EnumSet<NameType> nameTypes)
    '''
def loadAllDisplayNames():
    '''public void loadAllDisplayNames()
    '''
def getDisplayNames():
    '''public void getDisplayNames(final String tzID, final NameType[] types, final long date, final String[] dest, final int destOffset)
    '''
def MatchInfo():
    '''public MatchInfo(final NameType nameType, final String tzID, final String mzID, final int matchLength)
    '''
def tzID():
    '''public String tzID()
    '''
def mzID():
    '''public String mzID()
    '''
def nameType():
    '''public NameType nameType()
    '''
def matchLength():
    '''public int matchLength()
    '''
def getAvailableMetaZoneIDs():
    '''public Set<String> getAvailableMetaZoneIDs()
    public Set<String> getAvailableMetaZoneIDs(final String tzID)
    '''
def getMetaZoneID():
    '''public String getMetaZoneID(final String tzID, final long date)
    '''
def getReferenceZoneID():
    '''public String getReferenceZoneID(final String mzID, final String region)
    '''
def getMetaZoneDisplayName():
    '''public String getMetaZoneDisplayName(final String mzID, final NameType type)
    '''
def getTimeZoneDisplayName():
    '''public String getTimeZoneDisplayName(final String tzID, final NameType type)
    '''
def getTimeZoneNames():
    '''public TimeZoneNames getTimeZoneNames(final ULocale locale)
    '''
