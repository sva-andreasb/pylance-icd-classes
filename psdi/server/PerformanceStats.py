def put():
    '''public static void put(final String trans, final PerformanceStats ps)
    '''
def getList():
    '''public static Iterator getList()
    '''
def get():
    '''public static PerformanceStats get(final Object trans)
    '''
def reset():
    '''public static void reset()
    '''
def enable():
    '''public static void enable()
    '''
def disable():
    '''public static void disable()
    '''
def isEnabled():
    '''public static boolean isEnabled()
    '''
def PerformanceStats():
    '''public PerformanceStats()
    '''
def incrementSQLTime():
    '''public void incrementSQLTime(long t)
    '''
def incrementSQLCount():
    '''public void incrementSQLCount()
    public void incrementSQLCount(final String stmt)
    '''
def getSQLStatements():
    '''public Iterator getSQLStatements()
    '''
def getStatementIndividualTime():
    '''public String getStatementIndividualTime(final Object obj)
    '''
def getStatementCount():
    '''public int getStatementCount(final Object obj)
    '''
def getSQLCount():
    '''public long getSQLCount()
    '''
def getSQLTime():
    '''public long getSQLTime()
    '''
def incrementMboCount():
    '''public void incrementMboCount()
    public void incrementMboCount(final String name)
    '''
def getMboString():
    '''public String getMboString()
    '''
def getMboCount():
    '''public long getMboCount()
    '''
def incrementMboSetCount():
    '''public void incrementMboSetCount()
    public void incrementMboSetCount(final String name)
    '''
def getMboSetString():
    '''public String getMboSetString()
    '''
def getMboSetCount():
    '''public long getMboSetCount()
    '''
def hasValue():
    '''public boolean hasValue()
    '''
def addStackTrace():
    '''public void addStackTrace(final String stm, final Object obj)
    '''
def normalizeStackTrace():
    '''public Vector normalizeStackTrace(final Throwable e)
    '''
def display():
    '''public String display(final String stmt)
    '''
