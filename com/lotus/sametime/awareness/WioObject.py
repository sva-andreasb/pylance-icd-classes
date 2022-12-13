def WioObject():
'''public WioObject(final STWatchedObject watchedObject, final short type)
public WioObject(final STWatchedObject watchedObject, final STGroup stGroup)
'''
pass
def setStatus():
'''public void setStatus(final short n, final String s)
'''
pass
def addWatch():
'''public void addWatch(final Integer n)
public void addWatch(final STGroup stGroup)
'''
pass
def removeWatch():
'''public void removeWatch(final Integer key)
public void removeWatch(final STGroup key)
'''
pass
def isWatched():
'''public boolean isWatched(final Integer key)
public boolean isWatched(final Object key)
public boolean isWatched()
'''
pass
def getWatchingSessions():
'''public Enumeration getWatchingSessions()
'''
pass
def getWatchingGroups():
'''public Enumeration getWatchingGroups()
'''
pass
def dumpToStream():
'''public void dumpToStream(final NdrOutputStream ndrOutputStream)
'''
pass
def isWatchedBySession():
'''public boolean isWatchedBySession()
'''
pass
def getWatchedObject():
'''public STWatchedObject getWatchedObject()
'''
pass
