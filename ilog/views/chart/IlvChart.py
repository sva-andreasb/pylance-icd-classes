CARTESIAN = "int  1"
POLAR = "int  2"
PIE = "int  3"
RADAR = "int  4"
TREEMAP = "int  5"
DRAW_BELOW = "int  -1"
DRAW_ABOVE = "int  1"
STYLE_DEFAULT_MASK = "int  384"
FIXED_LEFT_MARGIN = "int  1"
FIXED_RIGHT_MARGIN = "int  2"
FIXED_TOP_MARGIN = "int  4"
FIXED_BOTTOM_MARGIN = "int  8"
def getBeanDescriptor():
    '''returns BeanDescriptor\n\n
    getBeanDescriptor()\n
    '''
def getAdditionalBeanInfo():
    '''returns BeanInfo[]\n\n
    getAdditionalBeanInfo()\n
    '''
def getPropertyDescriptors():
    '''returns PropertyDescriptor[]\n\n
    getPropertyDescriptors()\n
    '''
def getIcon():
    '''returns Image\n\n
    getIcon(final int n)\n
    '''
def setUsingEventThread():
    '''returns None\n\n
    setUsingEventThread(final boolean b)\n
    '''
def isUsingEventThread():
    '''returns boolean\n\n
    isUsingEventThread()\n
    '''
def getLock():
    '''returns Object\n\n
    getLock()\n
    '''
def ():
    '''returns IlvChartAreaPaintAction\n\n
    ()\n
    (final int n)\n
    (final int n, final boolean b)\n
    (final int width, final int height, final JComponent component)\n
    (final int width, final int height, final JComponent d)\n
    (final Container container)\n
    (final Container container)\n
    '''
def componentAdded():
    '''returns None\n\n
    componentAdded(final ContainerEvent containerEvent)\n
    componentAdded(final ContainerEvent containerEvent)\n
    '''
