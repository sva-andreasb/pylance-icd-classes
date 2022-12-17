WRITE_MODE = "int  1"
DIFFERED_CHANGES_MODE = "int  2"
DIRECT_ACCESS_MODE = "int  4"
ONLY_SAVE_MODIFICATIONS_MODE = "int  8"
def ():
    '''returns ModelNode\n\n
    (final int c)\n
    (final IlvSettings ilvSettings, final int n)\n
    (final IlvSettings ilvSettings)\n
    ()\n
    (final String s)\n
    ()\n
    (final IlvSettings a, final String c, final IlvSettings ilvSettings, final int n)\n
    '''
def commit():
    '''returns None\n\n
    commit()\n
    commit(final IlvSettings ilvSettings)\n
    '''
def cancelModifications():
    '''returns None\n\n
    cancelModifications()\n
    cancelModifications()\n
    '''
def getWritableModel():
    '''returns IlvSettings\n\n
    getWritableModel()\n
    getWritableModel()\n
    '''
def addModel():
    '''returns None\n\n
    addModel(final IlvSettings ilvSettings, final String s)\n
    addModel(final IlvSettingsElement ilvSettingsElement, final String s)\n
    addModel(final IlvSettingsElement ilvSettingsElement)\n
    '''
def getParent():
    '''returns Object\n\n
    getParent(final Object o)\n
    '''
def getChildren():
    '''returns Object[]\n\n
    getChildren(final Object o)\n
    '''
def getAttributeValue():
    '''returns Object\n\n
    getAttributeValue(final Object o, final String s)\n
    '''
def getType():
    '''returns String\n\n
    getType(final Object o)\n
    '''
def getAttributes():
    '''returns String[]\n\n
    getAttributes(final Object o)\n
    '''
def addXMLFile():
    '''returns None\n\n
    addXMLFile(final URL url, final String s)\n
    '''
def addBeanObjects():
    '''returns None\n\n
    addBeanObjects(final Object[] array, final String s)\n
    '''
def getAllSettings():
    '''returns IlvSettings\n\n
    getAllSettings()\n
    '''
def removeModel():
    '''returns boolean\n\n
    removeModel(final IlvSettings ilvSettings)\n
    removeModel(final String s)\n
    '''
def dump():
    '''returns None\n\n
    dump()\n
    dump()\n
    '''
def getID():
    '''returns Object\n\n
    getID(final Object o)\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
def getModel():
    '''returns IlvSettings\n\n
    getModel()\n
    '''
