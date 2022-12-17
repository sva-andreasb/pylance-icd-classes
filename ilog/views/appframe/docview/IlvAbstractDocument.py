UNDO_CMD = "String  \"Undo\""
REDO_CMD = "String  \"Redo\""
def ():
    '''returns IlvAbstractDocument\n\n
    ()\n
    '''
def propertyChange():
    '''returns None\n\n
    propertyChange(final PropertyChangeEvent propertyChangeEvent)\n
    propertyChange(final PropertyChangeEvent propertyChangeEvent)\n
    '''
def actionPerformed():
    '''returns None\n\n
    actionPerformed(final ActionEvent actionEvent)\n
    actionPerformed(final ActionEvent actionEvent)\n
    actionPerformed(final ActionEvent actionEvent)\n
    '''
def initializeDocument():
    '''returns boolean\n\n
    initializeDocument(final Object o)\n
    '''
def documentClosing():
    '''returns None\n\n
    documentClosing()\n
    '''
def documentClosed():
    '''returns None\n\n
    documentClosed()\n
    '''
def clean():
    '''returns None\n\n
    clean()\n
    '''
def activated():
    '''returns None\n\n
    activated(final boolean b)\n
    '''
def getViewCount():
    '''returns int\n\n
    getViewCount()\n
    '''
def removeView():
    '''returns boolean\n\n
    removeView(final IlvDocumentView ilvDocumentView)\n
    '''
def removeViews():
    '''returns None\n\n
    removeViews()\n
    '''
def addView():
    '''returns None\n\n
    addView(final IlvDocumentView ilvDocumentView)\n
    '''
def getView():
    '''returns IlvDocumentView\n\n
    getView(final int n)\n
    '''
def getViews():
    '''returns IlvDocumentView[]\n\n
    getViews()\n
    '''
def getActiveView():
    '''returns IlvDocumentView\n\n
    getActiveView()\n
    '''
def isModified():
    '''returns boolean\n\n
    isModified()\n
    '''
def setModified():
    '''returns None\n\n
    setModified(final boolean b)\n
    '''
def getTitle():
    '''returns String\n\n
    getTitle()\n
    '''
def setTitle():
    '''returns None\n\n
    setTitle(final String s)\n
    '''
def getDocumentTemplate():
    '''returns IlvDocumentTemplate\n\n
    getDocumentTemplate()\n
    '''
def updateAction():
    '''returns boolean\n\n
    updateAction(final Action action)\n
    '''
def isProcessingAction():
    '''returns boolean\n\n
    isProcessingAction(final String s)\n
    '''
def addActionHandler():
    '''returns None\n\n
    addActionHandler(final ActionHandler actionHandler)\n
    '''
def removeActionHandler():
    '''returns boolean\n\n
    removeActionHandler(final ActionHandler actionHandler)\n
    '''
def receiveMessage():
    '''returns None\n\n
    receiveMessage(final MessageEvent messageEvent)\n
    '''
def getUndoManager():
    '''returns UndoManager\n\n
    getUndoManager()\n
    '''
def canUndo():
    '''returns boolean\n\n
    canUndo()\n
    '''
def undo():
    '''returns None\n\n
    undo()\n
    undo()\n
    '''
def canRedo():
    '''returns boolean\n\n
    canRedo()\n
    '''
def redo():
    '''returns None\n\n
    redo()\n
    redo()\n
    '''
def addEdit():
    '''returns boolean\n\n
    addEdit(final UndoableEdit undoableEdit)\n
    addEdit(final UndoableEdit undoableEdit)\n
    '''
def setProperty():
    '''returns Object\n\n
    setProperty(final String s, final Object o)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String s)\n
    '''
def getApplication():
    '''returns IlvApplication\n\n
    getApplication()\n
    '''
def setApplication():
    '''returns None\n\n
    setApplication(final IlvApplication ilvApplication)\n
    '''
def addPropertyChangeListener():
    '''returns None\n\n
    addPropertyChangeListener(final PropertyChangeListener propertyChangeListener)\n
    '''
def removePropertyChangeListener():
    '''returns None\n\n
    removePropertyChangeListener(final PropertyChangeListener propertyChangeListener)\n
    '''
def attachDocument():
    '''returns None\n\n
    attachDocument(final IlvDocument ilvDocument, final boolean b)\n
    '''
def discardAllEdits():
    '''returns None\n\n
    discardAllEdits()\n
    '''
