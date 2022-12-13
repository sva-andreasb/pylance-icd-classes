ACTIVITY_ROWS = "int  0"
RESOURCE_ROWS = "int  1"
DEFAULT_ROW_HEIGHT = "int  20"
def IlvVerticalDisplayController():
    '''    public IlvVerticalDisplayController(final int n)
    '''
def getRowType():
    '''    public int getRowType()
    '''
def getGanttConfiguration():
    '''    public IlvGanttConfiguration getGanttConfiguration()
    '''
def getRootDataNode():
    '''    public IlvHierarchyNode getRootDataNode()
    '''
def getRootNode():
    '''    public IlvHierarchyNode getRootNode()
    '''
def getFirstNode():
    '''    public IlvHierarchyNode getFirstNode()
    '''
def getNodeForRow():
    '''    public IlvHierarchyNode getNodeForRow(final int n)
    '''
def getRowForNode():
    '''    public int getRowForNode(final IlvHierarchyNode ilvHierarchyNode)
    '''
def getRowCount():
    '''    public int getRowCount()
    '''
def validateRowHeights():
    '''    public void validateRowHeights()
    '''
def isFixedRowHeight():
    '''    public boolean isFixedRowHeight()
    '''
def getRowHeight():
    '''    public int getRowHeight()
    public int getRowHeight(final IlvHierarchyNode ilvHierarchyNode)
    '''
def setRowHeight():
    '''    public void setRowHeight(final int rowHeight)
    public void setRowHeight(final IlvHierarchyNode ilvHierarchyNode, final int n)
    '''
def getRowAtPosition():
    '''    public int getRowAtPosition(final int n)
    '''
def getDisplayedRowAtPosition():
    '''    public int getDisplayedRowAtPosition(final int n)
    '''
def getNodeAtPosition():
    '''    public IlvHierarchyNode getNodeAtPosition(final int n)
    '''
def getDisplayedNodeAtPosition():
    '''    public IlvHierarchyNode getDisplayedNodeAtPosition(final int n)
    '''
def getRowBounds():
    '''    public Rectangle getRowBounds(final int n)
    '''
def getNodeBounds():
    '''    public Rectangle getNodeBounds(final IlvHierarchyNode ilvHierarchyNode)
    '''
def isRootNodeVisible():
    '''    public boolean isRootNodeVisible()
    '''
def setRootNodeVisible():
    '''    public void setRootNodeVisible(final boolean rootRowVisible)
    '''
def isExpanded():
    '''    public boolean isExpanded(final IlvHierarchyNode ilvHierarchyNode)
    '''
def isVisible():
    '''    public boolean isVisible(final IlvHierarchyNode ilvHierarchyNode)
    '''
def visibleNodesIterator():
    '''    public Iterator<IlvHierarchyNode> visibleNodesIterator(final IlvHierarchyNode ilvHierarchyNode)
    public Iterator<IlvHierarchyNode> visibleNodesIterator()
    '''
def makeVisible():
    '''    public void makeVisible(final IlvHierarchyNode ilvHierarchyNode)
    '''
def expandNode():
    '''    public void expandNode(final IlvHierarchyNode ilvHierarchyNode)
    '''
def collapseNode():
    '''    public void collapseNode(final IlvHierarchyNode ilvHierarchyNode)
    '''
def addExpandable():
    '''    public synchronized void addExpandable(final IlvVerticalExpandable ilvVerticalExpandable)
    '''
def removeExpandable():
    '''    public synchronized void removeExpandable(final IlvVerticalExpandable ilvVerticalExpandable)
    '''
def setVerticalExpansionMaster():
    '''    public void setVerticalExpansionMaster(final IlvVerticalExpansionMaster f)
    '''
def addExpansionListener():
    '''    public void addExpansionListener(final VerticalExpansionListener verticalExpansionListener)
    '''
def removeExpansionListener():
    '''    public void removeExpansionListener(final VerticalExpansionListener verticalExpansionListener)
    '''
def getMaxPosition():
    '''    public int getMaxPosition()
    '''
def setMaxPosition():
    '''    public void setMaxPosition(final int maxVerticalPosition)
    '''
def getPosition():
    '''    public int getPosition()
    '''
def setPosition():
    '''    public void setPosition(final int verticalPosition)
    '''
def getExtent():
    '''    public int getExtent()
    '''
def setExtent():
    '''    public void setExtent(final int verticalExtent)
    '''
def addScrollable():
    '''    public void addScrollable(final IlvVerticalScrollable ilvVerticalScrollable)
    '''
def removeScrollable():
    '''    public void removeScrollable(final IlvVerticalScrollable ilvVerticalScrollable)
    '''
def addScrollListener():
    '''    public void addScrollListener(final VerticalScrollListener verticalScrollListener)
    '''
def removeScrollListener():
    '''    public void removeScrollListener(final VerticalScrollListener verticalScrollListener)
    '''
def makeDisplayed():
    '''    public void makeDisplayed(final IlvHierarchyNode ilvHierarchyNode)
    '''
def run():
    '''    public void run()
    '''
def scrollBoundsToDisplay():
    '''    public void scrollBoundsToDisplay(final Rectangle rectangle)
    '''
def computeScrollPosition():
    '''    public int computeScrollPosition(final int n)
    '''
def inform():
    '''    public void inform(final GanttModelChangedEvent ganttModelChangedEvent)
    public void inform(final ResourcesInsertedEvent resourcesInsertedEvent)
    public void inform(final ResourcesRemovedEvent resourcesRemovedEvent)
    public void inform(final ResourceMovedEvent resourceMovedEvent)
    public void inform(final ActivitiesInsertedEvent activitiesInsertedEvent)
    public void inform(final ActivitiesRemovedEvent activitiesRemovedEvent)
    public void inform(final ActivityMovedEvent activityMovedEvent)
    '''
def fireGanttModelChanged():
    '''    public void fireGanttModelChanged(final GanttModelChangedEvent ganttModelChangedEvent)
    '''
def fireNodesInserted():
    '''    public void fireNodesInserted(final RowsInsertedEvent rowsInsertedEvent)
    '''
def fireNodesRemoved():
    '''    public void fireNodesRemoved(final RowsRemovedEvent rowsRemovedEvent)
    '''
def fireNodeMoved():
    '''    public void fireNodeMoved(final RowMovedEvent rowMovedEvent)
    '''
def fireNodeExpanded():
    '''    public void fireNodeExpanded(final RowExpandedEvent rowExpandedEvent)
    '''
def fireNodeCollapsed():
    '''    public void fireNodeCollapsed(final RowCollapsedEvent rowCollapsedEvent)
    '''
def fireRootRowVisibilityChanged():
    '''    public void fireRootRowVisibilityChanged(final RootRowVisibilityChangedEvent rootRowVisibilityChangedEvent)
    '''
def evaluate():
    '''    public boolean evaluate(final IlvHierarchyNode ilvHierarchyNode)
    '''
