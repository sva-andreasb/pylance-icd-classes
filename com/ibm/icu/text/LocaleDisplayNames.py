def getInstance():
'''public static LocaleDisplayNames getInstance(final ULocale locale)
public static LocaleDisplayNames getInstance(final Locale locale)
public static LocaleDisplayNames getInstance(final ULocale locale, final DialectHandling dialectHandling)
public static LocaleDisplayNames getInstance(final ULocale locale, final DisplayContext... contexts)
public static LocaleDisplayNames getInstance(final Locale locale, final DisplayContext... contexts)
'''
pass
def scriptDisplayNameInContext():
'''public String scriptDisplayNameInContext(final String script)
'''
pass
def getUiList():
'''public List<UiListItem> getUiList(final Set<ULocale> localeSet, final boolean inSelf, final Comparator<Object> collator)
'''
pass
def UiListItem():
'''public UiListItem(final ULocale minimized, final ULocale modified, final String nameInDisplayLocale, final String nameInSelf)
'''
pass
def equals():
'''public boolean equals(final Object obj)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def toString():
'''public String toString()
'''
pass
def getComparator():
'''public static Comparator<UiListItem> getComparator(final Comparator<Object> comparator, final boolean inSelf)
'''
pass
def compare():
'''public int compare(final UiListItem o1, final UiListItem o2)
'''
pass
def getLocale():
'''public ULocale getLocale()
'''
pass
def getDialectHandling():
'''public DialectHandling getDialectHandling()
'''
pass
def getContext():
'''public DisplayContext getContext(final DisplayContext.Type type)
'''
pass
def localeDisplayName():
'''public String localeDisplayName(final ULocale locale)
public String localeDisplayName(final Locale locale)
public String localeDisplayName(final String localeId)
'''
pass
def languageDisplayName():
'''public String languageDisplayName(final String lang)
'''
pass
def scriptDisplayName():
'''public String scriptDisplayName(final String script)
public String scriptDisplayName(final int scriptCode)
'''
pass
def regionDisplayName():
'''public String regionDisplayName(final String region)
'''
pass
def variantDisplayName():
'''public String variantDisplayName(final String variant)
'''
pass
def keyDisplayName():
'''public String keyDisplayName(final String key)
'''
pass
def keyValueDisplayName():
'''public String keyValueDisplayName(final String key, final String value)
'''
pass
def getUiListCompareWholeItems():
'''public List<UiListItem> getUiListCompareWholeItems(final Set<ULocale> localeSet, final Comparator<UiListItem> comparator)
'''
pass
