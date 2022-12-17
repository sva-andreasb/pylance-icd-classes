def ():
    '''returns DebugJComponent\n\n
    ()\n
    (final String htmlText)\n
    (final IlvInputStream ilvInputStream)\n
    (final E1 obj1, final E2 obj2)\n
    (final Element elem)\n
    ()\n
    '''
def getHTMLText():
    '''returns String\n\n
    getHTMLText()\n
    '''
def setHTMLText():
    '''returns None\n\n
    setHTMLText(final String n)\n
    '''
def setFractionalMetrics():
    '''returns None\n\n
    setFractionalMetrics(final boolean o)\n
    '''
def setAntiAliasing():
    '''returns None\n\n
    setAntiAliasing(final boolean p)\n
    '''
def getDefaultFont():
    '''returns Font\n\n
    getDefaultFont()\n
    '''
def setDefaultFont():
    '''returns None\n\n
    setDefaultFont(final Font q)\n
    '''
def getPageWidth():
    '''returns float\n\n
    getPageWidth()\n
    '''
def setPageWidth():
    '''returns None\n\n
    setPageWidth(final float r)\n
    '''
def setLeftMargin():
    '''returns None\n\n
    setLeftMargin(final float s)\n
    '''
def setRightMargin():
    '''returns None\n\n
    setRightMargin(final float t)\n
    '''
def setTopMargin():
    '''returns None\n\n
    setTopMargin(final float u)\n
    '''
def setBottomMargin():
    '''returns None\n\n
    setBottomMargin(final float v)\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    contains(final int x, final int y)\n
    '''
def applyTransform():
    '''returns None\n\n
    applyTransform(final IlvTransformer ilvTransformer)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    '''
def processMouseClicked():
    '''returns None\n\n
    processMouseClicked(final MouseEvent mouseEvent, final IlvTransformer ilvTransformer)\n
    '''
def addHTMLInteractionListener():
    '''returns None\n\n
    addHTMLInteractionListener(final HTMLInteractionListener l)\n
    '''
def removeHTMLInteractionListener():
    '''returns None\n\n
    removeHTMLInteractionListener(final HTMLInteractionListener l)\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def get():
    '''returns V\n\n
    get(final K obj)\n
    '''
def put():
    '''returns None\n\n
    put(final K obj, final V obj2)\n
    '''
def getLayoutViewCount():
    '''returns int\n\n
    getLayoutViewCount()\n
    getLayoutViewCount()\n
    '''
def getLayoutView():
    '''returns View\n\n
    getLayoutView(final int index)\n
    getLayoutView(final int index)\n
    '''
def replaceLayoutView():
    '''returns None\n\n
    replaceLayoutView(final int offset, final View view)\n
    replaceLayoutView(final int offset, final View view)\n
    '''
def getPreferredSpan():
    '''returns float\n\n
    getPreferredSpan(final int n)\n
    '''
def getMinimumSpan():
    '''returns float\n\n
    getMinimumSpan(final int axis)\n
    '''
def getMaximumSpan():
    '''returns float\n\n
    getMaximumSpan(final int axis)\n
    '''
def setSize():
    '''returns None\n\n
    setSize(final float n, final float n2)\n
    '''
def getBreakWeight():
    '''returns int\n\n
    getBreakWeight(final int axis, final float pos, final float len)\n
    '''
def getResizeWeight():
    '''returns int\n\n
    getResizeWeight(final int axis)\n
    '''
def breakView():
    '''returns View\n\n
    breakView(final int axis, final int offset, final float n, final float n2)\n
    '''
def getViewCount():
    '''returns int\n\n
    getViewCount()\n
    '''
def getView():
    '''returns View\n\n
    getView(final int n)\n
    '''
def getDocument():
    '''returns Document\n\n
    getDocument()\n
    getDocument()\n
    '''
def getStartOffset():
    '''returns int\n\n
    getStartOffset()\n
    getStartOffset()\n
    '''
def getEndOffset():
    '''returns int\n\n
    getEndOffset()\n
    getEndOffset()\n
    '''
def paint():
    '''returns None\n\n
    paint(final Graphics graphics, final Shape shape)\n
    paint(final Graphics g)\n
    '''
def modelToView():
    '''returns Shape\n\n
    modelToView(final int n, final Shape shape, final Position.Bias bias)\n
    '''
def viewToModel():
    '''returns int\n\n
    viewToModel(final float n, final float n2, final Shape shape, final Position.Bias[] array)\n
    '''
def getAttributes():
    '''returns AttributeSet\n\n
    getAttributes()\n
    getAttributes()\n
    '''
def getParentElement():
    '''returns Element\n\n
    getParentElement()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getElementIndex():
    '''returns int\n\n
    getElementIndex(final int n)\n
    '''