def componentRemoved():
    '''returns None\n\n
    componentRemoved(final ContainerEvent containerEvent)\n
    componentRemoved(final ContainerEvent containerEvent)\n
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
def updateUI():
    '''returns None\n\n
    updateUI()\n
    '''
def setBounds():
    '''returns None\n\n
    setBounds(final int x, final int y, final int width, final int height)\n
    setBounds(final int x, final int y, final int width, final int height)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    '''
def setAntiAliasing():
    '''returns None\n\n
    setAntiAliasing(final boolean b)\n
    '''
def setAntiAliasingText():
    '''returns None\n\n
    setAntiAliasingText(final boolean b)\n
    '''
def setBaseTextDirection():
    '''returns None\n\n
    setBaseTextDirection(final int au)\n
    '''
def getResolvedBaseTextDirection():
    '''returns int\n\n
    getResolvedBaseTextDirection()\n
    '''
def setCursor():
    '''returns None\n\n
    setCursor(final Cursor cursor)\n
    '''
def isCursorSet():
    '''returns boolean\n\n
    isCursorSet()\n
    '''
def setOptimizedRepaint():
    '''returns None\n\n
    setOptimizedRepaint(final boolean b)\n
    '''
def isShiftScroll():
    '''returns boolean\n\n
    isShiftScroll()\n
    '''
def setShiftScroll():
    '''returns None\n\n
    setShiftScroll(final boolean b)\n
    '''
def getScrollRatio():
    '''returns double\n\n
    getScrollRatio()\n
    '''
def setScrollRatio():
    '''returns None\n\n
    setScrollRatio(final double at)\n
    '''
def getType():
    '''returns int\n\n
    getType()\n
    '''
def setType():
    '''returns None\n\n
    setType(final int n)\n
    '''
def setPolarParameters():
    '''returns None\n\n
    setPolarParameters(final double n, final double n2, final boolean symmetric)\n
    '''
def setStartingAngle():
    '''returns None\n\n
    setStartingAngle(final double n)\n
    '''
def setAngleRange():
    '''returns None\n\n
    setAngleRange(final double n)\n
    '''
def isProjectorReversed():
    '''returns boolean\n\n
    isProjectorReversed()\n
    '''
def setProjectorReversed():
    '''returns None\n\n
    setProjectorReversed(final boolean reversed)\n
    '''
def getDefaultColors():
    '''returns Color[]\n\n
    getDefaultColors()\n
    '''
def setDefaultColors():
    '''returns None\n\n
    setDefaultColors(final Color[] bj)\n
    '''
def isScalingFont():
    '''returns boolean\n\n
    isScalingFont()\n
    '''
def setScalingFont():
    '''returns None\n\n
    setScalingFont(final boolean enabled)\n
    '''
def setAutoScaleTitleRotation():
    '''returns None\n\n
    setAutoScaleTitleRotation(final boolean b)\n
    '''
def getXAxis():
    '''returns IlvAxis\n\n
    getXAxis()\n
    '''
def setXAxisReversed():
    '''returns None\n\n
    setXAxisReversed(final boolean reversed)\n
    '''
def setXScale():
    '''returns None\n\n
    setXScale(final IlvScale ilvScale)\n
    '''
def isXScaleVisible():
    '''returns boolean\n\n
    isXScaleVisible()\n
    '''
def setXScaleVisible():
    '''returns None\n\n
    setXScaleVisible(final boolean visible)\n
    '''
def getXScaleTitle():
    '''returns String\n\n
    getXScaleTitle()\n
    '''
def setXScaleTitle():
    '''returns None\n\n
    setXScaleTitle(final String s)\n
    '''
def getXScaleTitleRotation():
    '''returns double\n\n
    getXScaleTitleRotation()\n
    '''
def setXScaleTitleRotation():
    '''returns None\n\n
    setXScaleTitleRotation(final double rotation)\n
    '''
def getYAxisCount():
    '''returns int\n\n
    getYAxisCount()\n
    '''
def getYAxis():
    '''returns IlvAxis\n\n
    getYAxis(final int n)\n
    '''
def setYAxisReversed():
    '''returns None\n\n
    setYAxisReversed(final boolean reversed)\n
    '''
def addYAxis():
    '''returns IlvAxis\n\n
    addYAxis(final boolean b, final boolean b2)\n
    '''
def setYScale():
    '''returns None\n\n
    setYScale(final int n, final IlvScale ilvScale)\n
    '''
def isYScaleVisible():
    '''returns boolean\n\n
    isYScaleVisible()\n
    '''
def setYScaleVisible():
    '''returns None\n\n
    setYScaleVisible(final boolean visible)\n
    '''
def getYScaleTitle():
    '''returns String\n\n
    getYScaleTitle()\n
    '''
def setYScaleTitle():
    '''returns None\n\n
    setYScaleTitle(final String s)\n
    '''
def getYScaleTitleRotation():
    '''returns double\n\n
    getYScaleTitleRotation()\n
    '''
def setYScaleTitleRotation():
    '''returns None\n\n
    setYScaleTitleRotation(final double rotation)\n
    '''
def setXGrid():
    '''returns None\n\n
    setXGrid(final IlvGrid ilvGrid)\n
    '''
def isXGridVisible():
    '''returns boolean\n\n
    isXGridVisible()\n
    '''
def setXGridVisible():
    '''returns None\n\n
    setXGridVisible(final boolean majorLineVisible)\n
    '''
def setYGrid():
    '''returns None\n\n
    setYGrid(final int n, final IlvGrid ilvGrid)\n
    '''
def isYGridVisible():
    '''returns boolean\n\n
    isYGridVisible()\n
    '''
def setYGridVisible():
    '''returns None\n\n
    setYGridVisible(final boolean majorLineVisible)\n
    '''
def formatXValue():
    '''returns String\n\n
    formatXValue(final double n)\n
    '''
def formatYValue():
    '''returns String\n\n
    formatYValue(final int n, final double n2)\n
    '''
def setXValueFormat():
    '''returns None\n\n
    setXValueFormat(final IlvValueFormat ilvValueFormat)\n
    '''
def setYValueFormat():
    '''returns None\n\n
    setYValueFormat(final int n, final IlvValueFormat ilvValueFormat)\n
    '''
def getDecorations():
    '''returns List<IlvChartDecoration>\n\n
    getDecorations()\n
    '''
def addDecoration():
    '''returns None\n\n
    addDecoration(final IlvChartDecoration ilvChartDecoration)\n
    '''
def removeDecoration():
    '''returns None\n\n
    removeDecoration(final IlvChartDecoration o)\n
    '''
def setDecorations():
    '''returns None\n\n
    setDecorations(final List<IlvChartDecoration> list)\n
    '''
def getRenderers():
    '''returns List<IlvChartRenderer>\n\n
    getRenderers()\n
    '''
def getRendererIterator():
    '''returns Iterator<IlvChartRenderer>\n\n
    getRendererIterator()\n
    '''
def getAllRendererIterator():
    '''returns Iterator<IlvChartRenderer>\n\n
    getAllRendererIterator()\n
    '''
def getRenderer():
    '''returns IlvChartRenderer\n\n
    getRenderer(final int index)\n
    '''
def setRenderer():
    '''returns None\n\n
    setRenderer(final int index, final IlvChartRenderer ilvChartRenderer)\n
    '''
def setRendererType():
    '''returns None\n\n
    setRendererType(final int n, final int n2)\n
    '''
def removeRenderer():
    '''returns None\n\n
    removeRenderer(final IlvChartRenderer ilvChartRenderer)\n
    '''
def getRendererCount():
    '''returns int\n\n
    getRendererCount()\n
    '''
def addRenderer():
    '''returns None\n\n
    addRenderer(final int n, final IlvChartRenderer ilvChartRenderer, final int n2)\n
    addRenderer(final IlvChartRenderer ilvChartRenderer, final int n)\n
    '''
def setRendererAxis():
    '''returns None\n\n
    setRendererAxis(final IlvChartRenderer ilvChartRenderer, final int yAxisIdx)\n
    '''
def addData():
    '''returns None\n\n
    addData(final IlvDataSource dataSource, final int n)\n
    '''
def setRenderingType():
    '''returns None\n\n
    setRenderingType(final int ax)\n
    '''
def getDataSetIterator():
    '''returns Iterator<IlvDataSet>\n\n
    getDataSetIterator()\n
    '''
def next():
    '''returns IlvDataSet\n\n
    next()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
