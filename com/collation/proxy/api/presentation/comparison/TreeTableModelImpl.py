def ():
    '''returns TreeTableModelImpl\n\n
    (final CompareResults[] results, final long version1)\n
    ()\n
    '''
def getColumnClass():
    '''returns Class\n\n
    getColumnClass(final int column)\n
    '''
def getColumnCount():
    '''returns int\n\n
    getColumnCount()\n
    '''
def getColumnName():
    '''returns String\n\n
    getColumnName(final int column)\n
    '''
def getValueAt():
    '''returns Object\n\n
    getValueAt(final int row, final int col)\n
    getValueAt(final Object node, final int column)\n
    '''
def getRow():
    '''returns CompareResultRow\n\n
    getRow(final int row)\n
    '''
def getRowForNode():
    '''returns int\n\n
    getRowForNode(final CompareResultRow node)\n
    '''
def getChildren():
    '''returns List\n\n
    getChildren(final Object parent)\n
    '''
def isCellEditable():
    '''returns boolean\n\n
    isCellEditable(final Object node, final int column)\n
    isCellEditable(final int r, final int c)\n
    '''
def getRowCount():
    '''returns int\n\n
    getRowCount()\n
    '''
def getRoot():
    '''returns CompareResultRow\n\n
    getRoot()\n
    '''
def getChild():
    '''returns Object\n\n
    getChild(final Object parent, final int index)\n
    '''
def getChildCount():
    '''returns int\n\n
    getChildCount(final Object parent)\n
    '''
def isLeaf():
    '''returns boolean\n\n
    isLeaf(final Object parent)\n
    '''
def getIndexOfChild():
    '''returns int\n\n
    getIndexOfChild(final Object parent, final Object child)\n
    '''
def valueForPathChanged():
    '''returns None\n\n
    valueForPathChanged(final TreePath path, final Object newValue)\n
    '''
def addTreeModelListener():
    '''returns None\n\n
    addTreeModelListener(final TreeModelListener listener)\n
    '''
def removeTreeModelListener():
    '''returns None\n\n
    removeTreeModelListener(final TreeModelListener listener)\n
    '''
def setObjectAt():
    '''returns None\n\n
    setObjectAt(final Object value, final Object node, final int column)\n
    '''
def setValueAt():
    '''returns None\n\n
    setValueAt(final Object o, final int r, final int c)\n
    setValueAt(final Object o, final Object r, final int c)\n
    '''
def addTableModelListener():
    '''returns None\n\n
    addTableModelListener(final TableModelListener listener)\n
    '''
def removeTableModelListener():
    '''returns None\n\n
    removeTableModelListener(final TableModelListener listener)\n
    '''
