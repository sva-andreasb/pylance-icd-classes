def RouteSpecificPool():
    '''    public RouteSpecificPool(final HttpRoute route, final int maxEntries)
    public RouteSpecificPool(final HttpRoute route, final ConnPerRoute connPerRoute)
    '''
def getMaxForRoute():
    '''    public int getMaxForRoute(final HttpRoute unused)
    '''
def getRoute():
    '''    public final HttpRoute getRoute()
    '''
def getMaxEntries():
    '''    public final int getMaxEntries()
    '''
def isUnused():
    '''    public boolean isUnused()
    '''
def getCapacity():
    '''    public int getCapacity()
    '''
def getEntryCount():
    '''    public final int getEntryCount()
    '''
def allocEntry():
    '''    public BasicPoolEntry allocEntry(final Object state)
    '''
def freeEntry():
    '''    public void freeEntry(final BasicPoolEntry entry)
    '''
def createdEntry():
    '''    public void createdEntry(final BasicPoolEntry entry)
    '''
def deleteEntry():
    '''    public boolean deleteEntry(final BasicPoolEntry entry)
    '''
def dropEntry():
    '''    public void dropEntry()
    '''
def queueThread():
    '''    public void queueThread(final WaitingThread wt)
    '''
def hasThread():
    '''    public boolean hasThread()
    '''
def nextThread():
    '''    public WaitingThread nextThread()
    '''
def removeThread():
    '''    public void removeThread(final WaitingThread wt)
    '''
