TIME_CONVERTER_PROPERTY = "String  \"timeConverter\""
HH_NONE = "int  0"
HH_BLUR = "int  1"
HH_BRIGHTEN = "int  2"
HH_GRAYSCALE = "int  3"
HH_SHARPEN = "int  4"
HH_INVERT_COLORS = "int  5"
HH_CUSTOM = "int  6"
def IlvGanttSheet():
    '''public IlvGanttSheet()
    '''
def layerChanged():
    '''public void layerChanged(final ManagerLayerEvent managerLayerEvent)
    '''
def layerInserted():
    '''public void layerInserted(final ManagerLayerInsertedEvent managerLayerInsertedEvent)
    '''
def layerMoved():
    '''public void layerMoved(final ManagerLayerMovedEvent managerLayerMovedEvent)
    '''
def layerRemoved():
    '''public void layerRemoved(final ManagerLayerRemovedEvent managerLayerRemovedEvent)
    '''
def getDefaultTimeIndicatorReshapeFeedback():
    '''public IlvTimeIndicatorReshapeFeedback getDefaultTimeIndicatorReshapeFeedback()
    '''
def getGanttConfiguration():
    '''public final IlvGanttConfiguration getGanttConfiguration()
    '''
def getGanttModel():
    '''public final IlvGanttModel getGanttModel()
    '''
def setComponentOrientation():
    '''public void setComponentOrientation(final ComponentOrientation componentOrientation)
    '''
def getBaseTextDirection():
    '''public final int getBaseTextDirection()
    '''
def setBaseTextDirection():
    '''public void setBaseTextDirection(final int e)
    '''
def getParentBaseTextDirection():
    '''public final int getParentBaseTextDirection()
    '''
def setParentBaseTextDirection():
    '''public void setParentBaseTextDirection(final int f)
    '''
def getResolvedBaseTextDirection():
    '''public int getResolvedBaseTextDirection()
    '''
def getActivityRendererFactory():
    '''public IlvActivityRendererFactory getActivityRendererFactory()
    '''
def setActivityRendererFactory():
    '''public void setActivityRendererFactory(final IlvActivityRendererFactory u)
    '''
def getConstraintGraphicFactory():
    '''public IlvConstraintGraphicFactory getConstraintGraphicFactory()
    '''
def setConstraintGraphicFactory():
    '''public void setConstraintGraphicFactory(final IlvConstraintGraphicFactory v)
    '''
def getConstraintFactory():
    '''public IlvConstraintFactory getConstraintFactory()
    '''
def setConstraintFactory():
    '''public void setConstraintFactory(final IlvConstraintFactory q)
    '''
def getActivityFactory():
    '''public IlvActivityFactory getActivityFactory()
    '''
def setActivityFactory():
    '''public void setActivityFactory(final IlvActivityFactory r)
    '''
def getReservationFactory():
    '''public IlvReservationFactory getReservationFactory()
    '''
def setReservationFactory():
    '''public void setReservationFactory(final IlvReservationFactory s)
    '''
def getResourceFactory():
    '''public IlvResourceFactory getResourceFactory()
    '''
def setResourceFactory():
    '''public void setResourceFactory(final IlvResourceFactory t)
    '''
def getHorizontalGridLayerIndex():
    '''public int getHorizontalGridLayerIndex()
    '''
def getVerticalGridLayerIndex():
    '''public int getVerticalGridLayerIndex()
    '''
def getActivityGraphicLayerIndex():
    '''public int getActivityGraphicLayerIndex()
    '''
def getConstraintGraphicLayerIndex():
    '''public int getConstraintGraphicLayerIndex()
    '''
def getDefaultConstraintGraphicLayerIndex():
    '''public int getDefaultConstraintGraphicLayerIndex()
    '''
def getConstraintGraphicLayerPolicy():
    '''public IlvConstraintGraphicLayerPolicy getConstraintGraphicLayerPolicy()
    '''
def setConstraintGraphicLayerPolicy():
    '''public void setConstraintGraphicLayerPolicy(final IlvConstraintGraphicLayerPolicy ilvConstraintGraphicLayerPolicy)
    '''
def getTimeIndicatorLayerIndex():
    '''public int getTimeIndicatorLayerIndex()
    '''
def swapLayers():
    '''public void swapLayers(final int n, final int n2)
    '''
def isDisplayingConstraints():
    '''public boolean isDisplayingConstraints()
    '''
def setDisplayingConstraints():
    '''public void setDisplayingConstraints(final boolean b)
    '''
def isConstraintLayerVisible():
    '''public boolean isConstraintLayerVisible()
    '''
