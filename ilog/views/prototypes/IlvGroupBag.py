NO_LOCAL_REDRAW = "int  0"
LOCAL_REDRAW_FOR_ANIMATIONS = "int  1"
LOCAL_REDRAW_FOR_ALL = "int  2"
def ():
    '''returns IlvGroupBag\n\n
    ()\n
    (final IlvManager manager)\n
    '''
def setManager():
    '''returns None\n\n
    setManager(final IlvManager a)\n
    '''
def getManager():
    '''returns IlvManager\n\n
    getManager()\n
    '''
def addValueSource():
    '''returns None\n\n
    addValueSource(final IlvValueSource ilvValueSource)\n
    '''
def removeValueSource():
    '''returns None\n\n
    removeValueSource(final IlvValueSource obj)\n
    '''
def removeAllValueSources():
    '''returns None\n\n
    removeAllValueSources()\n
    '''
def getValueSources():
    '''returns Enumeration\n\n
    getValueSources()\n
    '''
def getValueSource():
    '''returns IlvValueSource\n\n
    getValueSource(final String anObject)\n
    '''
def addGroup():
    '''returns None\n\n
    addGroup(final IlvGroup ilvGroup)\n
    '''
def removeGroup():
    '''returns None\n\n
    removeGroup(final IlvGroup obj)\n
    '''
def replaceGroup():
    '''returns None\n\n
    replaceGroup(final IlvGroup o, final IlvGroup obj)\n
    '''
def removeAllGroups():
    '''returns None\n\n
    removeAllGroups()\n
    '''
def getGroups():
    '''returns Enumeration\n\n
    getGroups()\n
    '''
def getGroupCount():
    '''returns int\n\n
    getGroupCount()\n
    '''
def getGroup():
    '''returns IlvGroup\n\n
    getGroup(final String anObject)\n
    '''
def selectGroup():
    '''returns None\n\n
    selectGroup(final IlvGroup ilvGroup, final boolean b)\n
    selectGroup(final IlvGroup ilvGroup, final IlvGroupFrame ilvGroupFrame, final boolean b)\n
    '''
def deSelectGroup():
    '''returns None\n\n
    deSelectGroup(final IlvGroup ilvGroup, final boolean b)\n
    '''
def getSelectedGroups():
    '''returns Enumeration\n\n
    getSelectedGroups()\n
    '''
def deSelectAllGroups():
    '''returns None\n\n
    deSelectAllGroups(final boolean b)\n
    '''
def isSelected():
    '''returns boolean\n\n
    isSelected(final IlvGroup ilvGroup)\n
    '''
def addLibrary():
    '''returns None\n\n
    addLibrary(final IlvPrototypeLibrary ilvPrototypeLibrary)\n
    '''
def removeLibrary():
    '''returns None\n\n
    removeLibrary(final IlvPrototypeLibrary obj)\n
    '''
def getLibraries():
    '''returns Enumeration\n\n
    getLibraries()\n
    '''
def setGroupSelectionEnabled():
    '''returns None\n\n
    setGroupSelectionEnabled(final boolean f)\n
    '''
def isGroupSelectionEnabled():
    '''returns boolean\n\n
    isGroupSelectionEnabled()\n
    '''
def setLocalRedraw():
    '''returns None\n\n
    setLocalRedraw(final int g)\n
    '''
def getLocalRedraw():
    '''returns int\n\n
    getLocalRedraw()\n
    '''
