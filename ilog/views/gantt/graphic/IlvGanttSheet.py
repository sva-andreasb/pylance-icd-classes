TIME_CONVERTER_PROPERTY = "String  \"timeConverter\""
HH_NONE = "int  0"
HH_BLUR = "int  1"
HH_BRIGHTEN = "int  2"
HH_GRAYSCALE = "int  3"
HH_SHARPEN = "int  4"
HH_INVERT_COLORS = "int  5"
HH_CUSTOM = "int  6"
def ():
    '''returns FitWidthCalculator\n\n
    ()\n
    (final IlvManagerView.FitAreaCalculator a)\n
    '''
def layerChanged():
    '''returns None\n\n
    layerChanged(final ManagerLayerEvent managerLayerEvent)\n
    '''
def layerInserted():
    '''returns None\n\n
    layerInserted(final ManagerLayerInsertedEvent managerLayerInsertedEvent)\n
    '''
def layerMoved():
    '''returns None\n\n
    layerMoved(final ManagerLayerMovedEvent managerLayerMovedEvent)\n
    '''
def layerRemoved():
    '''returns None\n\n
    layerRemoved(final ManagerLayerRemovedEvent managerLayerRemovedEvent)\n
    '''
def getDefaultTimeIndicatorReshapeFeedback():
    '''returns IlvTimeIndicatorReshapeFeedback\n\n
    getDefaultTimeIndicatorReshapeFeedback()\n
    '''
def setComponentOrientation():
    '''returns None\n\n
    setComponentOrientation(final ComponentOrientation componentOrientation)\n
    '''
def setBaseTextDirection():
    '''returns None\n\n
    setBaseTextDirection(final int e)\n
    '''
def setParentBaseTextDirection():
    '''returns None\n\n
    setParentBaseTextDirection(final int f)\n
    '''
def getResolvedBaseTextDirection():
    '''returns int\n\n
    getResolvedBaseTextDirection()\n
    '''
def getActivityRendererFactory():
    '''returns IlvActivityRendererFactory\n\n
    getActivityRendererFactory()\n
    '''
def setActivityRendererFactory():
    '''returns None\n\n
    setActivityRendererFactory(final IlvActivityRendererFactory u)\n
    '''
def getConstraintGraphicFactory():
    '''returns IlvConstraintGraphicFactory\n\n
    getConstraintGraphicFactory()\n
    '''
def setConstraintGraphicFactory():
    '''returns None\n\n
    setConstraintGraphicFactory(final IlvConstraintGraphicFactory v)\n
    '''
def getConstraintFactory():
    '''returns IlvConstraintFactory\n\n
    getConstraintFactory()\n
    '''
def setConstraintFactory():
    '''returns None\n\n
    setConstraintFactory(final IlvConstraintFactory q)\n
    '''
def getActivityFactory():
    '''returns IlvActivityFactory\n\n
    getActivityFactory()\n
    '''
def setActivityFactory():
    '''returns None\n\n
    setActivityFactory(final IlvActivityFactory r)\n
    '''
def getReservationFactory():
    '''returns IlvReservationFactory\n\n
    getReservationFactory()\n
    '''
def setReservationFactory():
    '''returns None\n\n
    setReservationFactory(final IlvReservationFactory s)\n
    '''
def getResourceFactory():
    '''returns IlvResourceFactory\n\n
    getResourceFactory()\n
    '''
def setResourceFactory():
    '''returns None\n\n
    setResourceFactory(final IlvResourceFactory t)\n
    '''
def getHorizontalGridLayerIndex():
    '''returns int\n\n
    getHorizontalGridLayerIndex()\n
    '''
def getVerticalGridLayerIndex():
    '''returns int\n\n
    getVerticalGridLayerIndex()\n
    '''
def getActivityGraphicLayerIndex():
    '''returns int\n\n
    getActivityGraphicLayerIndex()\n
    '''