def isDefaultConstraintLayerVisible():
    '''public boolean isDefaultConstraintLayerVisible()
    '''
def setConstraintLayerVisible():
    '''public void setConstraintLayerVisible(final boolean b)
    '''
def setDefaultConstraintLayerVisible():
    '''public void setDefaultConstraintLayerVisible(final boolean b)
    '''
def isTimeIndicatorLayerVisible():
    '''public boolean isTimeIndicatorLayerVisible()
    '''
def setTimeIndicatorLayerVisible():
    '''public void setTimeIndicatorLayerVisible(final boolean b)
    '''
def setExpandableGanttConfigurationImpl():
    '''public void setExpandableGanttConfigurationImpl(final IlvGanttConfiguration d)
    '''
def ganttModelChanged():
    '''public void ganttModelChanged(final GanttModelChangedEvent ganttModelChangedEvent)
    public void ganttModelChanged(final GanttModelChangedEvent ganttModelChangedEvent)
    '''
def validateRowHeights():
    '''public void validateRowHeights()
    '''
def rowsInserted():
    '''public void rowsInserted(final RowsInsertedEvent rowsInsertedEvent)
    '''
def rowsRemoved():
    '''public void rowsRemoved(final RowsRemovedEvent rowsRemovedEvent)
    '''
def rowMoved():
    '''public void rowMoved(final RowMovedEvent rowMovedEvent)
    '''
def rowExpanded():
    '''public void rowExpanded(final RowExpandedEvent rowExpandedEvent)
    '''
def rowCollapsed():
    '''public void rowCollapsed(final RowCollapsedEvent rowCollapsedEvent)
    '''
def rowHeightChanged():
    '''public void rowHeightChanged(final RowHeightChangedEvent rowHeightChangedEvent)
    '''
def rootRowVisibilityChanged():
    '''public void rootRowVisibilityChanged(final RootRowVisibilityChangedEvent rootRowVisibilityChangedEvent)
    '''
def getGanttRowCount():
    '''public int getGanttRowCount()
    '''
def ganttRowIterator():
    '''public Iterator<IlvGanttRow> ganttRowIterator()
    '''
def getVisibleGanttRowCount():
    '''public int getVisibleGanttRowCount()
    '''
def getVisibleGanttRowAt():
    '''public IlvGanttRow getVisibleGanttRowAt(final int n)
    '''
def getVisibleGanttRowIndex():
    '''public int getVisibleGanttRowIndex(final IlvGanttRow ilvGanttRow)
    '''
def getGanttRowByIdentifier():
    '''public IlvGanttRow getGanttRowByIdentifier(final IlvHierarchyNode ilvHierarchyNode)
    '''
def ganttRowFromPosition():
    '''public IlvGanttRow ganttRowFromPosition(final int n)
    '''
def getTime():
    '''public Date getTime(final int n)
    '''
def getPosition():
    '''public long getPosition(final Date date)
    '''
def getGraphic():
    '''public IlvGraphic getGraphic(final Point2D point2D)
    '''
def getGraphicsInside():
    '''public Collection<IlvGraphic> getGraphicsInside(final Rectangle2D rectangle2D)
    '''
def apply():
    '''public void apply(final IlvGraphic ilvGraphic, final Object o)
    public void apply(final IlvGraphic ilvGraphic, final Object o)
    '''
def getGraphicsIntersects():
    '''public Collection<IlvGraphic> getGraphicsIntersects(final Rectangle2D rectangle2D)
    '''
def activityGraphicsIterator():
    '''public Iterator<IlvActivityGraphic> activityGraphicsIterator()
    public Iterator<IlvActivityGraphic> activityGraphicsIterator(final IlvActivity ilvActivity)
    '''
def getActivityGraphics():
    '''public Collection<IlvActivityGraphic> getActivityGraphics()
    '''
def getActivityGraphic():
    '''public IlvActivityGraphic getActivityGraphic(final IlvActivity ilvActivity)
    '''
def setActivityRenderer():
    '''public void setActivityRenderer(final IlvActivity ilvActivity, final IlvActivityRenderer activityRenderer)
    '''
def getReservationGraphic():
    '''public IlvReservationGraphic getReservationGraphic(final IlvReservation ilvReservation)
    '''
def setReservationRenderer():
    '''public void setReservationRenderer(final IlvReservation ilvReservation, final IlvActivityRenderer activityRenderer)
    '''
def isMultipleRowActivityGraphicsEnabled():
    '''public boolean isMultipleRowActivityGraphicsEnabled()
    '''