def getElementCount():
    '''returns int\n\n
    getElementCount()\n
    '''
def getElement():
    '''returns Element\n\n
    getElement(final int n)\n
    '''
def isLeaf():
    '''returns boolean\n\n
    isLeaf()\n
    '''
def getFontMetrics():
    '''returns FontMetrics\n\n
    getFontMetrics(final Font font)\n
    getFontMetrics(final Font font)\n
    '''
def revalidate():
    '''returns None\n\n
    revalidate()\n
    revalidate()\n
    '''
def apply():
    '''returns None\n\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    '''
def repaint():
    '''returns None\n\n
    repaint(final long n, final int n2, final int n3, final int n4, final int n5)\n
    repaint(final long tm, final int x, final int y, final int width, final int height)\n
    repaint(final Rectangle r)\n
    '''
def getFont():
    '''returns Font\n\n
    getFont()\n
    getFont()\n
    '''
def isManagingFocus():
    '''returns boolean\n\n
    isManagingFocus()\n
    isManagingFocus()\n
    '''
def getLocation():
    '''returns Point\n\n
    getLocation(final Point rv)\n
    '''
def print():
    '''returns None\n\n
    print(final Graphics g)\n
    '''
def getSize():
    '''returns Dimension\n\n
    getSize(final Dimension rv)\n
    '''
def isOpaque():
    '''returns boolean\n\n
    isOpaque()\n
    '''
def disable():
    '''returns None\n\n
    disable()\n
    '''
def enable():
    '''returns None\n\n
    enable()\n
    '''
def update():
    '''returns None\n\n
    update(final Graphics g)\n
    '''
def addAncestorListener():
    '''returns None\n\n
    addAncestorListener(final AncestorListener listener)\n
    '''
def addNotify():
    '''returns None\n\n
    addNotify()\n
    '''
def addVetoableChangeListener():
    '''returns None\n\n
    addVetoableChangeListener(final VetoableChangeListener listener)\n
    '''
def computeVisibleRect():
    '''returns None\n\n
    computeVisibleRect(final Rectangle visibleRect)\n
    '''
def createToolTip():
    '''returns JToolTip\n\n
    createToolTip()\n
    '''
def firePropertyChange():
    '''returns None\n\n
    firePropertyChange(final String propertyName, final boolean oldValue, final boolean newValue)\n
    firePropertyChange(final String propertyName, final int oldValue, final int newValue)\n
    firePropertyChange(final String propertyName, final char oldValue, final char newValue)\n
    '''
def getAccessibleContext():
    '''returns AccessibleContext\n\n
    getAccessibleContext()\n
    '''
def getActionForKeyStroke():
    '''returns ActionListener\n\n
    getActionForKeyStroke(final KeyStroke aKeyStroke)\n
    '''
def getAlignmentX():
    '''returns float\n\n
    getAlignmentX()\n
    '''
def getAlignmentY():
    '''returns float\n\n
    getAlignmentY()\n
    '''
def getAncestorListeners():
    '''returns AncestorListener[]\n\n
    getAncestorListeners()\n
    '''
def getAutoscrolls():
    '''returns boolean\n\n
    getAutoscrolls()\n
    '''
def getBorder():
    '''returns Border\n\n
    getBorder()\n
    '''
def getBounds():
    '''returns Rectangle\n\n
    getBounds(final Rectangle rv)\n
    '''
def getComponentPopupMenu():
    '''returns JPopupMenu\n\n
    getComponentPopupMenu()\n
    '''
