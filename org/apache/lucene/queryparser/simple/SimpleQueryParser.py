AND_OPERATOR = "int  1"
NOT_OPERATOR = "int  2"
OR_OPERATOR = "int  4"
PREFIX_OPERATOR = "int  8"
PHRASE_OPERATOR = "int  16"
PRECEDENCE_OPERATORS = "int  32"
ESCAPE_OPERATOR = "int  64"
WHITESPACE_OPERATOR = "int  128"
FUZZY_OPERATOR = "int  256"
NEAR_OPERATOR = "int  512"
def SimpleQueryParser():
    '''public SimpleQueryParser(final Analyzer analyzer, final String field)
    public SimpleQueryParser(final Analyzer analyzer, final Map<String, Float> weights)
    public SimpleQueryParser(final Analyzer analyzer, final Map<String, Float> weights, final int flags)
    '''
def parse():
    '''public Query parse(final String queryText)
    '''
def setDefaultOperator():
    '''public void setDefaultOperator(final BooleanClause.Occur operator)
    '''
