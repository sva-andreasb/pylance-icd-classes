def ():
    '''returns IlvJTable\n\n
    ()\n
    '''
def getColumnIndex():
    '''returns int\n\n
    getColumnIndex(final Object o)\n
    getColumnIndex(final TableColumn tableColumn)\n
    getColumnIndex(final IlvJTableColumn ilvJTableColumn)\n
    '''
def getColumn():
    '''returns TableColumn\n\n
    getColumn(final int n)\n
    getColumn(final IlvJTableColumn ilvJTableColumn)\n
    '''
def getTableColumn():
    '''returns IlvJTableColumn\n\n
    getTableColumn(final int n)\n
    getTableColumn(final Object identifier)\n
    getTableColumn(final TableColumn tableColumn)\n
    '''
def getTreeColumn():
    '''returns IlvTreeColumn\n\n
    getTreeColumn(final int n)\n
    getTreeColumn(final Object o)\n
    getTreeColumn(final TableColumn tableColumn)\n
    '''
def addColumn():
    '''returns None\n\n
    addColumn(final TableColumn tableColumn)\n
    addColumn(final IlvJTableColumn ilvJTableColumn)\n
    '''
def removeColumn():
    '''returns None\n\n
    removeColumn(final TableColumn tableColumn)\n
    removeColumn(final IlvJTableColumn ilvJTableColumn)\n
    removeColumn(final Object identifier)\n
    '''
def getULocale():
    '''returns ULocale\n\n
    getULocale()\n
    '''
def setULocale():
    '''returns None\n\n
    setULocale(final ULocale value)\n
    '''
def setLocale():
    '''returns None\n\n
    setLocale(final Locale locale)\n
    '''
def setComponentOrientation():
    '''returns None\n\n
    setComponentOrientation(final ComponentOrientation componentOrientation)\n
    '''
def setBaseTextDirection():
    '''returns None\n\n
    setBaseTextDirection(final int f)\n
    '''
def setParentBaseTextDirection():
    '''returns None\n\n
    setParentBaseTextDirection(final int g)\n
    '''
def getResolvedBaseTextDirection():
    '''returns int\n\n
    getResolvedBaseTextDirection()\n
    '''
def getColumnBaseTextDirection():
    '''returns int\n\n
    getColumnBaseTextDirection(final IlvJTableColumn ilvJTableColumn)\n
    '''
def setColumnBaseTextDirection():
    '''returns None\n\n
    setColumnBaseTextDirection(final IlvJTableColumn ilvJTableColumn, final int baseTextDirection)\n
    setColumnBaseTextDirection(final int n, final int n2)\n
    '''
def getResolvedColumnBaseTextDirection():
    '''returns int\n\n
    getResolvedColumnBaseTextDirection(final IlvJTableColumn ilvJTableColumn)\n
    getResolvedColumnBaseTextDirection(final int n)\n
    '''
def editCellAt():
    '''returns boolean\n\n
    editCellAt(final int n, final int n2)\n
    editCellAt(final int row, final int column, final EventObject e)\n
    '''
def removeEditor():
    '''returns None\n\n
    removeEditor()\n
    '''
def prepareRenderer():
    '''returns Component\n\n
    prepareRenderer(final TableCellRenderer renderer, final int row, final int column)\n
    '''
def prepareEditor():
    '''returns Component\n\n
    prepareEditor(final TableCellEditor editor, final int row, final int column)\n
    '''
def getEditingRow():
    '''returns int\n\n
    getEditingRow()\n
    '''
def updateUI():
    '''returns None\n\n
    updateUI()\n
    '''
def getHeader():
    '''returns IlvJTableHeader\n\n
    getHeader()\n
    '''
def getToolTipPolicy():
    '''returns ToolTipPolicy\n\n
    getToolTipPolicy()\n
    '''
def setToolTipPolicy():
    '''returns None\n\n
    setToolTipPolicy(final ToolTipPolicy h)\n
    '''
def getToolTipText():
    '''returns String\n\n
    getToolTipText(final MouseEvent event)\n
    getToolTipText(final IlvJTable ilvJTable, final MouseEvent mouseEvent, final IlvHierarchyNode a, final String s, final int n, final int n2)\n
    '''
def getToolTipLocation():
    '''returns Point\n\n
    getToolTipLocation(final MouseEvent event)\n
    getToolTipLocation(final IlvJTable ilvJTable, final MouseEvent mouseEvent, final int row, final int n)\n
    '''
def cellUpdated():
    '''returns None\n\n
    cellUpdated(final IlvHierarchyNode ilvHierarchyNode, final int column)\n
    '''
def columnHeaderUpdated():
    '''returns None\n\n
    columnHeaderUpdated(final int n)\n
    '''
def columnUpdated():
    '''returns None\n\n
    columnUpdated(final int n)\n
    '''
