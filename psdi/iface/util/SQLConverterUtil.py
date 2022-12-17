def ():
    '''returns SQLConverterUtil\n\n
    (final Connection conparam, final PrintStream outparam, final String schemaOwnerparam)\n
    '''
def writeDumpTable():
    '''returns int\n\n
    writeDumpTable(final String tbname, TreeMap tableCols, final PrintStream out, int maxLines, int numLines, final Unlcvt unlcvt, final boolean psFormat, final String whereClause, final boolean addRowStamp, final boolean useSequence, final boolean defaultDate, final boolean addDelete, final boolean skipLangCode, final int fileType, final String grantApp, List<Element> allData)\n
    '''
def buildSelectStatement():
    '''returns String\n\n
    buildSelectStatement(final String tbname, final TreeMap tableCols, final boolean includeDroppedCols, final boolean addRowstamp, final boolean addtenantID, final String colNameList)\n
    '''
def buildInsertElementDBC():
    '''returns Element\n\n
    buildInsertElementDBC(final String tbname, final ResultSet rs, final TreeMap tableCols, final List<Element> allData, Element header, final boolean defaultDate, final HashMap<String, String> allSeq, final boolean allowReplace)\n
    '''
def buildCSVfile():
    '''returns List<String>\n\n
    buildCSVfile(final String tbname, final ResultSet rs, final TreeMap tableCols, final boolean addColumns)\n
    '''
def buildDBCFile():
    '''returns byte[]\n\n
    buildDBCFile(final String fileName, final String dir, final List<Element> allData, final String scriptType, final boolean demoOnly)\n
    '''
def buildFreeForm():
    '''returns List<Element>\n\n
    buildFreeForm(final List<Element> allData, final String data, final String name)\n
    '''
def getFileName():
    '''returns String\n\n
    getFileName(final String dirName, final String name, final String ext)\n
    '''
def buildDefaineTableDBC():
    '''returns None\n\n
    buildDefaineTableDBC(final String tbname, final boolean mainObject, final List<Element> allData, final boolean addDelete)\n
    '''
def buildCreateRelationshipDBC():
    '''returns None\n\n
    buildCreateRelationshipDBC(final String parent, final String child, final String name, final String whereClause, final String remarks, final List<Element> allData)\n
    '''
def buildCreateSigOptionDBC():
    '''returns None\n\n
    buildCreateSigOptionDBC(final String app, final String optionName, final int esigenabled, final int visible, final String description, final String alsoGrants, final String alsoRevokes, final String prereq, final String langCode, final String grantApp, final boolean addDelete, final List<Element> allData)\n
    '''
def getMaxRowstamp():
    '''returns Object\n\n
    getMaxRowstamp(final String tableName)\n
    '''
def buildRecordList():
    '''returns String\n\n
    buildRecordList(final String tableName, final long maxRowStamp)\n
    '''
def buildRecordWhere():
    '''returns String\n\n
    buildRecordWhere(final String tableName, final long maxRowStamp)\n
    '''
