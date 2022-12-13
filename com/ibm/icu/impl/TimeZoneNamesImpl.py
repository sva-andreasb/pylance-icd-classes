NUM_NAME_TYPES = "int  7"
def TimeZoneNamesImpl():
    '''    public TimeZoneNamesImpl(final ULocale locale)
    '''
def getAvailableMetaZoneIDs():
    '''    public Set<String> getAvailableMetaZoneIDs()
    public Set<String> getAvailableMetaZoneIDs(final String tzID)
    '''
def getMetaZoneID():
    '''    public String getMetaZoneID(final String tzID, final long date)
    '''
def getReferenceZoneID():
    '''    public String getReferenceZoneID(final String mzID, final String region)
    '''
def getMetaZoneDisplayName():
    '''    public String getMetaZoneDisplayName(final String mzID, final NameType type)
    '''
def getTimeZoneDisplayName():
    '''    public String getTimeZoneDisplayName(final String tzID, final NameType type)
    '''
def getExemplarLocationName():
    '''    public String getExemplarLocationName(final String tzID)
    '''
def find():
    '''    public synchronized Collection<MatchInfo> find(final CharSequence text, final int start, final EnumSet<NameType> nameTypes)
    '''
def loadAllDisplayNames():
    '''    public synchronized void loadAllDisplayNames()
    '''
def getDisplayNames():
    '''    public void getDisplayNames(final String tzID, final NameType[] types, final long date, final String[] dest, final int destOffset)
    '''
def getDefaultExemplarLocationName():
    '''    public static String getDefaultExemplarLocationName(final String tzID)
    '''
def put():
    '''    public void put(final UResource.Key key, final UResource.Value value, final boolean noFallback)
    public void put(final UResource.Key key, final UResource.Value value, final boolean noFallback)
    '''
def handlePrefixMatch():
    '''    public boolean handlePrefixMatch(final int matchLength, final Iterator<NameInfo> values)
    '''
def getMatches():
    '''    public Collection<MatchInfo> getMatches()
    '''
def getMaxMatchLen():
    '''    public int getMaxMatchLen()
    '''
def resetResults():
    '''    public void resetResults()
    '''
def createMetaZoneAndPutInCache():
    '''    public static ZNames createMetaZoneAndPutInCache(final Map<String, ZNames> cache, final String[] names, final String mzID)
    '''
def createTimeZoneAndPutInCache():
    '''    public static ZNames createTimeZoneAndPutInCache(final Map<String, ZNames> cache, String[] names, final String tzID)
    '''
def getName():
    '''    public String getName(final NameType type)
    '''
def addAsMetaZoneIntoTrie():
    '''    public void addAsMetaZoneIntoTrie(final String mzID, final TextTrieMap<NameInfo> trie)
    '''
def addAsTimeZoneIntoTrie():
    '''    public void addAsTimeZoneIntoTrie(final String tzID, final TextTrieMap<NameInfo> trie)
    '''
