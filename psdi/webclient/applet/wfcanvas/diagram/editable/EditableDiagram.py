ITEM_NODE = "String  \"node\""
ITEM_LINE = "String  \"line\""
ITEM_NORMAL = "String  \"normal\""
ITEM_DRAW_LINE = "String  \"line_draw\""
ITEM_TASK = "String  \"task\""
ITEM_DRAW_NEGATIVE_LINE = "String  \"line_draw_neg\""
MODE_NORMAL = "int  0"
MODE_DRAW_LINE = "int  1"
MODE_DRAW_NEGATIVE_LINE = "int  2"
def ():
    '''returns EditableDiagram\n\n
    (final Workflow workflow, final WorkflowEditor editor, final WorkflowApplet applet, final boolean canEdit)\n
    '''
def setWorkflow():
    '''returns None\n\n
    setWorkflow(final Workflow workflow)\n
    setWorkflow(final Workflow workflow, final WorkflowEditor editor, final boolean canEdit)\n
    '''
def buildDiagram():
    '''returns None\n\n
    buildDiagram()\n
    '''
def setMode():
    '''returns None\n\n
    setMode(final int mode)\n
    '''
def getMode():
    '''returns int\n\n
    getMode()\n
    '''
def getModeCursor():
    '''returns Cursor\n\n
    getModeCursor()\n
    '''
def setCursor():
    '''returns None\n\n
    setCursor(final String name, final Cursor cursor)\n
    '''
def getCursor():
    '''returns Cursor\n\n
    getCursor(final String name)\n
    '''
def setToolTip():
    '''returns None\n\n
    setToolTip(final String name, final String text)\n
    '''
def setScrollPane():
    '''returns None\n\n
    setScrollPane(final JScrollPane scrollPane)\n
    '''
def setSelection():
    '''returns None\n\n
    setSelection(final WorkflowEntity selection, final JScrollPane scrollPane)\n
    '''
def getToolTip():
    '''returns String\n\n
    getToolTip(final String name)\n
    '''
def workflowChanged():
    '''returns None\n\n
    workflowChanged(final WorkflowEditEvent e)\n
    '''
def getPreferredSize():
    '''returns Dimension\n\n
    getPreferredSize()\n
    '''
def isDragOk():
    '''returns boolean\n\n
    isDragOk(final DropTargetDragEvent event)\n
    '''
def dragEnter():
    '''returns None\n\n
    dragEnter(final DropTargetDragEvent event)\n
    '''
def dragExit():
    '''returns None\n\n
    dragExit(final DropTargetEvent event)\n
    '''
def dragOver():
    '''returns None\n\n
    dragOver(final DropTargetDragEvent event)\n
    '''
def drop():
    '''returns None\n\n
    drop(final DropTargetDropEvent event)\n
    '''
def dropActionChanged():
    '''returns None\n\n
    dropActionChanged(final DropTargetDragEvent event)\n
    '''
def getAutoscrollInsets():
    '''returns Insets\n\n
    getAutoscrollInsets()\n
    '''
def autoscroll():
    '''returns None\n\n
    autoscroll(final Point p)\n
    '''
def run():
    '''returns None\n\n
    run()\n
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
def mouseDragged():
    '''returns None\n\n
    mouseDragged(final MouseEvent e)\n
    '''
def mouseMoved():
    '''returns None\n\n
    mouseMoved(final MouseEvent e)\n
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
