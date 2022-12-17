BaseHandleSelection = "int  0"
BaseBorderSelection = "int  1"
InvisibleSelection = "int  2"
CompositeHandleSelection = "int  3"
ResizingComposite = "int  0"
ResizingBase = "int  1"
TransformationModeAll = "int  1"
TransformationModeBaseOnly = "int  0"
def ():
    '''returns IlvCompositeGraphic\n\n
    ()\n
    (final IlvLayoutManager layout)\n
    (final IlvCompositeGraphic ilvCompositeGraphic)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid()\n
    '''
def invalidate():
    '''returns None\n\n
    invalidate(final boolean b)\n
    invalidate()\n
    '''
def validate():
    '''returns None\n\n
    validate()\n
    '''
def setLayout():
    '''returns None\n\n
    setLayout(final IlvLayoutManager a)\n
    '''
def getLayout():
    '''returns IlvLayoutManager\n\n
    getLayout()\n
    '''
def setChildren():
    '''returns None\n\n
    setChildren(final IlvGraphic[] b)\n
    setChildren(final int n, final IlvGraphic ilvGraphic)\n
    '''
def getChildren():
    '''returns IlvGraphic[]\n\n
    getChildren(final int n)\n
    getChildren()\n
    '''
def getParent():
    '''returns IlvComposite\n\n
    getParent()\n
    '''
def getRoot():
    '''returns IlvComposite\n\n
    getRoot()\n
    '''
def setConstraints():
    '''returns None\n\n
    setConstraints(final Object[] e)\n
    setConstraints(final int n, final Object o)\n
    '''
def getConstraints():
    '''returns Object\n\n
    getConstraints()\n
    getConstraints(final int n)\n
    '''
def getAttachables():
    '''returns IlvAttachable[]\n\n
    getAttachables()\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
    '''
def zoomable():
    '''returns boolean\n\n
    zoomable()\n
    '''
def moveResize():
    '''returns None\n\n
    moveResize(IlvRect b)\n
    '''
def resize():
    '''returns None\n\n
    resize(float n, float n2)\n
    '''
def scale():
    '''returns None\n\n
    scale(final double n, final double n2)\n
    '''
def setResizingPolicy():
    '''returns None\n\n
    setResizingPolicy(final int m)\n
    '''
def getResizingPolicy():
    '''returns int\n\n
    getResizingPolicy()\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def getIntersectionWithOutline():
    '''returns IlvPoint\n\n
    getIntersectionWithOutline(final IlvPoint ilvPoint, final IlvPoint obj, final IlvTransformer ilvTransformer)\n
    '''
def applyTransform():
    '''returns None\n\n
    applyTransform(final IlvTransformer ilvTransformer)\n
    '''
def setLayoutEnabled():
    '''returns None\n\n
    setLayoutEnabled(final boolean b, final boolean v)\n
    '''
def doLayout():
    '''returns None\n\n
    doLayout()\n
    '''
def setGraphicBag():
    '''returns None\n\n
    setGraphicBag(final IlvGraphicBag graphicBag)\n
    '''
def apply():
    '''returns None\n\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    '''
def getAttachmentBounds():
    '''returns IlvRect\n\n
    getAttachmentBounds()\n
    '''
def addChild():
    '''returns int\n\n
    addChild(final IlvGraphic ilvGraphic)\n
    '''
def getEventMaps():
    '''returns IlvEventMap\n\n
    getEventMaps()\n
    getEventMaps(final int n)\n
    '''
def setEventMaps():
    '''returns None\n\n
    setEventMaps(final IlvEventMap[] g)\n
    setEventMaps(final int n, final IlvEventMap ilvEventMap)\n
    '''
def setEventMap():
    '''returns None\n\n
    setEventMap(final IlvEventMap h)\n
    '''
def getEventMap():
    '''returns IlvEventMap\n\n
    getEventMap()\n
    '''
def selectionChanged():
    '''returns None\n\n
    selectionChanged(final ManagerSelectionChangedEvent managerSelectionChangedEvent)\n
    '''
def getObject():
    '''returns IlvGraphic\n\n
    getObject(final String s)\n
    '''
def setSelectionType():
    '''returns None\n\n
    setSelectionType(final int j)\n
    '''
def getSelectionType():
    '''returns int\n\n
    getSelectionType()\n
    '''
def makeSelection():
    '''returns IlvSelection\n\n
    makeSelection()\n
    '''
def getAction():
    '''returns Action\n\n
    getAction(final int n, final IlvMouseGesture ilvMouseGesture)\n
    '''
def hasActions():
    '''returns boolean\n\n
    hasActions(final int n)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def getHotSpot():
    '''returns IlvPoint\n\n
    getHotSpot()\n
    '''
def reshapeObject():
    '''returns None\n\n
    reshapeObject(final IlvGraphic ilvGraphic, final IlvRect ilvRect, final boolean b)\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def setLinkClippables():
    '''returns None\n\n
    setLinkClippables(final boolean[] l)\n
    setLinkClippables(final int n, final boolean b)\n
    '''
def getLinkClippables():
    '''returns boolean\n\n
    getLinkClippables()\n
    getLinkClippables(final int n)\n
    '''
def setVisibilityThresholds():
    '''returns None\n\n
    setVisibilityThresholds(final double[] k)\n
    setVisibilityThresholds(final int n, final double n2)\n
    '''
def getVisibilityThresholds():
    '''returns double\n\n
    getVisibilityThresholds()\n
    getVisibilityThresholds(final int n)\n
    '''
def getAttachableGraphic():
    '''returns IlvAttachableGraphic\n\n
    getAttachableGraphic(final IlvGraphic ilvGraphic)\n
    '''
def setLabel():
    '''returns None\n\n
    setLabel(final String label)\n
    '''
def getLabel():
    '''returns String\n\n
    getLabel()\n
    '''
def supportMultiline():
    '''returns boolean\n\n
    supportMultiline()\n
    '''
def getLabelBBox():
    '''returns IlvRect\n\n
    getLabelBBox(final IlvTransformer ilvTransformer)\n
    '''
def setTransformationMode():
    '''returns None\n\n
    setTransformationMode(final int p)\n
    '''
def getTransformationMode():
    '''returns int\n\n
    getTransformationMode()\n
    '''
def rotate():
    '''returns None\n\n
    rotate(final IlvPoint ilvPoint, final double n)\n
    '''
def getDefinitionRect():
    '''returns IlvRect\n\n
    getDefinitionRect()\n
    '''
def setDefinitionRect():
    '''returns None\n\n
    setDefinitionRect(final IlvRect ilvRect)\n
    '''
def getDefinitionTransformer():
    '''returns IlvTransformer\n\n
    getDefinitionTransformer()\n
    '''
def isVisible():
    '''returns boolean\n\n
    isVisible()\n
    '''
def setSensitive():
    '''returns None\n\n
    setSensitive(final boolean q)\n
    '''
def isSensitive():
    '''returns boolean\n\n
    isSensitive()\n
    '''
def isBaseTextDirectionSensitive():
    '''returns boolean\n\n
    isBaseTextDirectionSensitive()\n
    '''
def baseTextDirectionChanged():
    '''returns None\n\n
    baseTextDirectionChanged(final int n, final int n2)\n
    '''
def componentOrientationChanged():
    '''returns None\n\n
    componentOrientationChanged(final ComponentOrientation componentOrientation, final ComponentOrientation componentOrientation2)\n
    '''
