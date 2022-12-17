def ():
    '''returns SkeletonImpl\n\n
    ()\n
    '''
def add():
    '''returns None\n\n
    add(final String operation, final QName[] names, final ParameterMode[] modes, final String inputNamespace, final String outputNamespace, final String soapAction)\n
    add(final String operation, final String[] names, final ParameterMode[] modes, final String inputNamespace, final String outputNamespace, final String soapAction)\n
    '''
def getParameterName():
    '''returns QName\n\n
    getParameterName(final String operationName, final int n)\n
    '''
def getParameterMode():
    '''returns ParameterMode\n\n
    getParameterMode(final String operationName, final int n)\n
    '''
def getInputNamespace():
    '''returns String\n\n
    getInputNamespace(final String operationName)\n
    '''
def getOutputNamespace():
    '''returns String\n\n
    getOutputNamespace(final String operationName)\n
    '''
def getSOAPAction():
    '''returns String\n\n
    getSOAPAction(final String operationName)\n
    '''
