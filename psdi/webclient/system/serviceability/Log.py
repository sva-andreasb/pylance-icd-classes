def getLimit():
'''public int getLimit()
'''
pass
def setLimit():
'''public void setLimit(final int limit)
'''
pass
def clear():
'''public void clear()
'''
pass
def addLogListener():
'''public synchronized boolean addLogListener(final LogListener l)
'''
pass
def removeListener():
'''public synchronized boolean removeListener(final LogListener l)
'''
pass
def getLevel():
'''public Level getLevel(final Category category)
'''
pass
def getEffectiveLevel():
'''public Level getEffectiveLevel(final Category category)
'''
pass
def isEnabled():
'''public boolean isEnabled(final Level level, final Category category)
'''
pass
def setLevel():
'''public void setLevel(final Category category, final Level level)
'''
pass
def clearLevel():
'''public void clearLevel(final Category category)
'''
pass
def log():
'''public void log(final Level level, final Throwable t)
public void log(final Level level, final Category category, final Throwable t)
public void log(final Level level, final Category category, final String message)
public void log(final Level level, final Category category, final String message, final String detail)
public void log(final Level level, final Category category, final String message, final Throwable t)
'''
pass
def getEntries():
'''public LogEntry[] getEntries()
'''
pass
