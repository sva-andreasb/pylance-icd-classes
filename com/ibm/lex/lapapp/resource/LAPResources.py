LANGUAGE_KEY = "String  \"language\""
TITLE_KEY = "String  \"title\""
HEADING_KEY = "String  \"heading\""
FOOTING_KEY = "String  \"footing\""
ACCEPT_KEY = "String  \"accept\""
DECLINE_KEY = "String  \"decline\""
PRINT_KEY = "String  \"print\""
YES_KEY = "String  \"yes\""
NO_KEY = "String  \"no\""
ACCEPTED_URL_KEY = "String  \"url.accepted\""
DECLINED_URL_KEY = "String  \"url.declined\""
FONT_SIZE_KEY = "String  \"fontSize\""
CONFIRM_MESSAGE_KEY = "String  \"declinedMessage\""
CONFIRM_MSG_A_KEY = "String  \"declinedMsgA\""
CONFIRM_MSG_B_KEY = "String  \"declinedMsgB\""
CLILANGMSG_KEY = "String  \"clilangmsg\""
CLILANG2MSG_KEY = "String  \"clilang2msg\""
CLIMSG1_KEY = "String  \"climsg1\""
CLIMSG2_KEY = "String  \"climsg2\""
CLICONTMSG_KEY = "String  \"clicontmsg\""
CLICONTMSG_NONIBM_KEY = "String  \"clicontmsgnonibm\""
CLICONTMSG_NOPRINT_KEY = "String  \"clicontmsgnoprint\""
CLICONTMSG_NOPRINT_NONIBM_KEY = "String  \"clicontmsgnoprintnonibm\""
CLICONTMSG_ENGONLY_KEY = "String  \"clicontmsgengonly\""
CLICONTMSG_ENGONLY_NONIBM_KEY = "String  \"clicontmsgengonlynonibm\""
CLICONTMSG_ENGONLY_NOPRINT_KEY = "String  \"clicontmsgengonlynoprint\""
CLICONTMSG_ENGONLY_NOPRINT_NONIBM_KEY = "String  \"clicontmsgengonlynoprintnonibm\""
CLICFMMSG_KEY = "String  \"clicfmmsg\""
CLIACCMSG_KEY = "String  \"cliaccmsg\""
ASSUMED_FONT_WIDTH_KEY = "String  \"assumedFontWidth\""
ASSUMED_FONT_HEIGHT_KEY = "String  \"assumedFontHeight\""
CLICONTMSG_LANGREPLACE = "String  \"REPLACEWITHLANG\""
PRINT_ERROR_MSG_KEY = "String  \"printError\""
PRINT_ERROR_MSG_KEY_A = "String  \"printErrorA\""
PRINT_ERROR_MSG_KEY_B = "String  \"printErrorB\""
PRINTING_ERROR_TITLE = "String  \"printing_error_title\""
PRINTING_ERROR_NO_PRINTERS = "String  \"printing_error_no_printers\""
NON_IBM_KEY = "String  \"non_ibm_key\""
def ():
    '''returns LAPResources\n\n
    (final String laPath)\n
    (final URL laURL)\n
    '''
def getFontSize():
    '''returns int\n\n
    getFontSize()\n
    '''
def getImage():
    '''returns Image\n\n
    getImage(final String s)\n
    getImage(final String str, final ImageObserver imageObserver)\n
    '''
def getLocale():
    '''returns Locale\n\n
    getLocale()\n
    '''
def getText():
    '''returns String\n\n
    getText(final String key)\n
    '''
def getMessage():
    '''returns String[]\n\n
    getMessage(final String s)\n
    '''
def setLocale():
    '''returns None\n\n
    setLocale(final Locale locale)\n
    '''
