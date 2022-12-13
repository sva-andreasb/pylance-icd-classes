def SQLConverterUtil():
    '''public SQLConverterUtil(final Connection conparam, final PrintStream outparam, final String schemaOwnerparam)
    '''
def cacheSequences():
    '''public HashMap<String, String> cacheSequences(final String tableName)
    '''
def writeDumpTable():
    '''public int writeDumpTable(final String tbname, TreeMap tableCols, final PrintStream out, int maxLines, int numLines, final Unlcvt unlcvt, final boolean psFormat, final String whereClause, final boolean addRowStamp, final boolean useSequence, final boolean defaultDate, final boolean addDelete, final boolean skipLangCode, final int fileType, final String grantApp, List<Element> allData)
    '''
def buildSelectStatement():
    '''public String buildSelectStatement(final String tbname, final TreeMap tableCols, final boolean includeDroppedCols, final boolean addRowstamp, final boolean addtenantID, final String colNameList)
    '''
def buildInsertValuesStatement():
    '''public TreeMap<Integer, String> buildInsertValuesStatement(final String prefix, final ResultSet rs, final TreeMap tableCols, final boolean includeDroppedCols, final String rowstampValue, final boolean psFormat, final boolean defaultDate, final HashMap<String, String> allSeq, final String whereClause, final boolean dbc, final boolean addTenantID)
    '''
def buildInsertElementDBC():
    '''public Element buildInsertElementDBC(final String tbname, final ResultSet rs, final TreeMap tableCols, final List<Element> allData, Element header, final boolean defaultDate, final HashMap<String, String> allSeq, final boolean allowReplace)
    '''
def buildCSVfile():
    '''public List<String> buildCSVfile(final String tbname, final ResultSet rs, final TreeMap tableCols, final boolean addColumns)
    '''
def buildDBCFile():
    '''public byte[] buildDBCFile(final String fileName, final String dir, final List<Element> allData, final String scriptType, final boolean demoOnly)
    '''
def buildFreeForm():
    '''public List<Element> buildFreeForm(final List<Element> allData, final String data, final String name)
    '''
def getFileName():
    '''public String getFileName(final String dirName, final String name, final String ext)
    '''
def buildDefaineTableDBC():
    '''public void buildDefaineTableDBC(final String tbname, final boolean mainObject, final List<Element> allData, final boolean addDelete)
    '''
def buildCreateRelationshipDBC():
    '''public void buildCreateRelationshipDBC(final String parent, final String child, final String name, final String whereClause, final String remarks, final List<Element> allData)
    '''
def buildCreateSigOptionDBC():
    '''public void buildCreateSigOptionDBC(final String app, final String optionName, final int esigenabled, final int visible, final String description, final String alsoGrants, final String alsoRevokes, final String prereq, final String langCode, final String grantApp, final boolean addDelete, final List<Element> allData)
    '''
def getMaxRowstamp():
    '''public Object getMaxRowstamp(final String tableName)
    '''
def buildRecordList():
    '''public String buildRecordList(final String tableName, final long maxRowStamp)
    '''
def buildRecordWhere():
    '''public String buildRecordWhere(final String tableName, final long maxRowStamp)
    '''
