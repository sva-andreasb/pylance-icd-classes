def ():
    '''returns TypeDesc\n\n
    (final Class javaClass)\n
    (final Class javaClass, final boolean canSearchParents)\n
    '''
def getAnyDesc():
    '''returns BeanPropertyDescriptor\n\n
    getAnyDesc()\n
    '''
def getFields():
    '''returns FieldDesc[]\n\n
    getFields()\n
    getFields(final boolean searchParents)\n
    '''
def setFields():
    '''returns None\n\n
    setFields(final FieldDesc[] newFields)\n
    '''
def addFieldDesc():
    '''returns None\n\n
    addFieldDesc(final FieldDesc field)\n
    '''
def getElementNameForField():
    '''returns QName\n\n
    getElementNameForField(final String fieldName)\n
    '''
def getAttributeNameForField():
    '''returns QName\n\n
    getAttributeNameForField(final String fieldName)\n
    '''
def getFieldNameForElement():
    '''returns String\n\n
    getFieldNameForElement(final QName qname, final boolean ignoreNS)\n
    '''
def getFieldNameForAttribute():
    '''returns String\n\n
    getFieldNameForAttribute(final QName qname)\n
    '''
def getFieldByName():
    '''returns FieldDesc\n\n
    getFieldByName(final String name)\n
    '''
def hasAttributes():
    '''returns boolean\n\n
    hasAttributes()\n
    '''
def getXmlType():
    '''returns QName\n\n
    getXmlType()\n
    '''
def setXmlType():
    '''returns None\n\n
    setXmlType(final QName xmlType)\n
    '''
def getPropertyDescriptors():
    '''returns BeanPropertyDescriptor[]\n\n
    getPropertyDescriptors()\n
    '''
def getAnyContentDescriptor():
    '''returns BeanPropertyDescriptor\n\n
    getAnyContentDescriptor()\n
    '''
def getPropertyDescriptorMap():
    '''returns Map\n\n
    getPropertyDescriptorMap()\n
    '''
