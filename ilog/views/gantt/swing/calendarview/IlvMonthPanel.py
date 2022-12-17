CALENDAR_MODEL_CHANGED_PROPERTY = "String  \"calendarModel\""
CALENDAR_CHANGED_PROPERTY = "String  \"calendar\""
def ():
    '''returns MouseHandler\n\n
    ()\n
    (final IlvGanttModel ganttModel)\n
    ()\n
    ()\n
    '''
def getCalendarModel():
    '''returns IlvCalendarModel\n\n
    getCalendarModel()\n
    '''
def setCalendarModel():
    '''returns None\n\n
    setCalendarModel(final IlvCalendarModel ilvCalendarModel)\n
    '''
def getCalendar():
    '''returns Calendar\n\n
    getCalendar()\n
    '''
def setCalendar():
    '''returns None\n\n
    setCalendar(final Calendar calendar)\n
    setCalendar(final Calendar a)\n
    '''
def getDate():
    '''returns Date\n\n
    getDate()\n
    '''
def setDate():
    '''returns None\n\n
    setDate(final Date time)\n
    '''
def incrementMonth():
    '''returns None\n\n
    incrementMonth()\n
    '''
def decrementMonth():
    '''returns None\n\n
    decrementMonth()\n
    '''
def getGanttModel():
    '''returns IlvGanttModel\n\n
    getGanttModel()\n
    '''
def setGanttModel():
    '''returns None\n\n
    setGanttModel(final IlvGanttModel o)\n
    '''
def getHolidayModel():
    '''returns IlvGanttModel\n\n
    getHolidayModel()\n
    '''
def setHolidayModel():
    '''returns None\n\n
    setHolidayModel(final IlvGanttModel q)\n
    '''
def setSelected():
    '''returns None\n\n
    setSelected(final IlvActivity ilvActivity, final boolean b)\n
    '''
def deselectAllActivities():
    '''returns None\n\n
    deselectAllActivities()\n
    '''
def getSelectedActivities():
    '''returns List\n\n
    getSelectedActivities()\n
    '''
def isSelected():
    '''returns boolean\n\n
    isSelected(final IlvActivity ilvActivity)\n
    '''
def addSelectionListener():
    '''returns None\n\n
    addSelectionListener(final SelectionListener selectionListener)\n
    '''
def removeSelectionListener():
    '''returns None\n\n
    removeSelectionListener(final SelectionListener selectionListener)\n
    '''
def isMouseSelectionEnabled():
    '''returns boolean\n\n
    isMouseSelectionEnabled()\n
    '''
def setMouseSelectionEnabled():
    '''returns None\n\n
    setMouseSelectionEnabled(final boolean b)\n
    '''
def getRowCount():
    '''returns int\n\n
    getRowCount()\n
    '''
def getColumn():
    '''returns int\n\n
    getColumn(final Point point)\n
    getColumn(final Calendar calendar)\n
    getColumn(final Date time)\n
    '''
def getRow():
    '''returns int\n\n
    getRow(final Point point)\n
    getRow(final Calendar calendar)\n
    getRow(final Date time)\n
    '''
def getCellRect():
    '''returns Rectangle\n\n
    getCellRect(final int n, final int n2)\n
    getCellRect(final Calendar calendar)\n
    '''
def getCellDate():
    '''returns Calendar\n\n
    getCellDate(final int n, final int n2)\n
    getCellDate(final Point point)\n
    '''
def getActivity():
    '''returns IlvActivity\n\n
    getActivity(final Point point)\n
    getActivity(final int value, final int index)\n
    getActivity(final Calendar calendar, final int n)\n
    '''
def getActivityHeight():
    '''returns int\n\n
    getActivityHeight()\n
    '''
def setActivityHeight():
    '''returns None\n\n
    setActivityHeight(final int ap)\n
    '''
def getActivityMargin():
    '''returns int\n\n
    getActivityMargin()\n
    '''
def setActivityMargin():
    '''returns None\n\n
    setActivityMargin(final int aq)\n
    '''
def getActivitySpacing():
    '''returns int\n\n
    getActivitySpacing()\n
    '''
def setActivitySpacing():
    '''returns None\n\n
    setActivitySpacing(final int ar)\n
    '''
def getVisibleActivityCount():
    '''returns int\n\n
    getVisibleActivityCount()\n
    '''
def getActivityRenderer():
    '''returns IlvActivityCalendarRenderer\n\n
    getActivityRenderer()\n
    '''
def setActivityRenderer():
    '''returns None\n\n
    setActivityRenderer(final IlvActivityCalendarRenderer at)\n
    '''
def getHolidayRenderer():
    '''returns IlvActivityCalendarRenderer\n\n
    getHolidayRenderer()\n
    '''
def setHolidayRenderer():
    '''returns None\n\n
    setHolidayRenderer(final IlvActivityCalendarRenderer au)\n
    '''
def getMilestoneRenderer():
    '''returns IlvMilestoneCalendarRenderer\n\n
    getMilestoneRenderer()\n
    '''
