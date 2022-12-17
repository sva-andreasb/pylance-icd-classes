sid = "short  24"
BUILTIN_CONSOLIDATE_AREA = "byte  1"
BUILTIN_AUTO_OPEN = "byte  2"
BUILTIN_AUTO_CLOSE = "byte  3"
BUILTIN_DATABASE = "byte  4"
BUILTIN_CRITERIA = "byte  5"
BUILTIN_PRINT_AREA = "byte  6"
BUILTIN_PRINT_TITLE = "byte  7"
BUILTIN_RECORDER = "byte  8"
BUILTIN_DATA_FORM = "byte  9"
BUILTIN_AUTO_ACTIVATE = "byte  10"
BUILTIN_AUTO_DEACTIVATE = "byte  11"
BUILTIN_SHEET_TITLE = "byte  12"
BUILTIN_FILTER_DB = "byte  13"
OPT_HIDDEN_NAME = "int  1"
OPT_FUNCTION_NAME = "int  2"
OPT_COMMAND_NAME = "int  4"
OPT_MACRO = "int  8"
OPT_COMPLEX = "int  16"
OPT_BUILTIN = "int  32"
OPT_BINDATA = "int  4096"
def ():
    '''returns NameRecord\n\n
    ()\n
    (final byte builtin, final int sheetNumber)\n
    (final RecordInputStream ris)\n
    '''
def setOptionFlag():
    '''returns None\n\n
    setOptionFlag(final short flag)\n
    '''
def setKeyboardShortcut():
    '''returns None\n\n
    setKeyboardShortcut(final byte shortcut)\n
    '''
def getSheetNumber():
    '''returns int\n\n
    getSheetNumber()\n
    '''
def getFnGroup():
    '''returns byte\n\n
    getFnGroup()\n
    '''
def setSheetNumber():
    '''returns None\n\n
    setSheetNumber(final int value)\n
    '''
def setNameText():
    '''returns None\n\n
    setNameText(final String name)\n
    '''
def setCustomMenuText():
    '''returns None\n\n
    setCustomMenuText(final String text)\n
    '''
def setDescriptionText():
    '''returns None\n\n
    setDescriptionText(final String text)\n
    '''
def setHelpTopicText():
    '''returns None\n\n
    setHelpTopicText(final String text)\n
    '''
def setStatusBarText():
    '''returns None\n\n
    setStatusBarText(final String text)\n
    '''
def getOptionFlag():
    '''returns short\n\n
    getOptionFlag()\n
    '''
def getKeyboardShortcut():
    '''returns byte\n\n
    getKeyboardShortcut()\n
    '''
def isHiddenName():
    '''returns boolean\n\n
    isHiddenName()\n
    '''
def setHidden():
    '''returns None\n\n
    setHidden(final boolean b)\n
    '''
def isFunctionName():
    '''returns boolean\n\n
    isFunctionName()\n
    '''
def setFunction():
    '''returns None\n\n
    setFunction(final boolean function)\n
    '''
def hasFormula():
    '''returns boolean\n\n
    hasFormula()\n
    '''
def isCommandName():
    '''returns boolean\n\n
    isCommandName()\n
    '''
def isMacro():
    '''returns boolean\n\n
    isMacro()\n
    '''
def isComplexFunction():
    '''returns boolean\n\n
    isComplexFunction()\n
    '''
def isBuiltInName():
    '''returns boolean\n\n
    isBuiltInName()\n
    '''
def getNameText():
    '''returns String\n\n
    getNameText()\n
    '''
def getBuiltInName():
    '''returns byte\n\n
    getBuiltInName()\n
    '''
def getNameDefinition():
    '''returns Ptg[]\n\n
    getNameDefinition()\n
    '''
def setNameDefinition():
    '''returns None\n\n
    setNameDefinition(final Ptg[] ptgs)\n
    '''
def getCustomMenuText():
    '''returns String\n\n
    getCustomMenuText()\n
    '''
def getDescriptionText():
    '''returns String\n\n
    getDescriptionText()\n
    '''
def getHelpTopicText():
    '''returns String\n\n
    getHelpTopicText()\n
    '''
def getStatusBarText():
    '''returns String\n\n
    getStatusBarText()\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final ContinuableRecordOutput out)\n
    '''
def getExternSheetNumber():
    '''returns int\n\n
    getExternSheetNumber()\n
    '''
def getSid():
    '''returns short\n\n
    getSid()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
