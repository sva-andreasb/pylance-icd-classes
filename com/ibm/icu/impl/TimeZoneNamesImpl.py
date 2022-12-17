NUM_NAME_TYPES = "int  7"
def ():
    '''returns TimeZoneNamesImpl\n\n
    (final ULocale locale)\n
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
def getExemplarLocationName():
    '''returns String\n\n
    getExemplarLocationName(final String tzID)\n
    '''
def getDisplayNames():
    '''returns None\n\n
    getDisplayNames(final String tzID, final NameType[] types, final long date, final String[] dest, final int destOffset)\n
    '''
def put():
    '''returns None\n\n
    put(final UResource.Key key, final UResource.Value value, final boolean noFallback)\n
    put(final UResource.Key key, final UResource.Value value, final boolean noFallback)\n
    '''
def handlePrefixMatch():
    '''returns boolean\n\n
    handlePrefixMatch(final int matchLength, final Iterator<NameInfo> values)\n
    '''
def getMatches():
    '''returns Collection<MatchInfo>\n\n
    getMatches()\n
    '''
def getMaxMatchLen():
    '''returns int\n\n
    getMaxMatchLen()\n
    '''
def resetResults():
    '''returns None\n\n
    resetResults()\n
    '''
def getName():
    '''returns String\n\n
    getName(final NameType type)\n
    '''
def addAsMetaZoneIntoTrie():
    '''returns None\n\n
    addAsMetaZoneIntoTrie(final String mzID, final TextTrieMap<NameInfo> trie)\n
    '''
def addAsTimeZoneIntoTrie():
    '''returns None\n\n
    addAsTimeZoneIntoTrie(final String tzID, final TextTrieMap<NameInfo> trie)\n
    '''
