def ():
    '''returns TreeDragGestureListener\n\n
    ()\n
    (final IlvPaletteViewer a)\n
    (final IlvPaletteTreeViewer b)\n
    (final IlvPaletteTreeViewer a)\n
    (final IlvPaletteTreeViewer a)\n
    '''
def setPalette():
    '''returns None\n\n
    setPalette(final IlvPalette c)\n
    '''
def getPalette():
    '''returns IlvPalette\n\n
    getPalette()\n
    '''
def getComponent():
    '''returns JComponent\n\n
    getComponent()\n
    '''
def addPaletteViewerListener():
    '''returns None\n\n
    addPaletteViewerListener(final PaletteViewerListener l)\n
    '''
def removePaletteViewerListener():
    '''returns None\n\n
    removePaletteViewerListener(final PaletteViewerListener l)\n
    '''
def setEditable():
    '''returns None\n\n
    setEditable(final boolean f)\n
    '''
def isEditable():
    '''returns boolean\n\n
    isEditable()\n
    '''
def select():
    '''returns None\n\n
    select(final IlvPaletteObject ilvPaletteObject)\n
    '''
def getSelectedPaletteObjects():
    '''returns IlvPaletteObject[]\n\n
    getSelectedPaletteObjects()\n
    '''
def addDropListener():
    '''returns None\n\n
    addDropListener(final PaletteDropListener l)\n
    '''
def removeDropListener():
    '''returns None\n\n
    removeDropListener(final PaletteDropListener l)\n
    '''
def setMultiSelectionEnabled():
    '''returns None\n\n
    setMultiSelectionEnabled(final boolean b)\n
    '''
def dragEnter():
    '''returns None\n\n
    dragEnter(final DropTargetDragEvent dropTargetDragEvent)\n
    dragEnter(final DragSourceDragEvent dragSourceDragEvent)\n
    '''
def dragOver():
    '''returns None\n\n
    dragOver(final DropTargetDragEvent dropTargetDragEvent)\n
    dragOver(final DragSourceDragEvent dragSourceDragEvent)\n
    '''
def dragExit():
    '''returns None\n\n
    dragExit(final DropTargetEvent dropTargetEvent)\n
    dragExit(final DragSourceEvent dragSourceEvent)\n
    '''
def dropActionChanged():
    '''returns None\n\n
    dropActionChanged(final DropTargetDragEvent dropTargetDragEvent)\n
    dropActionChanged(final DragSourceDragEvent dragSourceDragEvent)\n
    '''
def drop():
    '''returns None\n\n
    drop(final DropTargetDropEvent dropTargetDropEvent)\n
    '''
def removeSelectionPath():
    '''returns None\n\n
    removeSelectionPath(final TreePath path)\n
    '''
def removeSelectionPaths():
    '''returns None\n\n
    removeSelectionPaths(final TreePath[] paths)\n
    '''
def getDropCandidat():
    '''returns Object\n\n
    getDropCandidat()\n
    '''
def setDropCandidat():
    '''returns None\n\n
    setDropCandidat(final Object a)\n
    '''
def valueChanged():
    '''returns None\n\n
    valueChanged(final TreeSelectionEvent treeSelectionEvent)\n
    '''
def convertValueToText():
    '''returns String\n\n
    convertValueToText(final Object value, final boolean selected, final boolean expanded, final boolean leaf, final int row, final boolean hasFocus)\n
    '''
def setSelectionPath():
    '''returns None\n\n
    setSelectionPath(final TreePath treePath)\n
    '''
def saveExpandedState():
    '''returns None\n\n
    saveExpandedState(final TreePath parent)\n
    '''
def restoreExpandedState():
    '''returns None\n\n
    restoreExpandedState()\n
    '''
def dragDropEnd():
    '''returns None\n\n
    dragDropEnd(final DragSourceDropEvent dragSourceDropEvent)\n
    '''
def dragGestureRecognized():
    '''returns None\n\n
    dragGestureRecognized(final DragGestureEvent dragGestureEvent)\n
    '''
