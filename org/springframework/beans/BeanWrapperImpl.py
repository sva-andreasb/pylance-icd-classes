def ():
    '''returns BeanWrapperImpl\n\n
    ()\n
    (final boolean registerDefaultEditors)\n
    (final Object object)\n
    (final Class clazz)\n
    (final Object object, final String nestedPath, final Object rootObject)\n
    '''
def setWrappedInstance():
    '''returns None\n\n
    setWrappedInstance(final Object object)\n
    setWrappedInstance(final Object object, final String nestedPath, final Object rootObject)\n
    '''
def getWrappedInstance():
    '''returns Object\n\n
    getWrappedInstance()\n
    '''
def getWrappedClass():
    '''returns Class\n\n
    getWrappedClass()\n
    '''
def getNestedPath():
    '''returns String\n\n
    getNestedPath()\n
    '''
def getRootInstance():
    '''returns Object\n\n
    getRootInstance()\n
    '''
def getRootClass():
    '''returns Class\n\n
    getRootClass()\n
    '''
def registerCustomEditor():
    '''returns None\n\n
    registerCustomEditor(final Class requiredType, final PropertyEditor propertyEditor)\n
    registerCustomEditor(final Class requiredType, final String propertyPath, final PropertyEditor propertyEditor)\n
    '''
def findCustomEditor():
    '''returns PropertyEditor\n\n
    findCustomEditor(Class requiredType, final String propertyPath)\n
    '''
def getPropertyValue():
    '''returns Object\n\n
    getPropertyValue(final String propertyName)\n
    '''
def setPropertyValue():
    '''returns None\n\n
    setPropertyValue(final String propertyName, final Object value)\n
    setPropertyValue(final PropertyValue pv)\n
    '''
def setPropertyValues():
    '''returns None\n\n
    setPropertyValues(final Map map)\n
    setPropertyValues(final PropertyValues pvs)\n
    setPropertyValues(final PropertyValues propertyValues, final boolean ignoreUnknown)\n
    '''
def doTypeConversionIfNecessary():
    '''returns Object\n\n
    doTypeConversionIfNecessary(final Object newValue, final Class requiredType)\n
    '''
def getPropertyDescriptors():
    '''returns PropertyDescriptor[]\n\n
    getPropertyDescriptors()\n
    '''
def getPropertyDescriptor():
    '''returns PropertyDescriptor\n\n
    getPropertyDescriptor(final String propertyName)\n
    '''
def getPropertyType():
    '''returns Class\n\n
    getPropertyType(final String propertyName)\n
    '''
def isReadableProperty():
    '''returns boolean\n\n
    isReadableProperty(final String propertyName)\n
    '''
def isWritableProperty():
    '''returns boolean\n\n
    isWritableProperty(final String propertyName)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
