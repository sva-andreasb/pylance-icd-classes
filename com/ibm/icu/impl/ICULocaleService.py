KIND_ANY = "int  -1"
VISIBLE = "boolean  true"
INVISIBLE = "boolean  false"
def ICULocaleService():
    '''    public ICULocaleService()
    public ICULocaleService(final String name)
    '''
def get():
    '''    public Object get(final ULocale locale)
    public Object get(final ULocale locale, final int kind)
    public Object get(final ULocale locale, final ULocale[] actualReturn)
    public Object get(final ULocale locale, final int kind, final ULocale[] actualReturn)
    '''
def registerObject():
    '''    public Factory registerObject(final Object obj, final ULocale locale)
    public Factory registerObject(final Object obj, final ULocale locale, final boolean visible)
    public Factory registerObject(final Object obj, final ULocale locale, final int kind)
    public Factory registerObject(final Object obj, final ULocale locale, final int kind, final boolean visible)
    '''
def getAvailableLocales():
    '''    public Locale[] getAvailableLocales()
    '''
def getAvailableULocales():
    '''    public ULocale[] getAvailableULocales()
    '''
def validateFallbackLocale():
    '''    public String validateFallbackLocale()
    '''
def createKey():
    '''    public Key createKey(final String id)
    public Key createKey(final String id, final int kind)
    public Key createKey(final ULocale l, final int kind)
    '''
def createWithCanonicalFallback():
    '''    public static LocaleKey createWithCanonicalFallback(final String primaryID, final String canonicalFallbackID)
    public static LocaleKey createWithCanonicalFallback(final String primaryID, final String canonicalFallbackID, final int kind)
    '''
def createWithCanonical():
    '''    public static LocaleKey createWithCanonical(final ULocale locale, final String canonicalFallbackID, final int kind)
    '''
def prefix():
    '''    public String prefix()
    '''
def kind():
    '''    public int kind()
    '''
def canonicalID():
    '''    public String canonicalID()
    '''
def currentID():
    '''    public String currentID()
    '''
def currentDescriptor():
    '''    public String currentDescriptor()
    '''
def canonicalLocale():
    '''    public ULocale canonicalLocale()
    '''
def currentLocale():
    '''    public ULocale currentLocale()
    '''
def fallback():
    '''    public boolean fallback()
    '''
def isFallbackOf():
    '''    public boolean isFallbackOf(final String id)
    '''
def create():
    '''    public Object create(final Key key, final ICUService service)
    public Object create(final Key key, final ICUService service)
    '''
def updateVisibleIDs():
    '''    public void updateVisibleIDs(final Map<String, Factory> result)
    public void updateVisibleIDs(final Map<String, Factory> result)
    public void updateVisibleIDs(final Map<String, Factory> result)
    '''
def getDisplayName():
    '''    public String getDisplayName(final String id, final ULocale locale)
    '''
def toString():
    '''    public String toString()
    public String toString()
    public String toString()
    '''
def SimpleLocaleKeyFactory():
    '''    public SimpleLocaleKeyFactory(final Object obj, final ULocale locale, final int kind, final boolean visible)
    public SimpleLocaleKeyFactory(final Object obj, final ULocale locale, final int kind, final boolean visible, final String name)
    '''
def ICUResourceBundleFactory():
    '''    public ICUResourceBundleFactory()
    public ICUResourceBundleFactory(final String bundleName)
    '''