def setMultipleRowActivityGraphicsEnabled():
    '''public void setMultipleRowActivityGraphicsEnabled(final boolean b)
    '''
def constraintGraphicsIterator():
    '''public Iterator<IlvConstraintGraphic> constraintGraphicsIterator()
    '''
def getConstraintGraphics():
    '''public Collection<IlvConstraintGraphic> getConstraintGraphics()
    '''
def getConstraintGraphic():
    '''public IlvConstraintGraphic getConstraintGraphic(final IlvConstraint ilvConstraint)
    '''
def replaceConstraintGraphic():
    '''public void replaceConstraintGraphic(final IlvConstraintGraphic ilvConstraintGraphic, final IlvConstraintGraphic ilvConstraintGraphic2, final boolean b)
    '''
def getTimeConverter():
    '''public IlvTimeConverter getTimeConverter()
    '''
def setTimeConverter():
    '''public void setTimeConverter(final IlvTimeConverter ilvTimeConverter)
    '''
def getActivityLayout():
    '''public IlvActivityLayout getActivityLayout()
    '''
def setActivityLayout():
    '''public void setActivityLayout(final IlvActivityLayout activityLayout)
    '''
def getHorizontalGrid():
    '''public IlvGanttGridRenderer getHorizontalGrid()
    '''
def setHorizontalGrid():
    '''public void setHorizontalGrid(final IlvGanttGridRenderer grid)
    '''
def getVerticalGrid():
    '''public IlvGanttGridRenderer getVerticalGrid()
    '''
def setVerticalGrid():
    '''public void setVerticalGrid(final IlvGanttGridRenderer grid)
    '''
def getRowHeight():
    '''public int getRowHeight()
    '''
def setRowHeight():
    '''public void setRowHeight(final int rowHeight)
    '''
def addTimeIndicator():
    '''public void addTimeIndicator(final IlvTimeIndicator ilvTimeIndicator)
    '''
def removeTimeIndicator():
    '''public void removeTimeIndicator(final IlvTimeIndicator ilvTimeIndicator)
    '''
def timeIndicatorsIterator():
    '''public Iterator<IlvTimeIndicator> timeIndicatorsIterator()
    '''
def getTimeIndicators():
    '''public Collection<IlvTimeIndicator> getTimeIndicators()
    '''
def getTimeIndicator():
    '''public IlvTimeIndicator getTimeIndicator(final Date date)
    '''
def replaceTimeIndicator():
    '''public void replaceTimeIndicator(final IlvTimeIndicator ilvTimeIndicator, final IlvTimeIndicator ilvTimeIndicator2, final boolean b)
    '''
def getMinVisibleTime():
    '''public Date getMinVisibleTime()
    '''
def setMinVisibleTime():
    '''public void setMinVisibleTime(final Date date)
    '''
def getMaxVisibleTime():
    '''public Date getMaxVisibleTime()
    '''
def setMaxVisibleTime():
    '''public void setMaxVisibleTime(final Date date)
    '''
def getMinVisibleDuration():
    '''public IlvDuration getMinVisibleDuration()
    '''
def setMinVisibleDuration():
    '''public void setMinVisibleDuration(final IlvDuration ilvDuration)
    '''
def getVisibleTime():
    '''public Date getVisibleTime()
    '''
def setVisibleTime():
    '''public void setVisibleTime(final Date param1)
    '''
def getVisibleDuration():
    '''public IlvDuration getVisibleDuration()
    '''
def setVisibleDuration():
    '''public void setVisibleDuration(final IlvDuration param1)
    '''
def getVisibleInterval():
    '''public IlvTimeInterval getVisibleInterval()
    '''
def setVisibleInterval():
    '''public void setVisibleInterval(final Date date, final IlvDuration ilvDuration)
    '''
def addTimeScrollListener():
    '''public void addTimeScrollListener(final TimeScrollListener timeScrollListener)
    '''
def removeTimeScrollListener():
    '''public void removeTimeScrollListener(final TimeScrollListener timeScrollListener)
    '''
def beginRedrawSession():
    '''public void beginRedrawSession(final boolean b)
    '''
def endRedrawSession():
    '''public void endRedrawSession()
    '''
def paint():
    '''public void paint(final Graphics graphics)
    '''
def print():
    '''public void print(final Graphics graphics, final IlvRect ilvRect, final IlvTransformer ilvTransformer)
    public void print(final Graphics graphics, final Rectangle rectangle, final IlvTransformer ilvTransformer)
    public void print(final Graphics graphics, final Rectangle rectangle, final IlvTransformer ilvTransformer, final boolean b)
    '''
