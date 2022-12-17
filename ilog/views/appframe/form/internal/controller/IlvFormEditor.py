MUST_EXIST_PROPERTY = "String  \"MustExist\""
RELEVANT_PROPERTY = "String  \"Relevant\""
UNPROCESSED = "int  0"
PROCESSING = "int  1"
UNPROCESSING = "int  2"
PROCESSED = "int  4"
CONSTRUCTION_STEP = "int  8"
FIRST_INITIALIZATION_STEP = "int  8"
MODEL_DATA_CONNEXION_STEP = "int  16"
MODEL_DATA_CONNECTED_STEP = "int  32"
UI_CONNEXION_STEP = "int  64"
UI_INITIALIZATION_STEP = "int  128"
def ():
    '''returns ValueDependentListener\n\n
    ()\n
    (final IlvFormEditor a)\n
    '''
def propertyChange():
    '''returns None\n\n
    propertyChange(final PropertyChangeEvent propertyChangeEvent)\n
    '''
def setParent():
    '''returns None\n\n
    setParent(final IlvFormContainerEditor c)\n
    '''
def getParent():
    '''returns IlvFormContainerEditor\n\n
    getParent()\n
    '''
def getEditionContext():
    '''returns IlvEditionContext\n\n
    getEditionContext()\n
    '''
def getForm():
    '''returns IlvForm\n\n
    getForm()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def construct():
    '''returns None\n\n
    construct(final IlvEditionContext b)\n
    '''
def initializeUI():
    '''returns None\n\n
    initializeUI(final IlvEditionContext ilvEditionContext)\n
    '''
def commitChanges():
    '''returns None\n\n
    commitChanges(final IlvEditionContext ilvEditionContext)\n
    '''
def connectModel():
    '''returns None\n\n
    connectModel(final IlvEditionContext ilvEditionContext)\n
    '''
def modelConnected():
    '''returns None\n\n
    modelConnected(final IlvEditionContext ilvEditionContext)\n
    '''
def disconnectModel():
    '''returns None\n\n
    disconnectModel(final IlvEditionContext ilvEditionContext)\n
    '''
def connectUI():
    '''returns None\n\n
    connectUI(final IlvEditionContext ilvEditionContext)\n
    '''
def disconnectUI():
    '''returns None\n\n
    disconnectUI(final IlvEditionContext ilvEditionContext)\n
    '''
def isRelevant():
    '''returns boolean\n\n
    isRelevant()\n
    '''
def setRelevant():
    '''returns None\n\n
    setRelevant(final boolean b)\n
    '''
def getInitializationStep():
    '''returns int\n\n
    getInitializationStep()\n
    '''
def getProcessingStep():
    '''returns int\n\n
    getProcessingStep()\n
    '''
def isInitializing():
    '''returns boolean\n\n
    isInitializing()\n
    '''
def setEditorStatus():
    '''returns None\n\n
    setEditorStatus(final int n, final int n2)\n
    '''
def getFormModel():
    '''returns IlvFormModel\n\n
    getFormModel()\n
    '''
def getModelQuery():
    '''returns IlvSettingsQuery\n\n
    getModelQuery()\n
    '''
def getBooleanProperty():
    '''returns boolean\n\n
    getBooleanProperty(final String s, final boolean b)\n
    '''
def setBooleanProperty():
    '''returns None\n\n
    setBooleanProperty(final String s, final boolean b)\n
    '''
def read():
    '''returns None\n\n
    read(final Element element)\n
    '''
def addEditorListener():
    '''returns None\n\n
    addEditorListener(final FormEditorListener formEditorListener)\n
    '''
def removeEditorListener():
    '''returns boolean\n\n
    removeEditorListener(final FormEditorListener formEditorListener)\n
    '''
def addValueDependentEditor():
    '''returns None\n\n
    addValueDependentEditor(final IlvFormEditor ilvFormEditor)\n
    '''
def removeValueDependentEditor():
    '''returns boolean\n\n
    removeValueDependentEditor(final IlvFormEditor ilvFormEditor)\n
    '''
def updateRelevancyState():
    '''returns None\n\n
    updateRelevancyState()\n
    '''
def validate():
    '''returns IlvValidationError\n\n
    validate(final int n, final IlvEditionContext ilvEditionContext)\n
    '''
def setValidators():
    '''returns None\n\n
    setValidators(final IlvValidatorList d)\n
    '''
def getValidators():
    '''returns IlvValidatorList\n\n
    getValidators()\n
    '''
def setProperty():
    '''returns Object\n\n
    setProperty(final String s, final Object o)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String s)\n
    '''
def addPropertyChangeListener():
    '''returns None\n\n
    addPropertyChangeListener(final PropertyChangeListener propertyChangeListener)\n
    '''
def removePropertyChangeListener():
    '''returns None\n\n
    removePropertyChangeListener(final PropertyChangeListener propertyChangeListener)\n
    '''
def lock():
    '''returns None\n\n
    lock()\n
    '''
def unlock():
    '''returns boolean\n\n
    unlock()\n
    '''
def validationErrorAdded():
    '''returns None\n\n
    validationErrorAdded(final ValidationEvent validationEvent)\n
    '''
def validationErrorRemoved():
    '''returns None\n\n
    validationErrorRemoved(final ValidationEvent validationEvent)\n
    '''
