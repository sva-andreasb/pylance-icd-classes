MESSAGE_PREFIX = "String  \"message.prefix\""
KEY_CODE_SUFFIX = "String  \".code\""
KEY_DESCRIPTION_SUFFIX = "String  \".description\""
def ():
    '''returns MessageHandler\n\n
    (final String bundleName)\n
    (final String bundleName, final ClassLoader loader)\n
    (final String bundleName, final boolean safeMode, final ClassLoader loader)\n
    '''
def getResourceBundle():
    '''returns ResourceBundle\n\n
    getResourceBundle(final String localeName)\n
    '''
def getLocalizedMessageWithLocale():
    '''returns String\n\n
    getLocalizedMessageWithLocale(final String localeName, final String key, final Object... args)\n
    '''
def getLocalizedMessage():
    '''returns String\n\n
    getLocalizedMessage(final String key, final Object... args)\n
    '''