def setMilestoneRenderer():
    '''returns None\n\n
    setMilestoneRenderer(final IlvMilestoneCalendarRenderer av)\n
    '''
def getGridColor():
    '''returns Color\n\n
    getGridColor()\n
    '''
def setGridColor():
    '''returns None\n\n
    setGridColor(final Color x)\n
    '''
def getHeaderHeight():
    '''returns int\n\n
    getHeaderHeight()\n
    '''
def setHeaderHeight():
    '''returns None\n\n
    setHeaderHeight(final int z)\n
    '''
def getHeaderFont():
    '''returns Font\n\n
    getHeaderFont()\n
    '''
def setHeaderFont():
    '''returns None\n\n
    setHeaderFont(final Font ab)\n
    '''
def getHeaderForeground():
    '''returns Color\n\n
    getHeaderForeground()\n
    '''
def setHeaderForeground():
    '''returns None\n\n
    setHeaderForeground(final Color ac)\n
    '''
def getDayOfWeekHeight():
    '''returns int\n\n
    getDayOfWeekHeight()\n
    '''
def setDayOfWeekHeight():
    '''returns None\n\n
    setDayOfWeekHeight(final int ae)\n
    '''
def getDayOfWeekFont():
    '''returns Font\n\n
    getDayOfWeekFont()\n
    '''
def setDayOfWeekFont():
    '''returns None\n\n
    setDayOfWeekFont(final Font ag)\n
    '''
def getDayOfWeekForeground():
    '''returns Color\n\n
    getDayOfWeekForeground()\n
    '''
def setDayOfWeekForeground():
    '''returns None\n\n
    setDayOfWeekForeground(final Color ah)\n
    '''
def getDayOfWeekBackground():
    '''returns Color\n\n
    getDayOfWeekBackground()\n
    '''
def setDayOfWeekBackground():
    '''returns None\n\n
    setDayOfWeekBackground(final Color ai)\n
    '''
def getDayOfMonthFont():
    '''returns Font\n\n
    getDayOfMonthFont()\n
    '''
def setDayOfMonthFont():
    '''returns None\n\n
    setDayOfMonthFont(final Font am)\n
    '''
def getDayOfMonthForeground():
    '''returns Color\n\n
    getDayOfMonthForeground()\n
    '''
def setDayOfMonthForeground():
    '''returns None\n\n
    setDayOfMonthForeground(final Color an)\n
    '''
def getWeekendBackground():
    '''returns Color\n\n
    getWeekendBackground()\n
    '''
def setWeekendBackground():
    '''returns None\n\n
    setWeekendBackground(final Color ao)\n
    '''
def paintComponent():
    '''returns None\n\n
    paintComponent(final Graphics graphics)\n
    '''
def getToolTipText():
    '''returns String\n\n
    getToolTipText(final MouseEvent event)\n
    '''
def getLabel():
    '''returns String\n\n
    getLabel()\n
    '''
def setLabel():
    '''returns None\n\n
    setLabel(final String c)\n
    '''
def getFillPaint():
    '''returns Paint\n\n
    getFillPaint()\n
    '''
def setFillPaint():
    '''returns None\n\n
    setFillPaint(final Paint d)\n
    '''
def getStrokePaint():
    '''returns Paint\n\n
    getStrokePaint()\n
    '''
def setStrokePaint():
    '''returns None\n\n
    setStrokePaint(final Paint e)\n
    '''
def getStroke():
    '''returns Stroke\n\n
    getStroke()\n
    '''
def setStroke():
    '''returns None\n\n
    setStroke(final Stroke f)\n
    '''
def getLabelFont():
    '''returns Font\n\n
    getLabelFont()\n
    '''
def setLabelFont():
    '''returns None\n\n
    setLabelFont(final Font g)\n
    '''
def getLabelPaint():
    '''returns Paint\n\n
    getLabelPaint()\n
    '''
def setLabelPaint():
    '''returns None\n\n
    setLabelPaint(final Paint h)\n
    '''
def getLabelMargin():
    '''returns int\n\n
    getLabelMargin()\n
    '''
def setLabelMargin():
    '''returns None\n\n
    setLabelMargin(final int i)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final Calendar calendar, final Rectangle rectangle, final ComponentOrientation componentOrientation)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def add():
    '''returns None\n\n
    add(final IlvActivity ilvActivity)\n
    '''
def getActivityCount():
    '''returns int\n\n
    getActivityCount()\n
    '''
def getActivityRowCount():
    '''returns int\n\n
    getActivityRowCount(final int value)\n
    '''
def compare():
    '''returns int\n\n
    compare(final Object obj, final Object obj2)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def mousePressed():
    '''returns None\n\n
    mousePressed(final MouseEvent mouseEvent)\n
    '''
def activityChanged():
    '''returns None\n\n
    activityChanged(final ActivityEvent activityEvent)\n
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
def calendarChanged():
    '''returns None\n\n
    calendarChanged(final CalendarModelEvent calendarModelEvent)\n
    '''
