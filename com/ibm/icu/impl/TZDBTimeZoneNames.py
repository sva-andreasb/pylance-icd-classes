def TZDBTimeZoneNames():
    '''    public TZDBTimeZoneNames(final ULocale loc)
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
def find():
    '''    public Collection<MatchInfo> find(final CharSequence text, final int start, final EnumSet<NameType> nameTypes)
    '''
def handlePrefixMatch():
    '''    public boolean handlePrefixMatch(final int matchLength, final Iterator<TZDBNameInfo> values)
    '''
def getMatches():
    '''    public Collection<MatchInfo> getMatches()
    '''
