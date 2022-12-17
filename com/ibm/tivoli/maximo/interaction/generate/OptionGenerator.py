def ():
    '''returns OptionGenerator\n\n
    ()\n
    '''
def addOption():
    '''returns String\n\n
    addOption(final String appName, final String interaction, final String description, final UserInfo userInfo, final boolean createMenu, final MXTransaction trans, final Vector selected, final boolean isSilent)\n
    addOption(final String appName, final String interaction, final String mapOption, final MXTransaction trans, final UserInfo userInfo, final Vector selected)\n
    '''
def deleteOption():
    '''returns None\n\n
    deleteOption(final String appName, final String optionName, final UserInfo userInfo, final MXTransaction trans)\n
    '''
def includeSigOption():
    '''returns String\n\n
    includeSigOption(final String interaction, final String appName, final String sigName, final String sigDesc, final boolean isSilent, final Document appDocument, final UserInfo userInfo, final MXTransaction trans, int start)\n
    '''
def addSigOption():
    '''returns String\n\n
    addSigOption(final String appName, final String sigName, final String sigDesc, final UserInfo userInfo, final MXTransaction trans)\n
    addSigOption(final String appName, final String sigName, final String sigDesc, final String alsoGrants, final String alsoRevokes, final String prerequisite, final UserInfo userInfo, final MXTransaction trans)\n
    '''
def includeAppAuth():
    '''returns None\n\n
    includeAppAuth(final String appName, final String sigName, final UserInfo userInfo, final MXTransaction trans, final Vector selected)\n
    includeAppAuth(final String appName, final String sigName, final String conditionNum, final UserInfo userInfo, final MXTransaction trans, final Vector selected)\n
    includeAppAuth(final String appName, final String sigName, final String conditionNum, final UserInfo userInfo, final MXTransaction trans, final Set<String> groupNames)\n
    '''
def addAllAppAuth():
    '''returns None\n\n
    addAllAppAuth(final String appName, final String sigName, final String prerequisite, final UserInfo userInfo, final MXTransaction trans)\n
    addAllAppAuth(final String appName, final String sigName, String prerequisite, final String conditionNum, final UserInfo userInfo, final MXTransaction trans)\n
    '''
def addAppToolOption():
    '''returns int\n\n
    addAppToolOption(final String appName, final String sigName, final String imageSource, int preferredSpot, final UserInfo userInfo, final MXTransaction trans)\n
    '''
def addMenuOption():
    '''returns None\n\n
    addMenuOption(final String appName, final String sigName, final String menuType, final int preferredSpot, final int preferredSubSpot, final String tabDisplay, final String imageSource, final UserInfo userInfo, final MXTransaction trans)\n
    addMenuOption(final String appName, final String sigName, final String menuType, final int preferredSpot, final int preferredSubSpot, final String tabDisplay, final String imageSource, final String accessKey, final UserInfo userInfo, final MXTransaction trans)\n
    '''
def checkSigOption():
    '''returns MboSetRemote\n\n
    checkSigOption(final String appName, final String sigName, final UserInfo userInfo)\n
    '''
def checkMenuOption():
    '''returns MboSetRemote\n\n
    checkMenuOption(final String appName, final String sigName, final UserInfo userInfo)\n
    '''
