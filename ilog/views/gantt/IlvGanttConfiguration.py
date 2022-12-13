ACTIVITY_ROWS = "int  0"
RESOURCE_ROWS = "int  1"
DEFAULT_ROW_HEIGHT = "int  20"
def IlvGanttConfiguration():
    '''    public IlvGanttConfiguration(final int i)
    public IlvGanttConfiguration(final IlvGanttModel ganttModel, final int n)
    '''
def rowsInserted():
    '''    public void rowsInserted(final RowsInsertedEvent rowsInsertedEvent)
    '''
def rowsRemoved():
    '''    public void rowsRemoved(final RowsRemovedEvent rowsRemovedEvent)
    '''
def rowMoved():
    '''    public void rowMoved(final RowMovedEvent rowMovedEvent)
    '''
def rowExpanded():
    '''    public void rowExpanded(final RowExpandedEvent rowExpandedEvent)
    '''
def rowCollapsed():
    '''    public void rowCollapsed(final RowCollapsedEvent rowCollapsedEvent)
    '''
def rowHeightChanged():
    '''    public void rowHeightChanged(final RowHeightChangedEvent rowHeightChangedEvent)
    '''
def rootRowVisibilityChanged():
    '''    public void rootRowVisibilityChanged(final RootRowVisibilityChangedEvent rootRowVisibilityChangedEvent)
    '''
def verticalPositionChanged():
    '''    public void verticalPositionChanged(final VerticalScrollEvent verticalScrollEvent)
    '''
def verticalExtentChanged():
    '''    public void verticalExtentChanged(final VerticalScrollEvent verticalScrollEvent)
    '''
def maxVerticalPositionChanged():
    '''    public void maxVerticalPositionChanged(final VerticalScrollEvent verticalScrollEvent)
    '''
def selectionChanged():
    '''    public void selectionChanged(final SelectionEvent selectionEvent)
    '''
def visibleTimeChanged():
    '''    public void visibleTimeChanged(final VisibleTimeChangedEvent visibleTimeChangedEvent)
    '''
def visibleDurationChanged():
    '''    public void visibleDurationChanged(final VisibleDurationChangedEvent visibleDurationChangedEvent)
    '''
def minVisibleTimeChanged():
    '''    public void minVisibleTimeChanged(final TimeChangedEvent timeChangedEvent)
    '''
def maxVisibleTimeChanged():
    '''    public void maxVisibleTimeChanged(final TimeChangedEvent timeChangedEvent)
    '''
def minVisibleDurationChanged():
    '''    public void minVisibleDurationChanged(final VisibleDurationChangedEvent visibleDurationChangedEvent)
    '''
def getGanttModel():
    '''    public IlvGanttModel getGanttModel()
    '''
def setGanttModel():
    '''    public void setGanttModel(final IlvGanttModel ilvGanttModel)
    '''
def addGanttModelListener():
    '''    public void addGanttModelListener(final GanttModelListener ganttModelListener)
    '''
def removeGanttModelListener():
    '''    public void removeGanttModelListener(final GanttModelListener ganttModelListener)
    '''
def getVerticalDisplayController():
    '''    public IlvVerticalDisplayController getVerticalDisplayController()
    '''
def getRowType():
    '''    public int getRowType()
    '''
def getRootRow():
    '''    public IlvHierarchyNode getRootRow()
    '''
def isRowExpanded():
    '''    public boolean isRowExpanded(final IlvHierarchyNode ilvHierarchyNode)
    '''
def expandRow():
    '''    public void expandRow(final IlvHierarchyNode ilvHierarchyNode)
    '''
def expandAllRows():
    '''    public void expandAllRows(final IlvHierarchyNode ilvHierarchyNode)
    public void expandAllRows()
    '''