def getConditionForKeyStroke():
    '''returns int\n\n
    getConditionForKeyStroke(final KeyStroke aKeyStroke)\n
    '''
def getDebugGraphicsOptions():
    '''returns int\n\n
    getDebugGraphicsOptions()\n
    '''
def getGraphics():
    '''returns Graphics\n\n
    getGraphics()\n
    '''
def getHeight():
    '''returns int\n\n
    getHeight()\n
    '''
def getInheritsPopupMenu():
    '''returns boolean\n\n
    getInheritsPopupMenu()\n
    '''
def getInputVerifier():
    '''returns InputVerifier\n\n
    getInputVerifier()\n
    '''
def getInsets():
    '''returns Insets\n\n
    getInsets()\n
    getInsets(final Insets insets)\n
    '''
def getListeners():
    '''returns EventListener[]\n\n
    getListeners(final Class listenerType)\n
    '''
def getMaximumSize():
    '''returns Dimension\n\n
    getMaximumSize()\n
    '''
def getMinimumSize():
    '''returns Dimension\n\n
    getMinimumSize()\n
    '''
def getNextFocusableComponent():
    '''returns Component\n\n
    getNextFocusableComponent()\n
    '''
def getPopupLocation():
    '''returns Point\n\n
    getPopupLocation(final MouseEvent event)\n
    '''
def getPreferredSize():
    '''returns Dimension\n\n
    getPreferredSize()\n
    '''
def getRegisteredKeyStrokes():
    '''returns KeyStroke[]\n\n
    getRegisteredKeyStrokes()\n
    '''
def getRootPane():
    '''returns JRootPane\n\n
    getRootPane()\n
    '''
def getToolTipLocation():
    '''returns Point\n\n
    getToolTipLocation(final MouseEvent event)\n
    '''
def getToolTipText():
    '''returns String\n\n
    getToolTipText()\n
    getToolTipText(final MouseEvent event)\n
    '''
def getTopLevelAncestor():
    '''returns Container\n\n
    getTopLevelAncestor()\n
    '''
def getTransferHandler():
    '''returns TransferHandler\n\n
    getTransferHandler()\n
    '''
def getUIClassID():
    '''returns String\n\n
    getUIClassID()\n
    '''
def getVerifyInputWhenFocusTarget():
    '''returns boolean\n\n
    getVerifyInputWhenFocusTarget()\n
    '''
def getVetoableChangeListeners():
    '''returns VetoableChangeListener[]\n\n
    getVetoableChangeListeners()\n
    '''
def getVisibleRect():
    '''returns Rectangle\n\n
    getVisibleRect()\n
    '''
def getWidth():
    '''returns int\n\n
    getWidth()\n
    '''
def getX():
    '''returns int\n\n
    getX()\n
    '''
def getY():
    '''returns int\n\n
    getY()\n
    '''
def grabFocus():
    '''returns None\n\n
    grabFocus()\n
    '''
def isDoubleBuffered():
    '''returns boolean\n\n
    isDoubleBuffered()\n
    '''
def isOptimizedDrawingEnabled():
    '''returns boolean\n\n
    isOptimizedDrawingEnabled()\n
    '''
def isPaintingTile():
    '''returns boolean\n\n
    isPaintingTile()\n
    '''
def isRequestFocusEnabled():
    '''returns boolean\n\n
    isRequestFocusEnabled()\n
    '''
def isValidateRoot():
    '''returns boolean\n\n
    isValidateRoot()\n
    '''
def paintImmediately():
    '''returns None\n\n
    paintImmediately(final int x, final int y, final int w, final int h)\n
    paintImmediately(final Rectangle r)\n
    '''
def printAll():
    '''returns None\n\n
    printAll(final Graphics g)\n
    '''
def registerKeyboardAction():
    '''returns None\n\n
    registerKeyboardAction(final ActionListener anAction, final String aCommand, final KeyStroke aKeyStroke, final int aCondition)\n
    registerKeyboardAction(final ActionListener anAction, final KeyStroke aKeyStroke, final int aCondition)\n
    '''
def removeAncestorListener():
    '''returns None\n\n
    removeAncestorListener(final AncestorListener listener)\n
    '''
