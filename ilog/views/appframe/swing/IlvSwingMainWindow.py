ICON_ATTRIBUTE = "String  \"icon\""
SWING_MAIN_WINDOW_SETTINGS_TYPE = "String  \"mdiMainFrame\""
DEFAULT_SETTINGS_NAME = "String  \"Default\""
SHOW_STATUS_BAR_ATTRIBUTE = "String  \"showStatusBar\""
SHOW_HIDE_STATUS_BAR_CMD = "String  \"showHideStatusBar\""
def ():
    '''returns DockingArea\n\n
    (final JFrame frame, final boolean b, final boolean b2)\n
    (final JFrame frame)\n
    (final Container container, final boolean b, final boolean b2)\n
    (final Container container)\n
    (final IlvSwingMainWindow a)\n
    '''
def getFrame():
    '''returns JFrame\n\n
    getFrame()\n
    '''
def setFrame():
    '''returns None\n\n
    setFrame(final JFrame frame)\n
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
def windowClosing():
    '''returns None\n\n
    windowClosing(final WindowEvent windowEvent)\n
    '''
def setContainer():
    '''returns None\n\n
    setContainer(Container j)\n
    '''
def getContainer():
    '''returns Container\n\n
    getContainer()\n
    '''
def getApplication():
    '''returns IlvApplication\n\n
    getApplication()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def registerStaticContainer():
    '''returns None\n\n
    registerStaticContainer(final String s, final IlvViewContainer ilvViewContainer)\n
    '''
def unregisterStaticContainer():
    '''returns boolean\n\n
    unregisterStaticContainer(final IlvViewContainer ilvViewContainer)\n
    '''
def containerActivated():
    '''returns None\n\n
    containerActivated(final IlvViewContainer ilvViewContainer)\n
    '''
def setMDIClientParent():
    '''returns None\n\n
    setMDIClientParent(final Container j)\n
    '''
def getMDIClientParent():
    '''returns Container\n\n
    getMDIClientParent()\n
    '''
def setMDIClient():
    '''returns None\n\n
    setMDIClient(final IlvMDIClient l)\n
    '''
def getMDIClient():
    '''returns IlvMDIClient\n\n
    getMDIClient()\n
    '''
def getActiveViewContainer():
    '''returns IlvViewContainer\n\n
    getActiveViewContainer()\n
    '''
def getMainBars():
    '''returns Object[]\n\n
    getMainBars()\n
    '''
def setApplication():
    '''returns None\n\n
    setApplication(final IlvApplication application)\n
    '''
def propertyChange():
    '''returns None\n\n
    propertyChange(final PropertyChangeEvent propertyChangeEvent)\n
    '''
def isProcessingAction():
    '''returns boolean\n\n
    isProcessingAction(final String s)\n
    '''
def updateAction():
    '''returns boolean\n\n
    updateAction(final Action action)\n
    '''
def actionPerformed():
    '''returns None\n\n
    actionPerformed(final ActionEvent actionEvent)\n
    '''
def localeSettingsChanged():
    '''returns None\n\n
    localeSettingsChanged(final LocaleSettingsEvent localeSettingsEvent)\n
    '''
def getSettingsType():
    '''returns String\n\n
    getSettingsType()\n
    '''
def setSettingsType():
    '''returns None\n\n
    setSettingsType(final String s)\n
    '''
def getSettingsName():
    '''returns String\n\n
    getSettingsName()\n
    '''
def setSettingsName():
    '''returns None\n\n
    setSettingsName(final String w)\n
    '''
def setSettingsQuery():
    '''returns None\n\n
    setSettingsQuery(final IlvSettingsQuery settingsQuery)\n
    '''
def getSettingsQuery():
    '''returns IlvSettingsQuery\n\n
    getSettingsQuery()\n
    '''
def setSettingsElement():
    '''returns None\n\n
    setSettingsElement(final IlvSettingsElement settingsElement)\n
    '''
def getSettingsElement():
    '''returns IlvSettingsElement\n\n
    getSettingsElement()\n
    '''
def getSettings():
    '''returns IlvSettings\n\n
    getSettings()\n
    '''
def setSettings():
    '''returns None\n\n
    setSettings(final IlvSettings settings)\n
    '''
def readSettings():
    '''returns None\n\n
    readSettings(final IlvSettingsElement ilvSettingsElement)\n
    readSettings(final IlvSettingsElement ilvSettingsElement, final Object o)\n
    '''
def writeSettings():
    '''returns None\n\n
    writeSettings(final IlvSettingsElement ilvSettingsElement)\n
    writeSettings(final IlvSettingsElement ilvSettingsElement, final Object o)\n
    '''
def getStatusBar():
    '''returns IlvStatusBar\n\n
    getStatusBar()\n
    '''
def setSettingsSerializer():
    '''returns None\n\n
    setSettingsSerializer(final IlvSettingsSerializer r)\n
    '''
def setStatusBarVisible():
    '''returns None\n\n
    setStatusBarVisible(final boolean b)\n
    '''
def isStatusBarVisible():
    '''returns boolean\n\n
    isStatusBarVisible()\n
    '''
def registerActionMethod():
    '''returns None\n\n
    registerActionMethod(final String s, final String s2)\n
    '''
def registerActionStateMethod():
    '''returns None\n\n
    registerActionStateMethod(final String s, final String s2)\n
    '''
def setFileChooserHTMLPage():
    '''returns None\n\n
    setFileChooserHTMLPage(final URL ac)\n
    '''
def getFileChooserHTMLPage():
    '''returns URL\n\n
    getFileChooserHTMLPage()\n
    '''
def setFileChooserChoices():
    '''returns None\n\n
    setFileChooserChoices(final URL[] array)\n
    '''
def getFileChooserChoices():
    '''returns URL[]\n\n
    getFileChooserChoices()\n
    '''
def applicationEventReceived():
    '''returns None\n\n
    applicationEventReceived(final ApplicationEvent applicationEvent)\n
    '''
def getDockingArea():
    '''returns IlvDockingArea\n\n
    getDockingArea()\n
    '''
def getDockingBarArea():
    '''returns IlvDockingBarArea\n\n
    getDockingBarArea()\n
    '''
def getApplet():
    '''returns Applet\n\n
    getApplet()\n
    '''
def setMDIPane():
    '''returns None\n\n
    setMDIPane(final String mdiPane)\n
    '''
def setDockableComponent():
    '''returns boolean\n\n
    setDockableComponent(final String anObject, final Component c)\n
    '''
def getDockableComponent():
    '''returns Component\n\n
    getDockableComponent(final String anObject)\n
    '''
