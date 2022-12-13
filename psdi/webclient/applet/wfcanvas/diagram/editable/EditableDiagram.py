ITEM_NODE = "String  node""
ITEM_LINE = "String  line""
ITEM_NORMAL = "String  normal""
ITEM_DRAW_LINE = "String  line_draw""
ITEM_TASK = "String  task""
ITEM_DRAW_NEGATIVE_LINE = "String  line_draw_neg""
MODE_NORMAL = "int  0"
MODE_DRAW_LINE = "int  1"
MODE_DRAW_NEGATIVE_LINE = "int  2"
def EditableDiagram():
'''public EditableDiagram(final Workflow workflow, final WorkflowEditor editor, final WorkflowApplet applet, final boolean canEdit)
'''
pass
def setWorkflow():
'''public void setWorkflow(final Workflow workflow)
public void setWorkflow(final Workflow workflow, final WorkflowEditor editor, final boolean canEdit)
'''
pass
def buildDiagram():
'''public void buildDiagram()
'''
pass
def setMode():
'''public void setMode(final int mode)
'''
pass
def getMode():
'''public int getMode()
'''
pass
def getModeCursor():
'''public Cursor getModeCursor()
'''
pass
def setCursor():
'''public void setCursor(final String name, final Cursor cursor)
'''
pass
def getCursor():
'''public Cursor getCursor(final String name)
'''
pass
def setToolTip():
'''public void setToolTip(final String name, final String text)
'''
pass
def setScrollPane():
'''public void setScrollPane(final JScrollPane scrollPane)
'''
pass
def setSelection():
'''public void setSelection(final WorkflowEntity selection, final JScrollPane scrollPane)
'''
pass
def getToolTip():
'''public String getToolTip(final String name)
'''
pass
def workflowChanged():
'''public void workflowChanged(final WorkflowEditEvent e)
'''
pass
def getPreferredSize():
'''public Dimension getPreferredSize()
'''
pass
def isDragOk():
'''public boolean isDragOk(final DropTargetDragEvent event)
'''
pass
def dragEnter():
'''public void dragEnter(final DropTargetDragEvent event)
'''
pass
def dragExit():
'''public void dragExit(final DropTargetEvent event)
'''
pass
def dragOver():
'''public void dragOver(final DropTargetDragEvent event)
'''
pass
def drop():
'''public void drop(final DropTargetDropEvent event)
'''
pass
def dropActionChanged():
'''public void dropActionChanged(final DropTargetDragEvent event)
'''
pass
def getAutoscrollInsets():
'''public Insets getAutoscrollInsets()
'''
pass
def autoscroll():
'''public void autoscroll(final Point p)
'''
pass
def run():
'''public void run()
'''
pass
def mouseClicked():
'''public void mouseClicked(final MouseEvent e)
'''
pass
def mouseEntered():
'''public void mouseEntered(final MouseEvent e)
'''
pass
def mouseExited():
'''public void mouseExited(final MouseEvent e)
'''
pass
def mousePressed():
'''public void mousePressed(final MouseEvent e)
'''
pass
def mouseReleased():
'''public void mouseReleased(final MouseEvent e)
'''
pass
def mouseDragged():
'''public void mouseDragged(final MouseEvent e)
'''
pass
def mouseMoved():
'''public void mouseMoved(final MouseEvent e)
'''
pass
def getProxy():
'''public Transferable getProxy(final DiagramWorkflowNode node)
'''
pass
def isDropSupported():
'''public boolean isDropSupported()
'''
pass
def dropComplete():
'''public void dropComplete(final WorkflowNode sourceNode, final WorkflowNode dropNode)
'''
pass
def clearCursor():
'''public void clearCursor()
'''
pass
