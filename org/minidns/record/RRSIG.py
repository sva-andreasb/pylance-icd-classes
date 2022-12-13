def parse():
'''public static RRSIG parse(final DataInputStream dis, final byte[] data, final int length)
'''
pass
def RRSIG():
'''public RRSIG(final Record.TYPE typeCovered, final int algorithm, final byte labels, final long originalTtl, final Date signatureExpiration, final Date signatureInception, final int keyTag, final DnsName signerName, final byte[] signature)
public RRSIG(final Record.TYPE typeCovered, final int algorithm, final byte labels, final long originalTtl, final Date signatureExpiration, final Date signatureInception, final int keyTag, final String signerName, final byte[] signature)
public RRSIG(final Record.TYPE typeCovered, final DnssecConstants.SignatureAlgorithm algorithm, final byte labels, final long originalTtl, final Date signatureExpiration, final Date signatureInception, final int keyTag, final DnsName signerName, final byte[] signature)
public RRSIG(final Record.TYPE typeCovered, final DnssecConstants.SignatureAlgorithm algorithm, final byte labels, final long originalTtl, final Date signatureExpiration, final Date signatureInception, final int keyTag, final String signerName, final byte[] signature)
'''
pass
def serialize():
'''public void serialize(final DataOutputStream dos)
'''
pass
def writePartialSignature():
'''public void writePartialSignature(final DataOutputStream dos)
'''
pass
def toString():
'''public String toString()
'''
pass
