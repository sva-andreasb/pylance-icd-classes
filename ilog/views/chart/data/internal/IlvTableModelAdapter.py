BEFORE_UPDATE = "int  20"
AFTER_UPDATE = "int  21"
def ():
    '''returns IlvTableModelAdapter\n\n
    (final TableModel a)\n
    '''
def getModel():
    '''returns TableModel\n\n
    getModel()\n
    '''
def getColumnCount():
    '''returns int\n\n
    getColumnCount()\n
    '''
def getRowCount():
    '''returns int\n\n
    getRowCount()\n
    '''
def getColumnClass():
    '''returns Class\n\n
    getColumnClass(final int n)\n
    '''
def getColumnName():
    '''returns String\n\n
    getColumnName(final int n)\n
    '''
def isCellEditable():
    '''returns boolean\n\n
    isCellEditable(final int n, final int n2)\n
    '''
def getValueAt():
    '''returns Object\n\n
    getValueAt(final int n, final int n2)\n
    '''
def tableChanged():
    '''returns None\n\n
    tableChanged(final TableModelEvent tableModelEvent)\n
    '''
