def reportError():
    '''returns None\n\n
    reportError(final BaseRecognizer br, final RecognitionException re)\n
    '''
def recover():
    '''returns None\n\n
    recover(final Lexer lex, final RecognitionException re)\n
    recover(final BaseRecognizer br, final IntStream input, final RecognitionException re)\n
    '''
def mismatch():
    '''returns boolean\n\n
    mismatch(final BaseRecognizer br, final IntStream input, final int ttype, final BitSet follow)\n
    '''
def recoverFromMismatchedToken():
    '''returns Object\n\n
    recoverFromMismatchedToken(final BaseRecognizer br, final IntStream input, final int ttype, final BitSet follow)\n
    '''
def errorExpr():
    '''returns expr\n\n
    errorExpr(final PythonTree t)\n
    '''
def errorMod():
    '''returns mod\n\n
    errorMod(final PythonTree t)\n
    '''
def errorSlice():
    '''returns slice\n\n
    errorSlice(final PythonTree t)\n
    '''
def errorStmt():
    '''returns stmt\n\n
    errorStmt(final PythonTree t)\n
    '''
def error():
    '''returns None\n\n
    error(final String message, final PythonTree t)\n
    '''
