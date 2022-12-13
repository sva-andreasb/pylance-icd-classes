def JDocComment():
    '''public JDocComment(final JCodeModel owner)
    '''
def append():
    '''public JDocComment append(final Object o)
    '''
def addParam():
    '''public JCommentPart addParam(final String param)
    public JCommentPart addParam(final JVar param)
    '''
def addThrows():
    '''public JCommentPart addThrows(final Class<? extends Throwable> exception)
    public JCommentPart addThrows(final JClass exception)
    '''
def addReturn():
    '''public JCommentPart addReturn()
    '''
def addDeprecated():
    '''public JCommentPart addDeprecated()
    '''
def addXdoclet():
    '''public Map<String, String> addXdoclet(final String name)
    public Map<String, String> addXdoclet(final String name, final Map<String, String> attributes)
    public Map<String, String> addXdoclet(final String name, final String attribute, final String value)
    '''
def generate():
    '''public void generate(final JFormatter f)
    '''
