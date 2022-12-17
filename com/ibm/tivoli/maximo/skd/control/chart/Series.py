NAME = "String  \"name\""
LEGEND_TITLE = "String  \"legend\""
DATA = "String  \"data\""
OPTIONS = "String  \"options\""
X_LABELS = "String  \"xlabels\""
Y_LABELS = "String  \"ylabels\""
X = "String  \"x\""
Y = "String  \"y\""
X_LABEL = "String  \"x_label\""
Y_LABEL = "String  \"y_label\""
TOOLTIP = "String  \"tooltip\""
LEGEND = "String  \"legend\""
X_REAL = "String  \"x_real\""
LABEL_VALUE = "Object  \"value\""
LABEL_TEXT = "Object  \"text\""
def ():
    '''returns Series\n\n
    ()\n
    (final String name)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def getData():
    '''returns JSONArray\n\n
    getData()\n
    '''
def setData():
    '''returns None\n\n
    setData(final JSONArray data)\n
    '''
def setOptions():
    '''returns None\n\n
    setOptions(final JSONObject options)\n
    '''
def getOptions():
    '''returns JSONObject\n\n
    getOptions()\n
    '''
def addPoint():
    '''returns JSONObject\n\n
    addPoint(final Number x, final Number y)\n
    addPoint(final Number x, final String xlabel, final Number y, final String ylabel)\n
    '''
def addPiePoint():
    '''returns JSONObject\n\n
    addPiePoint(final Number y, final String label, final String legend)\n
    '''
def normalizeSequence():
    '''returns None\n\n
    normalizeSequence()\n
    '''
def getXLabels():
    '''returns JSONArray\n\n
    getXLabels()\n
    '''
def getYLabels():
    '''returns JSONArray\n\n
    getYLabels()\n
    '''