def setDataSource():
    '''returns None\n\n
    setDataSource(final IlvDataSource dataSource)\n
    '''
def getDataSource():
    '''returns IlvDataSource\n\n
    getDataSource()\n
    '''
def getProjectorRect():
    '''returns Rectangle\n\n
    getProjectorRect()\n
    '''
def toDisplay():
    '''returns None\n\n
    toDisplay(final IlvDoublePoints ilvDoublePoints, final int n)\n
    '''
def toData():
    '''returns None\n\n
    toData(final IlvDoublePoints ilvDoublePoints, final int n)\n
    '''
def getProjector():
    '''returns IlvChartProjector\n\n
    getProjector()\n
    '''
def getNearestPoint():
    '''returns IlvDisplayPoint\n\n
    getNearestPoint(final IlvChartDataPicker ilvChartDataPicker)\n
    '''
def getNearestItem():
    '''returns IlvDisplayPoint\n\n
    getNearestItem(final IlvChartDataPicker ilvChartDataPicker, final double[] array)\n
    '''
def getDisplayItem():
    '''returns IlvDisplayPoint\n\n
    getDisplayItem(final IlvChartDataPicker ilvChartDataPicker)\n
    '''
def getDisplayItems():
    '''returns List<IlvDisplayPoint>\n\n
    getDisplayItems(final IlvChartDataPicker ilvChartDataPicker)\n
    '''
def scroll():
    '''returns None\n\n
    scroll(final double n, final double n2, final int n3)\n
    '''
def zoom():
    '''returns None\n\n
    zoom(final IlvDataWindow ilvDataWindow, final int n)\n
    '''
def invalidateScales():
    '''returns None\n\n
    invalidateScales()\n
    '''
def updateScales():
    '''returns None\n\n
    updateScales()\n
    '''
def updateScalesIfNeeded():
    '''returns None\n\n
    updateScalesIfNeeded()\n
    '''
def dataSetContentsChanged():
    '''returns None\n\n
    dataSetContentsChanged(final DataSetContentsEvent dataSetContentsEvent, final IlvChartRenderer ilvChartRenderer)\n
    '''
def updateDataRange():
    '''returns boolean\n\n
    updateDataRange()\n
    '''
def updateDataRangeAndRepaint():
    '''returns None\n\n
    updateDataRangeAndRepaint()\n
    '''
def getDataRangePolicy():
    '''returns IlvDataRangePolicy\n\n
    getDataRangePolicy()\n
    '''
def setDataRangePolicy():
    '''returns None\n\n
    setDataRangePolicy(final IlvDataRangePolicy bb)\n
    '''
def setResizingPolicy():
    '''returns None\n\n
    setResizingPolicy(final IlvChartResizingPolicy ba)\n
    '''
def getStyleSheets():
    '''returns String\n\n
    getStyleSheets()\n
    getStyleSheets(final int n)\n
    '''
