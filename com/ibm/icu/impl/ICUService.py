def ICUService():
'''public ICUService()
public ICUService(final String name)
'''
pass
def get():
'''public Object get(final String descriptor)
public Object get(final String descriptor, final String[] actualReturn)
'''
pass
def getKey():
'''public Object getKey(final Key key)
public Object getKey(final Key key, final String[] actualReturn)
public Object getKey(final Key key, final String[] actualReturn, final Factory factory)
'''
pass
def getVisibleIDs():
'''public Set<String> getVisibleIDs()
public Set<String> getVisibleIDs(final String matchID)
'''
pass
def getDisplayName():
'''public String getDisplayName(final String id)
public String getDisplayName(final String id, final ULocale locale)
public String getDisplayName(final String identifier, final ULocale locale)
'''
pass
def getDisplayNames():
'''public SortedMap<String, String> getDisplayNames()
public SortedMap<String, String> getDisplayNames(final ULocale locale)
public SortedMap<String, String> getDisplayNames(final ULocale locale, final Comparator<Object> com)
public SortedMap<String, String> getDisplayNames(final ULocale locale, final String matchID)
public SortedMap<String, String> getDisplayNames(final ULocale locale, final Comparator<Object> com, final String matchID)
'''
pass
def factories():
'''public final List<Factory> factories()
'''
pass
def registerObject():
'''public Factory registerObject(final Object obj, final String id)
public Factory registerObject(final Object obj, final String id, final boolean visible)
'''
pass
def registerFactory():
'''public final Factory registerFactory(final Factory factory)
'''
pass
def unregisterFactory():
'''public final boolean unregisterFactory(final Factory factory)
'''
pass
def reset():
'''public final void reset()
'''
pass
def isDefault():
'''public boolean isDefault()
'''
pass
def createKey():
'''public Key createKey(final String id)
'''
pass
def stats():
'''public String stats()
'''
pass
def getName():
'''public String getName()
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def Key():
'''public Key(final String id)
'''
pass
def id():
'''public final String id()
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
def fallback():
'''public boolean fallback()
'''
pass
def isFallbackOf():
'''public boolean isFallbackOf(final String idToCheck)
'''
pass
def SimpleFactory():
'''public SimpleFactory(final Object instance, final String id)
public SimpleFactory(final Object instance, final String id, final boolean visible)
'''
pass
def create():
'''public Object create(final Key key, final ICUService service)
'''
pass
def updateVisibleIDs():
'''public void updateVisibleIDs(final Map<String, Factory> result)
'''
pass
