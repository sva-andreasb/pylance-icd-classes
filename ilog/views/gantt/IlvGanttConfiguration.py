ACTIVITY_ROWS = "int  0"
RESOURCE_ROWS = "int  1"
DEFAULT_ROW_HEIGHT = "int  20"
def IlvGanttConfiguration():
'''public IlvGanttConfiguration(final int i)
public IlvGanttConfiguration(final IlvGanttModel ganttModel, final int n)
'''
pass
def rowsInserted():
'''public void rowsInserted(final RowsInsertedEvent rowsInsertedEvent)
'''
pass
def rowsRemoved():
'''public void rowsRemoved(final RowsRemovedEvent rowsRemovedEvent)
'''
pass
def rowMoved():
'''public void rowMoved(final RowMovedEvent rowMovedEvent)
'''
pass
def rowExpanded():
'''public void rowExpanded(final RowExpandedEvent rowExpandedEvent)
'''
pass
def rowCollapsed():
'''public void rowCollapsed(final RowCollapsedEvent rowCollapsedEvent)
'''
pass
def rowHeightChanged():
'''public void rowHeightChanged(final RowHeightChangedEvent rowHeightChangedEvent)
'''
pass
def rootRowVisibilityChanged():
'''public void rootRowVisibilityChanged(final RootRowVisibilityChangedEvent rootRowVisibilityChangedEvent)
'''
pass
def verticalPositionChanged():
'''public void verticalPositionChanged(final VerticalScrollEvent verticalScrollEvent)
'''
pass
def verticalExtentChanged():
'''public void verticalExtentChanged(final VerticalScrollEvent verticalScrollEvent)
'''
pass
def maxVerticalPositionChanged():
'''public void maxVerticalPositionChanged(final VerticalScrollEvent verticalScrollEvent)
'''
pass
def selectionChanged():
'''public void selectionChanged(final SelectionEvent selectionEvent)
'''
pass
def visibleTimeChanged():
'''public void visibleTimeChanged(final VisibleTimeChangedEvent visibleTimeChangedEvent)
'''
pass
def visibleDurationChanged():
'''public void visibleDurationChanged(final VisibleDurationChangedEvent visibleDurationChangedEvent)
'''
pass
def minVisibleTimeChanged():
'''public void minVisibleTimeChanged(final TimeChangedEvent timeChangedEvent)
'''
pass
def maxVisibleTimeChanged():
'''public void maxVisibleTimeChanged(final TimeChangedEvent timeChangedEvent)
'''
pass
def minVisibleDurationChanged():
'''public void minVisibleDurationChanged(final VisibleDurationChangedEvent visibleDurationChangedEvent)
'''
pass
def getGanttModel():
'''public IlvGanttModel getGanttModel()
'''
pass
def setGanttModel():
'''public void setGanttModel(final IlvGanttModel ilvGanttModel)
'''
pass
def addGanttModelListener():
'''public void addGanttModelListener(final GanttModelListener ganttModelListener)
'''
pass
def removeGanttModelListener():
'''public void removeGanttModelListener(final GanttModelListener ganttModelListener)
'''
pass
def getVerticalDisplayController():
'''public IlvVerticalDisplayController getVerticalDisplayController()
'''
pass
def getRowType():
'''public int getRowType()
'''
pass
def getRootRow():
'''public IlvHierarchyNode getRootRow()
'''
pass
def isRowExpanded():
'''public boolean isRowExpanded(final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def expandRow():
'''public void expandRow(final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def expandAllRows():
'''public void expandAllRows(final IlvHierarchyNode ilvHierarchyNode)
public void expandAllRows()
'''
pass
def collapseRow():
'''public void collapseRow(final IlvHierarchyNode ilvHierarchyNode)
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
def getRootVisibleRow():
'''public IlvHierarchyNode getRootVisibleRow()
'''
pass
def getFirstVisibleRow():
'''public IlvHierarchyNode getFirstVisibleRow()
'''
pass
def isRootRowVisible():
'''public boolean isRootRowVisible()
'''
pass
def setRootRowVisible():
'''public void setRootRowVisible(final boolean rootNodeVisible)
'''
pass
def getRowIndex():
'''public int getRowIndex(final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def getRow():
'''public IlvHierarchyNode getRow(final int n)
'''
pass
def getVisibleRowCount():
'''public int getVisibleRowCount()
'''
pass
def isRowVisible():
'''public boolean isRowVisible(final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def visibleRowsIterator():
'''public Iterator<IlvHierarchyNode> visibleRowsIterator(final IlvHierarchyNode ilvHierarchyNode)
public Iterator<IlvHierarchyNode> visibleRowsIterator()
'''
pass
def makeRowVisible():
'''public void makeRowVisible(final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def getVisibleRowBounds():
'''public Rectangle getVisibleRowBounds(final int n)
public Rectangle getVisibleRowBounds(final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def getVisibleRowIndexAtPosition():
'''public int getVisibleRowIndexAtPosition(final int n)
'''
pass
def getVisibleRowAtPosition():
'''public IlvHierarchyNode getVisibleRowAtPosition(final int n)
'''
pass
def getDisplayedRowIndexAtPosition():
'''public int getDisplayedRowIndexAtPosition(final int n)
'''
pass
def getDisplayedRowAtPosition():
'''public IlvHierarchyNode getDisplayedRowAtPosition(final int n)
'''
pass
def makeRowDisplayed():
'''public void makeRowDisplayed(final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def computeVerticalScrollPosition():
'''public int computeVerticalScrollPosition(final int n)
'''
pass
def addVerticalExpandable():
'''public void addVerticalExpandable(final IlvVerticalExpandable ilvVerticalExpandable)
'''
pass
def removeVerticalExpandable():
'''public void removeVerticalExpandable(final IlvVerticalExpandable ilvVerticalExpandable)
'''
pass
def setVerticalExpansionMaster():
'''public void setVerticalExpansionMaster(final IlvVerticalExpansionMaster verticalExpansionMaster)
'''
pass
def addVerticalExpansionListener():
'''public void addVerticalExpansionListener(final VerticalExpansionListener verticalExpansionListener)
'''
pass
def removeVerticalExpansionListener():
'''public void removeVerticalExpansionListener(final VerticalExpansionListener verticalExpansionListener)
'''
pass
def getMaxVerticalPosition():
'''public int getMaxVerticalPosition()
'''
pass
def setMaxVerticalPosition():
'''public void setMaxVerticalPosition(final int maxPosition)
'''
pass
def getVerticalPosition():
'''public int getVerticalPosition()
'''
pass
def setVerticalPosition():
'''public void setVerticalPosition(final int position)
'''
pass
def getVerticalExtent():
'''public int getVerticalExtent()
'''
pass
def setVerticalExtent():
'''public void setVerticalExtent(final int extent)
'''
pass
def addVerticalScrollable():
'''public void addVerticalScrollable(final IlvVerticalScrollable ilvVerticalScrollable)
'''
pass
def removeVerticalScrollable():
'''public void removeVerticalScrollable(final IlvVerticalScrollable ilvVerticalScrollable)
'''
pass
def addVerticalScrollListener():
'''public void addVerticalScrollListener(final VerticalScrollListener verticalScrollListener)
'''
pass
def removeVerticalScrollListener():
'''public void removeVerticalScrollListener(final VerticalScrollListener verticalScrollListener)
'''
pass
def getMinVisibleTime():
'''public Date getMinVisibleTime()
'''
pass
def setMinVisibleTime():
'''public void setMinVisibleTime(final Date minVisibleTime)
'''
pass
def getMaxVisibleTime():
'''public Date getMaxVisibleTime()
'''
pass
def setMaxVisibleTime():
'''public void setMaxVisibleTime(final Date maxVisibleTime)
'''
pass
def getMinVisibleDuration():
'''public IlvDuration getMinVisibleDuration()
'''
pass
def setMinVisibleDuration():
'''public void setMinVisibleDuration(final IlvDuration minVisibleDuration)
'''
pass
def getVisibleTime():
'''public Date getVisibleTime()
'''
pass
def setVisibleTime():
'''public void setVisibleTime(final Date visibleTime)
'''
pass
def getVisibleDuration():
'''public IlvDuration getVisibleDuration()
'''
pass
def setVisibleDuration():
'''public void setVisibleDuration(final IlvDuration visibleDuration)
'''
pass
def getVisibleInterval():
'''public IlvTimeInterval getVisibleInterval()
'''
pass
def setVisibleInterval():
'''public void setVisibleInterval(final Date date, final IlvDuration ilvDuration)
'''
pass
def getVisibleIntervalAnimationSteps():
'''public final int getVisibleIntervalAnimationSteps()
'''
pass
def setVisibleIntervalAnimationSteps():
'''public final void setVisibleIntervalAnimationSteps(final int animationSteps)
'''
pass
def addTimeScrollable():
'''public void addTimeScrollable(final IlvTimeScrollable ilvTimeScrollable)
'''
pass
def removeTimeScrollable():
'''public void removeTimeScrollable(final IlvTimeScrollable ilvTimeScrollable)
'''
pass
def addTimeScrollListener():
'''public void addTimeScrollListener(final TimeScrollListener timeScrollListener)
'''
pass
def removeTimeScrollListener():
'''public void removeTimeScrollListener(final TimeScrollListener timeScrollListener)
'''
pass
def getCacheManager():
'''public IlvCacheManager getCacheManager()
'''
pass
def isReservationCachingEnabled():
'''public boolean isReservationCachingEnabled()
'''
pass
def setReservationCachingEnabled():
'''public void setReservationCachingEnabled(final boolean reservationCachingEnabled)
'''
pass
def getReservationCacheLoadThreshold():
'''public float getReservationCacheLoadThreshold()
'''
pass
def setReservationCacheLoadThreshold():
'''public void setReservationCacheLoadThreshold(final float reservationCacheLoadThreshold)
'''
pass
def getReservationCacheLoadFactor():
'''public float getReservationCacheLoadFactor()
'''
pass
def setReservationCacheLoadFactor():
'''public void setReservationCacheLoadFactor(final float reservationCacheLoadFactor)
'''
pass
def cacheAllReservations():
'''public void cacheAllReservations()
'''
pass
def addSelectable():
'''public void addSelectable(final IlvJTree ilvJTree)
public void addSelectable(final IlvJTable ilvJTable)
public void addSelectable(final IlvGanttSheet ilvGanttSheet)
'''
pass
def removeSelectable():
'''public void removeSelectable(final IlvJTree ilvJTree)
public void removeSelectable(final IlvJTable ilvJTable)
public void removeSelectable(final IlvGanttSheet ilvGanttSheet)
'''
pass
def isRowSelected():
'''public boolean isRowSelected(final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def selectRow():
'''public void selectRow(final int n, final boolean b)
public void selectRow(final IlvHierarchyNode ilvHierarchyNode, final boolean b)
'''
pass
def isSelectionAdjusting():
'''public boolean isSelectionAdjusting()
'''
pass
def setSelectionAdjusting():
'''public void setSelectionAdjusting(final boolean selectionAdjusting)
'''
pass
def deSelectAllRows():
'''public void deSelectAllRows()
'''
pass
def getSelectedRows():
'''public IlvHierarchyNode[] getSelectedRows()
'''
pass
def selectedRowsIterator():
'''public Iterator<IlvHierarchyNode> selectedRowsIterator()
'''
pass
def selectedGraphicsIterator():
'''public Iterator<IlvGraphic> selectedGraphicsIterator()
'''
pass
def getSelectedGraphics():
'''public IlvGraphic[] getSelectedGraphics()
'''
pass
def isGraphicSelected():
'''public boolean isGraphicSelected(final IlvGraphic ilvGraphic)
'''
pass
def getSelectedConstraints():
'''public IlvConstraint[] getSelectedConstraints()
'''
pass
def getSelectedReservations():
'''public IlvReservation[] getSelectedReservations()
'''
pass
def addSelectionListener():
'''public void addSelectionListener(final SelectionListener selectionListener)
'''
pass
def removeSelectionListener():
'''public void removeSelectionListener(final SelectionListener selectionListener)
'''
pass
def addListener():
'''public void addListener(final GenericEventListener genericEventListener)
public void addListener(final GenericEventListener genericEventListener, final Class clazz)
'''
pass
def addActivityHierarchyListener():
'''public void addActivityHierarchyListener(final ActivityHierarchyListener activityHierarchyListener)
'''
pass
def addActivityListener():
'''public void addActivityListener(final ActivityListener activityListener)
'''
pass
def addResourceHierarchyListener():
'''public void addResourceHierarchyListener(final ResourceHierarchyListener resourceHierarchyListener)
'''
pass
def addResourceListener():
'''public void addResourceListener(final ResourceListener resourceListener)
'''
pass
def addConstraintListener():
'''public void addConstraintListener(final ConstraintListener constraintListener)
'''
pass
def addReservationListener():
'''public void addReservationListener(final ReservationListener reservationListener)
'''
pass
def removeListener():
'''public void removeListener(final EventListener eventListener)
'''
pass
def run():
'''public void run()
'''
pass
def activitiesInserted():
'''public void activitiesInserted(final ActivitiesInsertedEvent activitiesInsertedEvent)
'''
pass
def activitiesRemoved():
'''public void activitiesRemoved(final ActivitiesRemovedEvent activitiesRemovedEvent)
'''
pass
def activityMoved():
'''public void activityMoved(final ActivityMovedEvent activityMovedEvent)
'''
pass
def activityChanged():
'''public void activityChanged(final ActivityEvent activityEvent)
'''
pass
def resourcesInserted():
'''public void resourcesInserted(final ResourcesInsertedEvent resourcesInsertedEvent)
'''
pass
def resourcesRemoved():
'''public void resourcesRemoved(final ResourcesRemovedEvent resourcesRemovedEvent)
'''
pass
def resourceMoved():
'''public void resourceMoved(final ResourceMovedEvent resourceMovedEvent)
'''
pass
def resourceChanged():
'''public void resourceChanged(final ResourceEvent resourceEvent)
'''
pass
def constraintChanged():
'''public void constraintChanged(final ConstraintEvent constraintEvent)
'''
pass
def reservationChanged():
'''public void reservationChanged(final ReservationEvent reservationEvent)
'''
pass
