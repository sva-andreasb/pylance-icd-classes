def BaseStoredProcedureResult():
'''public BaseStoredProcedureResult()
public BaseStoredProcedureResult(final StatementDescriptorImpl statementDescriptor_, final CallableStatement cstmt_, final Object... parametersFromMethod_)
'''
pass
def getOutAndInOutParameters():
'''public void getOutAndInOutParameters(final CallableStatement cstmt_, final boolean b)
'''
pass
def close():
'''public void close()
'''
pass
def getStatementDescriptor():
'''public StatementDescriptorImpl getStatementDescriptor()
'''
pass
def setStatementDescriptor():
'''public void setStatementDescriptor(final StatementDescriptorImpl statementDescriptor_)
'''
pass
def returnOutParameter():
'''public void returnOutParameter(final CallableStatement callableStatement, final int n, final Object o, final int n2)
'''
pass
def getUserParameters():
'''public Object[] getUserParameters()
'''
pass
def setUserParameters():
'''public void setUserParameters(final Object[] parametersFromMethod_)
'''
pass
def setCallableStatement():
'''public void setCallableStatement(final CallableStatement cstmt_)
'''
pass
def getArray():
'''public Map<String, Object>[] getArray()
public <T> T[] getArray(final Class<T> componentType)
public <T> T[] getArray(final RowHandler<T> rowHandler)
public <T> T[] getArray(final Class<T> componentType, final RowHandler<T> rowHandler)
'''
pass
def getCallStatement():
'''public CallableStatement getCallStatement()
'''
pass
def getIterator():
'''public Iterator<Map<String, Object>> getIterator()
public <T> Iterator<T> getIterator(final Class<T> clazz)
public <T> Iterator<T> getIterator(final RowHandler<T> rowHandler)
'''
pass
def getList():
'''public List<Map<String, Object>> getList()
public <T> List<T> getList(final Class<T> clazz)
public <T> List<T> getList(final RowHandler<T> rowHandler)
'''
pass
def getOutputParms():
'''public Object[] getOutputParms()
'''
pass
def getQuery():
'''public <T> T getQuery(final ResultHandler<T> resultHandler)
'''
pass
def getResults():
'''public ResultSet getResults()
'''
pass
def setupForResults():
'''public void setupForResults(final CallableStatement cstmt_)
'''
pass
def moveToNext():
'''public boolean moveToNext()
'''
pass
def setCallStatement():
'''public void setCallStatement(final CallableStatement cstmt_)
'''
pass
def run():
'''public Method run()
'''
pass