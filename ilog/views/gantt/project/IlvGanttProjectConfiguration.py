GANTT_CHART_TYPE = "String  \"activity\""
SCHEDULE_CHART_TYPE = "String  \"resource\""
def isSupportedChartType():
    '''returns boolean\n\n
    isSupportedChartType(final String s)\n
    '''
def getDataSource():
    '''returns IlvGanttDataSource\n\n
    getDataSource()\n
    '''
def getGanttModel():
    '''returns IlvGanttModel\n\n
    getGanttModel()\n
    '''
def getChartType():
    '''returns String\n\n
    getChartType()\n
    '''
def setChartType():
    '''returns None\n\n
    setChartType(final String str)\n
    setChartType(final IlvHierarchyChart ilvHierarchyChart)\n
    '''
def canApply():
    '''returns boolean\n\n
    canApply(final IlvStylable ilvStylable)\n
    '''
def apply():
    '''returns None\n\n
    apply(final IlvStylable obj)\n
    '''
def read():
    '''returns None\n\n
    read(final URL url)\n
    read(final URL h, final IlvGanttProjectConfiguration ilvGanttProjectConfiguration)\n
    '''
def write():
    '''returns None\n\n
    write(final URL url)\n
    write(final URL h, final IlvGanttProjectConfiguration ilvGanttProjectConfiguration)\n
    '''
def ():
    '''returns ConfigSerializer\n\n
    ()\n
    '''
