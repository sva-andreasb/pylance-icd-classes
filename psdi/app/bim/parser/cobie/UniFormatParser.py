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
def UniFormatParser():
    '''public UniFormatParser(final MessageLogger logger, final String fileName)
    '''
def execute():
    '''public void execute()
    '''
def getRootClass():
    '''public UniFormat getRootClass()
    '''
def parseUniFormat():
    '''public String[] parseUniFormat(final UniFormat parentClass, String[] values)
    '''
def buildLevelOneTree():
    '''public String[] buildLevelOneTree(final UniFormat parentClass, String[] values, final int idx_level)
    '''
def buildLevelTwoTree():
    '''public String[] buildLevelTwoTree(final UniFormat parentClass, String[] values, final int idx_level)
    '''
def buildLevelThreeTree():
    '''public String[] buildLevelThreeTree(final UniFormat parentClass, String[] values, final int idx_level)
    '''
def validateHeaderRow():
    '''public String[] validateHeaderRow(String[] values)
    '''
def parseHeaderRow():
    '''public String[] parseHeaderRow(String[] values)
    '''
def buildUniformatClass():
    '''public UniFormat buildUniformatClass(final int idx_level, final String[] values, final int level)
    '''
def buildUniformatXMLClass():
    '''public UniFormat buildUniformatXMLClass(final XmlnputTokenizer _tokenizer, final int level, final HashMap<Integer, String> wbs)
    '''
def main():
    '''public static void main(final String[] args)
    '''
