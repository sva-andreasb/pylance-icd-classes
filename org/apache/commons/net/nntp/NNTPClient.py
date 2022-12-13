def retrieveArticle():
    '''public Reader retrieveArticle(final String articleId, final ArticlePointer pointer)
    public Reader retrieveArticle(final String articleId)
    public Reader retrieveArticle()
    public Reader retrieveArticle(final int articleNumber, final ArticlePointer pointer)
    public Reader retrieveArticle(final int articleNumber)
    '''
def retrieveArticleHeader():
    '''public Reader retrieveArticleHeader(final String articleId, final ArticlePointer pointer)
    public Reader retrieveArticleHeader(final String articleId)
    public Reader retrieveArticleHeader()
    public Reader retrieveArticleHeader(final int articleNumber, final ArticlePointer pointer)
    public Reader retrieveArticleHeader(final int articleNumber)
    '''
def retrieveArticleBody():
    '''public Reader retrieveArticleBody(final String articleId, final ArticlePointer pointer)
    public Reader retrieveArticleBody(final String articleId)
    public Reader retrieveArticleBody()
    public Reader retrieveArticleBody(final int articleNumber, final ArticlePointer pointer)
    public Reader retrieveArticleBody(final int articleNumber)
    '''
def selectNewsgroup():
    '''public boolean selectNewsgroup(final String newsgroup, final NewsgroupInfo info)
    public boolean selectNewsgroup(final String newsgroup)
    '''
def listHelp():
    '''public String listHelp()
    '''
def selectArticle():
    '''public boolean selectArticle(final String articleId, final ArticlePointer pointer)
    public boolean selectArticle(final String articleId)
    public boolean selectArticle(final ArticlePointer pointer)
    public boolean selectArticle(final int articleNumber, final ArticlePointer pointer)
    public boolean selectArticle(final int articleNumber)
    '''
def selectPreviousArticle():
    '''public boolean selectPreviousArticle(final ArticlePointer pointer)
    public boolean selectPreviousArticle()
    '''
def selectNextArticle():
    '''public boolean selectNextArticle(final ArticlePointer pointer)
    public boolean selectNextArticle()
    '''
def listNewsgroups():
    '''public NewsgroupInfo[] listNewsgroups()
    public NewsgroupInfo[] listNewsgroups(final String wildmat)
    '''
def listNewNewsgroups():
    '''public NewsgroupInfo[] listNewNewsgroups(final NewGroupsOrNewsQuery query)
    '''
def listNewNews():
    '''public String[] listNewNews(final NewGroupsOrNewsQuery query)
    '''
def completePendingCommand():
    '''public boolean completePendingCommand()
    '''
def postArticle():
    '''public Writer postArticle()
    '''
def forwardArticle():
    '''public Writer forwardArticle(final String articleId)
    '''
def logout():
    '''public boolean logout()
    '''
def authenticate():
    '''public boolean authenticate(final String username, final String password)
    '''
def retrieveArticleInfo():
    '''public Reader retrieveArticleInfo(final int articleNumber)
    public Reader retrieveArticleInfo(final int lowArticleNumber, final int highArticleNumber)
    '''
def retrieveHeader():
    '''public Reader retrieveHeader(final String header, final int articleNumber)
    public Reader retrieveHeader(final String header, final int lowArticleNumber, final int highArticleNumber)
    '''
