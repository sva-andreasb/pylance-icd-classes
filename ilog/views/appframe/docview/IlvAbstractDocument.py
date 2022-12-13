UNDO_CMD = "String  \"Undo\""
REDO_CMD = "String  \"Redo\""
def IlvAbstractDocument():
    '''public IlvAbstractDocument()
    '''
def propertyChange():
    '''public void propertyChange(final PropertyChangeEvent propertyChangeEvent)
    public void propertyChange(final PropertyChangeEvent propertyChangeEvent)
    '''
def actionPerformed():
    '''public void actionPerformed(final ActionEvent actionEvent)
    public void actionPerformed(final ActionEvent actionEvent)
    public void actionPerformed(final ActionEvent actionEvent)
    '''
def initializeDocument():
    '''public boolean initializeDocument(final Object o)
    '''
def documentClosing():
    '''public void documentClosing()
    '''
def documentClosed():
    '''public void documentClosed()
    '''
def clean():
    '''public void clean()
    '''
def activated():
    '''public void activated(final boolean b)
    '''
def getViewCount():
    '''public int getViewCount()
    '''
def removeView():
    '''public boolean removeView(final IlvDocumentView ilvDocumentView)
    '''
def removeViews():
    '''public void removeViews()
    '''
def addView():
    '''public void addView(final IlvDocumentView ilvDocumentView)
    '''
def getView():
    '''public IlvDocumentView getView(final int n)
    '''
def getViews():
    '''public IlvDocumentView[] getViews()
    '''
def getActiveView():
    '''public IlvDocumentView getActiveView()
    '''
def isModified():
    '''public boolean isModified()
    '''
def setModified():
    '''public void setModified(final boolean b)
    '''
def getTitle():
    '''public String getTitle()
    '''
def setTitle():
    '''public void setTitle(final String s)
    '''
def getDocumentTemplate():
    '''public IlvDocumentTemplate getDocumentTemplate()
    '''
def updateAction():
    '''public boolean updateAction(final Action action)
    '''
def isProcessingAction():
    '''public boolean isProcessingAction(final String s)
    '''
def addActionHandler():
    '''public void addActionHandler(final ActionHandler actionHandler)
    '''
def removeActionHandler():
    '''public boolean removeActionHandler(final ActionHandler actionHandler)
    '''
def receiveMessage():
    '''public void receiveMessage(final MessageEvent messageEvent)
    '''
def getUndoManager():
    '''public UndoManager getUndoManager()
    '''
def canUndo():
    '''public boolean canUndo()
    '''
def undo():
    '''public void undo()
    public void undo()
    '''
def canRedo():
    '''public boolean canRedo()
    '''
def redo():
    '''public void redo()
    public void redo()
    '''
def addEdit():
    '''public void addEdit(final UndoableEdit undoableEdit)
    public boolean addEdit(final UndoableEdit undoableEdit)
    '''
def setProperty():
    '''public Object setProperty(final String s, final Object o)
    '''
def getProperty():
    '''public Object getProperty(final String s)
    '''
def getApplication():
    '''public IlvApplication getApplication()
    '''
def setApplication():
    '''public void setApplication(final IlvApplication ilvApplication)
    '''
def addPropertyChangeListener():
    '''public void addPropertyChangeListener(final PropertyChangeListener propertyChangeListener)
    '''
def removePropertyChangeListener():
    '''public void removePropertyChangeListener(final PropertyChangeListener propertyChangeListener)
    '''
def attachDocument():
    '''public void attachDocument(final IlvDocument ilvDocument, final boolean b)
    '''
def discardAllEdits():
    '''public void discardAllEdits()
    '''
