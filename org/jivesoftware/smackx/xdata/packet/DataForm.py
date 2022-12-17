NAMESPACE = "String  \"jabber:x:data\""
ELEMENT = "String  \"item\""
def ():
    '''returns Item\n\n
    (final Type type)\n
    (final List<FormField> fields)\n
    (final List<FormField> fields)\n
    '''
def getType():
    '''returns Type\n\n
    getType()\n
    '''
def getTitle():
    '''returns String\n\n
    getTitle()\n
    '''
def getInstructions():
    '''returns List<String>\n\n
    getInstructions()\n
    '''
def getReportedData():
    '''returns ReportedData\n\n
    getReportedData()\n
    '''
def getItems():
    '''returns List<Item>\n\n
    getItems()\n
    '''
def getFields():
    '''returns List<FormField>\n\n
    getFields()\n
    getFields()\n
    getFields()\n
    '''
def getField():
    '''returns FormField\n\n
    getField(final String variableName)\n
    '''
def hasField():
    '''returns boolean\n\n
    hasField(final String variableName)\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def setTitle():
    '''returns None\n\n
    setTitle(final String title)\n
    '''
def setInstructions():
    '''returns None\n\n
    setInstructions(final List<String> instructions)\n
    '''
def setReportedData():
    '''returns None\n\n
    setReportedData(final ReportedData reportedData)\n
    '''
def addField():
    '''returns None\n\n
    addField(final FormField field)\n
    '''
def addFields():
    '''returns boolean\n\n
    addFields(final Collection<FormField> fieldsToAdd)\n
    '''
def addInstruction():
    '''returns None\n\n
    addInstruction(final String instruction)\n
    '''
def addItem():
    '''returns None\n\n
    addItem(final Item item)\n
    '''
def addExtensionElement():
    '''returns None\n\n
    addExtensionElement(final Element element)\n
    '''
def getExtensionElements():
    '''returns List<Element>\n\n
    getExtensionElements()\n
    '''
def getHiddenFormTypeField():
    '''returns FormField\n\n
    getHiddenFormTypeField()\n
    '''
def hasHiddenFormTypeField():
    '''returns boolean\n\n
    hasHiddenFormTypeField()\n
    '''
def toXML():
    '''returns CharSequence\n\n
    toXML(final String enclosingNamespace)\n
    toXML()\n
    toXML()\n
    '''
