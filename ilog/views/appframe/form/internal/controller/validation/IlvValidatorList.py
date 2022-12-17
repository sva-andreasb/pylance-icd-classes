def connect():
    '''returns None\n\n
    connect(final Object o, final IlvForm ilvForm, final IlvEditionContext ilvEditionContext)\n
    '''
def disconnect():
    '''returns None\n\n
    disconnect(final Object o, final IlvForm ilvForm, final IlvEditionContext ilvEditionContext)\n
    '''
def validate():
    '''returns IlvValidationError\n\n
    validate(final int n, final IlvEditionContext ilvEditionContext)\n
    '''
def getValidationMode():
    '''returns int\n\n
    getValidationMode()\n
    '''
def read():
    '''returns None\n\n
    read(final Element element)\n
    '''
def addValidator():
    '''returns None\n\n
    addValidator(final IlvControlValidator ilvControlValidator)\n
    '''
def removeValidator():
    '''returns boolean\n\n
    removeValidator(final IlvControlValidator ilvControlValidator)\n
    '''
def getValidatorCount():
    '''returns int\n\n
    getValidatorCount()\n
    '''
def getValidator():
    '''returns IlvControlValidator\n\n
    getValidator(final int n)\n
    '''
def setEditor():
    '''returns None\n\n
    setEditor(final IlvFormEditor ilvFormEditor)\n
    '''
def addValidationListener():
    '''returns None\n\n
    addValidationListener(final ValidationListener validationListener)\n
    '''
def removeValidationListener():
    '''returns boolean\n\n
    removeValidationListener(final ValidationListener validationListener)\n
    '''
