def ():
    '''returns RowCallbackHandlerResultSetExtractor\n\n
    ()\n
    (final DataSource dataSource)\n
    (final DataSource dataSource, final boolean lazyInit)\n
    (final String sql)\n
    (final String callString)\n
    (final Object[] args)\n
    (final Object[] args, final int[] argTypes)\n
    (final RowCallbackHandler rch)\n
    '''
def setNativeJdbcExtractor():
    '''returns None\n\n
    setNativeJdbcExtractor(final NativeJdbcExtractor extractor)\n
    '''
def getNativeJdbcExtractor():
    '''returns NativeJdbcExtractor\n\n
    getNativeJdbcExtractor()\n
    '''
def setIgnoreWarnings():
    '''returns None\n\n
    setIgnoreWarnings(final boolean ignoreWarnings)\n
    '''
def isIgnoreWarnings():
    '''returns boolean\n\n
    isIgnoreWarnings()\n
    '''
def setFetchSize():
    '''returns None\n\n
    setFetchSize(final int fetchSize)\n
    '''
def getFetchSize():
    '''returns int\n\n
    getFetchSize()\n
    '''
def setMaxRows():
    '''returns None\n\n
    setMaxRows(final int maxRows)\n
    '''
def getMaxRows():
    '''returns int\n\n
    getMaxRows()\n
    '''
def afterPropertiesSet():
    '''returns None\n\n
    afterPropertiesSet()\n
    '''
def execute():
    '''returns Object\n\n
    execute(final ConnectionCallback action)\n
    execute(final StatementCallback action)\n
    execute(final String sql)\n
    execute(PreparedStatementCreator psc, final PreparedStatementCallback action)\n
    execute(final String sql, final PreparedStatementCallback action)\n
    execute(CallableStatementCreator csc, final CallableStatementCallback action)\n
    execute(final String callString, final CallableStatementCallback action)\n
    '''
def query():
    '''returns List\n\n
    query(final String sql, final ResultSetExtractor rse)\n
    query(final String sql, final RowCallbackHandler rch)\n
    query(final String sql, final RowMapper rowMapper)\n
    query(final PreparedStatementCreator psc, final ResultSetExtractor rse)\n
    query(final String sql, final PreparedStatementSetter pss, final ResultSetExtractor rse)\n
    query(final String sql, final Object[] args, final int[] argTypes, final ResultSetExtractor rse)\n
    query(final String sql, final Object[] args, final ResultSetExtractor rse)\n
    query(final PreparedStatementCreator psc, final RowCallbackHandler rch)\n
    query(final String sql, final PreparedStatementSetter pss, final RowCallbackHandler rch)\n
    query(final String sql, final Object[] args, final int[] argTypes, final RowCallbackHandler rch)\n
    query(final String sql, final Object[] args, final RowCallbackHandler rch)\n
    query(final PreparedStatementCreator psc, final RowMapper rowMapper)\n
    query(final String sql, final PreparedStatementSetter pss, final RowMapper rowMapper)\n
    query(final String sql, final Object[] args, final int[] argTypes, final RowMapper rowMapper)\n
    query(final String sql, final Object[] args, final RowMapper rowMapper)\n
    '''
def queryForMap():
    '''returns Map\n\n
    queryForMap(final String sql)\n
    queryForMap(final String sql, final Object[] args, final int[] argTypes)\n
    queryForMap(final String sql, final Object[] args)\n
    '''
def queryForObject():
    '''returns Object\n\n
    queryForObject(final String sql, final RowMapper rowMapper)\n
    queryForObject(final String sql, final Class requiredType)\n
    queryForObject(final String sql, final Object[] args, final int[] argTypes, final RowMapper rowMapper)\n
    queryForObject(final String sql, final Object[] args, final RowMapper rowMapper)\n
    queryForObject(final String sql, final Object[] args, final int[] argTypes, final Class requiredType)\n
    queryForObject(final String sql, final Object[] args, final Class requiredType)\n
    '''
def queryForLong():
    '''returns long\n\n
    queryForLong(final String sql)\n
    queryForLong(final String sql, final Object[] args, final int[] argTypes)\n
    queryForLong(final String sql, final Object[] args)\n
    '''
def queryForInt():
    '''returns int\n\n
    queryForInt(final String sql)\n
    queryForInt(final String sql, final Object[] args, final int[] argTypes)\n
    queryForInt(final String sql, final Object[] args)\n
    '''
def queryForList():
    '''returns List\n\n
    queryForList(final String sql, final Class elementType)\n
    queryForList(final String sql)\n
    queryForList(final String sql, final Object[] args, final int[] argTypes, final Class elementType)\n
    queryForList(final String sql, final Object[] args, final Class elementType)\n
    queryForList(final String sql, final Object[] args, final int[] argTypes)\n
    queryForList(final String sql, final Object[] args)\n
    '''
def queryForRowSet():
    '''returns SqlRowSet\n\n
    queryForRowSet(final String sql)\n
    queryForRowSet(final String sql, final Object[] args, final int[] argTypes)\n
    queryForRowSet(final String sql, final Object[] args)\n
    '''
def update():
    '''returns int\n\n
    update(final String sql)\n
    update(final PreparedStatementCreator psc)\n
    update(final PreparedStatementCreator psc, final KeyHolder generatedKeyHolder)\n
    update(final String sql, final PreparedStatementSetter pss)\n
    update(final String sql, final Object[] args, final int[] argTypes)\n
    update(final String sql, final Object[] args)\n
    '''
def batchUpdate():
    '''returns int[]\n\n
    batchUpdate(final String[] sql)\n
    batchUpdate(final String sql, final BatchPreparedStatementSetter pss)\n
    '''
def doInPreparedStatement():
    '''returns Object\n\n
    doInPreparedStatement(final PreparedStatement ps)\n
    doInPreparedStatement(final PreparedStatement ps)\n
    doInPreparedStatement(final PreparedStatement ps)\n
    doInPreparedStatement(final PreparedStatement ps)\n
    '''
def call():
    '''returns Map\n\n
    call(final CallableStatementCreator csc, final List declaredParameters)\n
    '''
def doInCallableStatement():
    '''returns Object\n\n
    doInCallableStatement(final CallableStatement cs)\n
    '''
def doInStatement():
    '''returns Object\n\n
    doInStatement(final Statement stmt)\n
    doInStatement(final Statement stmt)\n
    doInStatement(final Statement stmt)\n
    doInStatement(final Statement stmt)\n
    '''
def getSql():
    '''returns String\n\n
    getSql()\n
    getSql()\n
    getSql()\n
    getSql()\n
    getSql()\n
    getSql()\n
    '''
def createPreparedStatement():
    '''returns PreparedStatement\n\n
    createPreparedStatement(final Connection con)\n
    '''
def createCallableStatement():
    '''returns CallableStatement\n\n
    createCallableStatement(final Connection con)\n
    '''
def setValues():
    '''returns None\n\n
    setValues(final PreparedStatement ps)\n
    setValues(final PreparedStatement ps)\n
    '''
def cleanupParameters():
    '''returns None\n\n
    cleanupParameters()\n
    cleanupParameters()\n
    '''
def extractData():
    '''returns Object\n\n
    extractData(final ResultSet rs)\n
    '''
