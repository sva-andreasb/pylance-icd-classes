REQUEST_PARAM = "String  \"request\""
HEIGHT = "String  \"height\""
WIDTH = "String  \"width\""
IMAGE_REQUEST = "String  \"image\""
CAPABILITIES_REQUEST = "String  \"capabilities\""
HITMAP_REQUEST = "String  \"hitmap\""
VERBOSE_PARAM = "String  \"verbose\""
START_TIME_PARAM = "String  \"startTime\""
END_TIME_PARAM = "String  \"endTime\""
VERT_POSITION_PARAM = "String  \"vpos\""
HORZ_POSITION_PARAM = "String  \"hpos\""
ACTION_PARAM = "String  \"action\""
IMAGE_FORMAT_PARAM = "String  \"format\""
JPEG_IMAGE_FORMAT = "String  \"JPEG\""
PNG_IMAGE_FORMAT = "String  \"PNG\""
CAP_FORMAT_PARAM = "String  \"format\""
JSON_CAP_FORMAT = "String  \"json\""
HTML_CAP_FORMAT = "String  \"html\""
OCTET_CAP_FORMAT = "String  \"octet-stream\""
COMPONENT_PARAM = "String  \"comp\""
CHART_COMPONENT = "String  \"chart\""
TABLE_COMPONENT = "String  \"table\""
SHEET_COMPONENT = "String  \"sheet\""
def ():
    '''returns IlvGanttServletSupport\n\n
    ()\n
    '''
def setPopupEnabled():
    '''returns None\n\n
    setPopupEnabled(final boolean l)\n
    '''
def setSelectionEnabled():
    '''returns None\n\n
    setSelectionEnabled(final boolean n)\n
    '''
def getConfigParameters():
    '''returns IlvServletParameters\n\n
    getConfigParameters()\n
    '''
def setConfigParameters():
    '''returns None\n\n
    setConfigParameters(final IlvServletParameters h)\n
    '''
def getServletContext():
    '''returns ServletContext\n\n
    getServletContext()\n
    '''
def setServletContext():
    '''returns None\n\n
    setServletContext(final ServletContext o)\n
    '''
def isVerbose():
    '''returns boolean\n\n
    isVerbose(final IlvServletRequestParameters ilvServletRequestParameters)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    '''
def handleRequest():
    '''returns boolean\n\n
    handleRequest(final HttpServletRequest httpServletRequest, final HttpServletResponse httpServletResponse)\n
    '''
def getHitmapSupport():
    '''returns IlvGanttHitmapSupport\n\n
    getHitmapSupport()\n
    '''
def setImageEncoder():
    '''returns None\n\n
    setImageEncoder(final String s, final IlvImageEncoder value)\n
    '''
def getImageEncoder():
    '''returns IlvImageEncoder\n\n
    getImageEncoder(final String key)\n
    '''
def getObjectAt():
    '''returns Object\n\n
    getObjectAt(final IlvServletRequestParameters ilvServletRequestParameters, final int i, final int j)\n
    getObjectAt(final IlvHierarchyChart ilvHierarchyChart, final int width, final int height, final IlvServletRequestParameters ilvServletRequestParameters, int n, int n2)\n
    getObjectAt(final IlvHierarchyChart ilvHierarchyChart, final int width, final int height, final IlvServletRequestParameters ilvServletRequestParameters, int n, int n2)\n
    getObjectAt(final IlvHierarchyChart ilvHierarchyChart, final int n, final int n2, final IlvServletRequestParameters ilvServletRequestParameters, final int n3, final int n4)\n
    '''
def getResult():
    '''returns Object\n\n
    getResult()\n
    '''
def print():
    '''returns None\n\n
    print(final Graphics2D graphics2D, final IlvHierarchyChart ilvHierarchyChart, final int n, final int n2, final IlvServletRequestParameters ilvServletRequestParameters)\n
    print(final Graphics2D graphics2D, final IlvHierarchyChart ilvHierarchyChart, final int n, final int n2, final IlvServletRequestParameters ilvServletRequestParameters)\n
    print(final Graphics2D graphics2D, final IlvHierarchyChart ilvHierarchyChart, final int n, final int n2, final IlvServletRequestParameters ilvServletRequestParameters)\n
    '''
