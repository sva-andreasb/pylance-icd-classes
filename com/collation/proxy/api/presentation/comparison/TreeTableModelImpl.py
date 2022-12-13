def TreeTableModelImpl():
'''public TreeTableModelImpl(final CompareResults[] results, final long version1)
public TreeTableModelImpl()
'''
pass
def getColumnClass():
'''public Class getColumnClass(final int column)
'''
pass
def getColumnCount():
'''public int getColumnCount()
'''
pass
def getColumnName():
'''public String getColumnName(final int column)
'''
pass
def getValueAt():
'''public Object getValueAt(final int row, final int col)
public Object getValueAt(final Object node, final int column)
'''
pass
def getRow():
'''public CompareResultRow getRow(final int row)
'''
pass
def getRowForNode():
'''public int getRowForNode(final CompareResultRow node)
'''
pass
def getChildren():
'''public List getChildren(final Object parent)
'''
pass
def isCellEditable():
'''public boolean isCellEditable(final Object node, final int column)
public boolean isCellEditable(final int r, final int c)
'''
pass
def getRowCount():
'''public int getRowCount()
'''
pass
def getRoot():
'''public CompareResultRow getRoot()
'''
pass
def getChild():
'''public Object getChild(final Object parent, final int index)
'''
pass
def getChildCount():
'''public int getChildCount(final Object parent)
'''
pass
def isLeaf():
'''public boolean isLeaf(final Object parent)
'''
pass
def getIndexOfChild():
'''public int getIndexOfChild(final Object parent, final Object child)
'''
pass
def valueForPathChanged():
'''public void valueForPathChanged(final TreePath path, final Object newValue)
'''
pass
def addTreeModelListener():
'''public void addTreeModelListener(final TreeModelListener listener)
'''
pass
def removeTreeModelListener():
'''public void removeTreeModelListener(final TreeModelListener listener)
'''
pass
def setObjectAt():
'''public void setObjectAt(final Object value, final Object node, final int column)
'''
pass
def setValueAt():
'''public void setValueAt(final Object o, final int r, final int c)
public void setValueAt(final Object o, final Object r, final int c)
'''
pass
def addTableModelListener():
'''public void addTableModelListener(final TableModelListener listener)
'''
pass
def removeTableModelListener():
'''public void removeTableModelListener(final TableModelListener listener)
'''
pass
