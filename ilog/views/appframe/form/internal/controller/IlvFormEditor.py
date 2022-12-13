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
def IlvFormEditor():
    '''    public IlvFormEditor()
    '''
def propertyChange():
    '''    public void propertyChange(final PropertyChangeEvent propertyChangeEvent)
    '''
def setParent():
    '''    public void setParent(final IlvFormContainerEditor c)
    '''
def getParent():
    '''    public IlvFormContainerEditor getParent()
    '''
def getEditionContext():
    '''    public IlvEditionContext getEditionContext()
    '''
def getForm():
    '''    public IlvForm getForm()
    '''
def getName():
    '''    public String getName()
    '''
def setName():
    '''    public void setName(final String name)
    '''
def construct():
    '''    public void construct(final IlvEditionContext b)
    '''
def initializeUI():
    '''    public void initializeUI(final IlvEditionContext ilvEditionContext)
    '''
def commitChanges():
    '''    public void commitChanges(final IlvEditionContext ilvEditionContext)
    '''
def connectModel():
    '''    public void connectModel(final IlvEditionContext ilvEditionContext)
    '''
def modelConnected():
    '''    public void modelConnected(final IlvEditionContext ilvEditionContext)
    '''
def disconnectModel():
    '''    public void disconnectModel(final IlvEditionContext ilvEditionContext)
    '''
def connectUI():
    '''    public void connectUI(final IlvEditionContext ilvEditionContext)
    '''
def disconnectUI():
    '''    public void disconnectUI(final IlvEditionContext ilvEditionContext)
    '''
def isRelevant():
    '''    public boolean isRelevant()
    '''
def setRelevant():
    '''    public void setRelevant(final boolean b)
    '''
def getInitializationStep():
    '''    public int getInitializationStep()
    '''
def getProcessingStep():
    '''    public int getProcessingStep()
    '''
def isInitializing():
    '''    public boolean isInitializing()
    '''
def setEditorStatus():
    '''    public void setEditorStatus(final int n, final int n2)
    '''
def getFormModel():
    '''    public IlvFormModel getFormModel()
    '''
def getModelQuery():
    '''    public IlvSettingsQuery getModelQuery()
    '''
def getBooleanProperty():
    '''    public boolean getBooleanProperty(final String s, final boolean b)
    '''
def setBooleanProperty():
    '''    public void setBooleanProperty(final String s, final boolean b)
    '''
def read():
    '''    public void read(final Element element)
    '''
def addEditorListener():
    '''    public void addEditorListener(final FormEditorListener formEditorListener)
    '''
def removeEditorListener():
    '''    public boolean removeEditorListener(final FormEditorListener formEditorListener)
    '''
def addValueDependentEditor():
    '''    public void addValueDependentEditor(final IlvFormEditor ilvFormEditor)
    '''
def removeValueDependentEditor():
    '''    public boolean removeValueDependentEditor(final IlvFormEditor ilvFormEditor)
    '''
def updateRelevancyState():
    '''    public void updateRelevancyState()
    '''
def validate():
    '''    public IlvValidationError validate(final int n, final IlvEditionContext ilvEditionContext)
    '''
def setValidators():
    '''    public void setValidators(final IlvValidatorList d)
    '''
def getValidators():
    '''    public IlvValidatorList getValidators()
    '''
def setProperty():
    '''    public Object setProperty(final String s, final Object o)
    '''
def getProperty():
    '''    public Object getProperty(final String s)
    '''
def addPropertyChangeListener():
    '''    public void addPropertyChangeListener(final PropertyChangeListener propertyChangeListener)
    '''
def removePropertyChangeListener():
    '''    public void removePropertyChangeListener(final PropertyChangeListener propertyChangeListener)
    '''
def ValueDependentListener():
    '''    public ValueDependentListener(final IlvFormEditor a)
    '''
def lock():
    '''    public void lock()
    '''
def unlock():
    '''    public boolean unlock()
    '''
def validationErrorAdded():
    '''    public void validationErrorAdded(final ValidationEvent validationEvent)
    '''
def validationErrorRemoved():
    '''    public void validationErrorRemoved(final ValidationEvent validationEvent)
    '''
