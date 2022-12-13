NAMESPACE = "String  jabber:x:data""
ELEMENT = "String  item""
def DataForm():
'''public DataForm(final Type type)
'''
pass
def getType():
'''public Type getType()
'''
pass
def getTitle():
'''public String getTitle()
'''
pass
def getInstructions():
'''public List<String> getInstructions()
'''
pass
def getReportedData():
'''public ReportedData getReportedData()
'''
pass
def getItems():
'''public List<Item> getItems()
'''
pass
def getFields():
'''public List<FormField> getFields()
public List<FormField> getFields()
public List<FormField> getFields()
'''
pass
def getField():
'''public FormField getField(final String variableName)
'''
pass
def hasField():
'''public boolean hasField(final String variableName)
'''
pass
def getElementName():
'''public String getElementName()
'''
pass
def getNamespace():
'''public String getNamespace()
'''
pass
def setTitle():
'''public void setTitle(final String title)
'''
pass
def setInstructions():
'''public void setInstructions(final List<String> instructions)
'''
pass
def setReportedData():
'''public void setReportedData(final ReportedData reportedData)
'''
pass
def addField():
'''public void addField(final FormField field)
'''
pass
def addFields():
'''public boolean addFields(final Collection<FormField> fieldsToAdd)
'''
pass
def addInstruction():
'''public void addInstruction(final String instruction)
'''
pass
def addItem():
'''public void addItem(final Item item)
'''
pass
def addExtensionElement():
'''public void addExtensionElement(final Element element)
'''
pass
def getExtensionElements():
'''public List<Element> getExtensionElements()
'''
pass
def getHiddenFormTypeField():
'''public FormField getHiddenFormTypeField()
'''
pass
def hasHiddenFormTypeField():
'''public boolean hasHiddenFormTypeField()
'''
pass
def toXML():
'''public XmlStringBuilder toXML(final String enclosingNamespace)
public CharSequence toXML()
public CharSequence toXML()
'''
pass
def from():
'''public static DataForm from(final Stanza packet)
'''
pass
def fromString():
'''public static Type fromString(final String string)
'''
pass
def ReportedData():
'''public ReportedData(final List<FormField> fields)
'''
pass
def Item():
'''public Item(final List<FormField> fields)
'''
pass
