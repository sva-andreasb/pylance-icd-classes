NUM_NAME_TYPES = "int  7"
def TimeZoneNamesImpl():
'''public TimeZoneNamesImpl(final ULocale locale)
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
def getExemplarLocationName():
'''public String getExemplarLocationName(final String tzID)
'''
pass
def find():
'''public synchronized Collection<MatchInfo> find(final CharSequence text, final int start, final EnumSet<NameType> nameTypes)
'''
pass
def loadAllDisplayNames():
'''public synchronized void loadAllDisplayNames()
'''
pass
def getDisplayNames():
'''public void getDisplayNames(final String tzID, final NameType[] types, final long date, final String[] dest, final int destOffset)
'''
pass
def getDefaultExemplarLocationName():
'''public static String getDefaultExemplarLocationName(final String tzID)
'''
pass
def put():
'''public void put(final UResource.Key key, final UResource.Value value, final boolean noFallback)
public void put(final UResource.Key key, final UResource.Value value, final boolean noFallback)
'''
pass
def handlePrefixMatch():
'''public boolean handlePrefixMatch(final int matchLength, final Iterator<NameInfo> values)
'''
pass
def getMatches():
'''public Collection<MatchInfo> getMatches()
'''
pass
def getMaxMatchLen():
'''public int getMaxMatchLen()
'''
pass
def resetResults():
'''public void resetResults()
'''
pass
def createMetaZoneAndPutInCache():
'''public static ZNames createMetaZoneAndPutInCache(final Map<String, ZNames> cache, final String[] names, final String mzID)
'''
pass
def createTimeZoneAndPutInCache():
'''public static ZNames createTimeZoneAndPutInCache(final Map<String, ZNames> cache, String[] names, final String tzID)
'''
pass
def getName():
'''public String getName(final NameType type)
'''
pass
def addAsMetaZoneIntoTrie():
'''public void addAsMetaZoneIntoTrie(final String mzID, final TextTrieMap<NameInfo> trie)
'''
pass
def addAsTimeZoneIntoTrie():
'''public void addAsTimeZoneIntoTrie(final String tzID, final TextTrieMap<NameInfo> trie)
'''
pass
