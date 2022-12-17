COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def resetModel():
    '''returns None\n\n
    resetModel()\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid()\n
    '''
def getErrorMessage():
    '''returns IloParameterizedMessage\n\n
    getErrorMessage()\n
    '''
def getWarningMessages():
    '''returns ArrayList<IloParameterizedMessage>\n\n
    getWarningMessages()\n
    '''
def isUsingCP():
    '''returns boolean\n\n
    isUsingCP()\n
    '''
def checkAndReportConform():
    '''returns boolean\n\n
    checkAndReportConform()\n
    '''
def isData():
    '''returns boolean\n\n
    isData(final String oplEltName)\n
    '''
def isRange():
    '''returns boolean\n\n
    isRange(final String oplEltName)\n
    '''
def isDExpr():
    '''returns boolean\n\n
    isDExpr(final String oplEltName)\n
    '''
def isConstraint():
    '''returns boolean\n\n
    isConstraint(final String oplEltName)\n
    '''
def isRegularArray():
    '''returns boolean\n\n
    isRegularArray(final String oplEltName)\n
    '''
def isDvarArray():
    '''returns boolean\n\n
    isDvarArray(final String oplEltName)\n
    '''
def ():
    '''returns IloOplRangeDefinitionInfo\n\n
    (final IloReportHandler reportHandler, final File modelFile)\n
    ()\n
    '''
def getModelName():
    '''returns String\n\n
    getModelName()\n
    '''
def getIndexNameForData():
    '''returns String\n\n
    getIndexNameForData(final String eltName, final int index)\n
    '''
def getIndexNamesForConstraint():
    '''returns List<IndexNameView>\n\n
    getIndexNamesForConstraint(final String eltName)\n
    getIndexNamesForConstraint(final IloOplElementDefinition elt)\n
    '''
def getConstraintNames():
    '''returns Set<String>\n\n
    getConstraintNames()\n
    '''
def getInputDataNames():
    '''returns Set<String>\n\n
    getInputDataNames()\n
    '''
def getInputDataNamesForRules():
    '''returns Set<String>\n\n
    getInputDataNamesForRules()\n
    '''
def getResultDataNames():
    '''returns Set<String>\n\n
    getResultDataNames()\n
    '''
def getSimpleTypeResultDataNames():
    '''returns Set<String>\n\n
    getSimpleTypeResultDataNames()\n
    '''
def getIntegerInputDataNames():
    '''returns Set<String>\n\n
    getIntegerInputDataNames()\n
    '''
def getIntegerResultDataNames():
    '''returns Set<String>\n\n
    getIntegerResultDataNames()\n
    '''
def getSimpleTypeInputDataNames():
    '''returns Set<String>\n\n
    getSimpleTypeInputDataNames()\n
    '''
def getRangeNames():
    '''returns Set<String>\n\n
    getRangeNames()\n
    '''
def getArrayNames():
    '''returns Set<String>\n\n
    getArrayNames()\n
    '''
def getDvarArrayNames():
    '''returns Set<String>\n\n
    getDvarArrayNames()\n
    '''
def getRange():
    '''returns IloOplRangeDefinitionInfo\n\n
    getRange(final String rangeName)\n
    '''
def getConstraintNamesUsingOplInput():
    '''returns Set<String>\n\n
    getConstraintNamesUsingOplInput(final String oplInputDataName)\n
    '''
def isLabelledArrayConstraint():
    '''returns boolean\n\n
    isLabelledArrayConstraint(final IloOplElementDefinition elt)\n
    '''
def constraintHasCenter():
    '''returns boolean\n\n
    constraintHasCenter(final IloOplElementDefinition ctElt)\n
    '''
def constraintHasBounds():
    '''returns boolean\n\n
    constraintHasBounds(final IloOplElementDefinition ctElt)\n
    '''
def constraintIsLogical():
    '''returns boolean\n\n
    constraintIsLogical(final IloOplElementDefinition ctElt)\n
    '''
def getObjectiveNames():
    '''returns Set<String>\n\n
    getObjectiveNames()\n
    '''
def getDExprNames():
    '''returns Set<String>\n\n
    getDExprNames()\n
    '''
def getIndexNamesForDExpr():
    '''returns List<IndexNameView>\n\n
    getIndexNamesForDExpr(final String eltName)\n
    getIndexNamesForDExpr(final IloOplElementDefinition elt)\n
    '''
def getSubDExprsForDExpr():
    '''returns String[]\n\n
    getSubDExprsForDExpr(final String eltName)\n
    '''
def reloadModelText():
    '''returns None\n\n
    reloadModelText(final String modelText)\n
    '''
def reloadModelFile():
    '''returns None\n\n
    reloadModelFile()\n
    '''
def getOplModelDefinitionOrThrow():
    '''returns IloOplModelDefinition\n\n
    getOplModelDefinitionOrThrow(final IloOplFactory oplF)\n
    '''
def getOplModelDefinitionOrNull():
    '''returns IloOplModelDefinition\n\n
    getOplModelDefinitionOrNull(final IloOplFactory oplF)\n
    '''
def addChangeListener():
    '''returns None\n\n
    addChangeListener(final ChangeListener listener)\n
    '''
def removeChangeListener():
    '''returns None\n\n
    removeChangeListener(final ChangeListener listener)\n
    '''
def getParentElement():
    '''returns IloModelElement\n\n
    getParentElement()\n
    '''
def fireChangedEvent():
    '''returns None\n\n
    fireChangedEvent()\n
    fireChangedEvent(final ModelModificationEvent event)\n
    '''
