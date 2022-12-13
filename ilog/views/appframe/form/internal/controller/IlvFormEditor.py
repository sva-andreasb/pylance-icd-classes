MUST_EXIST_PROPERTY = "String  MustExist""
RELEVANT_PROPERTY = "String  Relevant""
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
'''public IlvFormEditor()
'''
pass
def propertyChange():
'''public void propertyChange(final PropertyChangeEvent propertyChangeEvent)
'''
pass
def setParent():
'''public void setParent(final IlvFormContainerEditor c)
'''
pass
def getParent():
'''public IlvFormContainerEditor getParent()
'''
pass
def getEditionContext():
'''public IlvEditionContext getEditionContext()
'''
pass
def getForm():
'''public IlvForm getForm()
'''
pass
def getName():
'''public String getName()
'''
pass
def setName():
'''public void setName(final String name)
'''
pass
def construct():
'''public void construct(final IlvEditionContext b)
'''
pass
def initializeUI():
'''public void initializeUI(final IlvEditionContext ilvEditionContext)
'''
pass
def commitChanges():
'''public void commitChanges(final IlvEditionContext ilvEditionContext)
'''
pass
def connectModel():
'''public void connectModel(final IlvEditionContext ilvEditionContext)
'''
pass
def modelConnected():
'''public void modelConnected(final IlvEditionContext ilvEditionContext)
'''
pass
def disconnectModel():
'''public void disconnectModel(final IlvEditionContext ilvEditionContext)
'''
pass
def connectUI():
'''public void connectUI(final IlvEditionContext ilvEditionContext)
'''
pass
def disconnectUI():
'''public void disconnectUI(final IlvEditionContext ilvEditionContext)
'''
pass
def isRelevant():
'''public boolean isRelevant()
'''
pass
def setRelevant():
'''public void setRelevant(final boolean b)
'''
pass
def getInitializationStep():
'''public int getInitializationStep()
'''
pass
def getProcessingStep():
'''public int getProcessingStep()
'''
pass
def isInitializing():
'''public boolean isInitializing()
'''
pass
def setEditorStatus():
'''public void setEditorStatus(final int n, final int n2)
'''
pass
def getFormModel():
'''public IlvFormModel getFormModel()
'''
pass
def getModelQuery():
'''public IlvSettingsQuery getModelQuery()
'''
pass
def getBooleanProperty():
'''public boolean getBooleanProperty(final String s, final boolean b)
'''
pass
def setBooleanProperty():
'''public void setBooleanProperty(final String s, final boolean b)
'''
pass
def read():
'''public void read(final Element element)
'''
pass
def addEditorListener():
'''public void addEditorListener(final FormEditorListener formEditorListener)
'''
pass
def removeEditorListener():
'''public boolean removeEditorListener(final FormEditorListener formEditorListener)
'''
pass
def addValueDependentEditor():
'''public void addValueDependentEditor(final IlvFormEditor ilvFormEditor)
'''
pass
def removeValueDependentEditor():
'''public boolean removeValueDependentEditor(final IlvFormEditor ilvFormEditor)
'''
pass
def updateRelevancyState():
'''public void updateRelevancyState()
'''
pass
def validate():
'''public IlvValidationError validate(final int n, final IlvEditionContext ilvEditionContext)
'''
pass
def setValidators():
'''public void setValidators(final IlvValidatorList d)
'''
pass
def getValidators():
'''public IlvValidatorList getValidators()
'''
pass
def setProperty():
'''public Object setProperty(final String s, final Object o)
'''
pass
def getProperty():
'''public Object getProperty(final String s)
'''
pass
def addPropertyChangeListener():
'''public void addPropertyChangeListener(final PropertyChangeListener propertyChangeListener)
'''
pass
def removePropertyChangeListener():
'''public void removePropertyChangeListener(final PropertyChangeListener propertyChangeListener)
'''
pass
def ValueDependentListener():
'''public ValueDependentListener(final IlvFormEditor a)
'''
pass
def lock():
'''public void lock()
'''
pass
def unlock():
'''public boolean unlock()
'''
pass
def validationErrorAdded():
'''public void validationErrorAdded(final ValidationEvent validationEvent)
'''
pass
def validationErrorRemoved():
'''public void validationErrorRemoved(final ValidationEvent validationEvent)
'''
pass
