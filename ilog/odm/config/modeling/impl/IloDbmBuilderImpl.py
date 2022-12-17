COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloDbmBuilderImpl\n\n
    ()\n
    '''
def initStandalone():
    '''returns None\n\n
    initStandalone()\n
    '''
def createResource():
    '''returns Resource\n\n
    createResource(final URI uri)\n
    createResource(final File dbmFile)\n
    '''
def getOrCreateDatabase():
    '''returns Database\n\n
    getOrCreateDatabase()\n
    '''
def getOrCreateSchema():
    '''returns Schema\n\n
    getOrCreateSchema(final Database db)\n
    '''
def createTable():
    '''returns PersistentTable\n\n
    createTable(final Schema schema, final String name)\n
    '''
def createVirtualTable():
    '''returns PersistentTable\n\n
    createVirtualTable(final Schema schema, final String name)\n
    '''
def createColumn():
    '''returns Column\n\n
    createColumn(final Table table, final String name, final DataType type)\n
    '''
def createStringDataType():
    '''returns CharacterStringDataType\n\n
    createStringDataType(final int length)\n
    '''
def createBooleanDataType():
    '''returns BooleanDataType\n\n
    createBooleanDataType()\n
    '''
def createIntegerDataType():
    '''returns IntegerDataType\n\n
    createIntegerDataType()\n
    '''
def createLongDataType():
    '''returns IntegerDataType\n\n
    createLongDataType()\n
    '''
def createDoubleType():
    '''returns ApproximateNumericDataType\n\n
    createDoubleType()\n
    '''
def createDateDataType():
    '''returns DateDataType\n\n
    createDateDataType()\n
    '''
def createTimeDataType():
    '''returns TimeDataType\n\n
    createTimeDataType()\n
    '''
def createTimestampDataType():
    '''returns TimeDataType\n\n
    createTimestampDataType()\n
    '''
def createPrimaryKey():
    '''returns PrimaryKey\n\n
    createPrimaryKey(final BaseTable table, final List<Column> members)\n
    createPrimaryKey(final BaseTable table)\n
    '''
def createForeignKey():
    '''returns ForeignKey\n\n
    createForeignKey(final String name, final BaseTable sourceTable, final List<Column> sourceColumns, final BaseTable targetTable, final boolean isIdentifying, final boolean multiple)\n
    '''
def setSingleRow():
    '''returns None\n\n
    setSingleRow(final BaseTable dbmTable, final boolean b)\n
    '''
def setNotApplicable():
    '''returns None\n\n
    setNotApplicable(final PersistentTable table)\n
    '''
def finalize():
    '''returns None\n\n
    finalize()\n
    '''
def getUUID():
    '''returns String\n\n
    getUUID(final EObject eObject)\n
    '''
def setMinBound():
    '''returns None\n\n
    setMinBound(final Column col, final Column parameter, final Double value)\n
    '''
def setMaxBound():
    '''returns None\n\n
    setMaxBound(final Column col, final Column parameter, final Double value)\n
    '''
def setTimestampPrecision():
    '''returns None\n\n
    setTimestampPrecision(final Column col, final int precision)\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
