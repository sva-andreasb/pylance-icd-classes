CONTENT_PANE_PROPERTY = "String  \"contentPane\""
LAYERED_PANE_PROPERTY = "String  \"layeredPane\""
ROOT_PANE_PROPERTY = "String  \"rootPane\""
GLASS_PANE_PROPERTY = "String  \"glassPane\""
TITLE_PROPERTY = "String  \"title\""
ICON_PROPERTY = "String  \"icon\""
TAB_ICON_PROPERTY = "String  \"tabIcon\""
TOOLTIP_PROPERTY = "String  \"tooltip\""
PINABLE_PROPERTY = "String  \"pinable\""
CLOSABLE_PROPERTY = "String  \"closable\""
DOCKABLE_PROPERTY = "String  \"dockable\""
SCROLLABLE_PROPERTY = "String  \"scrollable\""
TITLE_VISIBLE_PROPERTY = "String  \"titleVisible\""
FIXED_WIDTH_PROPERTY = "String  \"fixedWidth\""
FIXED_HEIGHT_PROPERTY = "String  \"fixedHeight\""
PIN_STATE_PROPERTY = "String  \"pinState\""
MINIMUM_SIZE_PROPERTY = "String  \"minimumSize\""
WORKSPACE_DISPLAYED_NAME_PROPERTY = "String  \"WorkspaceDisplayedName\""
WORKSPACE_ICON_PROPERTY = "String  \"WorkspaceIcon\""
WORKSPACE_DESCRIPTION_PROPERTY = "String  \"WorkspaceDescription\""
WORKSPACE_TOOLTIP_PROPERTY = "String  \"WorkspaceTooltip\""
WORKSPACE_ACTION_COMMAND_PROPERTY = "String  \"WorkspaceActionCommand\""
WORKSPACE_WRITABLE_PROPERTY = "String  \"WorkspaceWritable\""
def ():
    '''returns DockableVisibilityActionHandler\n\n
    ()\n
    (final String s, final String a)\n
    (final String a, final String b)\n
    '''
def actionPerformed():
    '''returns None\n\n
    actionPerformed(final ActionEvent actionEvent)\n
    actionPerformed(final ActionEvent actionEvent)\n
    actionPerformed(final ActionEvent actionEvent)\n
    actionPerformed(final ActionEvent actionEvent)\n
    actionPerformed(final ActionEvent actionEvent)\n
    actionPerformed(final ActionEvent actionEvent)\n
    '''
def setLayout():
    '''returns None\n\n
    setLayout(final LayoutManager layout)\n
    '''
def getContentPane():
    '''returns Container\n\n
    getContentPane()\n
    '''
def setContentPane():
    '''returns None\n\n
    setContentPane(final Container container)\n
    '''
def getLayeredPane():
    '''returns JLayeredPane\n\n
    getLayeredPane()\n
    '''
def setLayeredPane():
    '''returns None\n\n
    setLayeredPane(final JLayeredPane layeredPane)\n
    '''
def getGlassPane():
    '''returns Component\n\n
    getGlassPane()\n
    '''
def setGlassPane():
    '''returns None\n\n
    setGlassPane(final Component component)\n
    '''
def getRootPane():
    '''returns JRootPane\n\n
    getRootPane()\n
    '''
def getApplication():
    '''returns IlvApplication\n\n
    getApplication()\n
    '''
def setApplication():
    '''returns None\n\n
    setApplication(final IlvApplication g)\n
    '''
def setWorkspaceConfiguration():
    '''returns None\n\n
    setWorkspaceConfiguration(final String s)\n
    '''
def getWorkspaceConfiguration():
    '''returns String\n\n
    getWorkspaceConfiguration()\n
    '''
def duplicateWorkspaceConfiguration():
    '''returns boolean\n\n
    duplicateWorkspaceConfiguration(final String s, final String s2)\n
    '''
def readWorkspaceConfiguration():
    '''returns None\n\n
    readWorkspaceConfiguration(final String s, final IlvSettingsElement ilvSettingsElement)\n
    '''
def writeWorkspaceConfiguration():
    '''returns None\n\n
    writeWorkspaceConfiguration(final String s, final IlvSettingsElement ilvSettingsElement)\n
    '''
