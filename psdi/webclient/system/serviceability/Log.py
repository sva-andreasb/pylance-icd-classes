def getLimit():
    '''    public int getLimit()
    '''
def setLimit():
    '''    public void setLimit(final int limit)
    '''
def clear():
    '''    public void clear()
    '''
def addLogListener():
    '''    public synchronized boolean addLogListener(final LogListener l)
    '''
def removeListener():
    '''    public synchronized boolean removeListener(final LogListener l)
    '''
def getLevel():
    '''    public Level getLevel(final Category category)
    '''
def getEffectiveLevel():
    '''    public Level getEffectiveLevel(final Category category)
    '''
def isEnabled():
    '''    public boolean isEnabled(final Level level, final Category category)
    '''
def setLevel():
    '''    public void setLevel(final Category category, final Level level)
    '''
def clearLevel():
    '''    public void clearLevel(final Category category)
    '''
def log():
    '''    public void log(final Level level, final Throwable t)
    public void log(final Level level, final Category category, final Throwable t)
    public void log(final Level level, final Category category, final String message)
    public void log(final Level level, final Category category, final String message, final String detail)
    public void log(final Level level, final Category category, final String message, final Throwable t)
    '''
def getEntries():
    '''    public LogEntry[] getEntries()
    '''
