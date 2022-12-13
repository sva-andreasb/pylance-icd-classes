def builder():
'''public static Builder builder()
'''
pass
def LocaleMatcher():
'''public LocaleMatcher(final LocalePriorityList supportedLocales)
public LocaleMatcher(final String supportedLocales)
'''
pass
def getBestMatch():
'''public ULocale getBestMatch(final ULocale desiredLocale)
public ULocale getBestMatch(final Iterable<ULocale> desiredLocales)
public ULocale getBestMatch(final String desiredLocaleList)
'''
pass
def getBestLocale():
'''public Locale getBestLocale(final Locale desiredLocale)
public Locale getBestLocale(final Iterable<Locale> desiredLocales)
'''
pass
def getBestMatchResult():
'''public Result getBestMatchResult(final ULocale desiredLocale)
public Result getBestMatchResult(final Iterable<ULocale> desiredLocales)
'''
pass
def getBestLocaleResult():
'''public Result getBestLocaleResult(final Locale desiredLocale)
public Result getBestLocaleResult(final Iterable<Locale> desiredLocales)
'''
pass
def match():
'''public double match(final ULocale desired, final ULocale desiredMax, final ULocale supported, final ULocale supportedMax)
'''
pass
def canonicalize():
'''public ULocale canonicalize(final ULocale locale)
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def remove():
'''public void remove()
'''
pass
def getDesiredULocale():
'''public ULocale getDesiredULocale()
'''
pass
def getDesiredLocale():
'''public Locale getDesiredLocale()
'''
pass
def getSupportedULocale():
'''public ULocale getSupportedULocale()
'''
pass
def getSupportedLocale():
'''public Locale getSupportedLocale()
'''
pass
def getDesiredIndex():
'''public int getDesiredIndex()
'''
pass
def getSupportedIndex():
'''public int getSupportedIndex()
'''
pass
def makeResolvedULocale():
'''public ULocale makeResolvedULocale()
'''
pass
def makeResolvedLocale():
'''public Locale makeResolvedLocale()
'''
pass
def setSupportedLocales():
'''public Builder setSupportedLocales(final String locales)
public Builder setSupportedLocales(final Collection<Locale> locales)
'''
pass
def setSupportedULocales():
'''public Builder setSupportedULocales(final Collection<ULocale> locales)
'''
pass
def addSupportedULocale():
'''public Builder addSupportedULocale(final ULocale locale)
'''
pass
def addSupportedLocale():
'''public Builder addSupportedLocale(final Locale locale)
'''
pass
def setDefaultULocale():
'''public Builder setDefaultULocale(final ULocale defaultLocale)
'''
pass
def setDefaultLocale():
'''public Builder setDefaultLocale(final Locale defaultLocale)
'''
pass
def setFavorSubtag():
'''public Builder setFavorSubtag(final FavorSubtag subtag)
'''
pass
def setDemotionPerDesiredLocale():
'''public Builder setDemotionPerDesiredLocale(final Demotion demotion)
'''
pass
def setDirection():
'''public Builder setDirection(final Direction direction)
'''
pass
def internalSetThresholdDistance():
'''public Builder internalSetThresholdDistance(int thresholdDistance)
'''
pass
def build():
'''public LocaleMatcher build()
'''
pass
def hasNext():
'''public boolean hasNext()
public boolean hasNext()
'''
pass
def next():
'''public LSR next()
public LSR next()
'''
pass
def rememberCurrent():
'''public void rememberCurrent(final int desiredIndex)
public void rememberCurrent(final int desiredIndex)
'''
pass
