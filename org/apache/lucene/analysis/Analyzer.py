def ():
    '''returns TokenStreamComponents\n\n
    ()\n
    (final ReuseStrategy reuseStrategy)\n
    (final Consumer<Reader> source, final TokenStream result)\n
    (final Tokenizer tokenizer, final TokenStream result)\n
    (final Tokenizer tokenizer)\n
    '''
def getPositionIncrementGap():
    '''returns int\n\n
    getPositionIncrementGap(final String fieldName)\n
    '''
def getOffsetGap():
    '''returns int\n\n
    getOffsetGap(final String fieldName)\n
    '''
def setVersion():
    '''returns None\n\n
    setVersion(final Version v)\n
    '''
def getVersion():
    '''returns Version\n\n
    getVersion()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getReusableComponents():
    '''returns TokenStreamComponents\n\n
    getReusableComponents(final Analyzer analyzer, final String fieldName)\n
    getReusableComponents(final Analyzer analyzer, final String fieldName)\n
    '''
def setReusableComponents():
    '''returns None\n\n
    setReusableComponents(final Analyzer analyzer, final String fieldName, final TokenStreamComponents components)\n
    setReusableComponents(final Analyzer analyzer, final String fieldName, final TokenStreamComponents components)\n
    '''
def getTokenStream():
    '''returns TokenStream\n\n
    getTokenStream()\n
    '''
def getSource():
    '''returns Consumer<Reader>\n\n
    getSource()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def incrementToken():
    '''returns boolean\n\n
    incrementToken()\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
