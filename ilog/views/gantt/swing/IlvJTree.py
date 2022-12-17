def ():
    '''returns VisibleIterator\n\n
    ()\n
    (final IlvJTreeRenderPolicy renderPolicy)\n
    (final IlvJTree tree, final DefaultTreeCellRenderer renderer)\n
    (final IlvJTree tree, final DefaultTreeCellRenderer renderer, final TreeCellEditor editor)\n
    (final IlvHierarchyNode ilvHierarchyNode, final TreePath item)\n
    '''
def getRootVisibleRow():
    '''returns IlvHierarchyNode\n\n
    getRootVisibleRow()\n
    '''
def getFirstVisibleRow():
    '''returns IlvHierarchyNode\n\n
    getFirstVisibleRow()\n
    '''
def getRow():
    '''returns IlvHierarchyNode\n\n
    getRow(final int row)\n
    '''
def getRowIndex():
    '''returns int\n\n
    getRowIndex(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def getRowHeight():
    '''returns int\n\n
    getRowHeight(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def toggleExpandState():
    '''returns None\n\n
    toggleExpandState(final TreePath path)\n
    toggleExpandState(final int row)\n
    '''
def isExpanded():
    '''returns boolean\n\n
    isExpanded(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def isVisible():
    '''returns boolean\n\n
    isVisible(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def getPathForRow():
    '''returns TreePath\n\n
    getPathForRow(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def isPathEditable():
    '''returns boolean\n\n
    isPathEditable(final TreePath treePath)\n
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
    setBaseTextDirection(final int i)\n
    '''
def getResolvedBaseTextDirection():
    '''returns int\n\n
    getResolvedBaseTextDirection()\n
    '''
def getRenderPolicy():
    '''returns IlvJTreeRenderPolicy\n\n
    getRenderPolicy()\n
    '''
def setRenderPolicy():
    '''returns None\n\n
    setRenderPolicy(final IlvJTreeRenderPolicy g)\n
    '''
def convertValueToText():
    '''returns String\n\n
    convertValueToText(final Object o, final boolean selected, final boolean expanded, final boolean leaf, final int row, final boolean hasFocus)\n
    '''
def rowUpdated():
    '''returns None\n\n
    rowUpdated(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def getBasicUI():
    '''returns BasicTreeUI\n\n
    getBasicUI()\n
    '''
def updateUI():
    '''returns None\n\n
    updateUI()\n
    '''
def ganttModelChanged():
    '''returns None\n\n
    ganttModelChanged(final GanttModelChangedEvent ganttModelChangedEvent)\n
    ganttModelChanged(final GanttModelChangedEvent ganttModelChangedEvent)\n
    '''
def rowHeightChanged():
    '''returns None\n\n
    rowHeightChanged(final RowHeightChangedEvent rowHeightChangedEvent)\n
    '''
def rootRowVisibilityChanged():
    '''returns None\n\n
    rootRowVisibilityChanged(final RootRowVisibilityChangedEvent rootRowVisibilityChangedEvent)\n
    '''
def setExpandableGanttConfigurationImpl():
    '''returns None\n\n
    setExpandableGanttConfigurationImpl(final IlvGanttConfiguration e)\n
    '''
def validateRowHeights():
    '''returns None\n\n
    validateRowHeights()\n
    '''
def rowsInserted():
    '''returns None\n\n
    rowsInserted(final RowsInsertedEvent rowsInsertedEvent)\n
    rowsInserted(final IlvHierarchyNode ilvHierarchyNode, final IlvHierarchyNode[] array, final int[] array2)\n
    rowsInserted(final RowsInsertedEvent rowsInsertedEvent)\n
    '''
def rowsRemoved():
    '''returns None\n\n
    rowsRemoved(final RowsRemovedEvent rowsRemovedEvent)\n
    rowsRemoved(final IlvHierarchyNode ilvHierarchyNode, final IlvHierarchyNode[] array, final int[] array2)\n
    rowsRemoved(final RowsRemovedEvent rowsRemovedEvent)\n
    '''
def rowMoved():
    '''returns None\n\n
    rowMoved(final RowMovedEvent rowMovedEvent)\n
    rowMoved(final IlvHierarchyNode ilvHierarchyNode, final IlvHierarchyNode ilvHierarchyNode2, final int n, final IlvHierarchyNode ilvHierarchyNode3, final int n2)\n
    rowMoved(final RowMovedEvent rowMovedEvent)\n
    '''
def rowExpanded():
    '''returns None\n\n
    rowExpanded(final RowExpandedEvent rowExpandedEvent)\n
    rowExpanded(final IlvHierarchyNode ilvHierarchyNode)\n
    rowExpanded(final RowExpandedEvent rowExpandedEvent)\n
    '''
def rowCollapsed():
    '''returns None\n\n
    rowCollapsed(final RowCollapsedEvent rowCollapsedEvent)\n
    rowCollapsed(final IlvHierarchyNode ilvHierarchyNode)\n
    rowCollapsed(final RowCollapsedEvent rowCollapsedEvent)\n
    '''
def setExpansionMasterGanttConfigurationImpl():
    '''returns None\n\n
    setExpansionMasterGanttConfigurationImpl(final IlvGanttConfiguration ilvGanttConfiguration)\n
    '''
def treeExpanded():
    '''returns None\n\n
    treeExpanded(final TreeExpansionEvent treeExpansionEvent)\n
    '''
def treeCollapsed():
    '''returns None\n\n
    treeCollapsed(final TreeExpansionEvent treeExpansionEvent)\n
    '''
def getRoot():
    '''returns Object\n\n
    getRoot()\n
    '''
def getChild():
    '''returns Object\n\n
    getChild(final Object o, final int n)\n
    '''
def getChildCount():
    '''returns int\n\n
    getChildCount(final Object o)\n
    '''
def isLeaf():
    '''returns boolean\n\n
    isLeaf(final Object o)\n
    '''
def valueForPathChanged():
    '''returns None\n\n
    valueForPathChanged(final TreePath treePath, final Object o)\n
    '''
def getIndexOfChild():
    '''returns int\n\n
    getIndexOfChild(final Object o, final Object o2)\n
    '''
def addTreeModelListener():
    '''returns None\n\n
    addTreeModelListener(final TreeModelListener treeModelListener)\n
    '''
def removeTreeModelListener():
    '''returns None\n\n
    removeTreeModelListener(final TreeModelListener treeModelListener)\n
    '''
def getRealEditor():
    '''returns CellEditor\n\n
    getRealEditor()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns Object\n\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
