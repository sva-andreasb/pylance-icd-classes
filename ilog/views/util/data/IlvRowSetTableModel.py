def ():
    '''returns IlvRowSetTableModel\n\n
    ()\n
    (final RowSet set)\n
    (final boolean c)\n
    (final RowSet rowSet, final boolean c)\n
    '''
def setAutoCommit():
    '''returns None\n\n
    setAutoCommit(final boolean c)\n
    '''
def isAutoCommit():
    '''returns boolean\n\n
    isAutoCommit()\n
    '''
def refreshRows():
    '''returns None\n\n
    refreshRows()\n
    '''
def commit():
    '''returns None\n\n
    commit()\n
    '''
def rollback():
    '''returns None\n\n
    rollback()\n
    '''
def getRowCount():
    '''returns int\n\n
    getRowCount()\n
    '''
def getColumnCount():
    '''returns int\n\n
    getColumnCount()\n
    '''
def getColumnName():
    '''returns String\n\n
    getColumnName(final int n)\n
    '''
def getColumnClass():
    '''returns Class\n\n
    getColumnClass(final int n)\n
    '''
def getValueAt():
    '''returns Object\n\n
    getValueAt(final int n, final int n2)\n
    '''
def isCellEditable():
    '''returns boolean\n\n
    isCellEditable(final int n, final int n2)\n
    '''
def setValueAt():
    '''returns None\n\n
    setValueAt(final Object o, final int n, final int n2)\n
    '''
def addRow():
    '''returns None\n\n
    addRow(final Object[] array)\n
    '''
def insertRow():
    '''returns None\n\n
    insertRow(final int n, final Object[] array)\n
    '''
def removeRow():
    '''returns None\n\n
    removeRow(final int n)\n
    '''