def setStyleSheets():
    '''returns None\n\n
    setStyleSheets(final String[] styleSheets)\n
    setStyleSheets(final int n, final String s)\n
    '''
def getStyleSheetDebugMask():
    '''returns int\n\n
    getStyleSheetDebugMask()\n
    '''
def setStyleSheetDebugMask():
    '''returns None\n\n
    setStyleSheetDebugMask(final int styleSheetDebugMask)\n
    '''
def setDynamicStyling():
    '''returns None\n\n
    setDynamicStyling(final boolean b)\n
    '''
def getPseudoClasses():
    '''returns String[]\n\n
    getPseudoClasses()\n
    getPseudoClasses(final IlvDataSet key)\n
    getPseudoClasses(final IlvDataSet key, final int n)\n
    getPseudoClasses(final Object key)\n
    '''
def setPseudoClasses():
    '''returns None\n\n
    setPseudoClasses(final String[] mainPseudoClasses)\n
    setPseudoClasses(final IlvDataSet set, final String[] mainPseudoClasses)\n
    setPseudoClasses(final IlvDataSet set, final int n, final String[] array)\n
    setPseudoClasses(final Object o, final String[] array)\n
    '''
def addPseudoClass():
    '''returns None\n\n
    addPseudoClass(final String s)\n
    addPseudoClass(final IlvDataSet set, final String s)\n
    addPseudoClass(final IlvDataSet set, final int n, final String s)\n
    addPseudoClass(final Object o, final String s)\n
    '''
def removePseudoClass():
    '''returns None\n\n
    removePseudoClass(final String s)\n
    removePseudoClass(final IlvDataSet key, final String s)\n
    removePseudoClass(final IlvDataSet key, final int n, final String s)\n
    removePseudoClass(final Object o, final String s)\n
    '''
def clearPseudoClass():
    '''returns None\n\n
    clearPseudoClass(final String s)\n
    '''
def clearAllPseudoClasses():
    '''returns None\n\n
    clearAllPseudoClasses()\n
    '''
def registerFunction():
    '''returns None\n\n
    registerFunction(final IlvCSSFunction ilvCSSFunction)\n
    '''
def get3DView():
    '''returns IlvChart3DView\n\n
    get3DView()\n
    '''
def set3D():
    '''returns None\n\n
    set3D(final boolean b)\n
    '''
def getInteractors():
    '''returns IlvChartInteractor[]\n\n
    getInteractors()\n
    '''
def setInteractors():
    '''returns None\n\n
    setInteractors(IlvChartInteractor[] ad)\n
    '''
def addInteractor():
    '''returns None\n\n
    addInteractor(final IlvChartInteractor ilvChartInteractor)\n
    addInteractor(final String s)\n
    '''
def removeInteractor():
    '''returns None\n\n
    removeInteractor(final IlvChartInteractor ilvChartInteractor)\n
    '''
def getChartArea():
    '''returns Area\n\n
    getChartArea()\n
    '''
def getChartAreaBorder():
    '''returns Border\n\n
    getChartAreaBorder()\n
    '''
def setChartAreaBorder():
    '''returns None\n\n
    setChartAreaBorder(final Border border)\n
    '''
def getPlotAreaBackground():
    '''returns Color\n\n
    getPlotAreaBackground()\n
    '''
def setPlotAreaBackground():
    '''returns None\n\n
    setPlotAreaBackground(final Color fillPaint)\n
    '''
def getBackground():
    '''returns Color\n\n
    getBackground()\n
    getBackground()\n
    '''
def setBackgroundPaint():
    '''returns None\n\n
    setBackgroundPaint(final Paint bq)\n
    setBackgroundPaint(final Paint g)\n
    '''
def setBackground():
    '''returns None\n\n
    setBackground(final Color background)\n
    '''
def setForeground():
    '''returns None\n\n
    setForeground(final Color foreground)\n
    '''
def setLayout():
    '''returns None\n\n
    setLayout(final LayoutManager layout)\n
    setLayout(final LayoutManager layout)\n
    '''
def setHeader():
    '''returns None\n\n
    setHeader(final JComponent a6)\n
    '''
def getHeaderText():
    '''returns String\n\n
    getHeaderText()\n
    '''
def setHeaderText():
    '''returns None\n\n
    setHeaderText(final String text)\n
    '''
def setFooter():
    '''returns None\n\n
    setFooter(final JComponent a7)\n
    '''
def getFooterText():
    '''returns String\n\n
    getFooterText()\n
    '''