def getConstraintGraphicLayerIndex():
    '''returns int\n\n
    getConstraintGraphicLayerIndex()\n
    '''
def getDefaultConstraintGraphicLayerIndex():
    '''returns int\n\n
    getDefaultConstraintGraphicLayerIndex()\n
    '''
def getConstraintGraphicLayerPolicy():
    '''returns IlvConstraintGraphicLayerPolicy\n\n
    getConstraintGraphicLayerPolicy()\n
    '''
def setConstraintGraphicLayerPolicy():
    '''returns None\n\n
    setConstraintGraphicLayerPolicy(final IlvConstraintGraphicLayerPolicy ilvConstraintGraphicLayerPolicy)\n
    '''
def getTimeIndicatorLayerIndex():
    '''returns int\n\n
    getTimeIndicatorLayerIndex()\n
    '''
def swapLayers():
    '''returns None\n\n
    swapLayers(final int n, final int n2)\n
    '''
def isDisplayingConstraints():
    '''returns boolean\n\n
    isDisplayingConstraints()\n
    '''
def setDisplayingConstraints():
    '''returns None\n\n
    setDisplayingConstraints(final boolean b)\n
    '''
def isConstraintLayerVisible():
    '''returns boolean\n\n
    isConstraintLayerVisible()\n
    '''
def isDefaultConstraintLayerVisible():
    '''returns boolean\n\n
    isDefaultConstraintLayerVisible()\n
    '''
def setConstraintLayerVisible():
    '''returns None\n\n
    setConstraintLayerVisible(final boolean b)\n
    '''
def setDefaultConstraintLayerVisible():
    '''returns None\n\n
    setDefaultConstraintLayerVisible(final boolean b)\n
    '''
def isTimeIndicatorLayerVisible():
    '''returns boolean\n\n
    isTimeIndicatorLayerVisible()\n
    '''
def setTimeIndicatorLayerVisible():
    '''returns None\n\n
    setTimeIndicatorLayerVisible(final boolean b)\n
    '''
def setExpandableGanttConfigurationImpl():
    '''returns None\n\n
    setExpandableGanttConfigurationImpl(final IlvGanttConfiguration d)\n
    '''
def ganttModelChanged():
    '''returns None\n\n
    ganttModelChanged(final GanttModelChangedEvent ganttModelChangedEvent)\n
    ganttModelChanged(final GanttModelChangedEvent ganttModelChangedEvent)\n
    '''
