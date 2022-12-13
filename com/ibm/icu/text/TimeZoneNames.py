def getInstance():
'''public static TimeZoneNames getInstance(final ULocale locale)
public static TimeZoneNames getInstance(final Locale locale)
'''
pass
def getTZDBInstance():
'''public static TimeZoneNames getTZDBInstance(final ULocale locale)
'''
pass
def getDisplayName():
'''public final String getDisplayName(final String tzID, final NameType type, final long date)
'''
pass
def getExemplarLocationName():
'''public String getExemplarLocationName(final String tzID)
'''
pass
def find():
'''public Collection<MatchInfo> find(final CharSequence text, final int start, final EnumSet<NameType> types)
public Collection<MatchInfo> find(final CharSequence text, final int start, final EnumSet<NameType> nameTypes)
'''
pass
def loadAllDisplayNames():
'''public void loadAllDisplayNames()
'''
pass
def getDisplayNames():
'''public void getDisplayNames(final String tzID, final NameType[] types, final long date, final String[] dest, final int destOffset)
'''
pass
def MatchInfo():
'''public MatchInfo(final NameType nameType, final String tzID, final String mzID, final int matchLength)
'''
pass
def tzID():
'''public String tzID()
'''
pass
def mzID():
'''public String mzID()
'''
pass
def nameType():
'''public NameType nameType()
'''
pass
def matchLength():
'''public int matchLength()
'''
pass
def getAvailableMetaZoneIDs():
'''public Set<String> getAvailableMetaZoneIDs()
public Set<String> getAvailableMetaZoneIDs(final String tzID)
'''
pass
def getMetaZoneID():
'''public String getMetaZoneID(final String tzID, final long date)
'''
pass
def getReferenceZoneID():
'''public String getReferenceZoneID(final String mzID, final String region)
'''
pass
def getMetaZoneDisplayName():
'''public String getMetaZoneDisplayName(final String mzID, final NameType type)
'''
pass
def getTimeZoneDisplayName():
'''public String getTimeZoneDisplayName(final String tzID, final NameType type)
'''
pass
def getTimeZoneNames():
'''public TimeZoneNames getTimeZoneNames(final ULocale locale)
'''
pass
