def retrieveArticle():
    '''returns Reader\n\n
    retrieveArticle(final String articleId, final ArticlePointer pointer)\n
    retrieveArticle(final String articleId)\n
    retrieveArticle()\n
    retrieveArticle(final int articleNumber, final ArticlePointer pointer)\n
    retrieveArticle(final int articleNumber)\n
    '''
def retrieveArticleHeader():
    '''returns Reader\n\n
    retrieveArticleHeader(final String articleId, final ArticlePointer pointer)\n
    retrieveArticleHeader(final String articleId)\n
    retrieveArticleHeader()\n
    retrieveArticleHeader(final int articleNumber, final ArticlePointer pointer)\n
    retrieveArticleHeader(final int articleNumber)\n
    '''
def retrieveArticleBody():
    '''returns Reader\n\n
    retrieveArticleBody(final String articleId, final ArticlePointer pointer)\n
    retrieveArticleBody(final String articleId)\n
    retrieveArticleBody()\n
    retrieveArticleBody(final int articleNumber, final ArticlePointer pointer)\n
    retrieveArticleBody(final int articleNumber)\n
    '''
def selectNewsgroup():
    '''returns boolean\n\n
    selectNewsgroup(final String newsgroup, final NewsgroupInfo info)\n
    selectNewsgroup(final String newsgroup)\n
    '''
def listHelp():
    '''returns String\n\n
    listHelp()\n
    '''
def selectArticle():
    '''returns boolean\n\n
    selectArticle(final String articleId, final ArticlePointer pointer)\n
    selectArticle(final String articleId)\n
    selectArticle(final ArticlePointer pointer)\n
    selectArticle(final int articleNumber, final ArticlePointer pointer)\n
    selectArticle(final int articleNumber)\n
    '''
def selectPreviousArticle():
    '''returns boolean\n\n
    selectPreviousArticle(final ArticlePointer pointer)\n
    selectPreviousArticle()\n
    '''
def selectNextArticle():
    '''returns boolean\n\n
    selectNextArticle(final ArticlePointer pointer)\n
    selectNextArticle()\n
    '''
def listNewsgroups():
    '''returns NewsgroupInfo[]\n\n
    listNewsgroups()\n
    listNewsgroups(final String wildmat)\n
    '''
def listNewNewsgroups():
    '''returns NewsgroupInfo[]\n\n
    listNewNewsgroups(final NewGroupsOrNewsQuery query)\n
    '''
def listNewNews():
    '''returns String[]\n\n
    listNewNews(final NewGroupsOrNewsQuery query)\n
    '''
def completePendingCommand():
    '''returns boolean\n\n
    completePendingCommand()\n
    '''
def postArticle():
    '''returns Writer\n\n
    postArticle()\n
    '''
def forwardArticle():
    '''returns Writer\n\n
    forwardArticle(final String articleId)\n
    '''
def logout():
    '''returns boolean\n\n
    logout()\n
    '''
def authenticate():
    '''returns boolean\n\n
    authenticate(final String username, final String password)\n
    '''
def retrieveArticleInfo():
    '''returns Reader\n\n
    retrieveArticleInfo(final int articleNumber)\n
    retrieveArticleInfo(final int lowArticleNumber, final int highArticleNumber)\n
    '''
def retrieveHeader():
    '''returns Reader\n\n
    retrieveHeader(final String header, final int articleNumber)\n
    retrieveHeader(final String header, final int lowArticleNumber, final int highArticleNumber)\n
    '''
