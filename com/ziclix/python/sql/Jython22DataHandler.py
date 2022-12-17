def getMetaDataName():
    '''returns String\n\n
    getMetaDataName(final PyObject name)\n
    '''
def getProcedure():
    '''returns Procedure\n\n
    getProcedure(final PyCursor cursor, final PyObject name)\n
    '''
def getRowId():
    '''returns PyObject\n\n
    getRowId(final Statement stmt)\n
    '''
def preExecute():
    '''returns None\n\n
    preExecute(final Statement stmt)\n
    '''
def postExecute():
    '''returns None\n\n
    postExecute(final Statement stmt)\n
    '''
def setJDBCObject():
    '''returns None\n\n
    setJDBCObject(final PreparedStatement stmt, final int index, final PyObject object)\n
    setJDBCObject(final PreparedStatement stmt, final int index, PyObject object, final int type)\n
    '''
def getPyObject():
    '''returns PyObject\n\n
    getPyObject(final ResultSet set, final int col, final int type)\n
    getPyObject(final CallableStatement stmt, final int col, final int type)\n
    '''
def registerOut():
    '''returns None\n\n
    registerOut(final CallableStatement statement, final int index, final int colType, final int dataType, final String dataTypeName)\n
    '''
def __chain__():
    '''returns PyObject\n\n
    __chain__()\n
    '''
