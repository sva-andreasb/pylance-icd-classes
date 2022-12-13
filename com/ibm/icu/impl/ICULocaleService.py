KIND_ANY = "int  -1"
VISIBLE = "boolean  true"
INVISIBLE = "boolean  false"
def ICULocaleService():
'''public ICULocaleService()
public ICULocaleService(final String name)
'''
pass
def get():
'''public Object get(final ULocale locale)
public Object get(final ULocale locale, final int kind)
public Object get(final ULocale locale, final ULocale[] actualReturn)
public Object get(final ULocale locale, final int kind, final ULocale[] actualReturn)
'''
pass
def registerObject():
'''public Factory registerObject(final Object obj, final ULocale locale)
public Factory registerObject(final Object obj, final ULocale locale, final boolean visible)
public Factory registerObject(final Object obj, final ULocale locale, final int kind)
public Factory registerObject(final Object obj, final ULocale locale, final int kind, final boolean visible)
'''
pass
def getAvailableLocales():
'''public Locale[] getAvailableLocales()
'''
pass
def getAvailableULocales():
'''public ULocale[] getAvailableULocales()
'''
pass
def validateFallbackLocale():
'''public String validateFallbackLocale()
'''
pass
def createKey():
'''public Key createKey(final String id)
public Key createKey(final String id, final int kind)
public Key createKey(final ULocale l, final int kind)
'''
pass
def createWithCanonicalFallback():
'''public static LocaleKey createWithCanonicalFallback(final String primaryID, final String canonicalFallbackID)
public static LocaleKey createWithCanonicalFallback(final String primaryID, final String canonicalFallbackID, final int kind)
'''
pass
def createWithCanonical():
'''public static LocaleKey createWithCanonical(final ULocale locale, final String canonicalFallbackID, final int kind)
'''
pass
def prefix():
'''public String prefix()
'''
pass
def kind():
'''public int kind()
'''
pass
def canonicalID():
'''public String canonicalID()
'''
pass
def currentID():
'''public String currentID()
'''
pass
def currentDescriptor():
'''public String currentDescriptor()
'''
pass
def canonicalLocale():
'''public ULocale canonicalLocale()
'''
pass
def currentLocale():
'''public ULocale currentLocale()
'''
pass
def fallback():
'''public boolean fallback()
'''
pass
def isFallbackOf():
'''public boolean isFallbackOf(final String id)
'''
pass
def create():
'''public Object create(final Key key, final ICUService service)
public Object create(final Key key, final ICUService service)
'''
pass
def updateVisibleIDs():
'''public void updateVisibleIDs(final Map<String, Factory> result)
public void updateVisibleIDs(final Map<String, Factory> result)
public void updateVisibleIDs(final Map<String, Factory> result)
'''
pass
def getDisplayName():
'''public String getDisplayName(final String id, final ULocale locale)
'''
pass
def toString():
'''public String toString()
public String toString()
public String toString()
'''
pass
def SimpleLocaleKeyFactory():
'''public SimpleLocaleKeyFactory(final Object obj, final ULocale locale, final int kind, final boolean visible)
public SimpleLocaleKeyFactory(final Object obj, final ULocale locale, final int kind, final boolean visible, final String name)
'''
pass
def ICUResourceBundleFactory():
'''public ICUResourceBundleFactory()
public ICUResourceBundleFactory(final String bundleName)
'''
pass
