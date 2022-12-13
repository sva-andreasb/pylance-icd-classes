SINGLE_ROW_PARAMETERS = "int  1"
MULTI_ROW_PARAMETERS = "int  2"
NO_PARAMETERS = "int  3"
SINGLE_ROW_RESULT = "int  4"
MULTI_ROW_RESULT = "int  5"
ALLOW_STATIC_ROWSET_CURSORS = "int  6"
DISALLOW_STATIC_ROWSET_CURSORS = "int  7"
def getGeneratorVersion():
'''public String getGeneratorVersion()
'''
pass
def checkCompatibleRuntimeVersion():
'''public void checkCompatibleRuntimeVersion(final String s)
'''
pass
def BaseData():
'''public BaseData()
'''
pass
def queryArray():
'''public <ROW> ROW[] queryArray(final StatementDescriptor statementDescriptor, final HandlerContainer<?, ? extends ROW, ?> handlerContainer, final Class<ROW> clazz, final Object... array)
public Map<String, Object>[] queryArray(final String s, final Object... array)
public <ROW> ROW[] queryArray(final String s, final Class<ROW> clazz, final Object... array)
public <ROW> ROW[] queryArray(final String s, final Class<ROW> clazz, final RowHandler<ROW> rowHandler, final Object... array)
public <ROW> ROW[] queryArray(final StatementDescriptor statementDescriptor, final Class<ROW> clazz, final Object... array)
public <ROW> ROW[] queryArray(final String s, final RowHandler<ROW> rowHandler, final Object... array)
'''
pass
def queryFirst():
'''public <ROW> ROW queryFirst(final StatementDescriptor statementDescriptor, final HandlerContainer<?, ? extends ROW, ?> handlerContainer, final Object... array)
public Map<String, Object> queryFirst(final String s, final Object... array)
public <ROW> ROW queryFirst(final String s, final Class<ROW> clazz, final Object... array)
public <ROW> ROW queryFirst(final String s, final RowHandler<ROW> rowHandler, final Object... array)
public <ROW> ROW queryFirst(final StatementDescriptor statementDescriptor, final Object... array)
'''
pass
def queryIterator():
'''public <ROW> Iterator<ROW> queryIterator(final StatementDescriptor statementDescriptor, final HandlerContainer<?, ? extends ROW, ?> handlerContainer, final Object... array)
public Iterator<Map<String, Object>> queryIterator(final String s, final Object... array)
public <ROW> Iterator<ROW> queryIterator(final String s, final Class<ROW> clazz, final Object... array)
public <ROW> Iterator<ROW> queryIterator(final String s, final RowHandler<ROW> rowHandler, final Object... array)
public <ROW> Iterator<ROW> queryIterator(final StatementDescriptor statementDescriptor, final Object... array)
public <ROW> Iterator<ROW> queryIterator(final int n, final int n2, final int n3, final String s, final RowHandler<ROW> rowHandler, final Object... array)
public <ROW> Iterator<ROW> queryIterator(final int n, final int n2, final int n3, final String s, final Class<ROW> clazz, final Object... array)
public Iterator<Map<String, Object>> queryIterator(final int n, final int n2, final int n3, final String s, final Object... array)
'''
pass
def queryList():
'''public <ROW> List<ROW> queryList(final StatementDescriptor statementDescriptor, final HandlerContainer<?, ? extends ROW, ?> handlerContainer, final Object... array)
public List<Map<String, Object>> queryList(final String s, final Object... array)
public <ROW> List<ROW> queryList(final String s, final Class<ROW> clazz, final Object... array)
public <ROW> List<ROW> queryList(final String s, final RowHandler<ROW> rowHandler, final Object... array)
public <ROW> List<ROW> queryList(final StatementDescriptor statementDescriptor, final Object... array)
'''
pass
def queryResults():
'''public ResultSet queryResults(final StatementDescriptor statementDescriptor, final HandlerContainer<?, ?, ?> handlerContainer, final Object... array)
public ResultSet queryResults(final String s, final Object... array)
public ResultSet queryResults(final int n, final int n2, final int n3, final String s, final Object... array)
public ResultSet queryResults(final StatementDescriptor statementDescriptor, final Object... array)
'''
pass
def update():
'''public int update(final StatementDescriptor statementDescriptor, final HandlerContainer<?, ?, ?> handlerContainer, final Object... array)
public <ROW> int update(final ROW row, final StatementDescriptor statementDescriptor, final HandlerContainer<?, ? extends ROW, ?> handlerContainer, final Object... array)
public int update(final String s, final Object... array)
public <T> T update(final String s, final Class<T> clazz, final String[] array, final Object... array2)
public int update(final StatementDescriptor statementDescriptor, final Object... array)
public <ROW> int update(final ROW row, final StatementDescriptor statementDescriptor, final Object... array)
'''
pass
def updateMany():
'''public <T> int[] updateMany(final StatementDescriptor statementDescriptor, final HandlerContainer<?, ?, ?> handlerContainer, final Iterator<T> iterator)
public <T> int[] updateMany(final StatementDescriptor statementDescriptor, final HandlerContainer<?, ?, ?> handlerContainer, final Iterable<T> iterable)
public <T> int[] updateMany(final StatementDescriptor statementDescriptor, final HandlerContainer<?, ?, ?> handlerContainer, final T[] array)
public <T> int[] updateMany(final String s, final Iterable<T> iterable)
public <T> int[] updateMany(final String s, final Iterator<T> iterator)
public <T> int[] updateMany(final String s, final T[] array)
public int[] updateMany(final String... array)
public <T> int[] updateMany(final StatementDescriptor statementDescriptor, final Iterator<T> iterator)
public <T> int[] updateMany(final StatementDescriptor statementDescriptor, final Iterable<T> iterable)
public <T> int[] updateMany(final StatementDescriptor statementDescriptor, final T[] array)
'''
pass
def close():
'''public void close()
'''
pass
def commit():
'''public void commit()
'''
pass
def getAutoCommit():
'''public boolean getAutoCommit()
'''
pass
def getConnection():
'''public Connection getConnection()
'''
pass
def query():
'''public <RES> RES query(final String s, final ResultHandler<RES> resultHandler, final Object... array)
public <RES> RES query(final StatementDescriptor statementDescriptor, final HandlerContainer<? extends RES, ?, ?> handlerContainer, final Object... array)
public <RES> RES query(final StatementDescriptor statementDescriptor, final Object... array)
public <RES> RES query(final int n, final int n2, final int n3, final String s, final ResultHandler<RES> resultHandler, final Object... array)
public <RES> RES query(final int n, final int n2, final int n3, final String s, final ParameterHandler parameterHandler, final ResultHandler<RES> resultHandler, final Object... array)
'''
pass
def rollback():
'''public void rollback()
'''
pass
def setAutoCommit():
'''public void setAutoCommit(final boolean autoCommit)
'''
pass
def getData():
'''public Data getData()
'''
pass
def getStatementDescriptor():
'''public StatementDescriptor getStatementDescriptor(final String key)
public StatementDescriptor getStatementDescriptor(final String s, final String s2, final SqlStatementType sqlStatementType, final int n, final Object[] array)
'''
pass
def setData():
'''public void setData(final Data data)
'''
pass
def call():
'''public <CAL> CAL call(final String s, final CallHandler<CAL> callHandler, final Object... array)
public <CAL> CAL call(final String s, final CallHandlerWithParameters<CAL> callHandlerWithParameters, final Object... array)
public <CAL> CAL call(final String s, final ParameterHandler parameterHandler, final CallHandlerWithParameters<CAL> callHandlerWithParameters, final Object... array)
public StoredProcedureResult call(final String s, final Object... array)
public <CAL> CAL call(final StatementDescriptor statementDescriptor, final HandlerContainer<?, ?, ? extends CAL> handlerContainer, final Object... array)
public <CAL> CAL call(final StatementDescriptor statementDescriptor, final Object... array)
'''
pass
def testNull():
'''public static final <T> T testNull(final T t, final boolean b)
'''
pass
def createStatementDescriptor():
'''public static StatementDescriptor createStatementDescriptor(final String s, final String s2, final int[] array, final SqlStatementType sqlStatementType, final String[] array2, final ParameterHandler parameterHandler, final int[][] array3, final ResultHandler resultHandler, final RowHandler rowHandler, final int[][] array4, final CallHandlerWithParameters callHandlerWithParameters, final String s3, final long n, final String s4, final boolean b, final String s5, final int i)
public static StatementDescriptor createStatementDescriptor(final String s, final String s2, final int[] array, final SqlStatementType sqlStatementType, final String[] array2, final ParameterHandler parameterHandler, final int[][] array3, final ResultHandler resultHandler, final RowHandler rowHandler, final int[][] array4, final CallHandlerWithParameters callHandlerWithParameters, final String s3, final long n, final String s4, final int i)
public static StatementDescriptor createStatementDescriptor(final String s, final String s2, final int[] array, final SqlStatementType sqlStatementType, final String[] array2, final ParameterHandler parameterHandler, final int[][] array3, final RowHandler rowHandler, final int[][] array4, final CallHandlerWithParameters callHandlerWithParameters, final String s3, final long n, final String s4, final int i)
public static StatementDescriptor createStatementDescriptor(final String s, final String s2, final int[] array, final SqlStatementType sqlStatementType, final String[] array2, final ParameterHandler parameterHandler, final int[][] array3, final RowHandler rowHandler, final int[][] array4, final CallHandlerWithParameters callHandlerWithParameters, final String s3, final String s4, final long n, final int i)
public static StatementDescriptor createStatementDescriptor(final String s, final String s2, final SqlStatementType sqlStatementType, final String[] array, final com.ibm.db2.cmx.runtime.generator.ParameterHandler parameterHandler, final int[][] array2, final RowHandler rowHandler, final int[][] array3, final String s3, final String s4, final long n, final int i)
public static StatementDescriptor createStatementDescriptor(final String s, final String s2, final SqlStatementType sqlStatementType, final String[] array, final com.ibm.db2.cmx.runtime.generator.ParameterHandler parameterHandler, final int[][] array2, final RowHandler rowHandler, final int[][] array3, final CallHandler callHandler, final String s3, final String s4, final long n, final int i)
'''
pass
def getLogger():
'''public Logger getLogger()
'''
pass
def setLogger():
'''public void setLogger(final Logger logger_)
'''
pass
def endBatch():
'''public int[][] endBatch()
'''
pass
def cancelBatch():
'''public void cancelBatch()
'''
pass
def getBatchKind():
'''public HeterogeneousBatchKind getBatchKind()
'''
pass
def startBatch():
'''public void startBatch(final HeterogeneousBatchKind heterogeneousBatchKind)
'''
pass
def run():
'''public Field[] run()
'''
pass
def checkDriverVersion():
'''public static void checkDriverVersion(final String s)
'''
pass
