SMALL_ICONS = "int  0"
BIG_ICONS = "int  1"
ACTION_APPLICATION = "String  application""
ACTION_PROCESSED_IN_NEW_THREAD = "String  newThread""
ACTION_AUTOMATIC = "String  automatic""
ACTION_UPDATE_AFTER_PROCESSING = "String  updateAfterProcessing""
DOUBLE_CLICK_ACTION = "String  doubleClickAction""
ACTION_LIST = "String  isList""
ACTION_LIST_ITEMS = "String  listItems""
ACTION_LIST_IN_SUBMENU = "String  listInSubmenu""
ACTION_LIST_MENU_MAXLENGTH = "String  listMenuMaxLength""
ACTION_LIST_SELECTION = "String  listSelection""
ACTION_LIST_MENU_USENUMBERING = "String  listMenuNumbering""
ACTION_LIST_MENU_FIRSTNUMBER = "String  listMenuFirstNumber""
ACTION_LIST_MENU_EMPTYSTRING = "String  listMenuEmptyString""
ACTION_LIST_CHECK_SELECTION = "String  listCheckSelection""
ACTION_LIST_DYNAMIC_CONTENT = "String  listMenuDynamicContent""
ACTION_CHECKABLE = "String  checkable""
ACTION_CHECK_STATE = "String  check""
ACTION_CHECK_GROUP = "String  checkGroup""
ACTION_CHECK_ONE_SHOT = "String  oneShot""
ACTION_LOCK_ON_DOUBLECLICK = "String  lockOnDoubleClick""
ACTION_CHECK_LOOK = "String  checkLook""
ACTION_CHECKED_ICON = "String  checkedIcon""
ACTION_UNCHECKED_ICON = "String  uncheckedIcon""
ACTION_DEPENDING_ACTIONS = "String  dependingActions""
ACTION_ACCELERATOR_LIST = "String  accelerators""
def actionPerformed():
'''public void actionPerformed(final ActionEvent actionEvent)
public void actionPerformed(final ActionEvent actionEvent)
public void actionPerformed(final ActionEvent actionEvent)
'''
pass
def readSettings():
'''public void readSettings(final IlvSettingsElement ilvSettingsElement, final IlvApplication newValue)
'''
pass
def HasCategory():
'''public static boolean HasCategory(final Action action, final String anObject)
'''
pass
def GetCategories():
'''public static String[] GetCategories(final Action action)
'''
pass
def SetSelectionIndex():
'''public static void SetSelectionIndex(final Action action, final int value)
'''
pass
def SetSelectedItem():
'''public static void SetSelectedItem(final Action action, final Object o)
'''
pass
def GetSelectionIndex():
'''public static int GetSelectionIndex(final Action action)
'''
pass
def GetSelectedItem():
'''public static Object GetSelectedItem(final Action action)
'''
pass
def GetListItems():
'''public static Object[] GetListItems(final Action action)
'''
pass
def SetListItems():
'''public static void SetListItems(final Action action, final Object[] array)
'''
pass
def IsListMenuNumbering():
'''public static boolean IsListMenuNumbering(final Action action)
'''
pass
def IsAutomatic():
'''public static boolean IsAutomatic(final Action action)
'''
pass
def SetAutomatic():
'''public static boolean SetAutomatic(final Action action, final boolean b)
'''
pass
def IsActionList():
'''public static boolean IsActionList(final Action action)
'''
pass
def getApplication():
'''public IlvApplication getApplication()
'''
pass
def SetAction():
'''public static void SetAction(final Component component, final Action action, final IlvApplication ilvApplication)
public static void SetAction(final AbstractButton abstractButton, final Action action, final IlvApplication ilvApplication, final int value)
'''
pass
def propertyChange():
'''public void propertyChange(final PropertyChangeEvent propertyChangeEvent)
public void propertyChange(final PropertyChangeEvent propertyChangeEvent)
public void propertyChange(final PropertyChangeEvent propertyChangeEvent)
'''
pass
def mouseClicked():
'''public void mouseClicked(final MouseEvent mouseEvent)
'''
pass
def mouseEntered():
'''public void mouseEntered(final MouseEvent mouseEvent)
'''
pass
def mouseExited():
'''public void mouseExited(final MouseEvent mouseEvent)
'''
pass
def mousePressed():
'''public void mousePressed(final MouseEvent mouseEvent)
'''
pass
def mouseReleased():
'''public void mouseReleased(final MouseEvent mouseEvent)
'''
pass
def UpdateButtonProperties():
'''public static void UpdateButtonProperties(final AbstractButton abstractButton, final IlvApplication ilvApplication)
'''
pass
def SetChecked():
'''public static void SetChecked(final Action action, final boolean b)
public static void SetChecked(final Component component, final Action action, final boolean b)
'''
pass
def IsChecked():
'''public static boolean IsChecked(final Action action)
'''
pass
def ActionProcessTerminated():
'''public static void ActionProcessTerminated(final Action action)
'''
pass
def GetGroup():
'''public static String GetGroup(final Action action)
'''
pass
def GetSelectedGroupAction():
'''public static Action GetSelectedGroupAction(final IlvApplication ilvApplication, final String s)
'''
pass
def LockAction():
'''public static void LockAction(final Action action)
'''
pass
def UnlockAction():
'''public static void UnlockAction(final Action action)
'''
pass
def IsActionLocked():
'''public static boolean IsActionLocked(final Action action)
'''
pass
def RegisterActionInGroup():
'''public static void RegisterActionInGroup(final Action action, final Component component)
'''
pass
def UnregisterActionInGroup():
'''public static void UnregisterActionInGroup(final Component component)
'''
pass
def GetMnemonic():
'''public static char GetMnemonic(final Action action, final IlvApplication ilvApplication)
'''
pass
def AcceleratorFromString():
'''public static KeyStroke AcceleratorFromString(final String s)
'''
pass
def AcceleratorToString():
'''public static String AcceleratorToString(final KeyStroke keyStroke)
'''
pass
def DynActionPopupListener():
'''public DynActionPopupListener(final Action a, final IlvApplication b, final JPopupMenu c)
'''
pass
def popupMenuWillBecomeVisible():
'''public void popupMenuWillBecomeVisible(final PopupMenuEvent popupMenuEvent)
'''
pass
def popupMenuWillBecomeInvisible():
'''public void popupMenuWillBecomeInvisible(final PopupMenuEvent popupMenuEvent)
'''
pass
def popupMenuCanceled():
'''public void popupMenuCanceled(final PopupMenuEvent popupMenuEvent)
'''
pass
def ActionCheckListener():
'''public ActionCheckListener(final Component a, final Action b)
'''
pass
def ActionListListener():
'''public ActionListListener(final Component a, final Action c, final IlvApplication b)
'''
pass
def fill():
'''public void fill(final Object[] array, final Object[] array2)
'''
pass
def GetComponentIndex():
'''public static int GetComponentIndex(final Container container, final Component component)
'''
pass
def valueChanged():
'''public void valueChanged(final ListSelectionEvent listSelectionEvent)
'''
pass
