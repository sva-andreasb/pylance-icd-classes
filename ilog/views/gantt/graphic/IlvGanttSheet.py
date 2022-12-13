TIME_CONVERTER_PROPERTY = "String  timeConverter""
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
pass
def layerChanged():
'''public void layerChanged(final ManagerLayerEvent managerLayerEvent)
'''
pass
def layerInserted():
'''public void layerInserted(final ManagerLayerInsertedEvent managerLayerInsertedEvent)
'''
pass
def layerMoved():
'''public void layerMoved(final ManagerLayerMovedEvent managerLayerMovedEvent)
'''
pass
def layerRemoved():
'''public void layerRemoved(final ManagerLayerRemovedEvent managerLayerRemovedEvent)
'''
pass
def getDefaultTimeIndicatorReshapeFeedback():
'''public IlvTimeIndicatorReshapeFeedback getDefaultTimeIndicatorReshapeFeedback()
'''
pass
def getGanttConfiguration():
'''public final IlvGanttConfiguration getGanttConfiguration()
'''
pass
def getGanttModel():
'''public final IlvGanttModel getGanttModel()
'''
pass
def setComponentOrientation():
'''public void setComponentOrientation(final ComponentOrientation componentOrientation)
'''
pass
def getBaseTextDirection():
'''public final int getBaseTextDirection()
'''
pass
def setBaseTextDirection():
'''public void setBaseTextDirection(final int e)
'''
pass
def getParentBaseTextDirection():
'''public final int getParentBaseTextDirection()
'''
pass
def setParentBaseTextDirection():
'''public void setParentBaseTextDirection(final int f)
'''
pass
def getResolvedBaseTextDirection():
'''public int getResolvedBaseTextDirection()
'''
pass
def getActivityRendererFactory():
'''public IlvActivityRendererFactory getActivityRendererFactory()
'''
pass
def setActivityRendererFactory():
'''public void setActivityRendererFactory(final IlvActivityRendererFactory u)
'''
pass
def getConstraintGraphicFactory():
'''public IlvConstraintGraphicFactory getConstraintGraphicFactory()
'''
pass
def setConstraintGraphicFactory():
'''public void setConstraintGraphicFactory(final IlvConstraintGraphicFactory v)
'''
pass
def getConstraintFactory():
'''public IlvConstraintFactory getConstraintFactory()
'''
pass
def setConstraintFactory():
'''public void setConstraintFactory(final IlvConstraintFactory q)
'''
pass
def getActivityFactory():
'''public IlvActivityFactory getActivityFactory()
'''
pass
def setActivityFactory():
'''public void setActivityFactory(final IlvActivityFactory r)
'''
pass
def getReservationFactory():
'''public IlvReservationFactory getReservationFactory()
'''
pass
def setReservationFactory():
'''public void setReservationFactory(final IlvReservationFactory s)
'''
pass
def getResourceFactory():
'''public IlvResourceFactory getResourceFactory()
'''
pass
def setResourceFactory():
'''public void setResourceFactory(final IlvResourceFactory t)
'''
pass
def getHorizontalGridLayerIndex():
'''public int getHorizontalGridLayerIndex()
'''
pass
def getVerticalGridLayerIndex():
'''public int getVerticalGridLayerIndex()
'''
pass
def getActivityGraphicLayerIndex():
'''public int getActivityGraphicLayerIndex()
'''
pass
def getConstraintGraphicLayerIndex():
'''public int getConstraintGraphicLayerIndex()
'''
pass
def getDefaultConstraintGraphicLayerIndex():
'''public int getDefaultConstraintGraphicLayerIndex()
'''
pass
def getConstraintGraphicLayerPolicy():
'''public IlvConstraintGraphicLayerPolicy getConstraintGraphicLayerPolicy()
'''
pass
def setConstraintGraphicLayerPolicy():
'''public void setConstraintGraphicLayerPolicy(final IlvConstraintGraphicLayerPolicy ilvConstraintGraphicLayerPolicy)
'''
pass
def getTimeIndicatorLayerIndex():
'''public int getTimeIndicatorLayerIndex()
'''
pass
def swapLayers():
'''public void swapLayers(final int n, final int n2)
'''
pass
def isDisplayingConstraints():
'''public boolean isDisplayingConstraints()
'''
pass
def setDisplayingConstraints():
'''public void setDisplayingConstraints(final boolean b)
'''
pass
def isConstraintLayerVisible():
'''public boolean isConstraintLayerVisible()
'''
pass
def isDefaultConstraintLayerVisible():
'''public boolean isDefaultConstraintLayerVisible()
'''
pass
def setConstraintLayerVisible():
'''public void setConstraintLayerVisible(final boolean b)
'''
pass
def setDefaultConstraintLayerVisible():
'''public void setDefaultConstraintLayerVisible(final boolean b)
'''
pass
def isTimeIndicatorLayerVisible():
'''public boolean isTimeIndicatorLayerVisible()
'''
pass
def setTimeIndicatorLayerVisible():
'''public void setTimeIndicatorLayerVisible(final boolean b)
'''
pass
def setExpandableGanttConfigurationImpl():
'''public void setExpandableGanttConfigurationImpl(final IlvGanttConfiguration d)
'''
pass
def ganttModelChanged():
'''public void ganttModelChanged(final GanttModelChangedEvent ganttModelChangedEvent)
public void ganttModelChanged(final GanttModelChangedEvent ganttModelChangedEvent)
'''
pass
def validateRowHeights():
'''public void validateRowHeights()
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
def getGanttRowCount():
'''public int getGanttRowCount()
'''
pass
def ganttRowIterator():
'''public Iterator<IlvGanttRow> ganttRowIterator()
'''
pass
def getVisibleGanttRowCount():
'''public int getVisibleGanttRowCount()
'''
pass
def getVisibleGanttRowAt():
'''public IlvGanttRow getVisibleGanttRowAt(final int n)
'''
pass
def getVisibleGanttRowIndex():
'''public int getVisibleGanttRowIndex(final IlvGanttRow ilvGanttRow)
'''
pass
def getGanttRowByIdentifier():
'''public IlvGanttRow getGanttRowByIdentifier(final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def ganttRowFromPosition():
'''public IlvGanttRow ganttRowFromPosition(final int n)
'''
pass
def getTime():
'''public Date getTime(final int n)
'''
pass
def getPosition():
'''public long getPosition(final Date date)
'''
pass
def getGraphic():
'''public IlvGraphic getGraphic(final Point2D point2D)
'''
pass
def getGraphicsInside():
'''public Collection<IlvGraphic> getGraphicsInside(final Rectangle2D rectangle2D)
'''
pass
def apply():
'''public void apply(final IlvGraphic ilvGraphic, final Object o)
public void apply(final IlvGraphic ilvGraphic, final Object o)
'''
pass
def getGraphicsIntersects():
'''public Collection<IlvGraphic> getGraphicsIntersects(final Rectangle2D rectangle2D)
'''
pass
def activityGraphicsIterator():
'''public Iterator<IlvActivityGraphic> activityGraphicsIterator()
public Iterator<IlvActivityGraphic> activityGraphicsIterator(final IlvActivity ilvActivity)
'''
pass
def getActivityGraphics():
'''public Collection<IlvActivityGraphic> getActivityGraphics()
'''
pass
def getActivityGraphic():
'''public IlvActivityGraphic getActivityGraphic(final IlvActivity ilvActivity)
'''
pass
def setActivityRenderer():
'''public void setActivityRenderer(final IlvActivity ilvActivity, final IlvActivityRenderer activityRenderer)
'''
pass
def getReservationGraphic():
'''public IlvReservationGraphic getReservationGraphic(final IlvReservation ilvReservation)
'''
pass
def setReservationRenderer():
'''public void setReservationRenderer(final IlvReservation ilvReservation, final IlvActivityRenderer activityRenderer)
'''
pass
def isMultipleRowActivityGraphicsEnabled():
'''public boolean isMultipleRowActivityGraphicsEnabled()
'''
pass
def setMultipleRowActivityGraphicsEnabled():
'''public void setMultipleRowActivityGraphicsEnabled(final boolean b)
'''
pass
def constraintGraphicsIterator():
'''public Iterator<IlvConstraintGraphic> constraintGraphicsIterator()
'''
pass
def getConstraintGraphics():
'''public Collection<IlvConstraintGraphic> getConstraintGraphics()
'''
pass
def getConstraintGraphic():
'''public IlvConstraintGraphic getConstraintGraphic(final IlvConstraint ilvConstraint)
'''
pass
def replaceConstraintGraphic():
'''public void replaceConstraintGraphic(final IlvConstraintGraphic ilvConstraintGraphic, final IlvConstraintGraphic ilvConstraintGraphic2, final boolean b)
'''
pass
def getTimeConverter():
'''public IlvTimeConverter getTimeConverter()
'''
pass
def setTimeConverter():
'''public void setTimeConverter(final IlvTimeConverter ilvTimeConverter)
'''
pass
def getActivityLayout():
'''public IlvActivityLayout getActivityLayout()
'''
pass
def setActivityLayout():
'''public void setActivityLayout(final IlvActivityLayout activityLayout)
'''
pass
def getHorizontalGrid():
'''public IlvGanttGridRenderer getHorizontalGrid()
'''
pass
def setHorizontalGrid():
'''public void setHorizontalGrid(final IlvGanttGridRenderer grid)
'''
pass
def getVerticalGrid():
'''public IlvGanttGridRenderer getVerticalGrid()
'''
pass
def setVerticalGrid():
'''public void setVerticalGrid(final IlvGanttGridRenderer grid)
'''
pass
def getRowHeight():
'''public int getRowHeight()
'''
pass
def setRowHeight():
'''public void setRowHeight(final int rowHeight)
'''
pass
def addTimeIndicator():
'''public void addTimeIndicator(final IlvTimeIndicator ilvTimeIndicator)
'''
pass
def removeTimeIndicator():
'''public void removeTimeIndicator(final IlvTimeIndicator ilvTimeIndicator)
'''
pass
def timeIndicatorsIterator():
'''public Iterator<IlvTimeIndicator> timeIndicatorsIterator()
'''
pass
def getTimeIndicators():
'''public Collection<IlvTimeIndicator> getTimeIndicators()
'''
pass
def getTimeIndicator():
'''public IlvTimeIndicator getTimeIndicator(final Date date)
'''
pass
def replaceTimeIndicator():
'''public void replaceTimeIndicator(final IlvTimeIndicator ilvTimeIndicator, final IlvTimeIndicator ilvTimeIndicator2, final boolean b)
'''
pass
def getMinVisibleTime():
'''public Date getMinVisibleTime()
'''
pass
def setMinVisibleTime():
'''public void setMinVisibleTime(final Date date)
'''
pass
def getMaxVisibleTime():
'''public Date getMaxVisibleTime()
'''
pass
def setMaxVisibleTime():
'''public void setMaxVisibleTime(final Date date)
'''
pass
def getMinVisibleDuration():
'''public IlvDuration getMinVisibleDuration()
'''
pass
def setMinVisibleDuration():
'''public void setMinVisibleDuration(final IlvDuration ilvDuration)
'''
pass
def getVisibleTime():
'''public Date getVisibleTime()
'''
pass
def setVisibleTime():
'''public void setVisibleTime(final Date param1)
'''
pass
def getVisibleDuration():
'''public IlvDuration getVisibleDuration()
'''
pass
def setVisibleDuration():
'''public void setVisibleDuration(final IlvDuration param1)
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
def addTimeScrollListener():
'''public void addTimeScrollListener(final TimeScrollListener timeScrollListener)
'''
pass
def removeTimeScrollListener():
'''public void removeTimeScrollListener(final TimeScrollListener timeScrollListener)
'''
pass
def beginRedrawSession():
'''public void beginRedrawSession(final boolean b)
'''
pass
def endRedrawSession():
'''public void endRedrawSession()
'''
pass
def paint():
'''public void paint(final Graphics graphics)
'''
pass
def print():
'''public void print(final Graphics graphics, final IlvRect ilvRect, final IlvTransformer ilvTransformer)
public void print(final Graphics graphics, final Rectangle rectangle, final IlvTransformer ilvTransformer)
public void print(final Graphics graphics, final Rectangle rectangle, final IlvTransformer ilvTransformer, final boolean b)
'''
pass
def isConstantZoomFactorOnWidthChange():
'''public boolean isConstantZoomFactorOnWidthChange()
'''
pass
def setConstantZoomFactorOnWidthChange():
'''public void setConstantZoomFactorOnWidthChange(final boolean ag)
'''
pass
def verifyTransformer():
'''public void verifyTransformer()
'''
pass
def translate():
'''public void translate(final float n, final float n2, final boolean b)
'''
pass
def ensureVisible():
'''public void ensureVisible(final IlvGraphic ilvGraphic, final int n)
'''
pass
def addAccelerator():
'''public void addAccelerator(final IlvAccelerator ilvAccelerator)
'''
pass
def removeAccelerator():
'''public void removeAccelerator(final IlvAccelerator ilvAccelerator)
'''
pass
def isPopupMenusEnabled():
'''public boolean isPopupMenusEnabled()
'''
pass
def setPopupMenusEnabled():
'''public void setPopupMenusEnabled(final boolean ae)
'''
pass
def getHoverHighlightingImageOperation():
'''public IlvHoverHighlightingImageOperation getHoverHighlightingImageOperation()
'''
pass
def setHoverHighlightingImageOperation():
'''public void setHoverHighlightingImageOperation(final IlvHoverHighlightingImageOperation hoverHighlightingImageOperation)
'''
pass
def getHoverHighlightingMode():
'''public int getHoverHighlightingMode()
'''
pass
def setHoverHighlightingMode():
'''public void setHoverHighlightingMode(final int hoverHighlightingMode)
'''
pass
def isToolTipsEnabled():
'''public boolean isToolTipsEnabled()
'''
pass
def setToolTipsEnabled():
'''public void setToolTipsEnabled(final boolean af)
'''
pass
def isParentActivityMovable():
'''public boolean isParentActivityMovable()
'''
pass
def setParentActivityMovable():
'''public void setParentActivityMovable(final boolean ac)
'''
pass
def isParentActivityEditable():
'''public boolean isParentActivityEditable()
'''
pass
def setParentActivityEditable():
'''public void setParentActivityEditable(final boolean ad)
'''
pass
def isMilestoneConversionAllowed():
'''public boolean isMilestoneConversionAllowed()
'''
pass
def setMilestoneConversionAllowed():
'''public void setMilestoneConversionAllowed(final boolean at)
'''
pass
def isRefreshParentActivityRenderer():
'''public boolean isRefreshParentActivityRenderer()
'''
pass
def setRefreshParentActivityRenderer():
'''public void setRefreshParentActivityRenderer(final boolean au)
'''
pass
def isRefreshMilestoneRenderer():
'''public boolean isRefreshMilestoneRenderer()
'''
pass
def setRefreshMilestoneRenderer():
'''public void setRefreshMilestoneRenderer(final boolean ab)
'''
pass
def createTimeIndicatorContext():
'''public IlvTimeIndicatorContext createTimeIndicatorContext()
'''
pass
def createGridContext():
'''public IlvGanttGridContext createGridContext()
'''
pass
def run():
'''public void run()
'''
pass
def activityChanged():
'''public void activityChanged(final ActivityEvent activityEvent)
'''
pass
def FitWidthCalculator():
'''public FitWidthCalculator(final IlvManagerView.FitAreaCalculator a)
'''
pass
def getAreaToFit():
'''public IlvRect getAreaToFit(final IlvManagerView ilvManagerView)
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
def propertyChanged():
'''public void propertyChanged(final GanttModelPropertyEvent ganttModelPropertyEvent)
'''
pass
def getGanttSheet():
'''public final IlvGanttSheet getGanttSheet()
'''
pass
def removeLayer():
'''public void removeLayer(final int i, final boolean b)
'''
pass
def initReDraws():
'''public void initReDraws()
public void initReDraws(final boolean b)
'''
pass
def reDrawViews():
'''public void reDrawViews()
'''
pass
def blinkingReDraw():
'''public void blinkingReDraw()
'''
pass
def abortReDraws():
'''public void abortReDraws()
'''
pass
def invalidateRegion():
'''public void invalidateRegion(final IlvGraphic ilvGraphic)
public void invalidateRegion(final IlvRect ilvRect)
'''
pass
