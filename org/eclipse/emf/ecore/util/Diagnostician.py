def ():
    '''returns Diagnostician\n\n
    (final Registry eValidatorRegistry)\n
    ()\n
    '''
def getObjectLabel():
    '''returns String\n\n
    getObjectLabel(final EObject eObject)\n
    '''
def getFeatureLabel():
    '''returns String\n\n
    getFeatureLabel(final EStructuralFeature eStructuralFeature)\n
    '''
def getValueLabel():
    '''returns String\n\n
    getValueLabel(final EDataType eDataType, final Object value)\n
    '''
def validate():
    '''returns boolean\n\n
    validate(final EObject eObject)\n
    validate(final EObject eObject, final DiagnosticChain diagnostics)\n
    validate(final EObject eObject, final DiagnosticChain diagnostics, final Map context)\n
    validate(EClass eClass, final EObject eObject, final DiagnosticChain diagnostics, final Map context)\n
    validate(final EDataType eDataType, final Object value)\n
    validate(final EDataType eDataType, final Object value, final DiagnosticChain diagnostics, final Map context)\n
    '''
