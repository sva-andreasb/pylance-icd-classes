ITEM_NODE = "String  \"node\""
ITEM_LINE = "String  \"line\""
ITEM_NORMAL = "String  \"normal\""
ITEM_DRAW_LINE = "String  \"line_draw\""
ITEM_TASK = "String  \"task\""
ITEM_DRAW_NEGATIVE_LINE = "String  \"line_draw_neg\""
MODE_NORMAL = "int  0"
MODE_DRAW_LINE = "int  1"
MODE_DRAW_NEGATIVE_LINE = "int  2"
def EditableDiagram():
    '''    public EditableDiagram(final Workflow workflow, final WorkflowEditor editor, final WorkflowApplet applet, final boolean canEdit)
    '''
def setWorkflow():
    '''    public void setWorkflow(final Workflow workflow)
    public void setWorkflow(final Workflow workflow, final WorkflowEditor editor, final boolean canEdit)
    '''
def buildDiagram():
    '''    public void buildDiagram()
    '''
def setMode():
    '''    public void setMode(final int mode)
    '''
def getMode():
    '''    public int getMode()
    '''
def getModeCursor():
    '''    public Cursor getModeCursor()
    '''
def setCursor():
    '''    public void setCursor(final String name, final Cursor cursor)
    '''
def getCursor():
    '''    public Cursor getCursor(final String name)
    '''
def setToolTip():
    '''    public void setToolTip(final String name, final String text)
    '''
def setScrollPane():
    '''    public void setScrollPane(final JScrollPane scrollPane)
    '''
def setSelection():
    '''    public void setSelection(final WorkflowEntity selection, final JScrollPane scrollPane)
    '''
def getToolTip():
    '''    public String getToolTip(final String name)
    '''
def workflowChanged():
    '''    public void workflowChanged(final WorkflowEditEvent e)
    '''
def getPreferredSize():
    '''    public Dimension getPreferredSize()
    '''
def isDragOk():
    '''    public boolean isDragOk(final DropTargetDragEvent event)
    '''
def dragEnter():
    '''    public void dragEnter(final DropTargetDragEvent event)
    '''
def dragExit():
    '''    public void dragExit(final DropTargetEvent event)
    '''
def dragOver():
    '''    public void dragOver(final DropTargetDragEvent event)
    '''
def drop():
    '''    public void drop(final DropTargetDropEvent event)
    '''
def dropActionChanged():
    '''    public void dropActionChanged(final DropTargetDragEvent event)
    '''
def getAutoscrollInsets():
    '''    public Insets getAutoscrollInsets()
    '''
def autoscroll():
    '''    public void autoscroll(final Point p)
    '''
def run():
    '''    public void run()
    '''
def mouseClicked():
    '''    public void mouseClicked(final MouseEvent e)
    '''
def mouseEntered():
    '''    public void mouseEntered(final MouseEvent e)
    '''
def mouseExited():
    '''    public void mouseExited(final MouseEvent e)
    '''
def mousePressed():
    '''    public void mousePressed(final MouseEvent e)
    '''
def mouseReleased():
    '''    public void mouseReleased(final MouseEvent e)
    '''
def mouseDragged():
    '''    public void mouseDragged(final MouseEvent e)
    '''
def mouseMoved():
    '''    public void mouseMoved(final MouseEvent e)
    '''
def getProxy():
    '''    public Transferable getProxy(final DiagramWorkflowNode node)
    '''
def isDropSupported():
    '''    public boolean isDropSupported()
    '''
def dropComplete():
    '''    public void dropComplete(final WorkflowNode sourceNode, final WorkflowNode dropNode)
    '''
def clearCursor():
    '''    public void clearCursor()
    '''
