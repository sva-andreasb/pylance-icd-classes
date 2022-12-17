def ():
    '''returns IlvDefaultLabelingModel\n\n
    (final IlvManager d)\n
    '''
def createLabelingModel():
    '''returns IlvLabelingModel\n\n
    createLabelingModel(final Object o)\n
    '''
def getLabels():
    '''returns Enumeration\n\n
    getLabels()\n
    '''
def isLabel():
    '''returns boolean\n\n
    isLabel(final Object o)\n
    '''
def setLabel():
    '''returns None\n\n
    setLabel(final Object o, final boolean b)\n
    '''
def moveLabel():
    '''returns None\n\n
    moveLabel(final Object o, final float n, final float n2, final boolean b)\n
    '''
def getLabelOverlap():
    '''returns double\n\n
    getLabelOverlap(final Object o, final IlvRect ilvRect, final Object o2, final IlvRect ilvRect2, final float n)\n
    getLabelOverlap(final Object o, final IlvRect ilvRect, final double n, final Object o2, final IlvRect ilvRect2, final double n2, final float n3)\n
    '''
def getObstacles():
    '''returns Enumeration\n\n
    getObstacles()\n
    '''
def isObstacle():
    '''returns boolean\n\n
    isObstacle(final Object o)\n
    '''
def setObstacle():
    '''returns None\n\n
    setObstacle(final Object o, final boolean b)\n
    '''
def getObstacleOverlap():
    '''returns double\n\n
    getObstacleOverlap(final Object o, final IlvRect ilvRect, final Object o2, final IlvRect ilvRect2, final float n)\n
    getObstacleOverlap(final Object o, final IlvRect ilvRect, final double n, final Object o2, final IlvRect ilvRect2, final float n2)\n
    '''
def isPolylineObstacle():
    '''returns boolean\n\n
    isPolylineObstacle(final Object o)\n
    '''
def getPolylineWidth():
    '''returns float\n\n
    getPolylineWidth(final Object o)\n
    '''
def getPolylinePoints():
    '''returns IlvPoint[]\n\n
    getPolylinePoints(final Object o)\n
    '''
def getPolylineObstacleOverlap():
    '''returns double\n\n
    getPolylineObstacleOverlap(final Object o, final IlvRect ilvRect, final Object o2, final IlvPoint[] array, final float n, final float n2)\n
    getPolylineObstacleOverlap(final Object o, final IlvRect ilvRect, double degreesToRadians, final Object o2, final IlvPoint[] array, final float n, final float n2)\n
    '''
def getManager():
    '''returns IlvManager\n\n
    getManager()\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final Object o)\n
    '''
def isBoundingBoxDependent():
    '''returns boolean\n\n
    isBoundingBoxDependent()\n
    '''
def isLayoutNeeded():
    '''returns boolean\n\n
    isLayoutNeeded(final IlvLabelLayout ilvLabelLayout)\n
    '''
def beforeLayout():
    '''returns None\n\n
    beforeLayout(final IlvLabelLayout ilvLabelLayout, final boolean b)\n
    '''
def afterLayout():
    '''returns None\n\n
    afterLayout(final IlvLabelLayout ilvLabelLayout, final IlvLabelLayoutReport ilvLabelLayoutReport, final boolean b)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final Object o, final String s, final Object o2)\n
    setProperty(final String s, final Object o)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final Object o, final String s)\n
    getProperty(final String s)\n
    '''
def setCoordinatesMode():
    '''returns None\n\n
    setCoordinatesMode(final int coordinatesModeInternal)\n
    setCoordinatesMode(final int coordinatesMode)\n
    '''
def getCoordinatesMode():
    '''returns int\n\n
    getCoordinatesMode()\n
    getCoordinatesMode()\n
    '''
def setReferenceTransformer():
    '''returns None\n\n
    setReferenceTransformer(final IlvTransformer referenceTransformerInternal)\n
    '''
def getReferenceTransformer():
    '''returns IlvTransformer\n\n
    getReferenceTransformer()\n
    '''
def setReferenceView():
    '''returns None\n\n
    setReferenceView(final IlvManagerView referenceView)\n
    '''
def getReferenceView():
    '''returns IlvManagerView\n\n
    getReferenceView()\n
    '''
def setFullLayerNotification():
    '''returns None\n\n
    setFullLayerNotification(final boolean fullLayerNotification)\n
    '''
def saveParametersToNamedProperties():
    '''returns String\n\n
    saveParametersToNamedProperties(final IlvLabelLayout ilvLabelLayout, final boolean b)\n
    saveParametersToNamedProperties(final IlvLabelLayout ilvLabelLayout, final String s, final boolean b)\n
    '''
def loadParametersFromNamedProperties():
    '''returns IlvLabelLayout\n\n
    loadParametersFromNamedProperties(final IlvLabelLayout ilvLabelLayout)\n
    loadParametersFromNamedProperties(final IlvLabelLayout ilvLabelLayout, final String s)\n
    loadParametersFromNamedProperties(final String s)\n
    '''
def removeParametersFromNamedProperties():
    '''returns None\n\n
    removeParametersFromNamedProperties()\n
    removeParametersFromNamedProperties(final String s)\n
    removeParametersFromNamedProperties(final Class clazz)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getRotation():
    '''returns double\n\n
    getRotation(final Object o, final IlvRect ilvRect)\n
    '''
def setRotation():
    '''returns None\n\n
    setRotation(final Object o, final double n)\n
    '''
def getLayout():
    '''returns Object\n\n
    getLayout()\n
    '''
def getInstanceId():
    '''returns int\n\n
    getInstanceId()\n
    '''
def getModel():
    '''returns Object\n\n
    getModel()\n
    '''
def setOriginalCoordModeOfModel():
    '''returns None\n\n
    setOriginalCoordModeOfModel(final int n)\n
    '''
def getOriginalCoordModeOfModel():
    '''returns int\n\n
    getOriginalCoordModeOfModel()\n
    '''
def supportsSaveParametersToNamedProperties():
    '''returns boolean\n\n
    supportsSaveParametersToNamedProperties()\n
    '''
def createLayoutManagerProperty():
    '''returns IlvNamedProperty\n\n
    createLayoutManagerProperty(final String s, final boolean b)\n
    '''
def hasMoreElements():
    '''returns boolean\n\n
    hasMoreElements()\n
    hasMoreElements()\n
    '''
def nextElement():
    '''returns Object\n\n
    nextElement()\n
    nextElement()\n
    '''
