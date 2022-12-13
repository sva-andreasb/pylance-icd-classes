def TemplateCache():
'''public TemplateCache()
public TemplateCache(final TemplateLoader templateLoader)
public TemplateCache(final TemplateLoader templateLoader, final CacheStorage cacheStorage)
public TemplateCache(final TemplateLoader templateLoader, final Configuration config)
public TemplateCache(final TemplateLoader templateLoader, final CacheStorage cacheStorage, final Configuration config)
public TemplateCache(final TemplateLoader templateLoader, final CacheStorage cacheStorage, final TemplateLookupStrategy templateLookupStrategy, final TemplateNameFormat templateNameFormat, final Configuration config)
'''
pass
def setConfiguration():
'''public void setConfiguration(final Configuration config)
'''
pass
def getTemplateLoader():
'''public TemplateLoader getTemplateLoader()
'''
pass
def getCacheStorage():
'''public CacheStorage getCacheStorage()
'''
pass
def getTemplateLookupStrategy():
'''public TemplateLookupStrategy getTemplateLookupStrategy()
'''
pass
def getTemplateNameFormat():
'''public TemplateNameFormat getTemplateNameFormat()
'''
pass
def getTemplate():
'''public MaybeMissingTemplate getTemplate(String name, final Locale locale, final Object customLookupCondition, final String encoding, final boolean parseAsFTL)
public Template getTemplate(final String name, final Locale locale, final String encoding, final boolean parseAsFTL)
public Template getTemplate()
'''
pass
def getDelay():
'''public long getDelay()
'''
pass
def setDelay():
'''public void setDelay(final long delay)
'''
pass
def getLocalizedLookup():
'''public boolean getLocalizedLookup()
'''
pass
def setLocalizedLookup():
'''public void setLocalizedLookup(final boolean localizedLookup)
'''
pass
def clear():
'''public void clear()
'''
pass
def removeTemplate():
'''public void removeTemplate(final String name, final Locale locale, final String encoding, final boolean parse)
public void removeTemplate(String name, final Locale locale, final Object customLookupCondition, final String encoding, final boolean parse)
'''
pass
def getFullTemplatePath():
'''public static String getFullTemplatePath(final Environment env, final String baseName, final String targetName)
'''
pass
def equals():
'''public boolean equals(final Object o)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def cloneCachedTemplate():
'''public CachedTemplate cloneCachedTemplate()
'''
pass
def lookupWithAcquisitionStrategy():
'''public TemplateLookupResult lookupWithAcquisitionStrategy(final String name)
'''
pass
def lookupWithLocalizedThenAcquisitionStrategy():
'''public TemplateLookupResult lookupWithLocalizedThenAcquisitionStrategy(final String templateName, final Locale templateLocale)
'''
pass
def getMissingTemplateReason():
'''public String getMissingTemplateReason()
'''
pass
def getMissingTemplateNormalizedName():
'''public String getMissingTemplateNormalizedName()
'''
pass
