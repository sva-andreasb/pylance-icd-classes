def BaseTag():
    '''public BaseTag(final BaseTag parent, final String name)
    '''
def visit():
    '''public static void visit(final List<BaseTag> tags, final BaseTagVisitor visitor)
    '''
def getRootTag():
    '''public RootTag getRootTag()
    '''
def isRootTag():
    '''public boolean isRootTag()
    '''
def isGroupTag():
    '''public boolean isGroupTag()
    '''
def isFileTag():
    '''public boolean isFileTag()
    '''
def isExportFileTag():
    '''public boolean isExportFileTag()
    '''
def isImportFileTag():
    '''public boolean isImportFileTag()
    '''
def getParent():
    '''public BaseTag getParent()
    '''
def getChildren():
    '''public List<BaseTag> getChildren()
    '''
def addChild():
    '''public void addChild(final BaseTag child)
    '''
def getOptions():
    '''public Map<String, Option> getOptions()
    '''
def addOption():
    '''public void addOption(final Option option)
    '''
def getReplacementsInfo():
    '''public ReplacementsInfo getReplacementsInfo()
    '''
def getName():
    '''public String getName()
    '''
def setName():
    '''public void setName(final String name)
    '''
def getSummary():
    '''public String getSummary()
    '''
def setSummary():
    '''public void setSummary(final String summary)
    '''
def getIsSelected():
    '''public boolean getIsSelected()
    '''
def setIsSelected():
    '''public void setIsSelected()
    public void setIsSelected(final boolean isSelected)
    '''
def setNotSelected():
    '''public void setNotSelected()
    '''
def getHasError():
    '''public boolean getHasError()
    '''
def setHasError():
    '''public void setHasError(final boolean hasError)
    '''
def getMessages():
    '''public List<Message> getMessages()
    '''
def addMessage():
    '''public void addMessage(final Message mesg)
    '''
def accept():
    '''public void accept(final BaseTagVisitor visitor)
    public void accept(final BaseTagVisitor visitor, final boolean recurse)
    '''
def acceptReverse():
    '''public void acceptReverse(final BaseTagVisitor visitor)
    '''