def removeWorkspaceConfiguration():
    '''returns boolean\n\n
    removeWorkspaceConfiguration(final String s)\n
    '''
def getWorkspaceProperty():
    '''returns Object\n\n
    getWorkspaceProperty(final String s, final String s2)\n
    '''
def setWorkspaceProperty():
    '''returns None\n\n
    setWorkspaceProperty(final String s, final String s2, final Object o)\n
    '''
def addWorkspacePropertyChangeListener():
    '''returns None\n\n
    addWorkspacePropertyChangeListener(final String s, final PropertyChangeListener propertyChangeListener)\n
    '''
def removeWorkspacePropertyChangeListener():
    '''returns None\n\n
    removeWorkspacePropertyChangeListener(final String s, final PropertyChangeListener propertyChangeListener)\n
    '''
def getWorkspaceConfigurations():
    '''returns String[]\n\n
    getWorkspaceConfigurations()\n
    '''
def setWorkspaceActivationAction():
    '''returns None\n\n
    setWorkspaceActivationAction(final String s, final String s2)\n
    '''
def setDockableComponent():
    '''returns boolean\n\n
    setDockableComponent(final String s, final Component component)\n
    '''
def setDockableProperties():
    '''returns None\n\n
    setDockableProperties(final String s, final String s2, final String s3, final ImageIcon imageIcon, final ImageIcon imageIcon2)\n
    '''
def setDockableProperty():
    '''returns Object\n\n
    setDockableProperty(final String s, final String s2, final Object o)\n
    '''
def getDockableProperty():
    '''returns Object\n\n
    getDockableProperty(final String s, final String s2)\n
    '''
def getDockableComponent():
    '''returns Component\n\n
    getDockableComponent(final String s)\n
    '''
def getDockableView():
    '''returns IlvDocumentView\n\n
    getDockableView(final String s)\n
    '''
def getActiveDockable():
    '''returns IlvDockable\n\n
    getActiveDockable()\n
    '''
def setActiveDockable():
    '''returns None\n\n
    setActiveDockable(final IlvDockable ilvDockable)\n
    setActiveDockable(final String s)\n
    '''
def getActiveDockableName():
    '''returns String\n\n
    getActiveDockableName()\n
    '''
def addDockingListener():
    '''returns None\n\n
    addDockingListener(final DockingListener dockingListener)\n
    '''
def removeDockingListener():
    '''returns boolean\n\n
    removeDockingListener(final DockingListener dockingListener)\n
    '''
def lockUpdate():
    '''returns None\n\n
    lockUpdate()\n
    '''
def unlockUpdate():
    '''returns None\n\n
    unlockUpdate()\n
    '''
def getDockable():
    '''returns IlvDockable\n\n
    getDockable(final String s)\n
    '''
def isDockableVisible():
    '''returns boolean\n\n
    isDockableVisible(final String s)\n
    '''
def setDockableVisible():
    '''returns None\n\n
    setDockableVisible(final String s, final boolean b)\n
    '''
def isDockableDocked():
    '''returns boolean\n\n
    isDockableDocked(final String s)\n
    '''
def dock():
    '''returns None\n\n
    dock(final String s)\n
    dock(final String s, final int n, final double n2)\n
    '''
def split():
    '''returns boolean\n\n
    split(final String s, final String s2, final int n, final double n2)\n
    '''
def addTab():
    '''returns boolean\n\n
    addTab(final String s, final String s2, final boolean b)\n
    addTab(final String s, final String s2, final boolean b, final boolean b2)\n
    '''
def undock():
    '''returns None\n\n
    undock(final String s)\n
    undock(final String s, final Point point)\n
    '''
def isDockableUndocked():
    '''returns boolean\n\n
    isDockableUndocked(final String s)\n
    '''
def getFloatingLocation():
    '''returns Point\n\n
    getFloatingLocation(final String s)\n
    '''
def setDockableVisibilityAction():
    '''returns None\n\n
    setDockableVisibilityAction(final String s, final String s2)\n
    '''
def setMDIPane():
    '''returns None\n\n
    setMDIPane(final String c)\n
    '''
def getMDIPane():
    '''returns String\n\n
    getMDIPane()\n
    '''
