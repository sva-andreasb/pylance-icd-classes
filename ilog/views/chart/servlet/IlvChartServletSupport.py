REQUEST_PARAM = "String  \"request\""
IMAGE_REQUEST = "String  \"image\""
IMAGEMAP_REQUEST = "String  \"imagemap\""
HITMAP_REQUEST = "String  \"hitmap\""
VERBOSE_PARAM = "String  \"verbose\""
IMAGE_FORMAT_PARAM = "String  \"format\""
JPEG_IMAGE_FORMAT = "String  \"JPEG\""
PNG_IMAGE_FORMAT = "String  \"PNG\""
X_MIN_PARAM = "String  \"xMin\""
X_MAX_PARAM = "String  \"xMax\""
Y_MIN_PARAM = "String  \"yMin\""
Y_MAX_PARAM = "String  \"yMax\""
BG_COLOR_PARAM = "String  \"bgcolor\""
ACTION_PARAM = "String  \"action\""
COMPONENT_PARAM = "String  \"comp\""
CHART_COMPONENT = "String  \"chart\""
AREA_COMPONENT = "String  \"area\""
LEGEND_COMPONENT = "String  \"legend\""
OVERVIEW_COMPONENT = "String  \"overview\""
IMAGEMAP_NAME = "String  \"mapname\""
CAPABILITIES_REQUEST = "String  \"capabilities\""
CAP_FORMAT_PARAM = "String  \"format\""
JSON_CAP_FORMAT = "String  \"json\""
HTML_CAP_FORMAT = "String  \"html\""
OCTET_CAP_FORMAT = "String  \"octet-stream\""
def ():
    '''returns OverviewUpdater\n\n
    ()\n
    (final IlvChart ilvChart)\n
    (final JComponent component, final CapWriter capWriter)\n
    (final JComponent component, final CapWriter a)\n
    (final JComponent component)\n
    (final IlvChart ilvChart)\n
    (final JComponent component, final CapWriter capWriter)\n
    (final IlvChart ilvChart)\n
    (final IlvChart ilvChart)\n
    (final IlvLegend ilvLegend)\n
    (final JComponent component)\n
    (final IlvChart.Area area)\n
    (final IlvChart ilvChart)\n
    (final IlvLegend ilvLegend)\n
    (final JComponent component)\n
    (final JComponent component)\n
    (final IlvChart.Area area)\n
    (final IlvChart ilvChart)\n
    (final IlvLegend ilvLegend)\n
    (final JComponent component)\n
    (final JComponent component)\n
    (final IlvLegend ilvLegend)\n
    (final JComponent component)\n
    (final IlvChart.Area area)\n
    (final IlvChart.Area area)\n
    (final IlvChart ilvChart)\n
    (final IlvChart ilvChart)\n
    (final IlvChart a, final IlvChart ilvChart)\n
    '''
def setServlet():
    '''returns None\n\n
    setServlet(final HttpServlet j)\n
    '''
def getConfigParameters():
    '''returns IlvServletParameters\n\n
    getConfigParameters()\n
    '''
def setConfigParameters():
    '''returns None\n\n
    setConfigParameters(final IlvServletParameters f)\n
    '''
def isVerbose():
    '''returns boolean\n\n
    isVerbose(final IlvServletRequestParameters ilvServletRequestParameters)\n
    '''
def handleRequest():
    '''returns boolean\n\n
    handleRequest(final HttpServletRequest httpServletRequest, final HttpServletResponse httpServletResponse)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    run()\n
    '''
def setPopupEnabled():
    '''returns None\n\n
    setPopupEnabled(final boolean i)\n
    '''
def setImageEncoder():
    '''returns None\n\n
    setImageEncoder(final String s, final IlvImageEncoder value)\n
    '''
def getImageEncoder():
    '''returns IlvImageEncoder\n\n
    getImageEncoder(final String key)\n
    '''
def getHitmapSupport():
    '''returns IlvChartHitmapSupport\n\n
    getHitmapSupport()\n
    '''
def writeHTMLCapabilities():
    '''returns None\n\n
    writeHTMLCapabilities(final JComponent component, final PrintWriter printWriter, final IlvServletRequestParameters ilvServletRequestParameters)\n
    writeHTMLCapabilities(final JComponent component, final PrintWriter printWriter, final IlvServletRequestParameters ilvServletRequestParameters)\n
    '''
def prepareComponent():
    '''returns None\n\n
    prepareComponent(final IlvServletRequestParameters ilvServletRequestParameters)\n
    prepareComponent(final IlvServletRequestParameters ilvServletRequestParameters)\n
    prepareComponent(final IlvServletRequestParameters ilvServletRequestParameters)\n
    prepareComponent(final IlvServletRequestParameters ilvServletRequestParameters)\n
    prepareComponent(final IlvServletRequestParameters ilvServletRequestParameters)\n
    prepareComponent(final IlvServletRequestParameters ilvServletRequestParameters)\n
    prepareComponent(final IlvServletRequestParameters ilvServletRequestParameters)\n
    prepareComponent(final IlvServletRequestParameters ilvServletRequestParameters)\n
    prepareComponent(final IlvServletRequestParameters ilvServletRequestParameters)\n
    prepareComponent(final IlvServletRequestParameters ilvServletRequestParameters)\n
    prepareComponent(final IlvServletRequestParameters ilvServletRequestParameters)\n
    prepareComponent(final IlvServletRequestParameters ilvServletRequestParameters)\n
    prepareComponent(final IlvServletRequestParameters ilvServletRequestParameters)\n
    prepareComponent(final IlvServletRequestParameters ilvServletRequestParameters)\n
    '''
def toImage():
    '''returns BufferedImage\n\n
    toImage(final int n, final int n2, final Color color)\n
    toImage(final int n, final int n2, final Color color)\n
    toImage(final int n, final int n2, final Color color)\n
    '''
def dump():
    '''returns None\n\n
    dump(final BufferedImage bufferedImage, final boolean b)\n
    '''
def writeIMapCT():
    '''returns None\n\n
    writeIMapCT(final PrintWriter printWriter, final IlvServletRequestParameters ilvServletRequestParameters)\n
    writeIMapCT(final PrintWriter printWriter, final IlvServletRequestParameters ilvServletRequestParameters)\n
    '''
def writeIMap():
    '''returns None\n\n
    writeIMap(final PrintWriter printWriter, final IlvServletRequestParameters ilvServletRequestParameters)\n
    '''
def axisRangeChanged():
    '''returns None\n\n
    axisRangeChanged(final AxisRangeEvent axisRangeEvent)\n
    '''
def axisChanged():
    '''returns None\n\n
    axisChanged(final AxisChangeEvent axisChangeEvent)\n
    '''
