def getSiteRestrictionClause():
    '''    public static String getSiteRestrictionClause(final UserInfo userInfo, final String site)
    '''
def getOrgRestrictionClause():
    '''    public static String getOrgRestrictionClause(final UserInfo userInfo, final String org)
    '''
def getItemSetClause():
    '''    public static String getItemSetClause(final UserInfo userInfo, final String itemSet)
    '''
def getCompanySetClause():
    '''    public static String getCompanySetClause(final UserInfo userInfo, final String companySet)
    '''
def getSetClause():
    '''    public static String getSetClause(final UserInfo userInfo, final String itemSet, final String companySet, final int setType)
    '''
def getItemSetWhere():
    '''    public static String getItemSetWhere(final ProfileRemote profile, final boolean forLookup, final String appName, final UserInfo userInfo)
    '''
def getCompanySetWhere():
    '''    public static String getCompanySetWhere(final ProfileRemote profile, final boolean forLookup, final String appName, final UserInfo userInfo)
    '''
def getSiteOrgWhere():
    '''    public static String getSiteOrgWhere(final int siteOrgType, final ProfileRemote profile, final boolean forLookup, final String appName, final UserInfo userInfo, final String entityName)
    public static String getSiteOrgWhere(final MboSet mboSet, final int siteOrgType, final ProfileRemote profile, final boolean forLookup, final String appName, final UserInfo userInfo, final String entityName)
    '''
def getSiteFilter():
    '''    public static String getSiteFilter(final String entityName)
    public static String getSiteFilter(final String entityName, final boolean useInSubselect)
    '''
def getSiteIDs():
    '''    public static String getSiteIDs(final String appName, final UserInfo ui, final int siteOrgType, final String entityName)
    '''
def getOrgFilter():
    '''    public static String getOrgFilter(final String entityName)
    '''
def getSiteLookupFilter():
    '''    public static String getSiteLookupFilter(final MboRemote mbo)
    public static String getSiteLookupFilter(final MboRemote mbo, final ALNDomain domain)
    '''
def getOrgLookupFilter():
    '''    public static String getOrgLookupFilter(final MboRemote mbo)
    public static String getOrgLookupFilter(final MboRemote mbo, final ALNDomain domain)
    '''
