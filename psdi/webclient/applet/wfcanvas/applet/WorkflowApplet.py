LTR_DIRECTION = "String  \"LTR\""
RTL_DIRECTION = "String  \"RTL\""
CONTEXTUAL_DIRECTION = "String  \"CONTEXTUAL\""
NONE = "String  \"NONE\""
LRE = "String  \"\u202a\""
RLE = "String  \"\u202b\""
PDF = "String  \"\u202c\""
def ():
    '''returns WorkflowApplet\n\n
    ()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def setMaxvalueNodeTypes():
    '''returns None\n\n
    setMaxvalueNodeTypes(final String types)\n
    '''
def setTranslatedNodeTypes():
    '''returns None\n\n
    setTranslatedNodeTypes(final String types)\n
    '''
def setupProcess():
    '''returns None\n\n
    setupProcess(final String id, final String name, final boolean editable, final int zoomLevel)\n
    '''
def addNode():
    '''returns None\n\n
    addNode(final String id, final String row, final String type, final String x, final String y, String title, final boolean tobedeleted)\n
    '''
def addAction():
    '''returns None\n\n
    addAction(final String id, final String row, final String ownerrow, final String ownerid, final String memberid, final String ispositive, final boolean tobedeleted)\n
    '''
def setupApplet():
    '''returns None\n\n
    setupApplet()\n
    '''
def diagramChanged():
    '''returns None\n\n
    diagramChanged(final DiagramEvent e)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    '''
def setCursor():
    '''returns None\n\n
    setCursor(final boolean on)\n
    setCursor(final Cursor cursor)\n
    '''
def movenode():
    '''returns None\n\n
    movenode()\n
    '''
def newnode():
    '''returns None\n\n
    newnode(final String id, final int row)\n
    '''
def moveaction():
    '''returns None\n\n
    moveaction()\n
    '''
def newaction():
    '''returns None\n\n
    newaction(final String id, final int row)\n
    '''
def deleteEntity():
    '''returns None\n\n
    deleteEntity()\n
    '''
def select():
    '''returns None\n\n
    select(final Object ent)\n
    select()\n
    '''
def workflowChanged():
    '''returns None\n\n
    workflowChanged(final WorkflowEditEvent e)\n
    '''
def actionPerformed():
    '''returns None\n\n
    actionPerformed(final ActionEvent e)\n
    '''
def openWorkflow():
    '''returns None\n\n
    openWorkflow(final int zoomLevel, int nodeRow, int actionRow, final String selected, final boolean reload)\n
    '''
def showError():
    '''returns None\n\n
    showError(final String errorText)\n
    showError(final Hashtable appletResources, final String errorText)\n
    showError(final Hashtable appletResources)\n
    '''
def itemStateChanged():
    '''returns None\n\n
    itemStateChanged(final ItemEvent e)\n
    '''
def setBidiEnabled():
    '''returns None\n\n
    setBidiEnabled(final boolean enabled)\n
    '''
def isBidiEnabled():
    '''returns boolean\n\n
    isBidiEnabled()\n
    '''
def setMaximoTextDirection():
    '''returns None\n\n
    setMaximoTextDirection(final String dir)\n
    '''
def getMaximoTextDirection():
    '''returns String\n\n
    getMaximoTextDirection()\n
    '''
def enforceBidiDirection():
    '''returns String\n\n
    enforceBidiDirection(String str, final String bidiDirection)\n
    '''
def sendEvent():
    '''returns None\n\n
    sendEvent(final String event, final WorkflowEntity entity)\n
    sendEvent(final String event, final WorkflowEntity entity, final Hashtable values)\n
    sendEvent(final String event, final Object value)\n
    sendEvent(final String event, final String target, final Hashtable values)\n
    sendEvent(final String event, final Hashtable values)\n
    '''
def getProxy():
    '''returns Transferable\n\n
    getProxy(final DiagramWorkflowNode node)\n
    '''
def isDropSupported():
    '''returns boolean\n\n
    isDropSupported()\n
    '''
def dropComplete():
    '''returns None\n\n
    dropComplete(final WorkflowNode sourceNode, final WorkflowNode dropNode)\n
    '''
def clearCursor():
    '''returns None\n\n
    clearCursor()\n
    '''
def mouseMoved():
    '''returns None\n\n
    mouseMoved(final MouseEvent e)\n
    '''
def mouseDragged():
    '''returns None\n\n
    mouseDragged(final MouseEvent e)\n
    '''
def mouseClicked():
    '''returns None\n\n
    mouseClicked(final MouseEvent e)\n
    '''
def mouseEntered():
    '''returns None\n\n
    mouseEntered(final MouseEvent e)\n
    '''
def mouseExited():
    '''returns None\n\n
    mouseExited(final MouseEvent e)\n
    '''
def mousePressed():
    '''returns None\n\n
    mousePressed(final MouseEvent e)\n
    '''
def mouseReleased():
    '''returns None\n\n
    mouseReleased(final MouseEvent e)\n
    '''
