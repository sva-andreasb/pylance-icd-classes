def ():
    '''returns PaintContext\n\n
    ()\n
    (final IlvTimeScaleVisibilityPolicy n)\n
    ()\n
    (final IlvTimeScale a, final Date date, final IlvDuration ilvDuration, final int viewStart, final int viewWidth, final Font d)\n
    (final IlvTimeScale ilvTimeScale, final Date date, final IlvDuration ilvDuration, final int n, final int n2)\n
    (final PaintContext paintContext)\n
    '''
def getPaintContext():
    '''returns PaintContext\n\n
    getPaintContext()\n
    '''
def createPaintContext():
    '''returns PaintContext\n\n
    createPaintContext(final Date date, final IlvDuration ilvDuration, final Rectangle rectangle)\n
    '''
def updateUI():
    '''returns None\n\n
    updateUI()\n
    '''
def addRow():
    '''returns None\n\n
    addRow(final IlvTimeScaleRow e)\n
    '''
def removeRow():
    '''returns None\n\n
    removeRow(final IlvTimeScaleRow o)\n
    '''
def getRow():
    '''returns IlvTimeScaleRow[]\n\n
    getRow(final int index)\n
    getRow()\n
    '''
def setRow():
    '''returns None\n\n
    setRow(final int index, final IlvTimeScaleRow element)\n
    setRow(final IlvTimeScaleRow[] array)\n
    '''
def getTotalRowSize():
    '''returns int\n\n
    getTotalRowSize()\n
    '''
def getTimeScaleRow():
    '''returns IlvTimeScaleRow\n\n
    getTimeScaleRow(final int n)\n
    '''
def getTime():
    '''returns Date\n\n
    getTime(final long n)\n
    getTime(final long n)\n
    '''
def getLocation():
    '''returns long\n\n
    getLocation(final Date date)\n
    getLocation(final Date date)\n
    '''
def showRow():
    '''returns None\n\n
    showRow(final IlvTimeScaleRow o)\n
    '''
def hideRow():
    '''returns None\n\n
    hideRow(final IlvTimeScaleRow o)\n
    '''
def revalidate():
    '''returns None\n\n
    revalidate()\n
    '''
def repaint():
    '''returns None\n\n
    repaint()\n
    '''
def paint():
    '''returns None\n\n
    paint(final Graphics graphics, final Rectangle rectangle, final PaintContext paintContext)\n
    '''
def setBounds():
    '''returns None\n\n
    setBounds(final int x, final int y, final int width, final int height)\n
    '''
def setIntegerZoomAllowed():
    '''returns None\n\n
    setIntegerZoomAllowed(final boolean j)\n
    '''
def isIntegerZoomAllowed():
    '''returns boolean\n\n
    isIntegerZoomAllowed()\n
    '''
def setZoomAllowed():
    '''returns None\n\n
    setZoomAllowed(final boolean k)\n
    '''
def isZoomAllowed():
    '''returns boolean\n\n
    isZoomAllowed()\n
    '''
def setTranslationAllowed():
    '''returns None\n\n
    setTranslationAllowed(final boolean l)\n
    '''
def isTranslationAllowed():
    '''returns boolean\n\n
    isTranslationAllowed()\n
    '''
def setOpaqueTranslation():
    '''returns None\n\n
    setOpaqueTranslation(final boolean m)\n
    '''
def isOpaqueTranslation():
    '''returns boolean\n\n
    isOpaqueTranslation()\n
    '''
def getPreferredSize():
    '''returns Dimension\n\n
    getPreferredSize()\n
    '''
def paintSeparator():
    '''returns None\n\n
    paintSeparator(final Graphics graphics, final int n, final int n2, final int n3)\n
    '''
def getTimeConverter():
    '''returns IlvTimeConverter\n\n
    getTimeConverter()\n
    '''
def setTimeConverter():
    '''returns None\n\n
    setTimeConverter(final IlvTimeConverter timeConverter)\n
    '''
def getVisibilityPolicy():
    '''returns IlvTimeScaleVisibilityPolicy\n\n
    getVisibilityPolicy()\n
    '''
def setVisibilityPolicy():
    '''returns None\n\n
    setVisibilityPolicy(final IlvTimeScaleVisibilityPolicy n)\n
    '''
def isVisibilityAdjusted():
    '''returns boolean\n\n
    isVisibilityAdjusted()\n
    '''
def setVisibilityAdjusted():
    '''returns None\n\n
    setVisibilityAdjusted(final boolean p)\n
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
def computeCalendar():
    '''returns None\n\n
    computeCalendar()\n
    '''
def getCalendar():
    '''returns Calendar\n\n
    getCalendar()\n
    getCalendar(final Date time)\n
    '''
def setTimeZone():
    '''returns None\n\n
    setTimeZone(final TimeZone d)\n
    '''
def getTimeZone():
    '''returns TimeZone\n\n
    getTimeZone()\n
    '''
def isConstantZoomFactorOnWidthChange():
    '''returns boolean\n\n
    isConstantZoomFactorOnWidthChange()\n
    '''
def setConstantZoomFactorOnWidthChange():
    '''returns None\n\n
    setConstantZoomFactorOnWidthChange(final boolean constantZoomFactorOnWidthChange)\n
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
    getVisibleTime()\n
    '''
def setVisibleTime():
    '''returns None\n\n
    setVisibleTime(final Date visibleTime)\n
    setVisibleTime(final Date visibleTime)\n
    setVisibleTime(final Date date)\n
    '''
def getVisibleDuration():
    '''returns IlvDuration\n\n
    getVisibleDuration()\n
    getVisibleDuration()\n
    '''
def setVisibleDuration():
    '''returns None\n\n
    setVisibleDuration(final IlvDuration visibleDuration)\n
    setVisibleDuration(final IlvDuration visibleDuration)\n
    setVisibleDuration(final IlvDuration ilvDuration)\n
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
def previousUnitTime():
    '''returns Date\n\n
    previousUnitTime(final Date date)\n
    '''
def getPreferredHeight():
    '''returns int\n\n
    getPreferredHeight()\n
    '''
def nextUnitTime():
    '''returns Date\n\n
    nextUnitTime(final Date date)\n
    '''
def getXTranslation():
    '''returns double\n\n
    getXTranslation()\n
    '''
def getXZoomFactor():
    '''returns double\n\n
    getXZoomFactor()\n
    '''
def getFont():
    '''returns Font\n\n
    getFont()\n
    '''
def setFont():
    '''returns None\n\n
    setFont(final Font d)\n
    '''
def computeVisibleTimeScroll():
    '''returns Date\n\n
    computeVisibleTimeScroll(final long n, final long n2)\n
    '''
def getSizeOf():
    '''returns int\n\n
    getSizeOf(final int n)\n
    '''
def getYearSize():
    '''returns int\n\n
    getYearSize()\n
    '''
def getQuarterSize():
    '''returns int\n\n
    getQuarterSize()\n
    '''
def getMonthSize():
    '''returns int\n\n
    getMonthSize()\n
    '''
def getWeekSize():
    '''returns int\n\n
    getWeekSize()\n
    '''
def getDaySize():
    '''returns int\n\n
    getDaySize()\n
    '''
def getHourSize():
    '''returns int\n\n
    getHourSize()\n
    '''
def getMinuteSize():
    '''returns int\n\n
    getMinuteSize()\n
    '''
def getTimeScale():
    '''returns IlvTimeScale\n\n
    getTimeScale()\n
    '''
