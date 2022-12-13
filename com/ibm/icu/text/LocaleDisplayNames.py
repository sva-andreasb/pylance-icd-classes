def getInstance():
    '''    public static LocaleDisplayNames getInstance(final ULocale locale)
    public static LocaleDisplayNames getInstance(final Locale locale)
    public static LocaleDisplayNames getInstance(final ULocale locale, final DialectHandling dialectHandling)
    public static LocaleDisplayNames getInstance(final ULocale locale, final DisplayContext... contexts)
    public static LocaleDisplayNames getInstance(final Locale locale, final DisplayContext... contexts)
    '''
def scriptDisplayNameInContext():
    '''    public String scriptDisplayNameInContext(final String script)
    '''
def getUiList():
    '''    public List<UiListItem> getUiList(final Set<ULocale> localeSet, final boolean inSelf, final Comparator<Object> collator)
    '''
def UiListItem():
    '''    public UiListItem(final ULocale minimized, final ULocale modified, final String nameInDisplayLocale, final String nameInSelf)
    '''
def equals():
    '''    public boolean equals(final Object obj)
    '''
def hashCode():
    '''    public int hashCode()
    '''
def toString():
    '''    public String toString()
    '''
def getComparator():
    '''    public static Comparator<UiListItem> getComparator(final Comparator<Object> comparator, final boolean inSelf)
    '''
def compare():
    '''    public int compare(final UiListItem o1, final UiListItem o2)
    '''
def getLocale():
    '''    public ULocale getLocale()
    '''
def getDialectHandling():
    '''    public DialectHandling getDialectHandling()
    '''
def getContext():
    '''    public DisplayContext getContext(final DisplayContext.Type type)
    '''
def localeDisplayName():
    '''    public String localeDisplayName(final ULocale locale)
    public String localeDisplayName(final Locale locale)
    public String localeDisplayName(final String localeId)
    '''
def languageDisplayName():
    '''    public String languageDisplayName(final String lang)
    '''
def scriptDisplayName():
    '''    public String scriptDisplayName(final String script)
    public String scriptDisplayName(final int scriptCode)
    '''
def regionDisplayName():
    '''    public String regionDisplayName(final String region)
    '''
def variantDisplayName():
    '''    public String variantDisplayName(final String variant)
    '''
def keyDisplayName():
    '''    public String keyDisplayName(final String key)
    '''
def keyValueDisplayName():
    '''    public String keyValueDisplayName(final String key, final String value)
    '''
def getUiListCompareWholeItems():
    '''    public List<UiListItem> getUiListCompareWholeItems(final Set<ULocale> localeSet, final Comparator<UiListItem> comparator)
    '''
