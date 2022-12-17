ACTIVITY_ROWS = "int  0"
RESOURCE_ROWS = "int  1"
DEFAULT_ROW_HEIGHT = "int  20"
def ():
    '''returns IlvVerticalDisplayController\n\n
    (final int n)\n
    '''
def getRowType():
    '''returns int\n\n
    getRowType()\n
    '''
def getGanttConfiguration():
    '''returns IlvGanttConfiguration\n\n
    getGanttConfiguration()\n
    '''
def getRootDataNode():
    '''returns IlvHierarchyNode\n\n
    getRootDataNode()\n
    '''
def getRootNode():
    '''returns IlvHierarchyNode\n\n
    getRootNode()\n
    '''
def getFirstNode():
    '''returns IlvHierarchyNode\n\n
    getFirstNode()\n
    '''
def getNodeForRow():
    '''returns IlvHierarchyNode\n\n
    getNodeForRow(final int n)\n
    '''
def getRowForNode():
    '''returns int\n\n
    getRowForNode(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def getRowCount():
    '''returns int\n\n
    getRowCount()\n
    '''
def validateRowHeights():
    '''returns None\n\n
    validateRowHeights()\n
    '''
def isFixedRowHeight():
    '''returns boolean\n\n
    isFixedRowHeight()\n
    '''
def getRowHeight():
    '''returns int\n\n
    getRowHeight()\n
    getRowHeight(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def setRowHeight():
    '''returns None\n\n
    setRowHeight(final int rowHeight)\n
    setRowHeight(final IlvHierarchyNode ilvHierarchyNode, final int n)\n
    '''
def getRowAtPosition():
    '''returns int\n\n
    getRowAtPosition(final int n)\n
    '''
def getDisplayedRowAtPosition():
    '''returns int\n\n
    getDisplayedRowAtPosition(final int n)\n
    '''
def getNodeAtPosition():
    '''returns IlvHierarchyNode\n\n
    getNodeAtPosition(final int n)\n
    '''
def getDisplayedNodeAtPosition():
    '''returns IlvHierarchyNode\n\n
    getDisplayedNodeAtPosition(final int n)\n
    '''
def getRowBounds():
    '''returns Rectangle\n\n
    getRowBounds(final int n)\n
    '''
def getNodeBounds():
    '''returns Rectangle\n\n
    getNodeBounds(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def isRootNodeVisible():
    '''returns boolean\n\n
    isRootNodeVisible()\n
    '''
def setRootNodeVisible():
    '''returns None\n\n
    setRootNodeVisible(final boolean rootRowVisible)\n
    '''
def isExpanded():
    '''returns boolean\n\n
    isExpanded(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def isVisible():
    '''returns boolean\n\n
    isVisible(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def visibleNodesIterator():
    '''returns Iterator<IlvHierarchyNode>\n\n
    visibleNodesIterator(final IlvHierarchyNode ilvHierarchyNode)\n
    visibleNodesIterator()\n
    '''
def makeVisible():
    '''returns None\n\n
    makeVisible(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def expandNode():
    '''returns None\n\n
    expandNode(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def collapseNode():
    '''returns None\n\n
    collapseNode(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def setVerticalExpansionMaster():
    '''returns None\n\n
    setVerticalExpansionMaster(final IlvVerticalExpansionMaster f)\n
    '''
def addExpansionListener():
    '''returns None\n\n
    addExpansionListener(final VerticalExpansionListener verticalExpansionListener)\n
    '''
def removeExpansionListener():
    '''returns None\n\n
    removeExpansionListener(final VerticalExpansionListener verticalExpansionListener)\n
    '''
def getMaxPosition():
    '''returns int\n\n
    getMaxPosition()\n
    '''
def setMaxPosition():
    '''returns None\n\n
    setMaxPosition(final int maxVerticalPosition)\n
    '''
def getPosition():
    '''returns int\n\n
    getPosition()\n
    '''
def setPosition():
    '''returns None\n\n
    setPosition(final int verticalPosition)\n
    '''
def getExtent():
    '''returns int\n\n
    getExtent()\n
    '''
def setExtent():
    '''returns None\n\n
    setExtent(final int verticalExtent)\n
    '''
def addScrollable():
    '''returns None\n\n
    addScrollable(final IlvVerticalScrollable ilvVerticalScrollable)\n
    '''
def removeScrollable():
    '''returns None\n\n
    removeScrollable(final IlvVerticalScrollable ilvVerticalScrollable)\n
    '''
def addScrollListener():
    '''returns None\n\n
    addScrollListener(final VerticalScrollListener verticalScrollListener)\n
    '''
def removeScrollListener():
    '''returns None\n\n
    removeScrollListener(final VerticalScrollListener verticalScrollListener)\n
    '''
def makeDisplayed():
    '''returns None\n\n
    makeDisplayed(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def scrollBoundsToDisplay():
    '''returns None\n\n
    scrollBoundsToDisplay(final Rectangle rectangle)\n
    '''
def computeScrollPosition():
    '''returns int\n\n
    computeScrollPosition(final int n)\n
    '''
def inform():
    '''returns None\n\n
    inform(final GanttModelChangedEvent ganttModelChangedEvent)\n
    inform(final ResourcesInsertedEvent resourcesInsertedEvent)\n
    inform(final ResourcesRemovedEvent resourcesRemovedEvent)\n
    inform(final ResourceMovedEvent resourceMovedEvent)\n
    inform(final ActivitiesInsertedEvent activitiesInsertedEvent)\n
    inform(final ActivitiesRemovedEvent activitiesRemovedEvent)\n
    inform(final ActivityMovedEvent activityMovedEvent)\n
    '''
def fireGanttModelChanged():
    '''returns None\n\n
    fireGanttModelChanged(final GanttModelChangedEvent ganttModelChangedEvent)\n
    '''
def fireNodesInserted():
    '''returns None\n\n
    fireNodesInserted(final RowsInsertedEvent rowsInsertedEvent)\n
    '''
def fireNodesRemoved():
    '''returns None\n\n
    fireNodesRemoved(final RowsRemovedEvent rowsRemovedEvent)\n
    '''
def fireNodeMoved():
    '''returns None\n\n
    fireNodeMoved(final RowMovedEvent rowMovedEvent)\n
    '''
def fireNodeExpanded():
    '''returns None\n\n
    fireNodeExpanded(final RowExpandedEvent rowExpandedEvent)\n
    '''
def fireNodeCollapsed():
    '''returns None\n\n
    fireNodeCollapsed(final RowCollapsedEvent rowCollapsedEvent)\n
    '''
def fireRootRowVisibilityChanged():
    '''returns None\n\n
    fireRootRowVisibilityChanged(final RootRowVisibilityChangedEvent rootRowVisibilityChangedEvent)\n
    '''
def evaluate():
    '''returns boolean\n\n
    evaluate(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
