NAMESPACE = "String  \"jabber:x:data\""
ELEMENT = "String  \"item\""
def DataForm():
    '''    public DataForm(final Type type)
    '''
def getType():
    '''    public Type getType()
    '''
def getTitle():
    '''    public String getTitle()
    '''
def getInstructions():
    '''    public List<String> getInstructions()
    '''
def getReportedData():
    '''    public ReportedData getReportedData()
    '''
def getItems():
    '''    public List<Item> getItems()
    '''
def getFields():
    '''    public List<FormField> getFields()
    public List<FormField> getFields()
    public List<FormField> getFields()
    '''
def getField():
    '''    public FormField getField(final String variableName)
    '''
def hasField():
    '''    public boolean hasField(final String variableName)
    '''
def getElementName():
    '''    public String getElementName()
    '''
def getNamespace():
    '''    public String getNamespace()
    '''
def setTitle():
    '''    public void setTitle(final String title)
    '''
def setInstructions():
    '''    public void setInstructions(final List<String> instructions)
    '''
def setReportedData():
    '''    public void setReportedData(final ReportedData reportedData)
    '''
def addField():
    '''    public void addField(final FormField field)
    '''
def addFields():
    '''    public boolean addFields(final Collection<FormField> fieldsToAdd)
    '''
def addInstruction():
    '''    public void addInstruction(final String instruction)
    '''
def addItem():
    '''    public void addItem(final Item item)
    '''
def addExtensionElement():
    '''    public void addExtensionElement(final Element element)
    '''
def getExtensionElements():
    '''    public List<Element> getExtensionElements()
    '''
def getHiddenFormTypeField():
    '''    public FormField getHiddenFormTypeField()
    '''
def hasHiddenFormTypeField():
    '''    public boolean hasHiddenFormTypeField()
    '''
def toXML():
    '''    public XmlStringBuilder toXML(final String enclosingNamespace)
    public CharSequence toXML()
    public CharSequence toXML()
    '''
def from():
    '''    public static DataForm from(final Stanza packet)
    '''
def fromString():
    '''    public static Type fromString(final String string)
    '''
def ReportedData():
    '''    public ReportedData(final List<FormField> fields)
    '''
def Item():
    '''    public Item(final List<FormField> fields)
    '''
