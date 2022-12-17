def ():
    '''returns RRSIG\n\n
    (final Record.TYPE typeCovered, final int algorithm, final byte labels, final long originalTtl, final Date signatureExpiration, final Date signatureInception, final int keyTag, final DnsName signerName, final byte[] signature)\n
    (final Record.TYPE typeCovered, final int algorithm, final byte labels, final long originalTtl, final Date signatureExpiration, final Date signatureInception, final int keyTag, final String signerName, final byte[] signature)\n
    (final Record.TYPE typeCovered, final DnssecConstants.SignatureAlgorithm algorithm, final byte labels, final long originalTtl, final Date signatureExpiration, final Date signatureInception, final int keyTag, final DnsName signerName, final byte[] signature)\n
    (final Record.TYPE typeCovered, final DnssecConstants.SignatureAlgorithm algorithm, final byte labels, final long originalTtl, final Date signatureExpiration, final Date signatureInception, final int keyTag, final String signerName, final byte[] signature)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final DataOutputStream dos)\n
    '''
def writePartialSignature():
    '''returns None\n\n
    writePartialSignature(final DataOutputStream dos)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
