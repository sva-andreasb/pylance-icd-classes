def PublicSuffixMatcher():
'''public PublicSuffixMatcher(final Collection<String> rules, final Collection<String> exceptions)
public PublicSuffixMatcher(final DomainType domainType, final Collection<String> rules, final Collection<String> exceptions)
public PublicSuffixMatcher(final Collection<PublicSuffixList> lists)
'''
pass
def getDomainRoot():
'''public String getDomainRoot(final String domain)
public String getDomainRoot(final String domain, final DomainType expectedType)
'''
pass
def matches():
'''public boolean matches(final String domain)
public boolean matches(final String domain, final DomainType expectedType)
'''
pass