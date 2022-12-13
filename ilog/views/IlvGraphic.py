def IlvGraphic():
    '''    public IlvGraphic()
    public IlvGraphic(final IlvGraphic ilvGraphic)
    public IlvGraphic(final IlvInputStream ilvInputStream)
    '''
def zoomable():
    '''    public boolean zoomable()
    '''
def setZOrderIndex():
    '''    public final void setZOrderIndex(final int j)
    '''
def getZOrderIndex():
    '''    public final int getZOrderIndex()
    '''
def callDraw():
    '''    public final void callDraw(final Graphics graphics, final IlvTransformer ilvTransformer)
    '''
def boundingBox():
    '''    public final IlvRect boundingBox()
    '''
def getCenter():
    '''    public IlvPoint getCenter(final IlvTransformer ilvTransformer)
    '''
def contains():
    '''    public boolean contains(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)
    '''
def intersects():
    '''    public boolean intersects(final IlvRect ilvRect, final IlvRect ilvRect2, final IlvTransformer ilvTransformer)
    '''
def inside():
    '''    public boolean inside(final IlvRect ilvRect, final IlvRect ilvRect2, final IlvTransformer ilvTransformer)
    '''
def getIntersectionWithOutline():
    '''    public IlvPoint getIntersectionWithOutline(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)
    '''
def move():
    '''    public void move(final float n, final float n2)
    public void move(final IlvPoint ilvPoint)
    '''
def moveResize():
    '''    public void moveResize(IlvRect a)
    '''
def translate():
    '''    public void translate(final float n, final float n2)
    '''
def rotate():
    '''    public void rotate(final IlvPoint ilvPoint, double degreesToRadians)
    '''
def scale():
    '''    public void scale(final double n, final double n2)
    '''
def resize():
    '''    public void resize(final float n, final float n2)
    '''
def setGraphicBag():
    '''    public void setGraphicBag(final IlvGraphicBag b)
    '''
def getGraphicBag():
    '''    public final IlvGraphicBag getGraphicBag()
    '''
def getTopLevelGraphicBag():
    '''    public final synchronized IlvGraphicBag getTopLevelGraphicBag()
    '''
def setForeground():
    '''    public void setForeground(final Color color)
    '''
def setBackground():
    '''    public void setBackground(final Color color)
    '''
def setFillOn():
    '''    public void setFillOn(final boolean b)
    '''
def setStrokeOn():
    '''    public void setStrokeOn(final boolean b)
    '''
def reDraw():
    '''    public void reDraw()
    '''
def setName():
    '''    public void setName(final String nameImpl)
    '''
def setNameImpl():
    '''    public void setNameImpl(final String s)
    '''
def getName():
    '''    public String getName()
    '''
def removeProperty():
    '''    public boolean removeProperty(final String s)
    '''
def setProperty():
    '''    public void setProperty(final String s, final Object o)
    '''
def replaceProperty():
    '''    public boolean replaceProperty(final String s, final Object o)
    '''
def getProperty():
    '''    public Object getProperty(final String s)
    '''
def hasProperty():
    '''    public boolean hasProperty(final String s, final Object o)
    '''
def isVisible():
    '''    public boolean isVisible()
    '''
def setVisible():
    '''    public final void setVisible(final boolean b)
    '''
def isMovable():
    '''    public boolean isMovable()
    '''
def setMovable():
    '''    public final void setMovable(final boolean b)
    '''
def isEditable():
    '''    public final boolean isEditable()
    '''
def setEditable():
    '''    public final void setEditable(final boolean b)
    '''
def isSelectable():
    '''    public boolean isSelectable()
    '''
def setSelectable():
    '''    public final void setSelectable(final boolean b)
    '''
def addActionListener():
    '''    public final void addActionListener(final ActionListener l)
    '''
def removeActionListener():
    '''    public final void removeActionListener(final ActionListener l)
    '''
def processActionEvent():
    '''    public void processActionEvent(final ActionEvent actionEvent)
    '''
def makeSelection():
    '''    public IlvSelection makeSelection()
    '''
def getDefaultInteractor():
    '''    public String getDefaultInteractor()
    '''
def getObjectInteractor():
    '''    public final IlvObjectInteractor getObjectInteractor()
    '''
def setObjectInteractor():
    '''    public final void setObjectInteractor(final IlvObjectInteractor ilvObjectInteractor)
    '''
def getAndAssociateObjectInteractor():
    '''    public final IlvObjectInteractor getAndAssociateObjectInteractor()
    '''
def write():
    '''    public void write(final IlvOutputStream ilvOutputStream)
    '''
def isPersistent():
    '''    public boolean isPersistent()
    '''