def rowUpdated():
    '''returns None\n\n
    rowUpdated(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def setExpandableGanttConfigurationImpl():
    '''returns None\n\n
    setExpandableGanttConfigurationImpl(final IlvGanttConfiguration e)\n
    '''
def ganttModelChanged():
    '''returns None\n\n
    ganttModelChanged(final GanttModelChangedEvent ganttModelChangedEvent)\n
    '''
def validateRowHeights():
    '''returns None\n\n
    validateRowHeights()\n
    '''
def getPreferredSize():
    '''returns Dimension\n\n
    getPreferredSize()\n
    '''
def getMinimumSize():
    '''returns Dimension\n\n
    getMinimumSize()\n
    '''
def getMaximumSize():
    '''returns Dimension\n\n
    getMaximumSize()\n
    '''
def paintComponent():
    '''returns None\n\n
    paintComponent(final Graphics g)\n
    '''
def rowsInserted():
    '''returns None\n\n
    rowsInserted(final RowsInsertedEvent rowsInsertedEvent)\n
    '''
def rowsRemoved():
    '''returns None\n\n
    rowsRemoved(final RowsRemovedEvent rowsRemovedEvent)\n
    '''
def rowMoved():
    '''returns None\n\n
    rowMoved(final RowMovedEvent rowMovedEvent)\n
    '''
def rowExpanded():
    '''returns None\n\n
    rowExpanded(final RowExpandedEvent rowExpandedEvent)\n
    '''
def rowCollapsed():
    '''returns None\n\n
    rowCollapsed(final RowCollapsedEvent rowCollapsedEvent)\n
    '''
def rowHeightChanged():
    '''returns None\n\n
    rowHeightChanged(final RowHeightChangedEvent rowHeightChangedEvent)\n
    '''
def rootRowVisibilityChanged():
    '''returns None\n\n
    rootRowVisibilityChanged(final RootRowVisibilityChangedEvent rootRowVisibilityChangedEvent)\n
    '''
def getNode():
    '''returns IlvHierarchyNode\n\n
    getNode(final int n)\n
    '''
def getMinSelectionIndex():
    '''returns int\n\n
    getMinSelectionIndex()\n
    '''
def getMaxSelectionIndex():
    '''returns int\n\n
    getMaxSelectionIndex()\n
    '''
def getValueIsAdjusting():
    '''returns boolean\n\n
    getValueIsAdjusting()\n
    '''
def getSelectionMode():
    '''returns int\n\n
    getSelectionMode()\n
    '''
def setSelectionMode():
    '''returns None\n\n
    setSelectionMode(final int c)\n
    '''
def isSelectedIndex():
    '''returns boolean\n\n
    isSelectedIndex(final int bitIndex)\n
    '''
def isSelectionEmpty():
    '''returns boolean\n\n
    isSelectionEmpty()\n
    '''
def addListSelectionListener():
    '''returns None\n\n
    addListSelectionListener(final ListSelectionListener l)\n
    '''
def removeListSelectionListener():
    '''returns None\n\n
    removeListSelectionListener(final ListSelectionListener l)\n
    '''
def setLeadAnchorNotificationEnabled():
    '''returns None\n\n
    setLeadAnchorNotificationEnabled(final boolean leadAnchorNotificationEnabled)\n
    '''
def isLeadAnchorNotificationEnabled():
    '''returns boolean\n\n
    isLeadAnchorNotificationEnabled()\n
    '''
def clearSelection():
    '''returns None\n\n
    clearSelection()\n
    '''
def setSelectionInterval():
    '''returns None\n\n
    setSelectionInterval(int n, final int n2)\n
    '''
def addSelectionInterval():
    '''returns None\n\n
    addSelectionInterval(final int n, final int n2)\n
    '''
def removeSelectionInterval():
    '''returns None\n\n
    removeSelectionInterval(final int n, final int n2)\n
    '''
def insertIndexInterval():
    '''returns None\n\n
    insertIndexInterval(final int n, final int n2, final boolean b)\n
    '''
def removeIndexInterval():
    '''returns None\n\n
    removeIndexInterval(final int n, final int n2)\n
    '''
def setValueIsAdjusting():
    '''returns None\n\n
    setValueIsAdjusting(final boolean j)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def getAnchorSelectionIndex():
    '''returns int\n\n
    getAnchorSelectionIndex()\n
    '''
def getLeadSelectionIndex():
    '''returns int\n\n
    getLeadSelectionIndex()\n
    '''
def setAnchorSelectionIndex():
    '''returns None\n\n
    setAnchorSelectionIndex(final int f)\n
    '''
def setLeadSelectionIndex():
    '''returns None\n\n
    setLeadSelectionIndex(final int n)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def iterator():
    '''returns Iterator<IlvJTableColumn>\n\n
    iterator()\n
    '''
def getColumnCount():
    '''returns int\n\n
    getColumnCount()\n
    '''
def getRowCount():
    '''returns int\n\n
    getRowCount()\n
    '''
def getValueAt():
    '''returns Object\n\n
    getValueAt(final int n, final int n2)\n
    '''
def setValueAt():
    '''returns None\n\n
    setValueAt(final Object o, final int n, final int n2)\n
    '''
def isCellEditable():
    '''returns boolean\n\n
    isCellEditable(final int n, final int n2)\n
    '''
def fireTableDataChanged():
    '''returns None\n\n
    fireTableDataChanged()\n
    '''
def fireTableColumnUpdated():
    '''returns None\n\n
    fireTableColumnUpdated(final int column)\n
    '''
def fireTableColumnHeaderUpdated():
    '''returns None\n\n
    fireTableColumnHeaderUpdated(final int column)\n
    '''
def mousePressed():
    '''returns None\n\n
    mousePressed(final MouseEvent anEvent)\n
    '''
