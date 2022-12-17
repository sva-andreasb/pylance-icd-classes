def ():
    '''returns TimeZoneGenericNames\n\n
    (final ULocale locale, final TimeZoneNames tznames)\n
    '''
def getDisplayName():
    '''returns String\n\n
    getDisplayName(final TimeZone tz, final GenericNameType type, final long date)\n
    '''
def getGenericLocationName():
    '''returns String\n\n
    getGenericLocationName(String canonicalTzID)\n
    '''
def setFormatPattern():
    '''returns TimeZoneGenericNames\n\n
    setFormatPattern(final Pattern patType, final String patStr)\n
    '''
def findBestMatch():
    '''returns GenericMatchInfo\n\n
    findBestMatch(final String text, final int start, final EnumSet<GenericNameType> genericTypes)\n
    '''
def find():
    '''returns Collection<GenericMatchInfo>\n\n
    find(final String text, final int start, final EnumSet<GenericNameType> genericTypes)\n
    '''
def isFrozen():
    '''returns boolean\n\n
    isFrozen()\n
    '''
def freeze():
    '''returns TimeZoneGenericNames\n\n
    freeze()\n
    '''
def cloneAsThawed():
    '''returns TimeZoneGenericNames\n\n
    cloneAsThawed()\n
    '''
def isFallbackTypeOf():
    '''returns boolean\n\n
    isFallbackTypeOf(final GenericNameType type)\n
    '''
def nameType():
    '''returns GenericNameType\n\n
    nameType()\n
    '''
def tzID():
    '''returns String\n\n
    tzID()\n
    '''
def matchLength():
    '''returns int\n\n
    matchLength()\n
    '''
def handlePrefixMatch():
    '''returns boolean\n\n
    handlePrefixMatch(final int matchLength, final Iterator<NameInfo> values)\n
    '''
def getMatches():
    '''returns Collection<GenericMatchInfo>\n\n
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
