def BaseTag():
'''public BaseTag(final BaseTag parent, final String name)
'''
pass
def visit():
'''public static void visit(final List<BaseTag> tags, final BaseTagVisitor visitor)
'''
pass
def getRootTag():
'''public RootTag getRootTag()
'''
pass
def isRootTag():
'''public boolean isRootTag()
'''
pass
def isGroupTag():
'''public boolean isGroupTag()
'''
pass
def isFileTag():
'''public boolean isFileTag()
'''
pass
def isExportFileTag():
'''public boolean isExportFileTag()
'''
pass
def isImportFileTag():
'''public boolean isImportFileTag()
'''
pass
def getParent():
'''public BaseTag getParent()
'''
pass
def getChildren():
'''public List<BaseTag> getChildren()
'''
pass
def addChild():
'''public void addChild(final BaseTag child)
'''
pass
def getOptions():
'''public Map<String, Option> getOptions()
'''
pass
def addOption():
'''public void addOption(final Option option)
'''
pass
def getReplacementsInfo():
'''public ReplacementsInfo getReplacementsInfo()
'''
pass
def getName():
'''public String getName()
'''
pass
def setName():
'''public void setName(final String name)
'''
pass
def getSummary():
'''public String getSummary()
'''
pass
def setSummary():
'''public void setSummary(final String summary)
'''
pass
def getIsSelected():
'''public boolean getIsSelected()
'''
pass
def setIsSelected():
'''public void setIsSelected()
public void setIsSelected(final boolean isSelected)
'''
pass
def setNotSelected():
'''public void setNotSelected()
'''
pass
def getHasError():
'''public boolean getHasError()
'''
pass
def setHasError():
'''public void setHasError(final boolean hasError)
'''
pass
def getMessages():
'''public List<Message> getMessages()
'''
pass
def addMessage():
'''public void addMessage(final Message mesg)
'''
pass
def accept():
'''public void accept(final BaseTagVisitor visitor)
public void accept(final BaseTagVisitor visitor, final boolean recurse)
'''
pass
def acceptReverse():
'''public void acceptReverse(final BaseTagVisitor visitor)
'''
pass
