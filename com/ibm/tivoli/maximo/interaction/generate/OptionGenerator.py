def OptionGenerator():
    '''    public OptionGenerator()
    '''
def addOption():
    '''    public String addOption(final String appName, final String interaction, final String description, final UserInfo userInfo, final boolean createMenu, final MXTransaction trans, final Vector selected, final boolean isSilent)
    public String addOption(final String appName, final String interaction, final String mapOption, final MXTransaction trans, final UserInfo userInfo, final Vector selected)
    '''
def deleteOption():
    '''    public void deleteOption(final String appName, final String optionName, final UserInfo userInfo, final MXTransaction trans)
    '''
def includeSigOption():
    '''    public String includeSigOption(final String interaction, final String appName, final String sigName, final String sigDesc, final boolean isSilent, final Document appDocument, final UserInfo userInfo, final MXTransaction trans, int start)
    '''
def addSigOption():
    '''    public String addSigOption(final String appName, final String sigName, final String sigDesc, final UserInfo userInfo, final MXTransaction trans)
    public String addSigOption(final String appName, final String sigName, final String sigDesc, final String alsoGrants, final String alsoRevokes, final String prerequisite, final UserInfo userInfo, final MXTransaction trans)
    '''
def includeAppAuth():
    '''    public void includeAppAuth(final String appName, final String sigName, final UserInfo userInfo, final MXTransaction trans, final Vector selected)
    public void includeAppAuth(final String appName, final String sigName, final String conditionNum, final UserInfo userInfo, final MXTransaction trans, final Vector selected)
    public void includeAppAuth(final String appName, final String sigName, final String conditionNum, final UserInfo userInfo, final MXTransaction trans, final Set<String> groupNames)
    '''
def addAllAppAuth():
    '''    public void addAllAppAuth(final String appName, final String sigName, final String prerequisite, final UserInfo userInfo, final MXTransaction trans)
    public void addAllAppAuth(final String appName, final String sigName, String prerequisite, final String conditionNum, final UserInfo userInfo, final MXTransaction trans)
    '''
def addAppToolOption():
    '''    public int addAppToolOption(final String appName, final String sigName, final String imageSource, int preferredSpot, final UserInfo userInfo, final MXTransaction trans)
    '''
def addMenuOption():
    '''    public void addMenuOption(final String appName, final String sigName, final String menuType, final int preferredSpot, final int preferredSubSpot, final String tabDisplay, final String imageSource, final UserInfo userInfo, final MXTransaction trans)
    public void addMenuOption(final String appName, final String sigName, final String menuType, final int preferredSpot, final int preferredSubSpot, final String tabDisplay, final String imageSource, final String accessKey, final UserInfo userInfo, final MXTransaction trans)
    '''
def checkSigOption():
    '''    public MboSetRemote checkSigOption(final String appName, final String sigName, final UserInfo userInfo)
    '''
def checkMenuOption():
    '''    public MboSetRemote checkMenuOption(final String appName, final String sigName, final UserInfo userInfo)
    '''