def validateRowHeights():
    '''returns None\n\n
    validateRowHeights()\n
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
def getGanttRowCount():
    '''returns int\n\n
    getGanttRowCount()\n
    '''
def ganttRowIterator():
    '''returns Iterator<IlvGanttRow>\n\n
    ganttRowIterator()\n
    '''
def getVisibleGanttRowCount():
    '''returns int\n\n
    getVisibleGanttRowCount()\n
    '''
def getVisibleGanttRowAt():
    '''returns IlvGanttRow\n\n
    getVisibleGanttRowAt(final int n)\n
    '''
def getVisibleGanttRowIndex():
    '''returns int\n\n
    getVisibleGanttRowIndex(final IlvGanttRow ilvGanttRow)\n
    '''
def getGanttRowByIdentifier():
    '''returns IlvGanttRow\n\n
    getGanttRowByIdentifier(final IlvHierarchyNode ilvHierarchyNode)\n
    '''
def ganttRowFromPosition():
    '''returns IlvGanttRow\n\n
    ganttRowFromPosition(final int n)\n
    '''
def getTime():
    '''returns Date\n\n
    getTime(final int n)\n
    '''
def getPosition():
    '''returns long\n\n
    getPosition(final Date date)\n
    '''
def getGraphic():
    '''returns IlvGraphic\n\n
    getGraphic(final Point2D point2D)\n
    '''
def getGraphicsInside():
    '''returns Collection<IlvGraphic>\n\n
    getGraphicsInside(final Rectangle2D rectangle2D)\n
    '''
def apply():
    '''returns None\n\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    '''
def getGraphicsIntersects():
    '''returns Collection<IlvGraphic>\n\n
    getGraphicsIntersects(final Rectangle2D rectangle2D)\n
    '''
def activityGraphicsIterator():
    '''returns Iterator<IlvActivityGraphic>\n\n
    activityGraphicsIterator()\n
    activityGraphicsIterator(final IlvActivity ilvActivity)\n
    '''
def getActivityGraphics():
    '''returns Collection<IlvActivityGraphic>\n\n
    getActivityGraphics()\n
    '''
def getActivityGraphic():
    '''returns IlvActivityGraphic\n\n
    getActivityGraphic(final IlvActivity ilvActivity)\n
    '''
def setActivityRenderer():
    '''returns None\n\n
    setActivityRenderer(final IlvActivity ilvActivity, final IlvActivityRenderer activityRenderer)\n
    '''
def getReservationGraphic():
    '''returns IlvReservationGraphic\n\n
    getReservationGraphic(final IlvReservation ilvReservation)\n
    '''
def setReservationRenderer():
    '''returns None\n\n
    setReservationRenderer(final IlvReservation ilvReservation, final IlvActivityRenderer activityRenderer)\n
    '''
def isMultipleRowActivityGraphicsEnabled():
    '''returns boolean\n\n
    isMultipleRowActivityGraphicsEnabled()\n
    '''
def setMultipleRowActivityGraphicsEnabled():
    '''returns None\n\n
    setMultipleRowActivityGraphicsEnabled(final boolean b)\n
    '''
def constraintGraphicsIterator():
    '''returns Iterator<IlvConstraintGraphic>\n\n
    constraintGraphicsIterator()\n
    '''
def getConstraintGraphics():
    '''returns Collection<IlvConstraintGraphic>\n\n
    getConstraintGraphics()\n
    '''
def getConstraintGraphic():
    '''returns IlvConstraintGraphic\n\n
    getConstraintGraphic(final IlvConstraint ilvConstraint)\n
    '''
def replaceConstraintGraphic():
    '''returns None\n\n
    replaceConstraintGraphic(final IlvConstraintGraphic ilvConstraintGraphic, final IlvConstraintGraphic ilvConstraintGraphic2, final boolean b)\n
    '''
def getTimeConverter():
    '''returns IlvTimeConverter\n\n
    getTimeConverter()\n
    '''
def setTimeConverter():
    '''returns None\n\n
    setTimeConverter(final IlvTimeConverter ilvTimeConverter)\n
    '''
def getActivityLayout():
    '''returns IlvActivityLayout\n\n
    getActivityLayout()\n
    '''
def setActivityLayout():
    '''returns None\n\n
    setActivityLayout(final IlvActivityLayout activityLayout)\n
    '''
def getHorizontalGrid():
    '''returns IlvGanttGridRenderer\n\n
    getHorizontalGrid()\n
    '''
def setHorizontalGrid():
    '''returns None\n\n
    setHorizontalGrid(final IlvGanttGridRenderer grid)\n
    '''
def getVerticalGrid():
    '''returns IlvGanttGridRenderer\n\n
    getVerticalGrid()\n
    '''
def setVerticalGrid():
    '''returns None\n\n
    setVerticalGrid(final IlvGanttGridRenderer grid)\n
    '''
def getRowHeight():
    '''returns int\n\n
    getRowHeight()\n
    '''
def setRowHeight():
    '''returns None\n\n
    setRowHeight(final int rowHeight)\n
    '''
def addTimeIndicator():
    '''returns None\n\n
    addTimeIndicator(final IlvTimeIndicator ilvTimeIndicator)\n
    '''
def removeTimeIndicator():
    '''returns None\n\n
    removeTimeIndicator(final IlvTimeIndicator ilvTimeIndicator)\n
    '''
def timeIndicatorsIterator():
    '''returns Iterator<IlvTimeIndicator>\n\n
    timeIndicatorsIterator()\n
    '''
def getTimeIndicators():
    '''returns Collection<IlvTimeIndicator>\n\n
    getTimeIndicators()\n
    '''
def getTimeIndicator():
    '''returns IlvTimeIndicator\n\n
    getTimeIndicator(final Date date)\n
    '''
def replaceTimeIndicator():
    '''returns None\n\n
    replaceTimeIndicator(final IlvTimeIndicator ilvTimeIndicator, final IlvTimeIndicator ilvTimeIndicator2, final boolean b)\n
    '''
def getMinVisibleTime():
    '''returns Date\n\n
    getMinVisibleTime()\n
    '''
def setMinVisibleTime():
    '''returns None\n\n
    setMinVisibleTime(final Date date)\n
    '''
def getMaxVisibleTime():
    '''returns Date\n\n
    getMaxVisibleTime()\n
    '''
def setMaxVisibleTime():
    '''returns None\n\n
    setMaxVisibleTime(final Date date)\n
    '''
def getMinVisibleDuration():
    '''returns IlvDuration\n\n
    getMinVisibleDuration()\n
    '''
def setMinVisibleDuration():
    '''returns None\n\n
    setMinVisibleDuration(final IlvDuration ilvDuration)\n
    '''
def getVisibleTime():
    '''returns Date\n\n
    getVisibleTime()\n
    '''
def setVisibleTime():
    '''returns None\n\n
    setVisibleTime(final Date param1)\n
    '''
def getVisibleDuration():
    '''returns IlvDuration\n\n
    getVisibleDuration()\n
    '''
def setVisibleDuration():
    '''returns None\n\n
    setVisibleDuration(final IlvDuration param1)\n
    '''
def getVisibleInterval():
    '''returns IlvTimeInterval\n\n
    getVisibleInterval()\n
    '''
def setVisibleInterval():
    '''returns None\n\n
    setVisibleInterval(final Date date, final IlvDuration ilvDuration)\n
    '''
def addTimeScrollListener():
    '''returns None\n\n
    addTimeScrollListener(final TimeScrollListener timeScrollListener)\n
    '''
def removeTimeScrollListener():
    '''returns None\n\n
    removeTimeScrollListener(final TimeScrollListener timeScrollListener)\n
    '''
def beginRedrawSession():
    '''returns None\n\n
    beginRedrawSession(final boolean b)\n
    '''
def endRedrawSession():
    '''returns None\n\n
    endRedrawSession()\n
    '''
def paint():
    '''returns None\n\n
    paint(final Graphics graphics)\n
    '''
def print():
    '''returns None\n\n
    print(final Graphics graphics, final IlvRect ilvRect, final IlvTransformer ilvTransformer)\n
    print(final Graphics graphics, final Rectangle rectangle, final IlvTransformer ilvTransformer)\n
    print(final Graphics graphics, final Rectangle rectangle, final IlvTransformer ilvTransformer, final boolean b)\n
    '''
def isConstantZoomFactorOnWidthChange():
    '''returns boolean\n\n
    isConstantZoomFactorOnWidthChange()\n
    '''
def setConstantZoomFactorOnWidthChange():
    '''returns None\n\n
    setConstantZoomFactorOnWidthChange(final boolean ag)\n
    '''
def verifyTransformer():
    '''returns None\n\n
    verifyTransformer()\n
    '''
def translate():
    '''returns None\n\n
    translate(final float n, final float n2, final boolean b)\n
    '''
def ensureVisible():
    '''returns None\n\n
    ensureVisible(final IlvGraphic ilvGraphic, final int n)\n
    '''
def addAccelerator():
    '''returns None\n\n
    addAccelerator(final IlvAccelerator ilvAccelerator)\n
    '''
def removeAccelerator():
    '''returns None\n\n
    removeAccelerator(final IlvAccelerator ilvAccelerator)\n
    '''
def isPopupMenusEnabled():
    '''returns boolean\n\n
    isPopupMenusEnabled()\n
    '''
def setPopupMenusEnabled():
    '''returns None\n\n
    setPopupMenusEnabled(final boolean ae)\n
    '''
def getHoverHighlightingImageOperation():
    '''returns IlvHoverHighlightingImageOperation\n\n
    getHoverHighlightingImageOperation()\n
    '''
def setHoverHighlightingImageOperation():
    '''returns None\n\n
    setHoverHighlightingImageOperation(final IlvHoverHighlightingImageOperation hoverHighlightingImageOperation)\n
    '''
def getHoverHighlightingMode():
    '''returns int\n\n
    getHoverHighlightingMode()\n
    '''
def setHoverHighlightingMode():
    '''returns None\n\n
    setHoverHighlightingMode(final int hoverHighlightingMode)\n
    '''
def isToolTipsEnabled():
    '''returns boolean\n\n
    isToolTipsEnabled()\n
    '''
def setToolTipsEnabled():
    '''returns None\n\n
    setToolTipsEnabled(final boolean af)\n
    '''
def isParentActivityMovable():
    '''returns boolean\n\n
    isParentActivityMovable()\n
    '''
def setParentActivityMovable():
    '''returns None\n\n
    setParentActivityMovable(final boolean ac)\n
    '''
def isParentActivityEditable():
    '''returns boolean\n\n
    isParentActivityEditable()\n
    '''
def setParentActivityEditable():
    '''returns None\n\n
    setParentActivityEditable(final boolean ad)\n
    '''
def isMilestoneConversionAllowed():
    '''returns boolean\n\n
    isMilestoneConversionAllowed()\n
    '''
def setMilestoneConversionAllowed():
    '''returns None\n\n
    setMilestoneConversionAllowed(final boolean at)\n
    '''
def isRefreshParentActivityRenderer():
    '''returns boolean\n\n
    isRefreshParentActivityRenderer()\n
    '''
def setRefreshParentActivityRenderer():
    '''returns None\n\n
    setRefreshParentActivityRenderer(final boolean au)\n
    '''
def isRefreshMilestoneRenderer():
    '''returns boolean\n\n
    isRefreshMilestoneRenderer()\n
    '''
def setRefreshMilestoneRenderer():
    '''returns None\n\n
    setRefreshMilestoneRenderer(final boolean ab)\n
    '''
def createTimeIndicatorContext():
    '''returns IlvTimeIndicatorContext\n\n
    createTimeIndicatorContext()\n
    '''
def createGridContext():
    '''returns IlvGanttGridContext\n\n
    createGridContext()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def activityChanged():
    '''returns None\n\n
    activityChanged(final ActivityEvent activityEvent)\n
    '''
def getAreaToFit():
    '''returns IlvRect\n\n
    getAreaToFit(final IlvManagerView ilvManagerView)\n
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
def propertyChanged():
    '''returns None\n\n
    propertyChanged(final GanttModelPropertyEvent ganttModelPropertyEvent)\n
    '''
def removeLayer():
    '''returns None\n\n
    removeLayer(final int i, final boolean b)\n
    '''
def initReDraws():
    '''returns None\n\n
    initReDraws()\n
    initReDraws(final boolean b)\n
    '''
def reDrawViews():
    '''returns None\n\n
    reDrawViews()\n
    '''
def blinkingReDraw():
    '''returns None\n\n
    blinkingReDraw()\n
    '''
def abortReDraws():
    '''returns None\n\n
    abortReDraws()\n
    '''
def invalidateRegion():
    '''returns None\n\n
    invalidateRegion(final IlvGraphic ilvGraphic)\n
    invalidateRegion(final IlvRect ilvRect)\n
    '''
