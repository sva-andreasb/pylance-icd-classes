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
    '''    public NameRecord()
    public NameRecord(final byte builtin, final int sheetNumber)
    public NameRecord(final RecordInputStream ris)
    '''
def setOptionFlag():
    '''    public void setOptionFlag(final short flag)
    '''
def setKeyboardShortcut():
    '''    public void setKeyboardShortcut(final byte shortcut)
    '''
def getSheetNumber():
    '''    public int getSheetNumber()
    '''
def getFnGroup():
    '''    public byte getFnGroup()
    '''
def setSheetNumber():
    '''    public void setSheetNumber(final int value)
    '''
def setNameText():
    '''    public void setNameText(final String name)
    '''
def setCustomMenuText():
    '''    public void setCustomMenuText(final String text)
    '''
def setDescriptionText():
    '''    public void setDescriptionText(final String text)
    '''
def setHelpTopicText():
    '''    public void setHelpTopicText(final String text)
    '''
def setStatusBarText():
    '''    public void setStatusBarText(final String text)
    '''
def getOptionFlag():
    '''    public short getOptionFlag()
    '''
def getKeyboardShortcut():
    '''    public byte getKeyboardShortcut()
    '''
def isHiddenName():
    '''    public boolean isHiddenName()
    '''
def setHidden():
    '''    public void setHidden(final boolean b)
    '''
def isFunctionName():
    '''    public boolean isFunctionName()
    '''
def setFunction():
    '''    public void setFunction(final boolean function)
    '''
def hasFormula():
    '''    public boolean hasFormula()
    '''
def isCommandName():
    '''    public boolean isCommandName()
    '''
def isMacro():
    '''    public boolean isMacro()
    '''
def isComplexFunction():
    '''    public boolean isComplexFunction()
    '''
def isBuiltInName():
    '''    public boolean isBuiltInName()
    '''
def getNameText():
    '''    public String getNameText()
    '''
def getBuiltInName():
    '''    public byte getBuiltInName()
    '''
def getNameDefinition():
    '''    public Ptg[] getNameDefinition()
    '''
def setNameDefinition():
    '''    public void setNameDefinition(final Ptg[] ptgs)
    '''
def getCustomMenuText():
    '''    public String getCustomMenuText()
    '''
def getDescriptionText():
    '''    public String getDescriptionText()
    '''
def getHelpTopicText():
    '''    public String getHelpTopicText()
    '''
def getStatusBarText():
    '''    public String getStatusBarText()
    '''
def serialize():
    '''    public void serialize(final ContinuableRecordOutput out)
    '''
def getExternSheetNumber():
    '''    public int getExternSheetNumber()
    '''
def getSid():
    '''    public short getSid()
    '''
def toString():
    '''    public String toString()
    '''
def isFormula():
    '''    public static final boolean isFormula(final int optValue)
    '''
