def WioObject():
    '''    public WioObject(final STWatchedObject watchedObject, final short type)
    public WioObject(final STWatchedObject watchedObject, final STGroup stGroup)
    '''
def setStatus():
    '''    public void setStatus(final short n, final String s)
    '''
def addWatch():
    '''    public void addWatch(final Integer n)
    public void addWatch(final STGroup stGroup)
    '''
def removeWatch():
    '''    public void removeWatch(final Integer key)
    public void removeWatch(final STGroup key)
    '''
def isWatched():
    '''    public boolean isWatched(final Integer key)
    public boolean isWatched(final Object key)
    public boolean isWatched()
    '''
def getWatchingSessions():
    '''    public Enumeration getWatchingSessions()
    '''
def getWatchingGroups():
    '''    public Enumeration getWatchingGroups()
    '''
def dumpToStream():
    '''    public void dumpToStream(final NdrOutputStream ndrOutputStream)
    '''
def isWatchedBySession():
    '''    public boolean isWatchedBySession()
    '''
def getWatchedObject():
    '''    public STWatchedObject getWatchedObject()
    '''
