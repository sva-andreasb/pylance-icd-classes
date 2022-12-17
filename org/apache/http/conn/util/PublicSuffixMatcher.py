def ():
    '''returns PublicSuffixMatcher\n\n
    (final Collection<String> rules, final Collection<String> exceptions)\n
    (final DomainType domainType, final Collection<String> rules, final Collection<String> exceptions)\n
    (final Collection<PublicSuffixList> lists)\n
    '''
def getDomainRoot():
    '''returns String\n\n
    getDomainRoot(final String domain)\n
    getDomainRoot(final String domain, final DomainType expectedType)\n
    '''
def matches():
    '''returns boolean\n\n
    matches(final String domain)\n
    matches(final String domain, final DomainType expectedType)\n
    '''
