def create():
    '''returns EObject\n\n
    create(final EClass eClass)\n
    '''
def createFromString():
    '''returns Object\n\n
    createFromString(final EDataType eDataType, final String initialValue)\n
    '''
def convertToString():
    '''returns String\n\n
    convertToString(final EDataType eDataType, final Object instanceValue)\n
    '''
def createChangeDescription():
    '''returns ChangeDescription\n\n
    createChangeDescription()\n
    '''
def createFeatureChange():
    '''returns FeatureChange\n\n
    createFeatureChange()\n
    createFeatureChange(final EStructuralFeature feature, final Object oldValue, final boolean oldIsSet)\n
    '''
def createListChange():
    '''returns ListChange\n\n
    createListChange()\n
    '''
def createResourceChange():
    '''returns ResourceChange\n\n
    createResourceChange()\n
    createResourceChange(final Resource resource, final EList oldValue)\n
    '''
def createFeatureMapEntry():
    '''returns FeatureMapEntry\n\n
    createFeatureMapEntry()\n
    createFeatureMapEntry(final EStructuralFeature feature, final Object value)\n
    '''
def getChangePackage():
    '''returns ChangePackage\n\n
    getChangePackage()\n
    '''
