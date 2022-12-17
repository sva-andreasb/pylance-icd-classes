def getExemplarLocationName():
    '''returns String\n\n
    getExemplarLocationName(final String tzID)\n
    '''
def find():
    '''returns Collection<MatchInfo>\n\n
    find(final CharSequence text, final int start, final EnumSet<NameType> types)\n
    find(final CharSequence text, final int start, final EnumSet<NameType> nameTypes)\n
    '''
def loadAllDisplayNames():
    '''returns None\n\n
    loadAllDisplayNames()\n
    '''
def getDisplayNames():
    '''returns None\n\n
    getDisplayNames(final String tzID, final NameType[] types, final long date, final String[] dest, final int destOffset)\n
    '''
def ():
    '''returns MatchInfo\n\n
    (final NameType nameType, final String tzID, final String mzID, final int matchLength)\n
    '''
def tzID():
    '''returns String\n\n
    tzID()\n
    '''
def mzID():
    '''returns String\n\n
    mzID()\n
    '''
def nameType():
    '''returns NameType\n\n
    nameType()\n
    '''
def matchLength():
    '''returns int\n\n
    matchLength()\n
    '''
def getAvailableMetaZoneIDs():
    '''returns Set<String>\n\n
    getAvailableMetaZoneIDs()\n
    getAvailableMetaZoneIDs(final String tzID)\n
    '''
def getMetaZoneID():
    '''returns String\n\n
    getMetaZoneID(final String tzID, final long date)\n
    '''
def getReferenceZoneID():
    '''returns String\n\n
    getReferenceZoneID(final String mzID, final String region)\n
    '''
def getMetaZoneDisplayName():
    '''returns String\n\n
    getMetaZoneDisplayName(final String mzID, final NameType type)\n
    '''
def getTimeZoneDisplayName():
    '''returns String\n\n
    getTimeZoneDisplayName(final String tzID, final NameType type)\n
    '''
def getTimeZoneNames():
    '''returns TimeZoneNames\n\n
    getTimeZoneNames(final ULocale locale)\n
    '''