def setInnerSensibilityMargin():
    '''returns None\n\n
    setInnerSensibilityMargin(final int n)\n
    '''
def getInnerSensibilityMargin():
    '''returns int\n\n
    getInnerSensibilityMargin()\n
    '''
def setOuterSensibilityMargin():
    '''returns None\n\n
    setOuterSensibilityMargin(final int n)\n
    '''
def getOuterSensibilityMargin():
    '''returns int\n\n
    getOuterSensibilityMargin()\n
    '''
def removeDockable():
    '''returns boolean\n\n
    removeDockable(final String s)\n
    '''
def getDefaultCloseActionListener():
    '''returns ActionListener\n\n
    getDefaultCloseActionListener()\n
    '''
def setCloseActionListener():
    '''returns None\n\n
    setCloseActionListener(final String s, final ActionListener actionListener)\n
    setCloseActionListener(final ActionListener closeActionListener)\n
    '''
def getDefaultPinActionListener():
    '''returns ActionListener\n\n
    getDefaultPinActionListener()\n
    '''
def setPinActionListener():
    '''returns None\n\n
    setPinActionListener(final String s, final ActionListener actionListener)\n
    setPinActionListener(final ActionListener pinActionListener)\n
    '''
def updateComponentTreeUI():
    '''returns None\n\n
    updateComponentTreeUI()\n
    '''
def setCursor():
    '''returns None\n\n
    setCursor(final Cursor cursor)\n
    '''
def setDefaultFloatingMinimumSize():
    '''returns None\n\n
    setDefaultFloatingMinimumSize(final Dimension defaultFloatingMinimumSize)\n
    '''
def getDefaultFloatingMinimumSize():
    '''returns Dimension\n\n
    getDefaultFloatingMinimumSize(final Dimension dimension)\n
    '''
def setDefaultFloatingMaximumSize():
    '''returns None\n\n
    setDefaultFloatingMaximumSize(final Dimension defaultFloatingMaximumSize)\n
    '''
def getDefaultFloatingMaximumSize():
    '''returns Dimension\n\n
    getDefaultFloatingMaximumSize(final Dimension dimension)\n
    '''
def setUsingPreferredSize():
    '''returns None\n\n
    setUsingPreferredSize(final boolean usingPreferredSize)\n
    '''
def isUsingPreferredSize():
    '''returns boolean\n\n
    isUsingPreferredSize()\n
    '''
def isReadUserSettings():
    '''returns boolean\n\n
    isReadUserSettings()\n
    '''
def setReadUserSettings():
    '''returns None\n\n
    setReadUserSettings(final boolean f)\n
    '''
def isWriteUserSettings():
    '''returns boolean\n\n
    isWriteUserSettings()\n
    '''
def setWriteUserSettings():
    '''returns None\n\n
    setWriteUserSettings(final boolean e)\n
    '''
def setComponentOrientation():
    '''returns None\n\n
    setComponentOrientation(final ComponentOrientation componentOrientation)\n
    '''
def setAllowingDocking():
    '''returns None\n\n
    setAllowingDocking(final boolean allowingDocking)\n
    '''
def isAllowingDocking():
    '''returns boolean\n\n
    isAllowingDocking()\n
    '''
def setDockableThreshold():
    '''returns None\n\n
    setDockableThreshold(final int threshold)\n
    '''
def getDockableThreshold():
    '''returns int\n\n
    getDockableThreshold()\n
    '''
def setConstraintFloatable():
    '''returns None\n\n
    setConstraintFloatable(final boolean constraintFloatable)\n
    '''
def isConstraintFloatable():
    '''returns boolean\n\n
    isConstraintFloatable()\n
    '''
def dockingEventReceived():
    '''returns None\n\n
    dockingEventReceived(final DockingEvent dockingEvent)\n
    '''
def componentResized():
    '''returns None\n\n
    componentResized(final ComponentEvent componentEvent)\n
    '''
def componentMoved():
    '''returns None\n\n
    componentMoved(final ComponentEvent componentEvent)\n
    '''
def componentShown():
    '''returns None\n\n
    componentShown(final ComponentEvent componentEvent)\n
    '''
def componentHidden():
    '''returns None\n\n
    componentHidden(final ComponentEvent componentEvent)\n
    '''
