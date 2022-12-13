def RouteSpecificPool():
'''public RouteSpecificPool(final HttpRoute route, final int maxEntries)
public RouteSpecificPool(final HttpRoute route, final ConnPerRoute connPerRoute)
'''
pass
def getMaxForRoute():
'''public int getMaxForRoute(final HttpRoute unused)
'''
pass
def getRoute():
'''public final HttpRoute getRoute()
'''
pass
def getMaxEntries():
'''public final int getMaxEntries()
'''
pass
def isUnused():
'''public boolean isUnused()
'''
pass
def getCapacity():
'''public int getCapacity()
'''
pass
def getEntryCount():
'''public final int getEntryCount()
'''
pass
def allocEntry():
'''public BasicPoolEntry allocEntry(final Object state)
'''
pass
def freeEntry():
'''public void freeEntry(final BasicPoolEntry entry)
'''
pass
def createdEntry():
'''public void createdEntry(final BasicPoolEntry entry)
'''
pass
def deleteEntry():
'''public boolean deleteEntry(final BasicPoolEntry entry)
'''
pass
def dropEntry():
'''public void dropEntry()
'''
pass
def queueThread():
'''public void queueThread(final WaitingThread wt)
'''
pass
def hasThread():
'''public boolean hasThread()
'''
pass
def nextThread():
'''public WaitingThread nextThread()
'''
pass
def removeThread():
'''public void removeThread(final WaitingThread wt)
'''
pass
