def TreeTableModelImpl():
    '''    public TreeTableModelImpl(final CompareResults[] results, final long version1)
    public TreeTableModelImpl()
    '''
def getColumnClass():
    '''    public Class getColumnClass(final int column)
    '''
def getColumnCount():
    '''    public int getColumnCount()
    '''
def getColumnName():
    '''    public String getColumnName(final int column)
    '''
def getValueAt():
    '''    public Object getValueAt(final int row, final int col)
    public Object getValueAt(final Object node, final int column)
    '''
def getRow():
    '''    public CompareResultRow getRow(final int row)
    '''
def getRowForNode():
    '''    public int getRowForNode(final CompareResultRow node)
    '''
def getChildren():
    '''    public List getChildren(final Object parent)
    '''
def isCellEditable():
    '''    public boolean isCellEditable(final Object node, final int column)
    public boolean isCellEditable(final int r, final int c)
    '''
def getRowCount():
    '''    public int getRowCount()
    '''
def getRoot():
    '''    public CompareResultRow getRoot()
    '''
def getChild():
    '''    public Object getChild(final Object parent, final int index)
    '''
def getChildCount():
    '''    public int getChildCount(final Object parent)
    '''
def isLeaf():
    '''    public boolean isLeaf(final Object parent)
    '''
def getIndexOfChild():
    '''    public int getIndexOfChild(final Object parent, final Object child)
    '''
def valueForPathChanged():
    '''    public void valueForPathChanged(final TreePath path, final Object newValue)
    '''
def addTreeModelListener():
    '''    public void addTreeModelListener(final TreeModelListener listener)
    '''
def removeTreeModelListener():
    '''    public void removeTreeModelListener(final TreeModelListener listener)
    '''
def setObjectAt():
    '''    public void setObjectAt(final Object value, final Object node, final int column)
    '''
def setValueAt():
    '''    public void setValueAt(final Object o, final int r, final int c)
    public void setValueAt(final Object o, final Object r, final int c)
    '''
def addTableModelListener():
    '''    public void addTableModelListener(final TableModelListener listener)
    '''
def removeTableModelListener():
    '''    public void removeTableModelListener(final TableModelListener listener)
    '''
