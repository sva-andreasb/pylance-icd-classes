def builder():
    '''    public static Builder builder()
    '''
def LocaleMatcher():
    '''    public LocaleMatcher(final LocalePriorityList supportedLocales)
    public LocaleMatcher(final String supportedLocales)
    '''
def getBestMatch():
    '''    public ULocale getBestMatch(final ULocale desiredLocale)
    public ULocale getBestMatch(final Iterable<ULocale> desiredLocales)
    public ULocale getBestMatch(final String desiredLocaleList)
    '''
def getBestLocale():
    '''    public Locale getBestLocale(final Locale desiredLocale)
    public Locale getBestLocale(final Iterable<Locale> desiredLocales)
    '''
def getBestMatchResult():
    '''    public Result getBestMatchResult(final ULocale desiredLocale)
    public Result getBestMatchResult(final Iterable<ULocale> desiredLocales)
    '''
def getBestLocaleResult():
    '''    public Result getBestLocaleResult(final Locale desiredLocale)
    public Result getBestLocaleResult(final Iterable<Locale> desiredLocales)
    '''
def match():
    '''    public double match(final ULocale desired, final ULocale desiredMax, final ULocale supported, final ULocale supportedMax)
    '''
def canonicalize():
    '''    public ULocale canonicalize(final ULocale locale)
    '''
def toString():
    '''    public String toString()
    public String toString()
    '''
def remove():
    '''    public void remove()
    '''
def getDesiredULocale():
    '''    public ULocale getDesiredULocale()
    '''
def getDesiredLocale():
    '''    public Locale getDesiredLocale()
    '''
def getSupportedULocale():
    '''    public ULocale getSupportedULocale()
    '''
def getSupportedLocale():
    '''    public Locale getSupportedLocale()
    '''
def getDesiredIndex():
    '''    public int getDesiredIndex()
    '''
def getSupportedIndex():
    '''    public int getSupportedIndex()
    '''
def makeResolvedULocale():
    '''    public ULocale makeResolvedULocale()
    '''
def makeResolvedLocale():
    '''    public Locale makeResolvedLocale()
    '''
def setSupportedLocales():
    '''    public Builder setSupportedLocales(final String locales)
    public Builder setSupportedLocales(final Collection<Locale> locales)
    '''
def setSupportedULocales():
    '''    public Builder setSupportedULocales(final Collection<ULocale> locales)
    '''
def addSupportedULocale():
    '''    public Builder addSupportedULocale(final ULocale locale)
    '''
def addSupportedLocale():
    '''    public Builder addSupportedLocale(final Locale locale)
    '''
def setDefaultULocale():
    '''    public Builder setDefaultULocale(final ULocale defaultLocale)
    '''
def setDefaultLocale():
    '''    public Builder setDefaultLocale(final Locale defaultLocale)
    '''
def setFavorSubtag():
    '''    public Builder setFavorSubtag(final FavorSubtag subtag)
    '''
def setDemotionPerDesiredLocale():
    '''    public Builder setDemotionPerDesiredLocale(final Demotion demotion)
    '''
def setDirection():
    '''    public Builder setDirection(final Direction direction)
    '''
def internalSetThresholdDistance():
    '''    public Builder internalSetThresholdDistance(int thresholdDistance)
    '''
def build():
    '''    public LocaleMatcher build()
    '''
def hasNext():
    '''    public boolean hasNext()
    public boolean hasNext()
    '''
def next():
    '''    public LSR next()
    public LSR next()
    '''
def rememberCurrent():
    '''    public void rememberCurrent(final int desiredIndex)
    public void rememberCurrent(final int desiredIndex)
    '''
