TITLE_LEVEL_1 = "String  \"Level 1\""
TITLE_LEVEL_2 = "String  \"Level 2\""
TITLE_LEVEL_3 = "String  \"Level 3\""
TITLE_LEVEL_4 = "String  \"Level 4\""
TITLE_LEVEL_5 = "String  \"Level 5\""
TITLE_LEVEL_6 = "String  \"Level 6\""
TITLE_LEVEL_7 = "String  \"Level 7\""
LEVEL_1 = "int  1"
LEVEL_2 = "int  2"
LEVEL_3 = "int  3"
LEVEL_4 = "int  4"
SHEET_UNIFORMAT = "String  \"UniFormat\""
CATALOG_TAG = "String  \"Catalog\""
ITEM_GROUP_TAG = "String  \"ItemGroup\""
WBS_TAG = "String  \"WBS\""
NAME_TAG = "String  \"Name\""
def ():
    '''returns UniFormatParser\n\n
    (final MessageLogger logger, final String fileName)\n
    '''
def execute():
    '''returns None\n\n
    execute()\n
    '''
def getRootClass():
    '''returns UniFormat\n\n
    getRootClass()\n
    '''
def parseUniFormat():
    '''returns String[]\n\n
    parseUniFormat(final UniFormat parentClass, String[] values)\n
    '''
def buildLevelOneTree():
    '''returns String[]\n\n
    buildLevelOneTree(final UniFormat parentClass, String[] values, final int idx_level)\n
    '''
def buildLevelTwoTree():
    '''returns String[]\n\n
    buildLevelTwoTree(final UniFormat parentClass, String[] values, final int idx_level)\n
    '''
def buildLevelThreeTree():
    '''returns String[]\n\n
    buildLevelThreeTree(final UniFormat parentClass, String[] values, final int idx_level)\n
    '''
def validateHeaderRow():
    '''returns String[]\n\n
    validateHeaderRow(String[] values)\n
    '''
def parseHeaderRow():
    '''returns String[]\n\n
    parseHeaderRow(String[] values)\n
    '''
def buildUniformatClass():
    '''returns UniFormat\n\n
    buildUniformatClass(final int idx_level, final String[] values, final int level)\n
    '''
def buildUniformatXMLClass():
    '''returns UniFormat\n\n
    buildUniformatXMLClass(final XmlnputTokenizer _tokenizer, final int level, final HashMap<Integer, String> wbs)\n
    '''
