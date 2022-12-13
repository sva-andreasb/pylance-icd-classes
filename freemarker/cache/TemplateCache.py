def TemplateCache():
    '''    public TemplateCache()
    public TemplateCache(final TemplateLoader templateLoader)
    public TemplateCache(final TemplateLoader templateLoader, final CacheStorage cacheStorage)
    public TemplateCache(final TemplateLoader templateLoader, final Configuration config)
    public TemplateCache(final TemplateLoader templateLoader, final CacheStorage cacheStorage, final Configuration config)
    public TemplateCache(final TemplateLoader templateLoader, final CacheStorage cacheStorage, final TemplateLookupStrategy templateLookupStrategy, final TemplateNameFormat templateNameFormat, final Configuration config)
    '''
def setConfiguration():
    '''    public void setConfiguration(final Configuration config)
    '''
def getTemplateLoader():
    '''    public TemplateLoader getTemplateLoader()
    '''
def getCacheStorage():
    '''    public CacheStorage getCacheStorage()
    '''
def getTemplateLookupStrategy():
    '''    public TemplateLookupStrategy getTemplateLookupStrategy()
    '''
def getTemplateNameFormat():
    '''    public TemplateNameFormat getTemplateNameFormat()
    '''
def getTemplate():
    '''    public MaybeMissingTemplate getTemplate(String name, final Locale locale, final Object customLookupCondition, final String encoding, final boolean parseAsFTL)
    public Template getTemplate(final String name, final Locale locale, final String encoding, final boolean parseAsFTL)
    public Template getTemplate()
    '''
def getDelay():
    '''    public long getDelay()
    '''
def setDelay():
    '''    public void setDelay(final long delay)
    '''
def getLocalizedLookup():
    '''    public boolean getLocalizedLookup()
    '''
def setLocalizedLookup():
    '''    public void setLocalizedLookup(final boolean localizedLookup)
    '''
def clear():
    '''    public void clear()
    '''
def removeTemplate():
    '''    public void removeTemplate(final String name, final Locale locale, final String encoding, final boolean parse)
    public void removeTemplate(String name, final Locale locale, final Object customLookupCondition, final String encoding, final boolean parse)
    '''
def getFullTemplatePath():
    '''    public static String getFullTemplatePath(final Environment env, final String baseName, final String targetName)
    '''
def equals():
    '''    public boolean equals(final Object o)
    '''
def hashCode():
    '''    public int hashCode()
    '''
def cloneCachedTemplate():
    '''    public CachedTemplate cloneCachedTemplate()
    '''
def lookupWithAcquisitionStrategy():
    '''    public TemplateLookupResult lookupWithAcquisitionStrategy(final String name)
    '''
def lookupWithLocalizedThenAcquisitionStrategy():
    '''    public TemplateLookupResult lookupWithLocalizedThenAcquisitionStrategy(final String templateName, final Locale templateLocale)
    '''
def getMissingTemplateReason():
    '''    public String getMissingTemplateReason()
    '''
def getMissingTemplateNormalizedName():
    '''    public String getMissingTemplateNormalizedName()
    '''
