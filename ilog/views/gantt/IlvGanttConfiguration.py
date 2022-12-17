ACTIVITY_ROWS = "int  0"
RESOURCE_ROWS = "int  1"
DEFAULT_ROW_HEIGHT = "int  20"
def ():
    '''returns IlvGanttConfiguration\n\n
    (final int i)\n
    (final IlvGanttModel ganttModel, final int n)\n
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
def verticalPositionChanged():
    '''returns None\n\n
    verticalPositionChanged(final VerticalScrollEvent verticalScrollEvent)\n
    '''
def verticalExtentChanged():
    '''returns None\n\n
    verticalExtentChanged(final VerticalScrollEvent verticalScrollEvent)\n
    '''
def maxVerticalPositionChanged():
    '''returns None\n\n
    maxVerticalPositionChanged(final VerticalScrollEvent verticalScrollEvent)\n
    '''
def selectionChanged():
    '''returns None\n\n
    selectionChanged(final SelectionEvent selectionEvent)\n
    '''
def visibleTimeChanged():
    '''returns None\n\n
    visibleTimeChanged(final VisibleTimeChangedEvent visibleTimeChangedEvent)\n
    '''
def visibleDurationChanged():
    '''returns None\n\n
    visibleDurationChanged(final VisibleDurationChangedEvent visibleDurationChangedEvent)\n
    '''
def minVisibleTimeChanged():
    '''returns None\n\n
    minVisibleTimeChanged(final TimeChangedEvent timeChangedEvent)\n
    '''
def maxVisibleTimeChanged():
    '''returns None\n\n
    maxVisibleTimeChanged(final TimeChangedEvent timeChangedEvent)\n
    '''
def minVisibleDurationChanged():
    '''returns None\n\n
    minVisibleDurationChanged(final VisibleDurationChangedEvent visibleDurationChangedEvent)\n
    '''
def getGanttModel():
    '''returns IlvGanttModel\n\n
    getGanttModel()\n
    '''
def setGanttModel():
    '''returns None\n\n
    setGanttModel(final IlvGanttModel ilvGanttModel)\n
    '''
def addGanttModelListener():
    '''returns None\n\n
    addGanttModelListener(final GanttModelListener ganttModelListener)\n
    '''
def removeGanttModelListener():
    '''returns None\n\n
    removeGanttModelListener(final GanttModelListener ganttModelListener)\n
    '''
def getVerticalDisplayController():
    '''returns IlvVerticalDisplayController\n\n
    getVerticalDisplayController()\n
    '''
def getRowType():
    '''returns int\n\n
    getRowType()\n
    '''
def getRootRow():
    '''returns IlvHierarchyNode\n\n
    getRootRow()\n
    '''
def isRowExpanded():
    '''returns boolean\n\n
    isRowExpanded(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def expandRow():
    '''returns None\n\n
    expandRow(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def expandAllRows():
    '''returns None\n\n
    expandAllRows(final IlvHierarchyNode ilvHierarchyNode)\n
    expandAllRows()\n
    '''
def collapseRow():
    '''returns None\n\n
    collapseRow(final IlvHierarchyNode ilvHierarchyNode)\n
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
def getRootVisibleRow():
    '''returns IlvHierarchyNode\n\n
    getRootVisibleRow()\n
    '''
def getFirstVisibleRow():
    '''returns IlvHierarchyNode\n\n
    getFirstVisibleRow()\n
    '''
def isRootRowVisible():
    '''returns boolean\n\n
    isRootRowVisible()\n
    '''
def setRootRowVisible():
    '''returns None\n\n
    setRootRowVisible(final boolean rootNodeVisible)\n
    '''
def getRowIndex():
    '''returns int\n\n
    getRowIndex(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def getRow():
    '''returns IlvHierarchyNode\n\n
    getRow(final int n)\n
    '''
def getVisibleRowCount():
    '''returns int\n\n
    getVisibleRowCount()\n
    '''
def isRowVisible():
    '''returns boolean\n\n
    isRowVisible(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def visibleRowsIterator():
    '''returns Iterator<IlvHierarchyNode>\n\n
    visibleRowsIterator(final IlvHierarchyNode ilvHierarchyNode)\n
    visibleRowsIterator()\n
    '''
def makeRowVisible():
    '''returns None\n\n
    makeRowVisible(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def getVisibleRowBounds():
    '''returns Rectangle\n\n
    getVisibleRowBounds(final int n)\n
    getVisibleRowBounds(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def getVisibleRowIndexAtPosition():
    '''returns int\n\n
    getVisibleRowIndexAtPosition(final int n)\n
    '''
def getVisibleRowAtPosition():
    '''returns IlvHierarchyNode\n\n
    getVisibleRowAtPosition(final int n)\n
    '''
def getDisplayedRowIndexAtPosition():
    '''returns int\n\n
    getDisplayedRowIndexAtPosition(final int n)\n
    '''
def getDisplayedRowAtPosition():
    '''returns IlvHierarchyNode\n\n
    getDisplayedRowAtPosition(final int n)\n
    '''
def makeRowDisplayed():
    '''returns None\n\n
    makeRowDisplayed(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def computeVerticalScrollPosition():
    '''returns int\n\n
    computeVerticalScrollPosition(final int n)\n
    '''
def addVerticalExpandable():
    '''returns None\n\n
    addVerticalExpandable(final IlvVerticalExpandable ilvVerticalExpandable)\n
    '''
def removeVerticalExpandable():
    '''returns None\n\n
    removeVerticalExpandable(final IlvVerticalExpandable ilvVerticalExpandable)\n
    '''
def setVerticalExpansionMaster():
    '''returns None\n\n
    setVerticalExpansionMaster(final IlvVerticalExpansionMaster verticalExpansionMaster)\n
    '''
def addVerticalExpansionListener():
    '''returns None\n\n
    addVerticalExpansionListener(final VerticalExpansionListener verticalExpansionListener)\n
    '''
def removeVerticalExpansionListener():
    '''returns None\n\n
    removeVerticalExpansionListener(final VerticalExpansionListener verticalExpansionListener)\n
    '''
def getMaxVerticalPosition():
    '''returns int\n\n
    getMaxVerticalPosition()\n
    '''
def setMaxVerticalPosition():
    '''returns None\n\n
    setMaxVerticalPosition(final int maxPosition)\n
    '''
def getVerticalPosition():
    '''returns int\n\n
    getVerticalPosition()\n
    '''
def setVerticalPosition():
    '''returns None\n\n
    setVerticalPosition(final int position)\n
    '''
def getVerticalExtent():
    '''returns int\n\n
    getVerticalExtent()\n
    '''
def setVerticalExtent():
    '''returns None\n\n
    setVerticalExtent(final int extent)\n
    '''
def addVerticalScrollable():
    '''returns None\n\n
    addVerticalScrollable(final IlvVerticalScrollable ilvVerticalScrollable)\n
    '''
def removeVerticalScrollable():
    '''returns None\n\n
    removeVerticalScrollable(final IlvVerticalScrollable ilvVerticalScrollable)\n
    '''
def addVerticalScrollListener():
    '''returns None\n\n
    addVerticalScrollListener(final VerticalScrollListener verticalScrollListener)\n
    '''
def removeVerticalScrollListener():
    '''returns None\n\n
    removeVerticalScrollListener(final VerticalScrollListener verticalScrollListener)\n
    '''
def getMinVisibleTime():
    '''returns Date\n\n
    getMinVisibleTime()\n
    '''
def setMinVisibleTime():
    '''returns None\n\n
    setMinVisibleTime(final Date minVisibleTime)\n
    '''
def getMaxVisibleTime():
    '''returns Date\n\n
    getMaxVisibleTime()\n
    '''
def setMaxVisibleTime():
    '''returns None\n\n
    setMaxVisibleTime(final Date maxVisibleTime)\n
    '''
def getMinVisibleDuration():
    '''returns IlvDuration\n\n
    getMinVisibleDuration()\n
    '''
def setMinVisibleDuration():
    '''returns None\n\n
    setMinVisibleDuration(final IlvDuration minVisibleDuration)\n
    '''
def getVisibleTime():
    '''returns Date\n\n
    getVisibleTime()\n
    '''
def setVisibleTime():
    '''returns None\n\n
    setVisibleTime(final Date visibleTime)\n
    '''
def getVisibleDuration():
    '''returns IlvDuration\n\n
    getVisibleDuration()\n
    '''
def setVisibleDuration():
    '''returns None\n\n
    setVisibleDuration(final IlvDuration visibleDuration)\n
    '''
def getVisibleInterval():
    '''returns IlvTimeInterval\n\n
    getVisibleInterval()\n
    '''
def setVisibleInterval():
    '''returns None\n\n
    setVisibleInterval(final Date date, final IlvDuration ilvDuration)\n
    '''
def addTimeScrollable():
    '''returns None\n\n
    addTimeScrollable(final IlvTimeScrollable ilvTimeScrollable)\n
    '''
def removeTimeScrollable():
    '''returns None\n\n
    removeTimeScrollable(final IlvTimeScrollable ilvTimeScrollable)\n
    '''
def addTimeScrollListener():
    '''returns None\n\n
    addTimeScrollListener(final TimeScrollListener timeScrollListener)\n
    '''
def removeTimeScrollListener():
    '''returns None\n\n
    removeTimeScrollListener(final TimeScrollListener timeScrollListener)\n
    '''
def getCacheManager():
    '''returns IlvCacheManager\n\n
    getCacheManager()\n
    '''
def isReservationCachingEnabled():
    '''returns boolean\n\n
    isReservationCachingEnabled()\n
    '''
def setReservationCachingEnabled():
    '''returns None\n\n
    setReservationCachingEnabled(final boolean reservationCachingEnabled)\n
    '''
def getReservationCacheLoadThreshold():
    '''returns float\n\n
    getReservationCacheLoadThreshold()\n
    '''
def setReservationCacheLoadThreshold():
    '''returns None\n\n
    setReservationCacheLoadThreshold(final float reservationCacheLoadThreshold)\n
    '''
def getReservationCacheLoadFactor():
    '''returns float\n\n
    getReservationCacheLoadFactor()\n
    '''
def setReservationCacheLoadFactor():
    '''returns None\n\n
    setReservationCacheLoadFactor(final float reservationCacheLoadFactor)\n
    '''
def cacheAllReservations():
    '''returns None\n\n
    cacheAllReservations()\n
    '''
def addSelectable():
    '''returns None\n\n
    addSelectable(final IlvJTree ilvJTree)\n
    addSelectable(final IlvJTable ilvJTable)\n
    addSelectable(final IlvGanttSheet ilvGanttSheet)\n
    '''
def removeSelectable():
    '''returns None\n\n
    removeSelectable(final IlvJTree ilvJTree)\n
    removeSelectable(final IlvJTable ilvJTable)\n
    removeSelectable(final IlvGanttSheet ilvGanttSheet)\n
    '''
def isRowSelected():
    '''returns boolean\n\n
    isRowSelected(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def selectRow():
    '''returns None\n\n
    selectRow(final int n, final boolean b)\n
    selectRow(final IlvHierarchyNode ilvHierarchyNode, final boolean b)\n
    '''
def isSelectionAdjusting():
    '''returns boolean\n\n
    isSelectionAdjusting()\n
    '''
def setSelectionAdjusting():
    '''returns None\n\n
    setSelectionAdjusting(final boolean selectionAdjusting)\n
    '''
def deSelectAllRows():
    '''returns None\n\n
    deSelectAllRows()\n
    '''
def getSelectedRows():
    '''returns IlvHierarchyNode[]\n\n
    getSelectedRows()\n
    '''
def selectedRowsIterator():
    '''returns Iterator<IlvHierarchyNode>\n\n
    selectedRowsIterator()\n
    '''
def selectedGraphicsIterator():
    '''returns Iterator<IlvGraphic>\n\n
    selectedGraphicsIterator()\n
    '''
def getSelectedGraphics():
    '''returns IlvGraphic[]\n\n
    getSelectedGraphics()\n
    '''
def isGraphicSelected():
    '''returns boolean\n\n
    isGraphicSelected(final IlvGraphic ilvGraphic)\n
    '''
def getSelectedConstraints():
    '''returns IlvConstraint[]\n\n
    getSelectedConstraints()\n
    '''
def getSelectedReservations():
    '''returns IlvReservation[]\n\n
    getSelectedReservations()\n
    '''
def addSelectionListener():
    '''returns None\n\n
    addSelectionListener(final SelectionListener selectionListener)\n
    '''
def removeSelectionListener():
    '''returns None\n\n
    removeSelectionListener(final SelectionListener selectionListener)\n
    '''
def addListener():
    '''returns None\n\n
    addListener(final GenericEventListener genericEventListener)\n
    addListener(final GenericEventListener genericEventListener, final Class clazz)\n
    '''
def addActivityHierarchyListener():
    '''returns None\n\n
    addActivityHierarchyListener(final ActivityHierarchyListener activityHierarchyListener)\n
    '''
def addActivityListener():
    '''returns None\n\n
    addActivityListener(final ActivityListener activityListener)\n
    '''
def addResourceHierarchyListener():
    '''returns None\n\n
    addResourceHierarchyListener(final ResourceHierarchyListener resourceHierarchyListener)\n
    '''
def addResourceListener():
    '''returns None\n\n
    addResourceListener(final ResourceListener resourceListener)\n
    '''
def addConstraintListener():
    '''returns None\n\n
    addConstraintListener(final ConstraintListener constraintListener)\n
    '''
def addReservationListener():
    '''returns None\n\n
    addReservationListener(final ReservationListener reservationListener)\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener(final EventListener eventListener)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def activitiesInserted():
    '''returns None\n\n
    activitiesInserted(final ActivitiesInsertedEvent activitiesInsertedEvent)\n
    '''
def activitiesRemoved():
    '''returns None\n\n
    activitiesRemoved(final ActivitiesRemovedEvent activitiesRemovedEvent)\n
    '''
def activityMoved():
    '''returns None\n\n
    activityMoved(final ActivityMovedEvent activityMovedEvent)\n
    '''
def activityChanged():
    '''returns None\n\n
    activityChanged(final ActivityEvent activityEvent)\n
    '''
def resourcesInserted():
    '''returns None\n\n
    resourcesInserted(final ResourcesInsertedEvent resourcesInsertedEvent)\n
    '''
def resourcesRemoved():
    '''returns None\n\n
    resourcesRemoved(final ResourcesRemovedEvent resourcesRemovedEvent)\n
    '''
def resourceMoved():
    '''returns None\n\n
    resourceMoved(final ResourceMovedEvent resourceMovedEvent)\n
    '''
def resourceChanged():
    '''returns None\n\n
    resourceChanged(final ResourceEvent resourceEvent)\n
    '''
def constraintChanged():
    '''returns None\n\n
    constraintChanged(final ConstraintEvent constraintEvent)\n
    '''
def reservationChanged():
    '''returns None\n\n
    reservationChanged(final ReservationEvent reservationEvent)\n
    '''
