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
def NameRecord():
'''public NameRecord()
public NameRecord(final byte builtin, final int sheetNumber)
public NameRecord(final RecordInputStream ris)
'''
pass
def setOptionFlag():
'''public void setOptionFlag(final short flag)
'''
pass
def setKeyboardShortcut():
'''public void setKeyboardShortcut(final byte shortcut)
'''
pass
def getSheetNumber():
'''public int getSheetNumber()
'''
pass
def getFnGroup():
'''public byte getFnGroup()
'''
pass
def setSheetNumber():
'''public void setSheetNumber(final int value)
'''
pass
def setNameText():
'''public void setNameText(final String name)
'''
pass
def setCustomMenuText():
'''public void setCustomMenuText(final String text)
'''
pass
def setDescriptionText():
'''public void setDescriptionText(final String text)
'''
pass
def setHelpTopicText():
'''public void setHelpTopicText(final String text)
'''
pass
def setStatusBarText():
'''public void setStatusBarText(final String text)
'''
pass
def getOptionFlag():
'''public short getOptionFlag()
'''
pass
def getKeyboardShortcut():
'''public byte getKeyboardShortcut()
'''
pass
def isHiddenName():
'''public boolean isHiddenName()
'''
pass
def setHidden():
'''public void setHidden(final boolean b)
'''
pass
def isFunctionName():
'''public boolean isFunctionName()
'''
pass
def setFunction():
'''public void setFunction(final boolean function)
'''
pass
def hasFormula():
'''public boolean hasFormula()
'''
pass
def isCommandName():
'''public boolean isCommandName()
'''
pass
def isMacro():
'''public boolean isMacro()
'''
pass
def isComplexFunction():
'''public boolean isComplexFunction()
'''
pass
def isBuiltInName():
'''public boolean isBuiltInName()
'''
pass
def getNameText():
'''public String getNameText()
'''
pass
def getBuiltInName():
'''public byte getBuiltInName()
'''
pass
def getNameDefinition():
'''public Ptg[] getNameDefinition()
'''
pass
def setNameDefinition():
'''public void setNameDefinition(final Ptg[] ptgs)
'''
pass
def getCustomMenuText():
'''public String getCustomMenuText()
'''
pass
def getDescriptionText():
'''public String getDescriptionText()
'''
pass
def getHelpTopicText():
'''public String getHelpTopicText()
'''
pass
def getStatusBarText():
'''public String getStatusBarText()
'''
pass
def serialize():
'''public void serialize(final ContinuableRecordOutput out)
'''
pass
def getExternSheetNumber():
'''public int getExternSheetNumber()
'''
pass
def getSid():
'''public short getSid()
'''
pass
def toString():
'''public String toString()
'''
pass
def isFormula():
'''public static final boolean isFormula(final int optValue)
'''
pass
