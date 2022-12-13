def TZDBTimeZoneNames():
'''public TZDBTimeZoneNames(final ULocale loc)
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
def find():
'''public Collection<MatchInfo> find(final CharSequence text, final int start, final EnumSet<NameType> nameTypes)
'''
pass
def handlePrefixMatch():
'''public boolean handlePrefixMatch(final int matchLength, final Iterator<TZDBNameInfo> values)
'''
pass
def getMatches():
'''public Collection<MatchInfo> getMatches()
'''
pass