def collapseRow():
    '''    public void collapseRow(final IlvHierarchyNode ilvHierarchyNode)
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
def getRootVisibleRow():
    '''    public IlvHierarchyNode getRootVisibleRow()
    '''
def getFirstVisibleRow():
    '''    public IlvHierarchyNode getFirstVisibleRow()
    '''
def isRootRowVisible():
    '''    public boolean isRootRowVisible()
    '''
def setRootRowVisible():
    '''    public void setRootRowVisible(final boolean rootNodeVisible)
    '''
def getRowIndex():
    '''    public int getRowIndex(final IlvHierarchyNode ilvHierarchyNode)
    '''
def getRow():
    '''    public IlvHierarchyNode getRow(final int n)
    '''
def getVisibleRowCount():
    '''    public int getVisibleRowCount()
    '''
def isRowVisible():
    '''    public boolean isRowVisible(final IlvHierarchyNode ilvHierarchyNode)
    '''
def visibleRowsIterator():
    '''    public Iterator<IlvHierarchyNode> visibleRowsIterator(final IlvHierarchyNode ilvHierarchyNode)
    public Iterator<IlvHierarchyNode> visibleRowsIterator()
    '''
def makeRowVisible():
    '''    public void makeRowVisible(final IlvHierarchyNode ilvHierarchyNode)
    '''
def getVisibleRowBounds():
    '''    public Rectangle getVisibleRowBounds(final int n)
    public Rectangle getVisibleRowBounds(final IlvHierarchyNode ilvHierarchyNode)
    '''
def getVisibleRowIndexAtPosition():
    '''    public int getVisibleRowIndexAtPosition(final int n)
    '''
def getVisibleRowAtPosition():
    '''    public IlvHierarchyNode getVisibleRowAtPosition(final int n)
    '''
def getDisplayedRowIndexAtPosition():
    '''    public int getDisplayedRowIndexAtPosition(final int n)
    '''
def getDisplayedRowAtPosition():
    '''    public IlvHierarchyNode getDisplayedRowAtPosition(final int n)
    '''
def makeRowDisplayed():
    '''    public void makeRowDisplayed(final IlvHierarchyNode ilvHierarchyNode)
    '''
def computeVerticalScrollPosition():
    '''    public int computeVerticalScrollPosition(final int n)
    '''
def addVerticalExpandable():
    '''    public void addVerticalExpandable(final IlvVerticalExpandable ilvVerticalExpandable)
    '''
def removeVerticalExpandable():
    '''    public void removeVerticalExpandable(final IlvVerticalExpandable ilvVerticalExpandable)
    '''
def setVerticalExpansionMaster():
    '''    public void setVerticalExpansionMaster(final IlvVerticalExpansionMaster verticalExpansionMaster)
    '''
def addVerticalExpansionListener():
    '''    public void addVerticalExpansionListener(final VerticalExpansionListener verticalExpansionListener)
    '''
def removeVerticalExpansionListener():
    '''    public void removeVerticalExpansionListener(final VerticalExpansionListener verticalExpansionListener)
    '''
def getMaxVerticalPosition():
    '''    public int getMaxVerticalPosition()
    '''
def setMaxVerticalPosition():
    '''    public void setMaxVerticalPosition(final int maxPosition)
    '''
def getVerticalPosition():
    '''    public int getVerticalPosition()
    '''
def setVerticalPosition():
    '''    public void setVerticalPosition(final int position)
    '''
def getVerticalExtent():
    '''    public int getVerticalExtent()
    '''
def setVerticalExtent():
    '''    public void setVerticalExtent(final int extent)
    '''
def addVerticalScrollable():
    '''    public void addVerticalScrollable(final IlvVerticalScrollable ilvVerticalScrollable)
    '''
def removeVerticalScrollable():
    '''    public void removeVerticalScrollable(final IlvVerticalScrollable ilvVerticalScrollable)
    '''
def addVerticalScrollListener():
    '''    public void addVerticalScrollListener(final VerticalScrollListener verticalScrollListener)
    '''
def removeVerticalScrollListener():
    '''    public void removeVerticalScrollListener(final VerticalScrollListener verticalScrollListener)
    '''
def getMinVisibleTime():
    '''    public Date getMinVisibleTime()
    '''
def setMinVisibleTime():
    '''    public void setMinVisibleTime(final Date minVisibleTime)
    '''
def getMaxVisibleTime():
    '''    public Date getMaxVisibleTime()
    '''
def setMaxVisibleTime():
    '''    public void setMaxVisibleTime(final Date maxVisibleTime)
    '''
def getMinVisibleDuration():
    '''    public IlvDuration getMinVisibleDuration()
    '''
def setMinVisibleDuration():
    '''    public void setMinVisibleDuration(final IlvDuration minVisibleDuration)
    '''
def getVisibleTime():
    '''    public Date getVisibleTime()
    '''
def setVisibleTime():
    '''    public void setVisibleTime(final Date visibleTime)
    '''
def getVisibleDuration():
    '''    public IlvDuration getVisibleDuration()
    '''
def setVisibleDuration():
    '''    public void setVisibleDuration(final IlvDuration visibleDuration)
    '''
def getVisibleInterval():
    '''    public IlvTimeInterval getVisibleInterval()
    '''
def setVisibleInterval():
    '''    public void setVisibleInterval(final Date date, final IlvDuration ilvDuration)
    '''
def getVisibleIntervalAnimationSteps():
    '''    public final int getVisibleIntervalAnimationSteps()
    '''
def setVisibleIntervalAnimationSteps():
    '''    public final void setVisibleIntervalAnimationSteps(final int animationSteps)
    '''
def addTimeScrollable():
    '''    public void addTimeScrollable(final IlvTimeScrollable ilvTimeScrollable)
    '''
def removeTimeScrollable():
    '''    public void removeTimeScrollable(final IlvTimeScrollable ilvTimeScrollable)
    '''
def addTimeScrollListener():
    '''    public void addTimeScrollListener(final TimeScrollListener timeScrollListener)
    '''
def removeTimeScrollListener():
    '''    public void removeTimeScrollListener(final TimeScrollListener timeScrollListener)
    '''
def getCacheManager():
    '''    public IlvCacheManager getCacheManager()
    '''
def isReservationCachingEnabled():
    '''    public boolean isReservationCachingEnabled()
    '''
def setReservationCachingEnabled():
    '''    public void setReservationCachingEnabled(final boolean reservationCachingEnabled)
    '''
def getReservationCacheLoadThreshold():
    '''    public float getReservationCacheLoadThreshold()
    '''
def setReservationCacheLoadThreshold():
    '''    public void setReservationCacheLoadThreshold(final float reservationCacheLoadThreshold)
    '''
def getReservationCacheLoadFactor():
    '''    public float getReservationCacheLoadFactor()
    '''
def setReservationCacheLoadFactor():
    '''    public void setReservationCacheLoadFactor(final float reservationCacheLoadFactor)
    '''
def cacheAllReservations():
    '''    public void cacheAllReservations()
    '''
def addSelectable():
    '''    public void addSelectable(final IlvJTree ilvJTree)
    public void addSelectable(final IlvJTable ilvJTable)
    public void addSelectable(final IlvGanttSheet ilvGanttSheet)
    '''
def removeSelectable():
    '''    public void removeSelectable(final IlvJTree ilvJTree)
    public void removeSelectable(final IlvJTable ilvJTable)
    public void removeSelectable(final IlvGanttSheet ilvGanttSheet)
    '''
def isRowSelected():
    '''    public boolean isRowSelected(final IlvHierarchyNode ilvHierarchyNode)
    '''
def selectRow():
    '''    public void selectRow(final int n, final boolean b)
    public void selectRow(final IlvHierarchyNode ilvHierarchyNode, final boolean b)
    '''
def isSelectionAdjusting():
    '''    public boolean isSelectionAdjusting()
    '''
def setSelectionAdjusting():
    '''    public void setSelectionAdjusting(final boolean selectionAdjusting)
    '''
def deSelectAllRows():
    '''    public void deSelectAllRows()
    '''
def getSelectedRows():
    '''    public IlvHierarchyNode[] getSelectedRows()
    '''
def selectedRowsIterator():
    '''    public Iterator<IlvHierarchyNode> selectedRowsIterator()
    '''
def selectedGraphicsIterator():
    '''    public Iterator<IlvGraphic> selectedGraphicsIterator()
    '''
def getSelectedGraphics():
    '''    public IlvGraphic[] getSelectedGraphics()
    '''
def isGraphicSelected():
    '''    public boolean isGraphicSelected(final IlvGraphic ilvGraphic)
    '''
def getSelectedConstraints():
    '''    public IlvConstraint[] getSelectedConstraints()
    '''
def getSelectedReservations():
    '''    public IlvReservation[] getSelectedReservations()
    '''
def addSelectionListener():
    '''    public void addSelectionListener(final SelectionListener selectionListener)
    '''
def removeSelectionListener():
    '''    public void removeSelectionListener(final SelectionListener selectionListener)
    '''
def addListener():
    '''    public void addListener(final GenericEventListener genericEventListener)
    public void addListener(final GenericEventListener genericEventListener, final Class clazz)
    '''
def addActivityHierarchyListener():
    '''    public void addActivityHierarchyListener(final ActivityHierarchyListener activityHierarchyListener)
    '''
def addActivityListener():
    '''    public void addActivityListener(final ActivityListener activityListener)
    '''
def addResourceHierarchyListener():
    '''    public void addResourceHierarchyListener(final ResourceHierarchyListener resourceHierarchyListener)
    '''
def addResourceListener():
    '''    public void addResourceListener(final ResourceListener resourceListener)
    '''
def addConstraintListener():
    '''    public void addConstraintListener(final ConstraintListener constraintListener)
    '''
def addReservationListener():
    '''    public void addReservationListener(final ReservationListener reservationListener)
    '''
def removeListener():
    '''    public void removeListener(final EventListener eventListener)
    '''
def run():
    '''    public void run()
    '''
def activitiesInserted():
    '''    public void activitiesInserted(final ActivitiesInsertedEvent activitiesInsertedEvent)
    '''
def activitiesRemoved():
    '''    public void activitiesRemoved(final ActivitiesRemovedEvent activitiesRemovedEvent)
    '''
def activityMoved():
    '''    public void activityMoved(final ActivityMovedEvent activityMovedEvent)
    '''
def activityChanged():
    '''    public void activityChanged(final ActivityEvent activityEvent)
    '''
def resourcesInserted():
    '''    public void resourcesInserted(final ResourcesInsertedEvent resourcesInsertedEvent)
    '''
def resourcesRemoved():
    '''    public void resourcesRemoved(final ResourcesRemovedEvent resourcesRemovedEvent)
    '''
def resourceMoved():
    '''    public void resourceMoved(final ResourceMovedEvent resourceMovedEvent)
    '''
def resourceChanged():
    '''    public void resourceChanged(final ResourceEvent resourceEvent)
    '''
def constraintChanged():
    '''    public void constraintChanged(final ConstraintEvent constraintEvent)
    '''
def reservationChanged():
    '''    public void reservationChanged(final ReservationEvent reservationEvent)
    '''
