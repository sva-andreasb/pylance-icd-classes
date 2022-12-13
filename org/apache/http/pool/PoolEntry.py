def PoolEntry():
'''public PoolEntry(final String id, final T route, final C conn, final long timeToLive, final TimeUnit tunit)
public PoolEntry(final String id, final T route, final C conn)
'''
pass
def getId():
'''public String getId()
'''
pass
def getRoute():
'''public T getRoute()
'''
pass
def getConnection():
'''public C getConnection()
'''
pass
def getCreated():
'''public long getCreated()
'''
pass
def getValidityDeadline():
'''public long getValidityDeadline()
'''
pass
def getValidUnit():
'''public long getValidUnit()
'''
pass
def getState():
'''public Object getState()
'''
pass
def setState():
'''public void setState(final Object state)
'''
pass
def getUpdated():
'''public synchronized long getUpdated()
'''
pass
def getExpiry():
'''public synchronized long getExpiry()
'''
pass
def updateExpiry():
'''public synchronized void updateExpiry(final long time, final TimeUnit tunit)
'''
pass
def isExpired():
'''public synchronized boolean isExpired(final long now)
'''
pass
def toString():
'''public String toString()
'''
pass
