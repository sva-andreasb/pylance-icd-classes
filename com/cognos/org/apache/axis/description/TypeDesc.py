def TypeDesc():
'''public TypeDesc(final Class javaClass)
public TypeDesc(final Class javaClass, final boolean canSearchParents)
'''
pass
def registerTypeDescForClass():
'''public static void registerTypeDescForClass(final Class cls, final TypeDesc td)
'''
pass
def getTypeDescForClass():
'''public static TypeDesc getTypeDescForClass(final Class cls)
'''
pass
def getAnyDesc():
'''public BeanPropertyDescriptor getAnyDesc()
'''
pass
def getFields():
'''public FieldDesc[] getFields()
public FieldDesc[] getFields(final boolean searchParents)
'''
pass
def setFields():
'''public void setFields(final FieldDesc[] newFields)
'''
pass
def addFieldDesc():
'''public void addFieldDesc(final FieldDesc field)
'''
pass
def getElementNameForField():
'''public QName getElementNameForField(final String fieldName)
'''
pass
def getAttributeNameForField():
'''public QName getAttributeNameForField(final String fieldName)
'''
pass
def getFieldNameForElement():
'''public String getFieldNameForElement(final QName qname, final boolean ignoreNS)
'''
pass
def getFieldNameForAttribute():
'''public String getFieldNameForAttribute(final QName qname)
'''
pass
def getFieldByName():
'''public FieldDesc getFieldByName(final String name)
'''
pass
def hasAttributes():
'''public boolean hasAttributes()
'''
pass
def getXmlType():
'''public QName getXmlType()
'''
pass
def setXmlType():
'''public void setXmlType(final QName xmlType)
'''
pass
def getPropertyDescriptors():
'''public BeanPropertyDescriptor[] getPropertyDescriptors()
'''
pass
def getAnyContentDescriptor():
'''public BeanPropertyDescriptor getAnyContentDescriptor()
'''
pass
def getPropertyDescriptorMap():
'''public Map getPropertyDescriptorMap()
'''
pass
