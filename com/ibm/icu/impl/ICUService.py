def ICUService():
    '''public ICUService()
    public ICUService(final String name)
    '''
def get():
    '''public Object get(final String descriptor)
    public Object get(final String descriptor, final String[] actualReturn)
    '''
def getKey():
    '''public Object getKey(final Key key)
    public Object getKey(final Key key, final String[] actualReturn)
    public Object getKey(final Key key, final String[] actualReturn, final Factory factory)
    '''
def getVisibleIDs():
    '''public Set<String> getVisibleIDs()
    public Set<String> getVisibleIDs(final String matchID)
    '''
def getDisplayName():
    '''public String getDisplayName(final String id)
    public String getDisplayName(final String id, final ULocale locale)
    public String getDisplayName(final String identifier, final ULocale locale)
    '''
def getDisplayNames():
    '''public SortedMap<String, String> getDisplayNames()
    public SortedMap<String, String> getDisplayNames(final ULocale locale)
    public SortedMap<String, String> getDisplayNames(final ULocale locale, final Comparator<Object> com)
    public SortedMap<String, String> getDisplayNames(final ULocale locale, final String matchID)
    public SortedMap<String, String> getDisplayNames(final ULocale locale, final Comparator<Object> com, final String matchID)
    '''
def factories():
    '''public final List<Factory> factories()
    '''
def registerObject():
    '''public Factory registerObject(final Object obj, final String id)
    public Factory registerObject(final Object obj, final String id, final boolean visible)
    '''
def registerFactory():
    '''public final Factory registerFactory(final Factory factory)
    '''
def unregisterFactory():
    '''public final boolean unregisterFactory(final Factory factory)
    '''
def reset():
    '''public final void reset()
    '''
def isDefault():
    '''public boolean isDefault()
    '''
def createKey():
    '''public Key createKey(final String id)
    '''
def stats():
    '''public String stats()
    '''
def getName():
    '''public String getName()
    '''
def toString():
    '''public String toString()
    public String toString()
    '''
def Key():
    '''public Key(final String id)
    '''
def id():
    '''public final String id()
    '''
def canonicalID():
    '''public String canonicalID()
    '''
def currentID():
    '''public String currentID()
    '''
def currentDescriptor():
    '''public String currentDescriptor()
    '''
def fallback():
    '''public boolean fallback()
    '''
def isFallbackOf():
    '''public boolean isFallbackOf(final String idToCheck)
    '''
def SimpleFactory():
    '''public SimpleFactory(final Object instance, final String id)
    public SimpleFactory(final Object instance, final String id, final boolean visible)
    '''
def create():
    '''public Object create(final Key key, final ICUService service)
    '''
def updateVisibleIDs():
    '''public void updateVisibleIDs(final Map<String, Factory> result)
    '''
