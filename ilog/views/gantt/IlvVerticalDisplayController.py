ACTIVITY_ROWS = "int  0"
RESOURCE_ROWS = "int  1"
DEFAULT_ROW_HEIGHT = "int  20"
def IlvVerticalDisplayController():
'''public IlvVerticalDisplayController(final int n)
'''
pass
def getRowType():
'''public int getRowType()
'''
pass
def getGanttConfiguration():
'''public IlvGanttConfiguration getGanttConfiguration()
'''
pass
def getRootDataNode():
'''public IlvHierarchyNode getRootDataNode()
'''
pass
def getRootNode():
'''public IlvHierarchyNode getRootNode()
'''
pass
def getFirstNode():
'''public IlvHierarchyNode getFirstNode()
'''
pass
def getNodeForRow():
'''public IlvHierarchyNode getNodeForRow(final int n)
'''
pass
def getRowForNode():
'''public int getRowForNode(final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def getRowCount():
'''public int getRowCount()
'''
pass
def validateRowHeights():
'''public void validateRowHeights()
'''
pass
def isFixedRowHeight():
'''public boolean isFixedRowHeight()
'''
pass
def getRowHeight():
'''public int getRowHeight()
public int getRowHeight(final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def setRowHeight():
'''public void setRowHeight(final int rowHeight)
public void setRowHeight(final IlvHierarchyNode ilvHierarchyNode, final int n)
'''
pass
def getRowAtPosition():
'''public int getRowAtPosition(final int n)
'''
pass
def getDisplayedRowAtPosition():
'''public int getDisplayedRowAtPosition(final int n)
'''
pass
def getNodeAtPosition():
'''public IlvHierarchyNode getNodeAtPosition(final int n)
'''
pass
def getDisplayedNodeAtPosition():
'''public IlvHierarchyNode getDisplayedNodeAtPosition(final int n)
'''
pass
def getRowBounds():
'''public Rectangle getRowBounds(final int n)
'''
pass
def getNodeBounds():
'''public Rectangle getNodeBounds(final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def isRootNodeVisible():
'''public boolean isRootNodeVisible()
'''
pass
def setRootNodeVisible():
'''public void setRootNodeVisible(final boolean rootRowVisible)
'''
pass
def isExpanded():
'''public boolean isExpanded(final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def isVisible():
'''public boolean isVisible(final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def visibleNodesIterator():
'''public Iterator<IlvHierarchyNode> visibleNodesIterator(final IlvHierarchyNode ilvHierarchyNode)
public Iterator<IlvHierarchyNode> visibleNodesIterator()
'''
pass
def makeVisible():
'''public void makeVisible(final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def expandNode():
'''public void expandNode(final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def collapseNode():
'''public void collapseNode(final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def addExpandable():
'''public synchronized void addExpandable(final IlvVerticalExpandable ilvVerticalExpandable)
'''
pass
def removeExpandable():
'''public synchronized void removeExpandable(final IlvVerticalExpandable ilvVerticalExpandable)
'''
pass
def setVerticalExpansionMaster():
'''public void setVerticalExpansionMaster(final IlvVerticalExpansionMaster f)
'''
pass
def addExpansionListener():
'''public void addExpansionListener(final VerticalExpansionListener verticalExpansionListener)
'''
pass
def removeExpansionListener():
'''public void removeExpansionListener(final VerticalExpansionListener verticalExpansionListener)
'''
pass
def getMaxPosition():
'''public int getMaxPosition()
'''
pass
def setMaxPosition():
'''public void setMaxPosition(final int maxVerticalPosition)
'''
pass
def getPosition():
'''public int getPosition()
'''
pass
def setPosition():
'''public void setPosition(final int verticalPosition)
'''
pass
def getExtent():
'''public int getExtent()
'''
pass
def setExtent():
'''public void setExtent(final int verticalExtent)
'''
pass
def addScrollable():
'''public void addScrollable(final IlvVerticalScrollable ilvVerticalScrollable)
'''
pass
def removeScrollable():
'''public void removeScrollable(final IlvVerticalScrollable ilvVerticalScrollable)
'''
pass
def addScrollListener():
'''public void addScrollListener(final VerticalScrollListener verticalScrollListener)
'''
pass
def removeScrollListener():
'''public void removeScrollListener(final VerticalScrollListener verticalScrollListener)
'''
pass
def makeDisplayed():
'''public void makeDisplayed(final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def run():
'''public void run()
'''
pass
def scrollBoundsToDisplay():
'''public void scrollBoundsToDisplay(final Rectangle rectangle)
'''
pass
def computeScrollPosition():
'''public int computeScrollPosition(final int n)
'''
pass
def inform():
'''public void inform(final GanttModelChangedEvent ganttModelChangedEvent)
public void inform(final ResourcesInsertedEvent resourcesInsertedEvent)
public void inform(final ResourcesRemovedEvent resourcesRemovedEvent)
public void inform(final ResourceMovedEvent resourceMovedEvent)
public void inform(final ActivitiesInsertedEvent activitiesInsertedEvent)
public void inform(final ActivitiesRemovedEvent activitiesRemovedEvent)
public void inform(final ActivityMovedEvent activityMovedEvent)
'''
pass
def fireGanttModelChanged():
'''public void fireGanttModelChanged(final GanttModelChangedEvent ganttModelChangedEvent)
'''
pass
def fireNodesInserted():
'''public void fireNodesInserted(final RowsInsertedEvent rowsInsertedEvent)
'''
pass
def fireNodesRemoved():
'''public void fireNodesRemoved(final RowsRemovedEvent rowsRemovedEvent)
'''
pass
def fireNodeMoved():
'''public void fireNodeMoved(final RowMovedEvent rowMovedEvent)
'''
pass
def fireNodeExpanded():
'''public void fireNodeExpanded(final RowExpandedEvent rowExpandedEvent)
'''
pass
def fireNodeCollapsed():
'''public void fireNodeCollapsed(final RowCollapsedEvent rowCollapsedEvent)
'''
pass
def fireRootRowVisibilityChanged():
'''public void fireRootRowVisibilityChanged(final RootRowVisibilityChangedEvent rootRowVisibilityChangedEvent)
'''
pass
def evaluate():
'''public boolean evaluate(final IlvHierarchyNode ilvHierarchyNode)
'''
pass
