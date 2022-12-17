COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
DATE_MAPPING_NAME = "String  \"DATE_MAPPING_INTERNAL\""
TIME_MAPPING_NAME = "String  \"TIME_MAPPING_INTERNAL\""
TIMESTAMP_MAPPING_NAME = "String  \"TIMESTAMP_MAPPING_INTERNAL\""
REFERENCE_TIME_TABLE = "String  \"REFERENCE_TIME_TABLE\""
REFERENCE_TIME_COLUMN = "String  \"REFERENCE_TIME_COLUMN\""
INCREMENT_TABLE = "String  \"INCREMENT_TABLE\""
INCREMENT_COLUMN = "String  \"INCREMENT_COLUMN\""
INCREMENT_UNITS = "String  \"INCREMENT_UNITS\""
INCREMENT_LITERAL = "String  \"LITERAL\""
def ():
    '''returns InternalDateMapping\n\n
    (final IloOplModelDefinition oplModelDef, final IloReportHandler oplReportHandler, final IloIssuesReport odmIssuesReport)\n
    (final IloMappingDefinition mappingDefinition)\n
    '''
def setOdmIssuesReport():
    '''returns None\n\n
    setOdmIssuesReport(final IloIssuesReport odmIssuesReport)\n
    '''
def abort():
    '''returns None\n\n
    abort()\n
    '''
def setOplModel():
    '''returns None\n\n
    setOplModel(final IloOplModel oplModel)\n
    '''
def getOplModel():
    '''returns IloOplModel\n\n
    getOplModel()\n
    '''
def getOplModelDefinition():
    '''returns IloOplModelDefinition\n\n
    getOplModelDefinition()\n
    '''
def getMappingDefinitionsList():
    '''returns IloMappingDefinitionsList\n\n
    getMappingDefinitionsList()\n
    '''
def addMappings():
    '''returns None\n\n
    addMappings(final IloMappingDefinitionsList mappingDS)\n
    '''
def write():
    '''returns None\n\n
    write(final IloOplElement elt)\n
    '''
def writeAll():
    '''returns None\n\n
    writeAll()\n
    '''
def getMapper():
    '''returns IloMapper\n\n
    getMapper(final IloOplElement elt, final boolean throwIfNotFound)\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def visitInt():
    '''returns None\n\n
    visitInt(final IloOplElementDefinition elt, final Object ctx)\n
    '''
def visitIntMap():
    '''returns None\n\n
    visitIntMap(final IloOplElementDefinition elt, final Object ctx)\n
    '''
def visitIntSet():
    '''returns None\n\n
    visitIntSet(final IloOplElementDefinition elt, final Object ctx)\n
    '''
def visitIntSetMap():
    '''returns None\n\n
    visitIntSetMap(final IloOplElementDefinition elt, final Object ctx)\n
    '''
def visitNum():
    '''returns None\n\n
    visitNum(final IloOplElementDefinition elt, final Object ctx)\n
    '''
def visitNumMap():
    '''returns None\n\n
    visitNumMap(final IloOplElementDefinition elt, final Object ctx)\n
    '''
def visitNumSet():
    '''returns None\n\n
    visitNumSet(final IloOplElementDefinition elt, final Object ctx)\n
    '''
def visitNumSetMap():
    '''returns None\n\n
    visitNumSetMap(final IloOplElementDefinition elt, final Object ctx)\n
    '''
def visitString():
    '''returns None\n\n
    visitString(final IloOplElementDefinition elt, final Object ctx)\n
    '''
def visitStringMap():
    '''returns None\n\n
    visitStringMap(final IloOplElementDefinition elt, final Object ctx)\n
    '''
def visitStringSet():
    '''returns None\n\n
    visitStringSet(final IloOplElementDefinition elt, final Object ctx)\n
    '''
def visitStringSetMap():
    '''returns None\n\n
    visitStringSetMap(final IloOplElementDefinition elt, final Object ctx)\n
    '''
def visitTuple():
    '''returns None\n\n
    visitTuple(final IloOplElementDefinition elt, final Object ctx)\n
    '''
def visitTupleMap():
    '''returns None\n\n
    visitTupleMap(final IloOplElementDefinition elt, final Object ctx)\n
    '''
def visitTupleSet():
    '''returns None\n\n
    visitTupleSet(final IloOplElementDefinition elt, final Object ctx)\n
    '''
def visitTupleSetMap():
    '''returns None\n\n
    visitTupleSetMap(final IloOplElementDefinition elt, final Object ctx)\n
    '''
def visitIntRange():
    '''returns None\n\n
    visitIntRange(final IloOplElementDefinition elt, final Object ctx)\n
    '''
def getType():
    '''returns IloDataType\n\n
    getType()\n
    '''
def isResolved():
    '''returns boolean\n\n
    isResolved()\n
    '''
def resolve():
    '''returns None\n\n
    resolve(final IloTable table)\n
    resolve(final IloTableContainer tableContainer)\n
    '''
def getReferenceTime():
    '''returns Date\n\n
    getReferenceTime()\n
    '''
def getIncrement():
    '''returns int\n\n
    getIncrement()\n
    '''
def getIncrementUnit():
    '''returns IloOdmTimeUnit\n\n
    getIncrementUnit()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
