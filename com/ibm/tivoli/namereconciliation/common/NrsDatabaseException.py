DATABASE_DEADLOCK = "int  2001"
ERROR_TEXT_DATABASE_DEADLOCK = "String  The database identified a deadlock condition. Please attempt this Request at a later time.""
STRING_TOO_LONG_TRUNCATED = "int  2002"
ERROR_TEXT_STRING_TOO_LONG_TRUNCATED = "String  The length of a string provided has exceeded the maximum length. Shorten the string length and try the request again.""
DATABASE_CONNECTION_ERROR = "int  2003"
ERROR_TEXT_DATABASE_CONNECTION_ERROR = "String  An Error has occurred in establishing a database connection. ""
DATABASE_CONNECTION_SHUTDOWN_ERROR = "int  2004"
ERROR_TEXT_DATABASE_CONNECTION_SHUTDOWN_ERROR = "String  An Error has occurred in closing a database connection. ""
DATABASE_CONNECTION_CLOSED_ERROR = "int  2005"
ERROR_TEXT_DATABASE_CONNECTION_CLOSED_ERROR = "String  A database has been closed. Need to re-establish the connection and/or call init()to refresh the cache""
OTHER_DATABASE_ERRORS = "int  3001"
ERROR_TEXT_OTHER_DATABASE_ERRORS = "String  An unexpected database system error has occurred. ""
def NrsDatabaseException():
'''public NrsDatabaseException(final int errorCode)
'''
pass
def getErrorText():
'''public static String getErrorText(final int errorCode)
'''
pass
def toString():
'''public String toString()
'''
pass