def setFooterText():
    '''returns None\n\n
    setFooterText(final String text)\n
    '''
def setLegend():
    '''returns None\n\n
    setLegend(final IlvLegend ilvLegend)\n
    '''
def addLegend():
    '''returns None\n\n
    addLegend(final IlvLegend ilvLegend, final String s)\n
    addLegend(final IlvLegend ilvLegend, String a, final boolean b)\n
    '''
def isLegendVisible():
    '''returns boolean\n\n
    isLegendVisible()\n
    '''
def setLegendVisible():
    '''returns None\n\n
    setLegendVisible(final boolean b)\n
    '''
def getLegendPosition():
    '''returns String\n\n
    getLegendPosition()\n
    '''
def setLegendPosition():
    '''returns None\n\n
    setLegendPosition(final String s)\n
    '''
def startRendererChanges():
    '''returns None\n\n
    startRendererChanges()\n
    '''
def endRendererChanges():
    '''returns None\n\n
    endRendererChanges()\n
    '''
def synchronizeAxis():
    '''returns None\n\n
    synchronizeAxis(final IlvChart ilvChart, final int n, final boolean b)\n
    '''
def unSynchronizeAxis():
    '''returns None\n\n
    unSynchronizeAxis(final int n)\n
    '''
def getXScrollBar():
    '''returns JScrollBar\n\n
    getXScrollBar()\n
    '''
def setXScrollBar():
    '''returns None\n\n
    setXScrollBar(final JScrollBar a9)\n
    '''
def attachBoundedModel():
    '''returns None\n\n
    attachBoundedModel(final BoundedRangeModel boundedRangeModel, final int n, final boolean b)\n
    attachBoundedModel(final BoundedRangeModel boundedRangeModel, final int n)\n
    '''
def detachBoundedModel():
    '''returns None\n\n
    detachBoundedModel(final BoundedRangeModel boundedRangeModel)\n
    '''
def paint():
    '''returns None\n\n
    paint(final Graphics g)\n
    paint(final Graphics2D g)\n
    paint(final Graphics2D graphics2D)\n
    '''
def revalidate():
    '''returns None\n\n
    revalidate()\n
    revalidate()\n
    '''
def repaint():
    '''returns None\n\n
    repaint()\n
    repaint()\n
    repaint(final IlvDataWindow ilvDataWindow, final int n)\n
    '''
def toImage():
    '''returns BufferedImage\n\n
    toImage(final BufferedImage bufferedImage, final boolean b)\n
    toImage(final int n, final int n2, final Color color)\n
    toImage(final int n, final int n2, final Color color)\n
    toImage(final BufferedImage bufferedImage, final boolean b)\n
    '''
def toPNG():
    '''returns None\n\n
    toPNG(final OutputStream outputStream, final boolean b)\n
    toPNG(final OutputStream outputStream)\n
    toPNG(final OutputStream outputStream, final int n, final int n2, final boolean b)\n
    toPNG(final OutputStream outputStream, final int n, final int n2)\n
    toPNG(final OutputStream outputStream, final boolean b)\n
    toPNG(final OutputStream outputStream)\n
    '''
def toJPEG():
    '''returns None\n\n
    toJPEG(final OutputStream outputStream)\n
    toJPEG(final OutputStream outputStream, final int n, final int n2)\n
    toJPEG(final OutputStream outputStream)\n
    '''
def paintCurrentThread():
    '''returns None\n\n
    paintCurrentThread(final Graphics2D graphics2D, final Color color)\n
    paintCurrentThread(final Graphics2D graphics2D, final Color color)\n
    '''
def print():
    '''returns None\n\n
    print(final Graphics graphics, final IlvChartPrintContext ilvChartPrintContext)\n
    '''
def printCurrentThread():
    '''returns None\n\n
    printCurrentThread(final Graphics graphics, final IlvChartPrintContext ilvChartPrintContext)\n
    '''
def paintToFO():
    '''returns Element\n\n
    paintToFO(final Document document, final boolean b)\n
    paintToFO(final Document document, final boolean b, final Color color)\n
    '''
def paintToFOCurrentThread():
    '''returns Element\n\n
    paintToFOCurrentThread(final Document document, final boolean b, final Color color)\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    dispose()\n
    dispose()\n
    '''
def getProject():
    '''returns URL\n\n
    getProject()\n
    '''
def setProject():
    '''returns None\n\n
    setProject(final URL bu)\n
    '''
