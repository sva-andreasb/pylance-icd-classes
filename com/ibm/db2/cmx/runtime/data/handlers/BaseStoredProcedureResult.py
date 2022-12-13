def BaseStoredProcedureResult():
    '''    public BaseStoredProcedureResult()
    public BaseStoredProcedureResult(final StatementDescriptorImpl statementDescriptor_, final CallableStatement cstmt_, final Object... parametersFromMethod_)
    '''
def getOutAndInOutParameters():
    '''    public void getOutAndInOutParameters(final CallableStatement cstmt_, final boolean b)
    '''
def close():
    '''    public void close()
    '''
def getStatementDescriptor():
    '''    public StatementDescriptorImpl getStatementDescriptor()
    '''
def setStatementDescriptor():
    '''    public void setStatementDescriptor(final StatementDescriptorImpl statementDescriptor_)
    '''
def returnOutParameter():
    '''    public void returnOutParameter(final CallableStatement callableStatement, final int n, final Object o, final int n2)
    '''
def getUserParameters():
    '''    public Object[] getUserParameters()
    '''
def setUserParameters():
    '''    public void setUserParameters(final Object[] parametersFromMethod_)
    '''
def setCallableStatement():
    '''    public void setCallableStatement(final CallableStatement cstmt_)
    '''
def getArray():
    '''    public Map<String, Object>[] getArray()
    public <T> T[] getArray(final Class<T> componentType)
    public <T> T[] getArray(final RowHandler<T> rowHandler)
    public <T> T[] getArray(final Class<T> componentType, final RowHandler<T> rowHandler)
    '''
def getCallStatement():
    '''    public CallableStatement getCallStatement()
    '''
def getIterator():
    '''    public Iterator<Map<String, Object>> getIterator()
    public <T> Iterator<T> getIterator(final Class<T> clazz)
    public <T> Iterator<T> getIterator(final RowHandler<T> rowHandler)
    '''
def getList():
    '''    public List<Map<String, Object>> getList()
    public <T> List<T> getList(final Class<T> clazz)
    public <T> List<T> getList(final RowHandler<T> rowHandler)
    '''
def getOutputParms():
    '''    public Object[] getOutputParms()
    '''
def getQuery():
    '''    public <T> T getQuery(final ResultHandler<T> resultHandler)
    '''
def getResults():
    '''    public ResultSet getResults()
    '''
def setupForResults():
    '''    public void setupForResults(final CallableStatement cstmt_)
    '''
def moveToNext():
    '''    public boolean moveToNext()
    '''
def setCallStatement():
    '''    public void setCallStatement(final CallableStatement cstmt_)
    '''
def run():
    '''    public Method run()
    '''