def isConstantZoomFactorOnWidthChange():
    '''public boolean isConstantZoomFactorOnWidthChange()
    '''
def setConstantZoomFactorOnWidthChange():
    '''public void setConstantZoomFactorOnWidthChange(final boolean ag)
    '''
def verifyTransformer():
    '''public void verifyTransformer()
    '''
def translate():
    '''public void translate(final float n, final float n2, final boolean b)
    '''
def ensureVisible():
    '''public void ensureVisible(final IlvGraphic ilvGraphic, final int n)
    '''
def addAccelerator():
    '''public void addAccelerator(final IlvAccelerator ilvAccelerator)
    '''
def removeAccelerator():
    '''public void removeAccelerator(final IlvAccelerator ilvAccelerator)
    '''
def isPopupMenusEnabled():
    '''public boolean isPopupMenusEnabled()
    '''
def setPopupMenusEnabled():
    '''public void setPopupMenusEnabled(final boolean ae)
    '''
def getHoverHighlightingImageOperation():
    '''public IlvHoverHighlightingImageOperation getHoverHighlightingImageOperation()
    '''
def setHoverHighlightingImageOperation():
    '''public void setHoverHighlightingImageOperation(final IlvHoverHighlightingImageOperation hoverHighlightingImageOperation)
    '''
def getHoverHighlightingMode():
    '''public int getHoverHighlightingMode()
    '''
def setHoverHighlightingMode():
    '''public void setHoverHighlightingMode(final int hoverHighlightingMode)
    '''
def isToolTipsEnabled():
    '''public boolean isToolTipsEnabled()
    '''
def setToolTipsEnabled():
    '''public void setToolTipsEnabled(final boolean af)
    '''
def isParentActivityMovable():
    '''public boolean isParentActivityMovable()
    '''
def setParentActivityMovable():
    '''public void setParentActivityMovable(final boolean ac)
    '''
def isParentActivityEditable():
    '''public boolean isParentActivityEditable()
    '''
def setParentActivityEditable():
    '''public void setParentActivityEditable(final boolean ad)
    '''
def isMilestoneConversionAllowed():
    '''public boolean isMilestoneConversionAllowed()
    '''
def setMilestoneConversionAllowed():
    '''public void setMilestoneConversionAllowed(final boolean at)
    '''
def isRefreshParentActivityRenderer():
    '''public boolean isRefreshParentActivityRenderer()
    '''
def setRefreshParentActivityRenderer():
    '''public void setRefreshParentActivityRenderer(final boolean au)
    '''
def isRefreshMilestoneRenderer():
    '''public boolean isRefreshMilestoneRenderer()
    '''
def setRefreshMilestoneRenderer():
    '''public void setRefreshMilestoneRenderer(final boolean ab)
    '''
def createTimeIndicatorContext():
    '''public IlvTimeIndicatorContext createTimeIndicatorContext()
    '''
def createGridContext():
    '''public IlvGanttGridContext createGridContext()
    '''
def run():
    '''public void run()
    '''
def activityChanged():
    '''public void activityChanged(final ActivityEvent activityEvent)
    '''
def FitWidthCalculator():
    '''public FitWidthCalculator(final IlvManagerView.FitAreaCalculator a)
    '''
def getAreaToFit():
    '''public IlvRect getAreaToFit(final IlvManagerView ilvManagerView)
    '''
def activitiesInserted():
    '''public void activitiesInserted(final ActivitiesInsertedEvent activitiesInsertedEvent)
    '''
def activitiesRemoved():
    '''public void activitiesRemoved(final ActivitiesRemovedEvent activitiesRemovedEvent)
    '''
def activityMoved():
    '''public void activityMoved(final ActivityMovedEvent activityMovedEvent)
    '''
def propertyChanged():
    '''public void propertyChanged(final GanttModelPropertyEvent ganttModelPropertyEvent)
    '''
def getGanttSheet():
    '''public final IlvGanttSheet getGanttSheet()
    '''
def removeLayer():
    '''public void removeLayer(final int i, final boolean b)
    '''
def initReDraws():
    '''public void initReDraws()
    public void initReDraws(final boolean b)
    '''
def reDrawViews():
    '''public void reDrawViews()
    '''
def blinkingReDraw():
    '''public void blinkingReDraw()
    '''
def abortReDraws():
    '''public void abortReDraws()
    '''
def invalidateRegion():
    '''public void invalidateRegion(final IlvGraphic ilvGraphic)
    public void invalidateRegion(final IlvRect ilvRect)
    '''
