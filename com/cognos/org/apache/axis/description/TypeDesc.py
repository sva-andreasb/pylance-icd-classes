def TypeDesc():
    '''public TypeDesc(final Class javaClass)
    public TypeDesc(final Class javaClass, final boolean canSearchParents)
    '''
def registerTypeDescForClass():
    '''public static void registerTypeDescForClass(final Class cls, final TypeDesc td)
    '''
def getTypeDescForClass():
    '''public static TypeDesc getTypeDescForClass(final Class cls)
    '''
def getAnyDesc():
    '''public BeanPropertyDescriptor getAnyDesc()
    '''
def getFields():
    '''public FieldDesc[] getFields()
    public FieldDesc[] getFields(final boolean searchParents)
    '''
def setFields():
    '''public void setFields(final FieldDesc[] newFields)
    '''
def addFieldDesc():
    '''public void addFieldDesc(final FieldDesc field)
    '''
def getElementNameForField():
    '''public QName getElementNameForField(final String fieldName)
    '''
def getAttributeNameForField():
    '''public QName getAttributeNameForField(final String fieldName)
    '''
def getFieldNameForElement():
    '''public String getFieldNameForElement(final QName qname, final boolean ignoreNS)
    '''
def getFieldNameForAttribute():
    '''public String getFieldNameForAttribute(final QName qname)
    '''
def getFieldByName():
    '''public FieldDesc getFieldByName(final String name)
    '''
def hasAttributes():
    '''public boolean hasAttributes()
    '''
def getXmlType():
    '''public QName getXmlType()
    '''
def setXmlType():
    '''public void setXmlType(final QName xmlType)
    '''
def getPropertyDescriptors():
    '''public BeanPropertyDescriptor[] getPropertyDescriptors()
    '''
def getAnyContentDescriptor():
    '''public BeanPropertyDescriptor getAnyContentDescriptor()
    '''
def getPropertyDescriptorMap():
    '''public Map getPropertyDescriptorMap()
    '''