def removeNotify():
    '''returns None\n\n
    removeNotify()\n
    '''
def removeVetoableChangeListener():
    '''returns None\n\n
    removeVetoableChangeListener(final VetoableChangeListener listener)\n
    '''
def requestDefaultFocus():
    '''returns boolean\n\n
    requestDefaultFocus()\n
    '''
def requestFocus():
    '''returns boolean\n\n
    requestFocus()\n
    requestFocus(final boolean temporary)\n
    '''
def requestFocusInWindow():
    '''returns boolean\n\n
    requestFocusInWindow()\n
    '''
def resetKeyboardActions():
    '''returns None\n\n
    resetKeyboardActions()\n
    '''
def reshape():
    '''returns None\n\n
    reshape(final int x, final int y, final int w, final int h)\n
    '''
def scrollRectToVisible():
    '''returns None\n\n
    scrollRectToVisible(final Rectangle aRect)\n
    '''
def setAlignmentX():
    '''returns None\n\n
    setAlignmentX(final float alignmentX)\n
    '''
def setAlignmentY():
    '''returns None\n\n
    setAlignmentY(final float alignmentY)\n
    '''
def setAutoscrolls():
    '''returns None\n\n
    setAutoscrolls(final boolean autoscrolls)\n
    '''
def setBackground():
    '''returns None\n\n
    setBackground(final Color background)\n
    '''
def setBorder():
    '''returns None\n\n
    setBorder(final Border border)\n
    '''
def setComponentPopupMenu():
    '''returns None\n\n
    setComponentPopupMenu(final JPopupMenu componentPopupMenu)\n
    '''
def setDebugGraphicsOptions():
    '''returns None\n\n
    setDebugGraphicsOptions(final int debugGraphicsOptions)\n
    '''
def setDoubleBuffered():
    '''returns None\n\n
    setDoubleBuffered(final boolean doubleBuffered)\n
    '''
def setEnabled():
    '''returns None\n\n
    setEnabled(final boolean enabled)\n
    '''
def setFocusTraversalKeys():
    '''returns None\n\n
    setFocusTraversalKeys(final int id, final Set keystrokes)\n
    '''
def setFont():
    '''returns None\n\n
    setFont(final Font font)\n
    '''
def setForeground():
    '''returns None\n\n
    setForeground(final Color foreground)\n
    '''
def setInheritsPopupMenu():
    '''returns None\n\n
    setInheritsPopupMenu(final boolean inheritsPopupMenu)\n
    '''
def setInputVerifier():
    '''returns None\n\n
    setInputVerifier(final InputVerifier inputVerifier)\n
    '''
def setMaximumSize():
    '''returns None\n\n
    setMaximumSize(final Dimension maximumSize)\n
    '''
def setMinimumSize():
    '''returns None\n\n
    setMinimumSize(final Dimension minimumSize)\n
    '''
def setNextFocusableComponent():
    '''returns None\n\n
    setNextFocusableComponent(final Component nextFocusableComponent)\n
    '''
def setOpaque():
    '''returns None\n\n
    setOpaque(final boolean opaque)\n
    '''
def setPreferredSize():
    '''returns None\n\n
    setPreferredSize(final Dimension preferredSize)\n
    '''
def setRequestFocusEnabled():
    '''returns None\n\n
    setRequestFocusEnabled(final boolean requestFocusEnabled)\n
    '''
def setToolTipText():
    '''returns None\n\n
    setToolTipText(final String toolTipText)\n
    '''
def setTransferHandler():
    '''returns None\n\n
    setTransferHandler(final TransferHandler transferHandler)\n
    '''
def setVerifyInputWhenFocusTarget():
    '''returns None\n\n
    setVerifyInputWhenFocusTarget(final boolean verifyInputWhenFocusTarget)\n
    '''
def setVisible():
    '''returns None\n\n
    setVisible(final boolean visible)\n
    '''
def unregisterKeyboardAction():
    '''returns None\n\n
    unregisterKeyboardAction(final KeyStroke aKeyStroke)\n
    '''
def updateUI():
    '''returns None\n\n
    updateUI()\n
    '''
