LEFT_WALL = "int  1"
RIGHT_WALL = "int  2"
TOP_WALL = "int  4"
BOTTOM_WALL = "int  8"
BACK_WALL = "int  16"
ORTHOGRAPHIC = "int  0"
OBLIQUE = "int  1"
def addPropertyChangeListener():
    '''    public void addPropertyChangeListener(final PropertyChangeListener listener)
    public void addPropertyChangeListener(final String propertyName, final PropertyChangeListener listener)
    '''
def removePropertyChangeListener():
    '''    public void removePropertyChangeListener(final PropertyChangeListener listener)
    public void removePropertyChangeListener(final String propertyName, final PropertyChangeListener listener)
    '''
def getScene():
    '''    public final IlvChart3DScene getScene()
    '''
def getChart():
    '''    public final IlvChart getChart()
    '''
def draw():
    '''    public synchronized void draw(final Graphics graphics)
    '''
def getFrontDepth():
    '''    public double getFrontDepth()
    '''
def getBackDepth():
    '''    public double getBackDepth()
    '''
def getZAnnotationRenderer():
    '''    public final IlvLabelRenderer getZAnnotationRenderer()
    '''
def setZAnnotationRenderer():
    '''    public void setZAnnotationRenderer(final IlvLabelRenderer ilvLabelRenderer)
    '''
def isZAnnotationColorVarying():
    '''    public final boolean isZAnnotationColorVarying()
    '''
def setZAnnotationColorVarying():
    '''    public void setZAnnotationColorVarying(final boolean b)
    '''
def isZAnnotationVisible():
    '''    public final boolean isZAnnotationVisible()
    '''
def setZAnnotationVisible():
    '''    public void setZAnnotationVisible(final boolean b)
    '''
def isZGridVisible():
    '''    public final boolean isZGridVisible()
    '''
def setZGridVisible():
    '''    public void setZGridVisible(final boolean b)
    '''
def getZGridStroke():
    '''    public final Stroke getZGridStroke()
    '''
def setZGridStroke():
    '''    public void setZGridStroke(final Stroke zGridStroke)
    '''
def getZGridPaint():
    '''    public final Paint getZGridPaint()
    '''
def setZGridPaint():
    '''    public void setZGridPaint(final Paint zGridPaint)
    '''
def getLightLatitude():
    '''    public final double getLightLatitude()
    '''
def setLightLatitude():
    '''    public void setLightLatitude(final double lightLatitude)
    '''
def getLightLongitude():
    '''    public final double getLightLongitude()
    '''
def setLightLongitude():
    '''    public void setLightLongitude(final double lightLongitude)
    '''
def getAmbientLight():
    '''    public final float getAmbientLight()
    '''
def setAmbientLight():
    '''    public void setAmbientLight(final float ambientLight)
    '''
def getProjectionType():
    '''    public final int getProjectionType()
    '''
def setProjectionType():
    '''    public void setProjectionType(final int projectionType)
    '''
def getElevation():
    '''    public final double getElevation()
    '''
def setElevation():
    '''    public void setElevation(double clamp)
    '''
def getRotation():
    '''    public final double getRotation()
    '''
def setRotation():
    '''    public void setRotation(final double i)
    '''
def setViewAngles():
    '''    public void setViewAngles(final double rotation, final double elevation)
    '''
def getDepth():
    '''    public final int getDepth()
    '''
def setDepth():
    '''    public void setDepth(int clamp)
    '''
def getDepthGap():
    '''    public final int getDepthGap()
    '''
def setDepthGap():
    '''    public void setDepthGap(int clamp)
    '''
def getZoom():
    '''    public final double getZoom()
    '''
def setZoom():
    '''    public void setZoom(double clamp)
    '''
def isAutoScaling():
    '''    public final boolean isAutoScaling()
    '''
def setAutoScaling():
    '''    public void setAutoScaling(final boolean f)
    '''
def setWallStyle():
    '''    public void setWallStyle(final int n, final IlvStyle style)
    '''
def toDisplay():
    '''    public IlvDoublePoints toDisplay(final IlvDoublePoints ilvDoublePoints, final int n, final double n2)
    '''
def getZLayers():
    '''    public List<ZLayer> getZLayers()
    '''
def getZMin():
    '''    public double getZMin()
    '''
def getZMax():
    '''    public double getZMax()
    '''
def getRenderers():
    '''    public List<IlvSingleChartRenderer> getRenderers()
    '''
