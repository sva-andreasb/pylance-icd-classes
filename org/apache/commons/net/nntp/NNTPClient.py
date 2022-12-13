def retrieveArticle():
'''public Reader retrieveArticle(final String articleId, final ArticlePointer pointer)
public Reader retrieveArticle(final String articleId)
public Reader retrieveArticle()
public Reader retrieveArticle(final int articleNumber, final ArticlePointer pointer)
public Reader retrieveArticle(final int articleNumber)
'''
pass
def retrieveArticleHeader():
'''public Reader retrieveArticleHeader(final String articleId, final ArticlePointer pointer)
public Reader retrieveArticleHeader(final String articleId)
public Reader retrieveArticleHeader()
public Reader retrieveArticleHeader(final int articleNumber, final ArticlePointer pointer)
public Reader retrieveArticleHeader(final int articleNumber)
'''
pass
def retrieveArticleBody():
'''public Reader retrieveArticleBody(final String articleId, final ArticlePointer pointer)
public Reader retrieveArticleBody(final String articleId)
public Reader retrieveArticleBody()
public Reader retrieveArticleBody(final int articleNumber, final ArticlePointer pointer)
public Reader retrieveArticleBody(final int articleNumber)
'''
pass
def selectNewsgroup():
'''public boolean selectNewsgroup(final String newsgroup, final NewsgroupInfo info)
public boolean selectNewsgroup(final String newsgroup)
'''
pass
def listHelp():
'''public String listHelp()
'''
pass
def selectArticle():
'''public boolean selectArticle(final String articleId, final ArticlePointer pointer)
public boolean selectArticle(final String articleId)
public boolean selectArticle(final ArticlePointer pointer)
public boolean selectArticle(final int articleNumber, final ArticlePointer pointer)
public boolean selectArticle(final int articleNumber)
'''
pass
def selectPreviousArticle():
'''public boolean selectPreviousArticle(final ArticlePointer pointer)
public boolean selectPreviousArticle()
'''
pass
def selectNextArticle():
'''public boolean selectNextArticle(final ArticlePointer pointer)
public boolean selectNextArticle()
'''
pass
def listNewsgroups():
'''public NewsgroupInfo[] listNewsgroups()
public NewsgroupInfo[] listNewsgroups(final String wildmat)
'''
pass
def listNewNewsgroups():
'''public NewsgroupInfo[] listNewNewsgroups(final NewGroupsOrNewsQuery query)
'''
pass
def listNewNews():
'''public String[] listNewNews(final NewGroupsOrNewsQuery query)
'''
pass
def completePendingCommand():
'''public boolean completePendingCommand()
'''
pass
def postArticle():
'''public Writer postArticle()
'''
pass
def forwardArticle():
'''public Writer forwardArticle(final String articleId)
'''
pass
def logout():
'''public boolean logout()
'''
pass
def authenticate():
'''public boolean authenticate(final String username, final String password)
'''
pass
def retrieveArticleInfo():
'''public Reader retrieveArticleInfo(final int articleNumber)
public Reader retrieveArticleInfo(final int lowArticleNumber, final int highArticleNumber)
'''
pass
def retrieveHeader():
'''public Reader retrieveHeader(final String header, final int articleNumber)
public Reader retrieveHeader(final String header, final int lowArticleNumber, final int highArticleNumber)
'''
pass
