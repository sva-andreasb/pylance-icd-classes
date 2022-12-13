def TimeZoneGenericNames():
'''public TimeZoneGenericNames(final ULocale locale, final TimeZoneNames tznames)
'''
pass
def getInstance():
'''public static TimeZoneGenericNames getInstance(final ULocale locale)
'''
pass
def getDisplayName():
'''public String getDisplayName(final TimeZone tz, final GenericNameType type, final long date)
'''
pass
def getGenericLocationName():
'''public String getGenericLocationName(String canonicalTzID)
'''
pass
def setFormatPattern():
'''public TimeZoneGenericNames setFormatPattern(final Pattern patType, final String patStr)
'''
pass
def findBestMatch():
'''public GenericMatchInfo findBestMatch(final String text, final int start, final EnumSet<GenericNameType> genericTypes)
'''
pass
def find():
'''public Collection<GenericMatchInfo> find(final String text, final int start, final EnumSet<GenericNameType> genericTypes)
'''
pass
def isFrozen():
'''public boolean isFrozen()
'''
pass
def freeze():
'''public TimeZoneGenericNames freeze()
'''
pass
def cloneAsThawed():
'''public TimeZoneGenericNames cloneAsThawed()
'''
pass
def isFallbackTypeOf():
'''public boolean isFallbackTypeOf(final GenericNameType type)
'''
pass
def nameType():
'''public GenericNameType nameType()
'''
pass
def tzID():
'''public String tzID()
'''
pass
def matchLength():
'''public int matchLength()
'''
pass
def handlePrefixMatch():
'''public boolean handlePrefixMatch(final int matchLength, final Iterator<NameInfo> values)
'''
pass
def getMatches():
'''public Collection<GenericMatchInfo> getMatches()
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
