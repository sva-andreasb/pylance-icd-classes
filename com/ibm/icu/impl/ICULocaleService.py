KIND_ANY = "int  -1"
VISIBLE = "boolean  true"
INVISIBLE = "boolean  false"
def ():
    '''returns ICUResourceBundleFactory\n\n
    ()\n
    (final String name)\n
    (final Object obj, final ULocale locale, final int kind, final boolean visible)\n
    (final Object obj, final ULocale locale, final int kind, final boolean visible, final String name)\n
    ()\n
    (final String bundleName)\n
    '''
def get():
    '''returns Object\n\n
    get(final ULocale locale)\n
    get(final ULocale locale, final int kind)\n
    get(final ULocale locale, final ULocale[] actualReturn)\n
    get(final ULocale locale, final int kind, final ULocale[] actualReturn)\n
    '''
def registerObject():
    '''returns Factory\n\n
    registerObject(final Object obj, final ULocale locale)\n
    registerObject(final Object obj, final ULocale locale, final boolean visible)\n
    registerObject(final Object obj, final ULocale locale, final int kind)\n
    registerObject(final Object obj, final ULocale locale, final int kind, final boolean visible)\n
    '''
def getAvailableLocales():
    '''returns Locale[]\n\n
    getAvailableLocales()\n
    '''
def getAvailableULocales():
    '''returns ULocale[]\n\n
    getAvailableULocales()\n
    '''
def validateFallbackLocale():
    '''returns String\n\n
    validateFallbackLocale()\n
    '''
def createKey():
    '''returns Key\n\n
    createKey(final String id)\n
    createKey(final String id, final int kind)\n
    createKey(final ULocale l, final int kind)\n
    '''
def prefix():
    '''returns String\n\n
    prefix()\n
    '''
def kind():
    '''returns int\n\n
    kind()\n
    '''
def canonicalID():
    '''returns String\n\n
    canonicalID()\n
    '''
def currentID():
    '''returns String\n\n
    currentID()\n
    '''
def currentDescriptor():
    '''returns String\n\n
    currentDescriptor()\n
    '''
def canonicalLocale():
    '''returns ULocale\n\n
    canonicalLocale()\n
    '''
def currentLocale():
    '''returns ULocale\n\n
    currentLocale()\n
    '''
def fallback():
    '''returns boolean\n\n
    fallback()\n
    '''
def isFallbackOf():
    '''returns boolean\n\n
    isFallbackOf(final String id)\n
    '''
def create():
    '''returns Object\n\n
    create(final Key key, final ICUService service)\n
    create(final Key key, final ICUService service)\n
    '''
def updateVisibleIDs():
    '''returns None\n\n
    updateVisibleIDs(final Map<String, Factory> result)\n
    updateVisibleIDs(final Map<String, Factory> result)\n
    updateVisibleIDs(final Map<String, Factory> result)\n
    '''
def getDisplayName():
    '''returns String\n\n
    getDisplayName(final String id, final ULocale locale)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    toString()\n
    '''
