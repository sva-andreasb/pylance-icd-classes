def getCatalog():
    '''public String getCatalog()
    '''
def setCatalog():
    '''public void setCatalog(final String catalog)
    '''
def getHoldability():
    '''public int getHoldability()
    '''
def setHoldability():
    '''public void setHoldability(final int h)
    '''
def setTypeMap():
    '''public void setTypeMap(final Map map)
    '''
def isReadOnly():
    '''public boolean isReadOnly()
    '''
def setReadOnly():
    '''public void setReadOnly(final boolean ro)
    '''
def nativeSQL():
    '''public String nativeSQL(final String sql)
    '''
def clearWarnings():
    '''public void clearWarnings()
    '''
def getWarnings():
    '''public SQLWarning getWarnings()
    '''
def createStatement():
    '''public Statement createStatement()
    public Statement createStatement(final int rsType, final int rsConcurr)
    '''
def prepareCall():
    '''public CallableStatement prepareCall(final String sql)
    public CallableStatement prepareCall(final String sql, final int rst, final int rsc)
    public CallableStatement prepareCall(final String sql, final int rst, final int rsc, final int rsh)
    '''
def prepareStatement():
    '''public PreparedStatement prepareStatement(final String sql)
    public PreparedStatement prepareStatement(final String sql, final int autoC)
    public PreparedStatement prepareStatement(final String sql, final int[] colInds)
    public PreparedStatement prepareStatement(final String sql, final String[] colNames)
    public PreparedStatement prepareStatement(final String sql, final int rst, final int rsc)
    '''
def setSavepoint():
    '''public Savepoint setSavepoint()
    public Savepoint setSavepoint(final String name)
    '''
def releaseSavepoint():
    '''public void releaseSavepoint(final Savepoint savepoint)
    '''
def rollback():
    '''public void rollback(final Savepoint savepoint)
    '''
def createStruct():
    '''public Struct createStruct(final String t, final Object[] attr)
    '''
