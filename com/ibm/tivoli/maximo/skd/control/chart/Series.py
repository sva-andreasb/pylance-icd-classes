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
def Series():
    '''    public Series()
    public Series(final String name)
    '''
def getName():
    '''    public String getName()
    '''
def setName():
    '''    public void setName(final String name)
    '''
def getData():
    '''    public JSONArray getData()
    '''
def setData():
    '''    public void setData(final JSONArray data)
    '''
def setOptions():
    '''    public void setOptions(final JSONObject options)
    '''
def getOptions():
    '''    public JSONObject getOptions()
    '''
def addPoint():
    '''    public JSONObject addPoint(final Number x, final Number y)
    public JSONObject addPoint(final Number x, final String xlabel, final Number y, final String ylabel)
    '''
def addPiePoint():
    '''    public JSONObject addPiePoint(final Number y, final String label, final String legend)
    '''
def normalizeSequence():
    '''    public void normalizeSequence()
    '''
def getXLabels():
    '''    public JSONArray getXLabels()
    '''
def getYLabels():
    '''    public JSONArray getYLabels()
    '''
