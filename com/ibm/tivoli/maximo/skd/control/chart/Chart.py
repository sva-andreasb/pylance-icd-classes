TOP = "String  \"top\""
BOTTOM = "String  \"bottom\""
TITLE = "String  \"title\""
TITLE_POS = "String  \"titlePos\""
TITLE_GAP = "String  \"titleGap\""
TITLE_FONT = "String  \"titleFont\""
TITLE_FONT_COLOR = "String  \"titleFontColor\""
OPTIONS = "String  \"options\""
SERIES = "String  \"seriesArray\""
CHART_TYPE = "String  \"type\""
AXIS = "String  \"axis\""
LEGEND = "String  \"legend\""
def ():
    '''returns Chart\n\n
    ()\n
    '''
def getOptionsNode():
    '''returns JSONObject\n\n
    getOptionsNode()\n
    '''
def setTitle():
    '''returns None\n\n
    setTitle(final String title)\n
    '''
def getTitle():
    '''returns String\n\n
    getTitle()\n
    '''
def getChartType():
    '''returns ChartType\n\n
    getChartType()\n
    '''
def setChartType():
    '''returns None\n\n
    setChartType(final ChartType type)\n
    '''
def normalize():
    '''returns Chart\n\n
    normalize()\n
    '''
def getSeriesArray():
    '''returns JSONArray\n\n
    getSeriesArray()\n
    '''
def addSeries():
    '''returns None\n\n
    addSeries(final Series s)\n
    '''
def compare():
    '''returns int\n\n
    compare(final JSONObject o1, final JSONObject o2)\n
    '''
def isNormalized():
    '''returns boolean\n\n
    isNormalized()\n
    '''
def setNormalized():
    '''returns None\n\n
    setNormalized(final boolean normalized)\n
    '''
def getXLabels():
    '''returns JSONArray\n\n
    getXLabels()\n
    '''
def getYLabels():
    '''returns JSONArray\n\n
    getYLabels()\n
    '''
def addAxis():
    '''returns Axis\n\n
    addAxis(final Axis axis)\n
    '''
def getAxis():
    '''returns Axis\n\n
    getAxis(final String id)\n
    '''
def getXAxis():
    '''returns Axis\n\n
    getXAxis()\n
    '''
def getYAxis():
    '''returns Axis\n\n
    getYAxis()\n
    '''
def getLegend():
    '''returns Legend\n\n
    getLegend()\n
    '''
def visit():
    '''returns None\n\n
    visit(final ISeriesVisitor visitor)\n
    '''
