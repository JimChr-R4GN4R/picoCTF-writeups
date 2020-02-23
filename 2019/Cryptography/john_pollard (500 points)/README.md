# Description:
Sometimes RSA certificates are breakable

Certificate is in Certificate.txt in the folder
# Hints:
- The flag is in the format picoCTF{p,q}
- Try swapping p and q if it does not work

# Journey

So opened terminal and typed <code>openssl x509 -in cert -text -noout</code>

We care for this:

######################################################

Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (53 bit)
                Modulus: 4966306421059967 (0x11a4d45212b17f)
                Exponent: 65537 (0x10001)
    Signature Algorithm: md2WithRSAEncryption
    
######################################################

From here we retrieve <code>n = 4966306421059967</code> and <code>e = 65537</code>

With the help of https://www.alpertron.com.ar/ECM.HTM we can easily find p and q

<code>p = 67867967</code>

<code>q = 73176001</code>

So from the hints we see that flag is picoCTF{p,q} !

So puted picoCTF{67867967,73176001} but didn't work.

So just switched p and q.

Flag: picoCTF{73176001,67867967}