def getGraphics():
    '''returns Graphics\n\n
    getGraphics()\n
    getGraphics()\n
    '''
def getImage():
    '''returns BufferedImage\n\n
    getImage()\n
    '''
def propertyChange():
    '''returns None\n\n
    propertyChange(final PropertyChangeEvent propertyChangeEvent)\n
    '''
def getDataPointPseudoClasses():
    '''returns String[]\n\n
    getDataPointPseudoClasses(final int n)\n
    '''
def setDataPointPseudoClasses():
    '''returns boolean\n\n
    setDataPointPseudoClasses(final int n, final String[] a2)\n
    '''
def addDataPointPseudoClass():
    '''returns boolean\n\n
    addDataPointPseudoClass(final int n, final String anObject)\n
    '''
def removeDataPointPseudoClass():
    '''returns boolean\n\n
    removeDataPointPseudoClass(final int n, final String anObject)\n
    '''
def getMainPseudoClasses():
    '''returns String[]\n\n
    getMainPseudoClasses()\n
    '''
def setMainPseudoClasses():
    '''returns boolean\n\n
    setMainPseudoClasses(final String[] array)\n
    '''
def addMainPseudoClass():
    '''returns boolean\n\n
    addMainPseudoClass(final String anObject)\n
    '''
def removeMainPseudoClass():
    '''returns boolean\n\n
    removeMainPseudoClass(final String anObject)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def axisRangeChanged():
    '''returns None\n\n
    axisRangeChanged(final AxisRangeEvent axisRangeEvent)\n
    '''
def axisChanged():
    '''returns None\n\n
    axisChanged(final AxisChangeEvent axisChangeEvent)\n
    '''
def getFont():
    '''returns Font\n\n
    getFont()\n
    '''
def setFont():
    '''returns None\n\n
    setFont(final Font font)\n
    '''
def isPlotRectIncludingAnnotations():
    '''returns boolean\n\n
    isPlotRectIncludingAnnotations()\n
    '''
def setPlotRectIncludingAnnotations():
    '''returns None\n\n
    setPlotRectIncludingAnnotations(final boolean a)\n
    '''
def setMargins():
    '''returns None\n\n
    setMargins(final Insets margins)\n
    '''
def setHorizontalMargins():
    '''returns None\n\n
    setHorizontalMargins(final int n, final int n2)\n
    '''
def setVerticalMargins():
    '''returns None\n\n
    setVerticalMargins(final int n, final int n2)\n
    '''
def setLeftMargin():
    '''returns None\n\n
    setLeftMargin(final int n)\n
    '''
def setRightMargin():
    '''returns None\n\n
    setRightMargin(final int n)\n
    '''
def setTopMargin():
    '''returns None\n\n
    setTopMargin(final int n)\n
    '''
def setBottomMargin():
    '''returns None\n\n
    setBottomMargin(final int n)\n
    '''
def getFixedMargins():
    '''returns int\n\n
    getFixedMargins()\n
    '''
def getMargins():
    '''returns Insets\n\n
    getMargins()\n
    '''
def getPlotStyle():
    '''returns IlvStyle\n\n
    getPlotStyle()\n
    '''
def setPlotStyle():
    '''returns None\n\n
    setPlotStyle(final IlvStyle c)\n
    '''
def isFilledPlottingArea():
    '''returns boolean\n\n
    isFilledPlottingArea()\n
    '''
def setFilledPlottingArea():
    '''returns None\n\n
    setFilledPlottingArea(final boolean fillOn)\n
    '''
def setPlotBackground():
    '''returns None\n\n
    setPlotBackground(final Paint fillPaint)\n
    setPlotBackground(final Color[] array, final boolean b)\n
    '''
def isValidateRoot():
    '''returns boolean\n\n
    isValidateRoot()\n
    '''
def isDirectRedrawEnabled():
    '''returns boolean\n\n
    isDirectRedrawEnabled()\n
    '''
def setDirectRedrawEnabled():
    '''returns None\n\n
    setDirectRedrawEnabled(final boolean b)\n
    '''
def getPreferredSize():
    '''returns Dimension\n\n
    getPreferredSize()\n
    '''
def getDrawRect():
    '''returns Rectangle\n\n
    getDrawRect()\n
    '''
def getPlotRect():
    '''returns Rectangle\n\n
    getPlotRect()\n
    '''
def revalidateLayout():
    '''returns None\n\n
    revalidateLayout()\n
    '''