def getTransferDataFlavors():
    '''    public DataFlavor[] getTransferDataFlavors()
    '''
def isDataFlavorSupported():
    '''    public boolean isDataFlavorSupported(final DataFlavor dataFlavor)
    '''
def getTransferData():
    '''    public Object getTransferData(final DataFlavor flavor)
    '''
def GetGraphicObject():
    '''    public static IlvGraphic GetGraphicObject(final Transferable transferable)
    '''
def toString():
    '''    public String toString()
    '''
def setBlinkingAction():
    '''    public void setBlinkingAction(final IlvBlinkingAction a)
    '''
def getBlinkingAction():
    '''    public IlvBlinkingAction getBlinkingAction()
    '''
def setBlinkingOnPeriod():
    '''    public void setBlinkingOnPeriod(long c)
    '''
def getBlinkingOnPeriod():
    '''    public long getBlinkingOnPeriod()
    '''
def setBlinkingOffPeriod():
    '''    public void setBlinkingOffPeriod(long d)
    '''
def getBlinkingOffPeriod():
    '''    public long getBlinkingOffPeriod()
    '''
def blinkingStateOn():
    '''    public final void blinkingStateOn(final boolean e)
    '''
def getBlinkingObjectOwner():
    '''    public IlvBlinkingObjectOwner getBlinkingObjectOwner()
    '''
def setToolTipText():
    '''    public void setToolTipText(final String s)
    '''
def getToolTipText():
    '''    public String getToolTipText()
    public String getToolTipText(final IlvPoint ilvPoint, final IlvTransformer ilvTransformer)
    '''
def setToolTipBaseTextDirection():
    '''    public void setToolTipBaseTextDirection(final int value)
    '''
def getToolTipBaseTextDirection():
    '''    public int getToolTipBaseTextDirection()
    '''
def setPopupMenu():
    '''    public void setPopupMenu(final JPopupMenu popupMenu)
    '''
def getPopupMenu():
    '''    public JPopupMenu getPopupMenu()
    public JPopupMenu getPopupMenu(final IlvPoint ilvPoint, final IlvTransformer ilvTransformer, final IlvManagerView ilvManagerView, final IlvPopupMenuManager ilvPopupMenuManager)
    '''
def setPopupMenuName():
    '''    public void setPopupMenuName(final String s)
    '''
def getPopupMenuName():
    '''    public String getPopupMenuName()
    '''
def getLocale():
    '''    public final Locale getLocale()
    '''
def getULocale():
    '''    public ULocale getULocale()
    '''
def isLocaleSensitive():
    '''    public boolean isLocaleSensitive()
    '''
def localeChanged():
    '''    public void localeChanged(final ULocale uLocale, final ULocale uLocale2)
    '''
def getComponentOrientation():
    '''    public ComponentOrientation getComponentOrientation()
    '''
def isComponentOrientationSensitive():
    '''    public boolean isComponentOrientationSensitive()
    '''
def componentOrientationChanged():
    '''    public void componentOrientationChanged(final ComponentOrientation componentOrientation, final ComponentOrientation componentOrientation2)
    '''
def setBaseTextDirection():
    '''    public void setBaseTextDirection(final int n)
    '''
def getBaseTextDirection():
    '''    public int getBaseTextDirection()
    '''
def getResolvedBaseTextDirection():
    '''    public int getResolvedBaseTextDirection()
    '''
def isBaseTextDirectionSensitive():
    '''    public boolean isBaseTextDirectionSensitive()
    '''
def usesBidiMarkers():
    '''    public boolean usesBidiMarkers()
    '''
def baseTextDirectionChanged():
    '''    public void baseTextDirectionChanged(final int n, final int n2)
    '''
def addNamedPropertyListener():
    '''    public void addNamedPropertyListener(final NamedPropertyListener l)
    '''
def removeNamedPropertyListener():
    '''    public void removeNamedPropertyListener(final NamedPropertyListener l)
    '''
def setNamedProperty():
    '''    public IlvNamedProperty setNamedProperty(final IlvNamedProperty value)
    '''
def getNamedProperty():
    '''    public IlvNamedProperty getNamedProperty(final String key)
    '''
def removeNamedProperty():
    '''    public void removeNamedProperty(final String key)
    '''
def isInApplyToObject():
    '''    public final boolean isInApplyToObject()
    '''
def setInApplyToObject():
    '''    public final boolean setInApplyToObject(final boolean b)
    '''
def apply():
    '''    public void apply(final IlvGraphic ilvGraphic, final Object o)
    '''
def viewChanged():
    '''    public void viewChanged(final ManagerViewsChangedEvent managerViewsChangedEvent)
    '''
