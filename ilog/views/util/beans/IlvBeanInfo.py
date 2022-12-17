BOUND = "String  \"bound\""
CONSTRAINED = "String  \"constrained\""
PROPERTYEDITORCLASS = "String  \"propertyEditorClass\""
DISPLAYNAME = "String  \"displayName\""
EXPERT = "String  \"expert\""
HIDDEN = "String  \"hidden\""
PREFERRED = "String  \"preferred\""
SHORTDESCRIPTION = "String  \"shortDescription\""
CUSTOMIZERCLASS = "String  \"customizerClass\""
PROPERTYNAME = "String  \"propertyName\""
FULLNAME = "String  \"fullName\""
GETTERNAME = "String  \"getterName\""
SETTERNAME = "String  \"setterName\""
INDEXEDGETTERNAME = "String  \"indexedGetterName\""
INDEXEDSETTERNAME = "String  \"indexedSetterName\""
RESOURCEBUNDLE = "String  \"resourceBundle\""
DEFAULT = "String  \"default\""
FOLDER = "String  \"FOLDER\""
TOOLBAR = "String  \"TOOLBAR\""
LOCALIZABLE_DISPLAYNAME_SUFFIX = "String  \".displayName\""
LOCALIZABLE_SHORTDESCRIPTION_SUFFIX = "String  \".shortDescription\""
def createBeanDescriptor():
    '''returns BeanDescriptor\n\n
    createBeanDescriptor(final Class clazz, final Object[] array)\n
    '''
def createPropertyDescriptor():
    '''returns PropertyDescriptor\n\n
    createPropertyDescriptor(final Class clazz, final String s, final Object[] array)\n
    '''
def createIndexedPropertyDescriptor():
    '''returns PropertyDescriptor\n\n
    createIndexedPropertyDescriptor(final Class clazz, final String s, final Object[] array)\n
    '''
def createFeatureDescriptor():
    '''returns FeatureDescriptor\n\n
    createFeatureDescriptor(final String name, final Object[] array)\n
    '''
def getIcon():
    '''returns Image\n\n
    getIcon(final int n)\n
    '''
