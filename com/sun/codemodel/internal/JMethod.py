def _throws():
    '''returns JMethod\n\n
    _throws(final JClass exception)\n
    _throws(final Class<? extends Throwable> exception)\n
    '''
def params():
    '''returns List<JVar>\n\n
    params()\n
    '''
def param():
    '''returns JVar\n\n
    param(final int mods, final JType type, final String name)\n
    param(final JType type, final String name)\n
    param(final int mods, final Class<?> type, final String name)\n
    param(final Class<?> type, final String name)\n
    '''
def varParam():
    '''returns JVar\n\n
    varParam(final Class<?> type, final String name)\n
    varParam(final JType type, final String name)\n
    '''
def annotate():
    '''returns JAnnotationUse\n\n
    annotate(final JClass clazz)\n
    annotate(final Class<? extends Annotation> clazz)\n
    '''
def annotations():
    '''returns Collection<JAnnotationUse>\n\n
    annotations()\n
    '''
def hasVarArgs():
    '''returns boolean\n\n
    hasVarArgs()\n
    '''
def name():
    '''returns None\n\n
    name()\n
    name(final String n)\n
    '''
def type():
    '''returns None\n\n
    type()\n
    type(final JType t)\n
    '''
def listParamTypes():
    '''returns JType[]\n\n
    listParamTypes()\n
    '''
def listVarParamType():
    '''returns JType\n\n
    listVarParamType()\n
    '''
def listParams():
    '''returns JVar[]\n\n
    listParams()\n
    '''
def listVarParam():
    '''returns JVar\n\n
    listVarParam()\n
    '''
def hasSignature():
    '''returns boolean\n\n
    hasSignature(final JType[] argTypes)\n
    '''
def body():
    '''returns JBlock\n\n
    body()\n
    '''
def declareDefaultValue():
    '''returns None\n\n
    declareDefaultValue(final JExpression value)\n
    '''
def javadoc():
    '''returns JDocComment\n\n
    javadoc()\n
    '''
def declare():
    '''returns None\n\n
    declare(final JFormatter f)\n
    '''
def mods():
    '''returns JMods\n\n
    mods()\n
    '''
def getMods():
    '''returns JMods\n\n
    getMods()\n
    '''
