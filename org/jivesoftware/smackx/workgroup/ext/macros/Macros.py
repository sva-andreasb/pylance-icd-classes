ELEMENT_NAME = "String  \"macros\""
NAMESPACE = "String  \"http://jivesoftware.com/protocol/workgroup\""
def ():
    '''returns Macros\n\n
    ()\n
    '''
def getRootGroup():
    '''returns MacroGroup\n\n
    getRootGroup()\n
    '''
def setRootGroup():
    '''returns None\n\n
    setRootGroup(final MacroGroup rootGroup)\n
    '''
def isPersonal():
    '''returns boolean\n\n
    isPersonal()\n
    '''
def setPersonal():
    '''returns None\n\n
    setPersonal(final boolean personal)\n
    '''
def getPersonalMacroGroup():
    '''returns MacroGroup\n\n
    getPersonalMacroGroup()\n
    '''
def setPersonalMacroGroup():
    '''returns None\n\n
    setPersonalMacroGroup(final MacroGroup personalMacroGroup)\n
    '''
def parse():
    '''returns Macros\n\n
    parse(final XmlPullParser parser, final int initialDepth)\n
    '''
def parseMacro():
    '''returns Macro\n\n
    parseMacro(final XmlPullParser parser)\n
    '''
def parseMacroGroup():
    '''returns MacroGroup\n\n
    parseMacroGroup(final XmlPullParser parser)\n
    '''
def parseMacroGroups():
    '''returns MacroGroup\n\n
    parseMacroGroups(final String macros)\n
    '''
