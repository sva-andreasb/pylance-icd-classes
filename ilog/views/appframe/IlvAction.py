SMALL_ICONS = "int  0"
BIG_ICONS = "int  1"
ACTION_APPLICATION = "String  \"application\""
ACTION_PROCESSED_IN_NEW_THREAD = "String  \"newThread\""
ACTION_AUTOMATIC = "String  \"automatic\""
ACTION_UPDATE_AFTER_PROCESSING = "String  \"updateAfterProcessing\""
DOUBLE_CLICK_ACTION = "String  \"doubleClickAction\""
ACTION_LIST = "String  \"isList\""
ACTION_LIST_ITEMS = "String  \"listItems\""
ACTION_LIST_IN_SUBMENU = "String  \"listInSubmenu\""
ACTION_LIST_MENU_MAXLENGTH = "String  \"listMenuMaxLength\""
ACTION_LIST_SELECTION = "String  \"listSelection\""
ACTION_LIST_MENU_USENUMBERING = "String  \"listMenuNumbering\""
ACTION_LIST_MENU_FIRSTNUMBER = "String  \"listMenuFirstNumber\""
ACTION_LIST_MENU_EMPTYSTRING = "String  \"listMenuEmptyString\""
ACTION_LIST_CHECK_SELECTION = "String  \"listCheckSelection\""
ACTION_LIST_DYNAMIC_CONTENT = "String  \"listMenuDynamicContent\""
ACTION_CHECKABLE = "String  \"checkable\""
ACTION_CHECK_STATE = "String  \"check\""
ACTION_CHECK_GROUP = "String  \"checkGroup\""
ACTION_CHECK_ONE_SHOT = "String  \"oneShot\""
ACTION_LOCK_ON_DOUBLECLICK = "String  \"lockOnDoubleClick\""
ACTION_CHECK_LOOK = "String  \"checkLook\""
ACTION_CHECKED_ICON = "String  \"checkedIcon\""
ACTION_UNCHECKED_ICON = "String  \"uncheckedIcon\""
ACTION_DEPENDING_ACTIONS = "String  \"dependingActions\""
ACTION_ACCELERATOR_LIST = "String  \"accelerators\""
def actionPerformed():
    '''    public void actionPerformed(final ActionEvent actionEvent)
    public void actionPerformed(final ActionEvent actionEvent)
    public void actionPerformed(final ActionEvent actionEvent)
    '''
def readSettings():
    '''    public void readSettings(final IlvSettingsElement ilvSettingsElement, final IlvApplication newValue)
    '''
def HasCategory():
    '''    public static boolean HasCategory(final Action action, final String anObject)
    '''
def GetCategories():
    '''    public static String[] GetCategories(final Action action)
    '''
def SetSelectionIndex():
    '''    public static void SetSelectionIndex(final Action action, final int value)
    '''
def SetSelectedItem():
    '''    public static void SetSelectedItem(final Action action, final Object o)
    '''
def GetSelectionIndex():
    '''    public static int GetSelectionIndex(final Action action)
    '''
def GetSelectedItem():
    '''    public static Object GetSelectedItem(final Action action)
    '''
def GetListItems():
    '''    public static Object[] GetListItems(final Action action)
    '''
def SetListItems():
    '''    public static void SetListItems(final Action action, final Object[] array)
    '''
def IsListMenuNumbering():
    '''    public static boolean IsListMenuNumbering(final Action action)
    '''
def IsAutomatic():
    '''    public static boolean IsAutomatic(final Action action)
    '''
def SetAutomatic():
    '''    public static boolean SetAutomatic(final Action action, final boolean b)
    '''
def IsActionList():
    '''    public static boolean IsActionList(final Action action)
    '''
def getApplication():
    '''    public IlvApplication getApplication()
    '''
def SetAction():
    '''    public static void SetAction(final Component component, final Action action, final IlvApplication ilvApplication)
    public static void SetAction(final AbstractButton abstractButton, final Action action, final IlvApplication ilvApplication, final int value)
    '''
def propertyChange():
    '''    public void propertyChange(final PropertyChangeEvent propertyChangeEvent)
    public void propertyChange(final PropertyChangeEvent propertyChangeEvent)
    public void propertyChange(final PropertyChangeEvent propertyChangeEvent)
    '''
def mouseClicked():
    '''    public void mouseClicked(final MouseEvent mouseEvent)
    '''
def mouseEntered():
    '''    public void mouseEntered(final MouseEvent mouseEvent)
    '''
def mouseExited():
    '''    public void mouseExited(final MouseEvent mouseEvent)
    '''
def mousePressed():
    '''    public void mousePressed(final MouseEvent mouseEvent)
    '''
def mouseReleased():
    '''    public void mouseReleased(final MouseEvent mouseEvent)
    '''
def UpdateButtonProperties():
    '''    public static void UpdateButtonProperties(final AbstractButton abstractButton, final IlvApplication ilvApplication)
    '''
def SetChecked():
    '''    public static void SetChecked(final Action action, final boolean b)
    public static void SetChecked(final Component component, final Action action, final boolean b)
    '''
def IsChecked():
    '''    public static boolean IsChecked(final Action action)
    '''
def ActionProcessTerminated():
    '''    public static void ActionProcessTerminated(final Action action)
    '''
def GetGroup():
    '''    public static String GetGroup(final Action action)
    '''
def GetSelectedGroupAction():
    '''    public static Action GetSelectedGroupAction(final IlvApplication ilvApplication, final String s)
    '''
def LockAction():
    '''    public static void LockAction(final Action action)
    '''
def UnlockAction():
    '''    public static void UnlockAction(final Action action)
    '''
def IsActionLocked():
    '''    public static boolean IsActionLocked(final Action action)
    '''
def RegisterActionInGroup():
    '''    public static void RegisterActionInGroup(final Action action, final Component component)
    '''
def UnregisterActionInGroup():
    '''    public static void UnregisterActionInGroup(final Component component)
    '''
def GetMnemonic():
    '''    public static char GetMnemonic(final Action action, final IlvApplication ilvApplication)
    '''
def AcceleratorFromString():
    '''    public static KeyStroke AcceleratorFromString(final String s)
    '''
def AcceleratorToString():
    '''    public static String AcceleratorToString(final KeyStroke keyStroke)
    '''
def DynActionPopupListener():
    '''    public DynActionPopupListener(final Action a, final IlvApplication b, final JPopupMenu c)
    '''
def popupMenuWillBecomeVisible():
    '''    public void popupMenuWillBecomeVisible(final PopupMenuEvent popupMenuEvent)
    '''
def popupMenuWillBecomeInvisible():
    '''    public void popupMenuWillBecomeInvisible(final PopupMenuEvent popupMenuEvent)
    '''
def popupMenuCanceled():
    '''    public void popupMenuCanceled(final PopupMenuEvent popupMenuEvent)
    '''
def ActionCheckListener():
    '''    public ActionCheckListener(final Component a, final Action b)
    '''
def ActionListListener():
    '''    public ActionListListener(final Component a, final Action c, final IlvApplication b)
    '''
def fill():
    '''    public void fill(final Object[] array, final Object[] array2)
    '''
def GetComponentIndex():
    '''    public static int GetComponentIndex(final Container container, final Component component)
    '''
def valueChanged():
    '''    public void valueChanged(final ListSelectionEvent listSelectionEvent)
    '''
