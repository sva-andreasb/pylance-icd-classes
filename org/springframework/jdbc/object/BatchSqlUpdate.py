def ():
    '''returns BatchSqlUpdate\n\n
    ()\n
    (final DataSource ds, final String sql)\n
    (final DataSource ds, final String sql, final int[] types)\n
    (final DataSource ds, final String sql, final int[] types, final int batchSize)\n
    '''
def setBatchSize():
    '''returns None\n\n
    setBatchSize(final int batchSize)\n
    '''
def update():
    '''returns int\n\n
    update(final Object[] args)\n
    '''
def flush():
    '''returns int[]\n\n
    flush()\n
    '''
def getBatchSize():
    '''returns int\n\n
    getBatchSize()\n
    '''
def setValues():
    '''returns None\n\n
    setValues(final PreparedStatement ps, final int index)\n
    '''
def getQueueCount():
    '''returns int\n\n
    getQueueCount()\n
    '''
def getExecutionCount():
    '''returns int\n\n
    getExecutionCount()\n
    '''
def getRowsAffected():
    '''returns int[]\n\n
    getRowsAffected()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
