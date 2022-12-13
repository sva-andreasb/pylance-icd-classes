def TimeZoneGenericNames():
    '''    public TimeZoneGenericNames(final ULocale locale, final TimeZoneNames tznames)
    '''
def getInstance():
    '''    public static TimeZoneGenericNames getInstance(final ULocale locale)
    '''
def getDisplayName():
    '''    public String getDisplayName(final TimeZone tz, final GenericNameType type, final long date)
    '''
def getGenericLocationName():
    '''    public String getGenericLocationName(String canonicalTzID)
    '''
def setFormatPattern():
    '''    public TimeZoneGenericNames setFormatPattern(final Pattern patType, final String patStr)
    '''
def findBestMatch():
    '''    public GenericMatchInfo findBestMatch(final String text, final int start, final EnumSet<GenericNameType> genericTypes)
    '''
def find():
    '''    public Collection<GenericMatchInfo> find(final String text, final int start, final EnumSet<GenericNameType> genericTypes)
    '''
def isFrozen():
    '''    public boolean isFrozen()
    '''
def freeze():
    '''    public TimeZoneGenericNames freeze()
    '''
def cloneAsThawed():
    '''    public TimeZoneGenericNames cloneAsThawed()
    '''
def isFallbackTypeOf():
    '''    public boolean isFallbackTypeOf(final GenericNameType type)
    '''
def nameType():
    '''    public GenericNameType nameType()
    '''
def tzID():
    '''    public String tzID()
    '''
def matchLength():
    '''    public int matchLength()
    '''
def handlePrefixMatch():
    '''    public boolean handlePrefixMatch(final int matchLength, final Iterator<NameInfo> values)
    '''
def getMatches():
    '''    public Collection<GenericMatchInfo> getMatches()
    '''
def getMaxMatchLen():
    '''    public int getMaxMatchLen()
    '''
def resetResults():
    '''    public void resetResults()
    '''
