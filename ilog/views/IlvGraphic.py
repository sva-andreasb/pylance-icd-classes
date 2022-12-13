def IlvGraphic():
'''public IlvGraphic()
public IlvGraphic(final IlvGraphic ilvGraphic)
public IlvGraphic(final IlvInputStream ilvInputStream)
'''
pass
def zoomable():
'''public boolean zoomable()
'''
pass
def setZOrderIndex():
'''public final void setZOrderIndex(final int j)
'''
pass
def getZOrderIndex():
'''public final int getZOrderIndex()
'''
pass
def callDraw():
'''public final void callDraw(final Graphics graphics, final IlvTransformer ilvTransformer)
'''
pass
def boundingBox():
'''public final IlvRect boundingBox()
'''
pass
def getCenter():
'''public IlvPoint getCenter(final IlvTransformer ilvTransformer)
'''
pass
def contains():
'''public boolean contains(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)
'''
pass
def intersects():
'''public boolean intersects(final IlvRect ilvRect, final IlvRect ilvRect2, final IlvTransformer ilvTransformer)
'''
pass
def inside():
'''public boolean inside(final IlvRect ilvRect, final IlvRect ilvRect2, final IlvTransformer ilvTransformer)
'''
pass
def getIntersectionWithOutline():
'''public IlvPoint getIntersectionWithOutline(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)
'''
pass
def move():
'''public void move(final float n, final float n2)
public void move(final IlvPoint ilvPoint)
'''
pass
def moveResize():
'''public void moveResize(IlvRect a)
'''
pass
def translate():
'''public void translate(final float n, final float n2)
'''
pass
def rotate():
'''public void rotate(final IlvPoint ilvPoint, double degreesToRadians)
'''
pass
def scale():
'''public void scale(final double n, final double n2)
'''
pass
def resize():
'''public void resize(final float n, final float n2)
'''
pass
def setGraphicBag():
'''public void setGraphicBag(final IlvGraphicBag b)
'''
pass
def getGraphicBag():
'''public final IlvGraphicBag getGraphicBag()
'''
pass
def getTopLevelGraphicBag():
'''public final synchronized IlvGraphicBag getTopLevelGraphicBag()
'''
pass
def setForeground():
'''public void setForeground(final Color color)
'''
pass
def setBackground():
'''public void setBackground(final Color color)
'''
pass
def setFillOn():
'''public void setFillOn(final boolean b)
'''
pass
def setStrokeOn():
'''public void setStrokeOn(final boolean b)
'''
pass
def reDraw():
'''public void reDraw()
'''
pass
def setName():
'''public void setName(final String nameImpl)
'''
pass
def setNameImpl():
'''public void setNameImpl(final String s)
'''
pass
def getName():
'''public String getName()
'''
pass
def removeProperty():
'''public boolean removeProperty(final String s)
'''
pass
def setProperty():
'''public void setProperty(final String s, final Object o)
'''
pass
def replaceProperty():
'''public boolean replaceProperty(final String s, final Object o)
'''
pass
def getProperty():
'''public Object getProperty(final String s)
'''
pass
def hasProperty():
'''public boolean hasProperty(final String s, final Object o)
'''
pass
def isVisible():
'''public boolean isVisible()
'''
pass
def setVisible():
'''public final void setVisible(final boolean b)
'''
pass
def isMovable():
'''public boolean isMovable()
'''
pass
def setMovable():
'''public final void setMovable(final boolean b)
'''
pass
def isEditable():
'''public final boolean isEditable()
'''
pass
def setEditable():
'''public final void setEditable(final boolean b)
'''
pass
def isSelectable():
'''public boolean isSelectable()
'''
pass
def setSelectable():
'''public final void setSelectable(final boolean b)
'''
pass
def addActionListener():
'''public final void addActionListener(final ActionListener l)
'''
pass
def removeActionListener():
'''public final void removeActionListener(final ActionListener l)
'''
pass
def processActionEvent():
'''public void processActionEvent(final ActionEvent actionEvent)
'''
pass
def makeSelection():
'''public IlvSelection makeSelection()
'''
pass
def getDefaultInteractor():
'''public String getDefaultInteractor()
'''
pass
def getObjectInteractor():
'''public final IlvObjectInteractor getObjectInteractor()
'''
pass
def setObjectInteractor():
'''public final void setObjectInteractor(final IlvObjectInteractor ilvObjectInteractor)
'''
pass
def getAndAssociateObjectInteractor():
'''public final IlvObjectInteractor getAndAssociateObjectInteractor()
'''
pass
def write():
'''public void write(final IlvOutputStream ilvOutputStream)
'''
pass
def isPersistent():
'''public boolean isPersistent()
'''
pass
def getTransferDataFlavors():
'''public DataFlavor[] getTransferDataFlavors()
'''
pass
def isDataFlavorSupported():
'''public boolean isDataFlavorSupported(final DataFlavor dataFlavor)
'''
pass
def getTransferData():
'''public Object getTransferData(final DataFlavor flavor)
'''
pass
def GetGraphicObject():
'''public static IlvGraphic GetGraphicObject(final Transferable transferable)
'''
pass
def toString():
'''public String toString()
'''
pass
def setBlinkingAction():
'''public void setBlinkingAction(final IlvBlinkingAction a)
'''
pass
def getBlinkingAction():
'''public IlvBlinkingAction getBlinkingAction()
'''
pass
def setBlinkingOnPeriod():
'''public void setBlinkingOnPeriod(long c)
'''
pass
def getBlinkingOnPeriod():
'''public long getBlinkingOnPeriod()
'''
pass
def setBlinkingOffPeriod():
'''public void setBlinkingOffPeriod(long d)
'''
pass
def getBlinkingOffPeriod():
'''public long getBlinkingOffPeriod()
'''
pass
def blinkingStateOn():
'''public final void blinkingStateOn(final boolean e)
'''
pass
def getBlinkingObjectOwner():
'''public IlvBlinkingObjectOwner getBlinkingObjectOwner()
'''
pass
def setToolTipText():
'''public void setToolTipText(final String s)
'''
pass
def getToolTipText():
'''public String getToolTipText()
public String getToolTipText(final IlvPoint ilvPoint, final IlvTransformer ilvTransformer)
'''
pass
def setToolTipBaseTextDirection():
'''public void setToolTipBaseTextDirection(final int value)
'''
pass
def getToolTipBaseTextDirection():
'''public int getToolTipBaseTextDirection()
'''
pass
def setPopupMenu():
'''public void setPopupMenu(final JPopupMenu popupMenu)
'''
pass
def getPopupMenu():
'''public JPopupMenu getPopupMenu()
public JPopupMenu getPopupMenu(final IlvPoint ilvPoint, final IlvTransformer ilvTransformer, final IlvManagerView ilvManagerView, final IlvPopupMenuManager ilvPopupMenuManager)
'''
pass
def setPopupMenuName():
'''public void setPopupMenuName(final String s)
'''
pass
def getPopupMenuName():
'''public String getPopupMenuName()
'''
pass
def getLocale():
'''public final Locale getLocale()
'''
pass
def getULocale():
'''public ULocale getULocale()
'''
pass
def isLocaleSensitive():
'''public boolean isLocaleSensitive()
'''
pass
def localeChanged():
'''public void localeChanged(final ULocale uLocale, final ULocale uLocale2)
'''
pass
def getComponentOrientation():
'''public ComponentOrientation getComponentOrientation()
'''
pass
def isComponentOrientationSensitive():
'''public boolean isComponentOrientationSensitive()
'''
pass
def componentOrientationChanged():
'''public void componentOrientationChanged(final ComponentOrientation componentOrientation, final ComponentOrientation componentOrientation2)
'''
pass
def setBaseTextDirection():
'''public void setBaseTextDirection(final int n)
'''
pass
def getBaseTextDirection():
'''public int getBaseTextDirection()
'''
pass
def getResolvedBaseTextDirection():
'''public int getResolvedBaseTextDirection()
'''
pass
def isBaseTextDirectionSensitive():
'''public boolean isBaseTextDirectionSensitive()
'''
pass
def usesBidiMarkers():
'''public boolean usesBidiMarkers()
'''
pass
def baseTextDirectionChanged():
'''public void baseTextDirectionChanged(final int n, final int n2)
'''
pass
def addNamedPropertyListener():
'''public void addNamedPropertyListener(final NamedPropertyListener l)
'''
pass
def removeNamedPropertyListener():
'''public void removeNamedPropertyListener(final NamedPropertyListener l)
'''
pass
def setNamedProperty():
'''public IlvNamedProperty setNamedProperty(final IlvNamedProperty value)
'''
pass
def getNamedProperty():
'''public IlvNamedProperty getNamedProperty(final String key)
'''
pass
def removeNamedProperty():
'''public void removeNamedProperty(final String key)
'''
pass
def isInApplyToObject():
'''public final boolean isInApplyToObject()
'''
pass
def setInApplyToObject():
'''public final boolean setInApplyToObject(final boolean b)
'''
pass
def apply():
'''public void apply(final IlvGraphic ilvGraphic, final Object o)
'''
pass
def viewChanged():
'''public void viewChanged(final ManagerViewsChangedEvent managerViewsChangedEvent)
'''
pass
