def ():
    '''returns TemplateCache\n\n
    ()\n
    (final TemplateLoader templateLoader)\n
    (final TemplateLoader templateLoader, final CacheStorage cacheStorage)\n
    (final TemplateLoader templateLoader, final Configuration config)\n
    (final TemplateLoader templateLoader, final CacheStorage cacheStorage, final Configuration config)\n
    (final TemplateLoader templateLoader, final CacheStorage cacheStorage, final TemplateLookupStrategy templateLookupStrategy, final TemplateNameFormat templateNameFormat, final Configuration config)\n
    '''
def setConfiguration():
    '''returns None\n\n
    setConfiguration(final Configuration config)\n
    '''
def getTemplateLoader():
    '''returns TemplateLoader\n\n
    getTemplateLoader()\n
    '''
def getCacheStorage():
    '''returns CacheStorage\n\n
    getCacheStorage()\n
    '''
def getTemplateLookupStrategy():
    '''returns TemplateLookupStrategy\n\n
    getTemplateLookupStrategy()\n
    '''
def getTemplateNameFormat():
    '''returns TemplateNameFormat\n\n
    getTemplateNameFormat()\n
    '''
def getTemplate():
    '''returns Template\n\n
    getTemplate(String name, final Locale locale, final Object customLookupCondition, final String encoding, final boolean parseAsFTL)\n
    getTemplate(final String name, final Locale locale, final String encoding, final boolean parseAsFTL)\n
    getTemplate()\n
    '''
def getDelay():
    '''returns long\n\n
    getDelay()\n
    '''
def setDelay():
    '''returns None\n\n
    setDelay(final long delay)\n
    '''
def getLocalizedLookup():
    '''returns boolean\n\n
    getLocalizedLookup()\n
    '''
def setLocalizedLookup():
    '''returns None\n\n
    setLocalizedLookup(final boolean localizedLookup)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def removeTemplate():
    '''returns None\n\n
    removeTemplate(final String name, final Locale locale, final String encoding, final boolean parse)\n
    removeTemplate(String name, final Locale locale, final Object customLookupCondition, final String encoding, final boolean parse)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def cloneCachedTemplate():
    '''returns CachedTemplate\n\n
    cloneCachedTemplate()\n
    '''
def lookupWithAcquisitionStrategy():
    '''returns TemplateLookupResult\n\n
    lookupWithAcquisitionStrategy(final String name)\n
    '''
def lookupWithLocalizedThenAcquisitionStrategy():
    '''returns TemplateLookupResult\n\n
    lookupWithLocalizedThenAcquisitionStrategy(final String templateName, final Locale templateLocale)\n
    '''
def getMissingTemplateReason():
    '''returns String\n\n
    getMissingTemplateReason()\n
    '''
def getMissingTemplateNormalizedName():
    '''returns String\n\n
    getMissingTemplateNormalizedName()\n
    '''
