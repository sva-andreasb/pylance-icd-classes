def ():
    '''returns TZDBTimeZoneNames\n\n
    (final ULocale loc)\n
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
def find():
    '''returns Collection<MatchInfo>\n\n
    find(final CharSequence text, final int start, final EnumSet<NameType> nameTypes)\n
    '''
def handlePrefixMatch():
    '''returns boolean\n\n
    handlePrefixMatch(final int matchLength, final Iterator<TZDBNameInfo> values)\n
    '''
def getMatches():
    '''returns Collection<MatchInfo>\n\n
    getMatches()\n
    '''
