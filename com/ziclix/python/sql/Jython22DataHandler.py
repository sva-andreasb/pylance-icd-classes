def getMetaDataName():
    '''    public String getMetaDataName(final PyObject name)
    '''
def getProcedure():
    '''    public Procedure getProcedure(final PyCursor cursor, final PyObject name)
    '''
def getRowId():
    '''    public PyObject getRowId(final Statement stmt)
    '''
def preExecute():
    '''    public void preExecute(final Statement stmt)
    '''
def postExecute():
    '''    public void postExecute(final Statement stmt)
    '''
def setJDBCObject():
    '''    public void setJDBCObject(final PreparedStatement stmt, final int index, final PyObject object)
    public void setJDBCObject(final PreparedStatement stmt, final int index, PyObject object, final int type)
    '''
def getPyObject():
    '''    public PyObject getPyObject(final ResultSet set, final int col, final int type)
    public PyObject getPyObject(final CallableStatement stmt, final int col, final int type)
    '''
def registerOut():
    '''    public void registerOut(final CallableStatement statement, final int index, final int colType, final int dataType, final String dataTypeName)
    '''
def __chain__():
    '''    public PyObject __chain__()
    '''
