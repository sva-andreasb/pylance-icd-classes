def getSiteRestrictionClause():
'''public static String getSiteRestrictionClause(final UserInfo userInfo, final String site)
'''
pass
def getOrgRestrictionClause():
'''public static String getOrgRestrictionClause(final UserInfo userInfo, final String org)
'''
pass
def getItemSetClause():
'''public static String getItemSetClause(final UserInfo userInfo, final String itemSet)
'''
pass
def getCompanySetClause():
'''public static String getCompanySetClause(final UserInfo userInfo, final String companySet)
'''
pass
def getSetClause():
'''public static String getSetClause(final UserInfo userInfo, final String itemSet, final String companySet, final int setType)
'''
pass
def getItemSetWhere():
'''public static String getItemSetWhere(final ProfileRemote profile, final boolean forLookup, final String appName, final UserInfo userInfo)
'''
pass
def getCompanySetWhere():
'''public static String getCompanySetWhere(final ProfileRemote profile, final boolean forLookup, final String appName, final UserInfo userInfo)
'''
pass
def getSiteOrgWhere():
'''public static String getSiteOrgWhere(final int siteOrgType, final ProfileRemote profile, final boolean forLookup, final String appName, final UserInfo userInfo, final String entityName)
public static String getSiteOrgWhere(final MboSet mboSet, final int siteOrgType, final ProfileRemote profile, final boolean forLookup, final String appName, final UserInfo userInfo, final String entityName)
'''
pass
def getSiteFilter():
'''public static String getSiteFilter(final String entityName)
public static String getSiteFilter(final String entityName, final boolean useInSubselect)
'''
pass
def getSiteIDs():
'''public static String getSiteIDs(final String appName, final UserInfo ui, final int siteOrgType, final String entityName)
'''
pass
def getOrgFilter():
'''public static String getOrgFilter(final String entityName)
'''
pass
def getSiteLookupFilter():
'''public static String getSiteLookupFilter(final MboRemote mbo)
public static String getSiteLookupFilter(final MboRemote mbo, final ALNDomain domain)
'''
pass
def getOrgLookupFilter():
'''public static String getOrgLookupFilter(final MboRemote mbo)
public static String getOrgLookupFilter(final MboRemote mbo, final ALNDomain domain)
'''
pass
