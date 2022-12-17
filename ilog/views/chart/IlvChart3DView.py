LEFT_WALL = "int  1"
RIGHT_WALL = "int  2"
TOP_WALL = "int  4"
BOTTOM_WALL = "int  8"
BACK_WALL = "int  16"
ORTHOGRAPHIC = "int  0"
OBLIQUE = "int  1"
def addPropertyChangeListener():
    '''returns None\n\n
    addPropertyChangeListener(final PropertyChangeListener listener)\n
    addPropertyChangeListener(final String propertyName, final PropertyChangeListener listener)\n
    '''
def removePropertyChangeListener():
    '''returns None\n\n
    removePropertyChangeListener(final PropertyChangeListener listener)\n
    removePropertyChangeListener(final String propertyName, final PropertyChangeListener listener)\n
    '''
def getFrontDepth():
    '''returns double\n\n
    getFrontDepth()\n
    '''
def getBackDepth():
    '''returns double\n\n
    getBackDepth()\n
    '''
def setZAnnotationRenderer():
    '''returns None\n\n
    setZAnnotationRenderer(final IlvLabelRenderer ilvLabelRenderer)\n
    '''
def setZAnnotationColorVarying():
    '''returns None\n\n
    setZAnnotationColorVarying(final boolean b)\n
    '''
def setZAnnotationVisible():
    '''returns None\n\n
    setZAnnotationVisible(final boolean b)\n
    '''
def setZGridVisible():
    '''returns None\n\n
    setZGridVisible(final boolean b)\n
    '''
def setZGridStroke():
    '''returns None\n\n
    setZGridStroke(final Stroke zGridStroke)\n
    '''
def setZGridPaint():
    '''returns None\n\n
    setZGridPaint(final Paint zGridPaint)\n
    '''
def setLightLatitude():
    '''returns None\n\n
    setLightLatitude(final double lightLatitude)\n
    '''
def setLightLongitude():
    '''returns None\n\n
    setLightLongitude(final double lightLongitude)\n
    '''
def setAmbientLight():
    '''returns None\n\n
    setAmbientLight(final float ambientLight)\n
    '''
def setProjectionType():
    '''returns None\n\n
    setProjectionType(final int projectionType)\n
    '''
def setElevation():
    '''returns None\n\n
    setElevation(double clamp)\n
    '''
def setRotation():
    '''returns None\n\n
    setRotation(final double i)\n
    '''
def setViewAngles():
    '''returns None\n\n
    setViewAngles(final double rotation, final double elevation)\n
    '''
def setDepth():
    '''returns None\n\n
    setDepth(int clamp)\n
    '''
def setDepthGap():
    '''returns None\n\n
    setDepthGap(int clamp)\n
    '''
def setZoom():
    '''returns None\n\n
    setZoom(double clamp)\n
    '''
def setAutoScaling():
    '''returns None\n\n
    setAutoScaling(final boolean f)\n
    '''
def setWallStyle():
    '''returns None\n\n
    setWallStyle(final int n, final IlvStyle style)\n
    '''
def toDisplay():
    '''returns IlvDoublePoints\n\n
    toDisplay(final IlvDoublePoints ilvDoublePoints, final int n, final double n2)\n
    '''
def getZLayers():
    '''returns List<ZLayer>\n\n
    getZLayers()\n
    '''
def getZMin():
    '''returns double\n\n
    getZMin()\n
    '''
def getZMax():
    '''returns double\n\n
    getZMax()\n
    '''
def getRenderers():
    '''returns List<IlvSingleChartRenderer>\n\n
    getRenderers()\n
    '''
