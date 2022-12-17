def ():
    '''returns Procedure\n\n
    (final PyCursor cursor, final PyObject name)\n
    '''
def prepareCall():
    '''returns CallableStatement\n\n
    prepareCall()\n
    prepareCall(final PyObject rsType, final PyObject rsConcur)\n
    '''
def normalizeInput():
    '''returns None\n\n
    normalizeInput(final PyObject params, final PyObject bindings)\n
    '''
def isInput():
    '''returns boolean\n\n
    isInput(final int index)\n
    '''
def toSql():
    '''returns String\n\n
    toSql()\n
    '''
