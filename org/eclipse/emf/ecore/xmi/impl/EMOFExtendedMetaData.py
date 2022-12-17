EMOF_PACKAGE_NS_PREFIX = "String  \"emof\""
EMOF_PACKAGE_NS_URI = "String  \"http://schema.omg.org/spec/mof/2.0/emof.xmi\""
EXTENSION = "String  \"Extension\""
XMI_EXTENSION_ELEMENT = "String  \"xmi:Extension\""
XMI_EXTENDER_ATTRIBUTE = "String  \"extender\""
EMOF_XMI_EXTENDER = "String  \"http://www.eclipse.org/emf/2002/Ecore\""
ECORE_EDATATYPE_HREF_PREFIX = "String  \"http://www.eclipse.org/emf/2002/Ecore#//\""
UNMAPPED_EMOF_EDATATYPE_HREF_PREFIX = "String  \"http://www.eclipse.org/emf/2002/Ecore.emof#ecore.\""
MAPPED_EMOF_EDATATYPE_HREF_PREFIX = "String  \"http://schema.omg.org/spec/mof/2.0/emof.xmi#\""
TAG = "String  \"Tag\""
EMOF_TAG = "String  \"emof:Tag\""
EMOF_TAG_NAME = "String  \"name\""
EMOF_TAG_VALUE = "String  \"value\""
EMOF_TAG_ELEMENT = "String  \"element\""
EMOF_PROPERTY_CLASS_NAME = "String  \"Property\""
def ():
    '''returns EMOFExtendedMetaData\n\n
    (final XMLResource.XMLMap xmlMap)\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace(final EPackage ePackage)\n
    '''
def getPackage():
    '''returns EPackage\n\n
    getPackage(final String namespace)\n
    '''
def getName():
    '''returns String\n\n
    getName(final EClassifier eClassifier)\n
    getName(final EStructuralFeature eStructuralFeature)\n
    '''
def getType():
    '''returns EClassifier\n\n
    getType(final EPackage ePackage, final String name)\n
    '''
def getFeatureKind():
    '''returns int\n\n
    getFeatureKind(final EStructuralFeature feature)\n
    '''
