def getMetaDataName():
'''public String getMetaDataName(final PyObject name)
'''
pass
def getProcedure():
'''public Procedure getProcedure(final PyCursor cursor, final PyObject name)
'''
pass
def getRowId():
'''public PyObject getRowId(final Statement stmt)
'''
pass
def preExecute():
'''public void preExecute(final Statement stmt)
'''
pass
def postExecute():
'''public void postExecute(final Statement stmt)
'''
pass
def setJDBCObject():
'''public void setJDBCObject(final PreparedStatement stmt, final int index, final PyObject object)
public void setJDBCObject(final PreparedStatement stmt, final int index, PyObject object, final int type)
'''
pass
def getPyObject():
'''public PyObject getPyObject(final ResultSet set, final int col, final int type)
public PyObject getPyObject(final CallableStatement stmt, final int col, final int type)
'''
pass
def registerOut():
'''public void registerOut(final CallableStatement statement, final int index, final int colType, final int dataType, final String dataTypeName)
'''
pass
def __chain__():
'''public PyObject __chain__()
'''
pass
