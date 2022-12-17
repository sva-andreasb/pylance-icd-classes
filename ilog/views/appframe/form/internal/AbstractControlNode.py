def getFormReaderContext():
    '''returns IlvFormReaderContext\n\n
    getFormReaderContext()\n
    '''
def setFormReaderContext():
    '''returns None\n\n
    setFormReaderContext(final IlvFormReaderContext h)\n
    '''
def getParent():
    '''returns AbstractControlNode\n\n
    getParent()\n
    '''
def setParent():
    '''returns None\n\n
    setParent(final AbstractControlNode a)\n
    '''
def addChild():
    '''returns None\n\n
    addChild(final AbstractControlNode abstractControlNode, final Object o, final int n)\n
    '''
def removeChild():
    '''returns boolean\n\n
    removeChild(final AbstractControlNode abstractControlNode)\n
    '''
def getControlNode():
    '''returns AbstractControlNode\n\n
    getControlNode(final int n)\n
    '''
def getControlNodeCount():
    '''returns int\n\n
    getControlNodeCount()\n
    '''
def putProperty():
    '''returns None\n\n
    putProperty(final String s, final Object o, final IlvServicesProvider ilvServicesProvider)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String s)\n
    '''
def putPropertyAsText():
    '''returns None\n\n
    putPropertyAsText(final String s, final String s2, final IlvServicesProvider ilvServicesProvider)\n
    '''
def getPropertyAsText():
    '''returns String\n\n
    getPropertyAsText(final String s)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String c)\n
    '''
def createControl():
    '''returns Object\n\n
    createControl(final IlvForm ilvForm, final String s, final Object o, final Class clazz, final Element element)\n
    '''
def getForm():
    '''returns IlvForm\n\n
    getForm()\n
    '''
def setForm():
    '''returns None\n\n
    setForm(final IlvForm f)\n
    '''
def getServicesProvider():
    '''returns IlvServicesProvider\n\n
    getServicesProvider()\n
    '''
def addControlListener():
    '''returns None\n\n
    addControlListener(final Class clazz, final ControlListener controlListener)\n
    '''
def removeControlListener():
    '''returns None\n\n
    removeControlListener(final Class clazz, final ControlListener controlListener)\n
    '''
def getAssociatedLabel():
    '''returns Object\n\n
    getAssociatedLabel()\n
    '''
def setAssociatedLabel():
    '''returns None\n\n
    setAssociatedLabel(final Object g)\n
    '''
def setEnabled():
    '''returns None\n\n
    setEnabled(final boolean b)\n
    '''
def isEnabled():
    '''returns boolean\n\n
    isEnabled()\n
    '''
def putLocalizedProperty():
    '''returns None\n\n
    putLocalizedProperty(final String key, final Object value)\n
    '''
def localeChanged():
    '''returns None\n\n
    localeChanged(final Locale locale)\n
    '''
def getFormServices():
    '''returns IlvServicesProvider\n\n
    getFormServices()\n
    '''
