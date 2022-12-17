DIAGNOSTIC_SOURCE = "String  \"org.eclipse.emf.ecore\""
EOBJECT__EVERY_MULTIPCITY_CONFORMS = "int  1"
EOBJECT__EVERY_DATA_VALUE_CONFORMS = "int  2"
EOBJECT__EVERY_REFERENCE_IS_CONTAINED = "int  3"
EOBJECT__EVERY_PROXY_RESOLVES = "int  4"
DATA_VALUE__VALUE_IN_RANGE = "int  5"
DATA_VALUE__LENGTH_IN_RANGE = "int  6"
DATA_VALUE__TYPE_CORRECT = "int  7"
DATA_VALUE__VALUE_IN_ENUMERATION = "int  8"
DATA_VALUE__MATCHES_PATTERN = "int  9"
DATA_VALUE__TOTAL_DIGITS_IN_RANGE = "int  10"
DATA_VALUE__FRACTION_DIGITS_IN_RANGE = "int  11"
def validate():
    '''returns boolean\n\n
    validate(final EObject eObject, final DiagnosticChain diagnostics, final Map context)\n
    validate(final EClass eClass, final EObject eObject, final DiagnosticChain diagnostics, final Map context)\n
    validate(final EDataType eDataType, final Object value, final DiagnosticChain diagnostics, final Map context)\n
    validate(final EDataType eDataType, final Object value, final DiagnosticChain diagnostics, final Map context)\n
    '''
def validate_EveryDefaultConstraint():
    '''returns boolean\n\n
    validate_EveryDefaultConstraint(final EObject object, final DiagnosticChain theDiagnostics, final Map context)\n
    '''
def validate_EveryMultiplicityConforms():
    '''returns boolean\n\n
    validate_EveryMultiplicityConforms(final EObject eObject, final DiagnosticChain diagnostics, final Map context)\n
    '''
def validate_EveryProxyResolves():
    '''returns boolean\n\n
    validate_EveryProxyResolves(final EObject eObject, final DiagnosticChain diagnostics, final Map context)\n
    '''
def validate_EveryReferenceIsContained():
    '''returns boolean\n\n
    validate_EveryReferenceIsContained(final EObject eObject, final DiagnosticChain diagnostics, final Map context)\n
    '''
def validate_EveryDataValueConforms():
    '''returns boolean\n\n
    validate_EveryDataValueConforms(final EObject eObject, final DiagnosticChain diagnostics, final Map context)\n
    '''
def ():
    '''returns DynamicEDataTypeValidator\n\n
    (EDataType eDataType)\n
    '''
