FOCUS_MANAGER_PROPERTY = "String  \"focusManager\""
FOCUS_LISTENER_INSTALLED = "int  1"
ROUTER_LISTENER_INSTALLED = "int  2"
ACTIVABLE_PROPERTY = "String  \"ActivableByClick\""
def addFocusListener():
    '''returns int\n\n
    addFocusListener(final Component component, final IlvViewContainer ilvViewContainer)\n
    addFocusListener(final Component key, final FocusRouter focusRouter, final ContainerListener containerListener)\n
    '''
def stateChanged():
    '''returns None\n\n
    stateChanged(final ChangeEvent changeEvent)\n
    '''
def internalFrameActivated():
    '''returns None\n\n
    internalFrameActivated(final InternalFrameEvent internalFrameEvent)\n
    '''
def removeFocusListener():
    '''returns None\n\n
    removeFocusListener(final Component component)\n
    '''
def setActivable():
    '''returns None\n\n
    setActivable(final JComponent component, final boolean b)\n
    '''
def isActivable():
    '''returns boolean\n\n
    isActivable(final Component o)\n
    '''
def propertyChange():
    '''returns None\n\n
    propertyChange(final PropertyChangeEvent propertyChangeEvent)\n
    '''
def setComponentFocus():
    '''returns None\n\n
    setComponentFocus(Component getFirstFocusableComponent)\n
    '''
def setActiveClosestView():
    '''returns None\n\n
    setActiveClosestView(final Component component, final Container container)\n
    '''
def isLocked():
    '''returns boolean\n\n
    isLocked()\n
    '''
def lock():
    '''returns None\n\n
    lock()\n
    '''
def unlock():
    '''returns None\n\n
    unlock()\n
    '''
def evaluate():
    '''returns boolean\n\n
    evaluate(final Object o)\n
    '''
def addFilterListener():
    '''returns None\n\n
    addFilterListener(final FilterListener filterListener)\n
    '''
def removeFilterListener():
    '''returns None\n\n
    removeFilterListener(final FilterListener filterListener)\n
    '''
def focusGained():
    '''returns None\n\n
    focusGained(final FocusEvent focusEvent)\n
    '''
def focusLost():
    '''returns None\n\n
    focusLost(final FocusEvent focusEvent)\n
    '''
def ():
    '''returns FocusRouter\n\n
    (final IlvFocusManager b, final FocusRouter a)\n
    (final IlvViewContainer a, final Component b)\n
    '''
def componentAdded():
    '''returns None\n\n
    componentAdded(final ContainerEvent containerEvent)\n
    '''
def componentRemoved():
    '''returns None\n\n
    componentRemoved(final ContainerEvent containerEvent)\n
    '''
def mousePressed():
    '''returns None\n\n
    mousePressed(final MouseEvent mouseEvent)\n
    '''
def componentActivated():
    '''returns None\n\n
    componentActivated(final Component component)\n
    '''
