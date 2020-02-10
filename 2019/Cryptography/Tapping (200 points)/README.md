# Description:
Theres tapping coming in from the wires. What's it saying <code>nc 2019shell1.picoctf.com 21897</code>.

# Hints:
- What kind of encoding uses dashes and dots?
- The flag is in the format PICOCTF{}

# Juorney

If we execute <code>nc 2019shell1.picoctf.com 21897 in terminal, we get this:
.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. .---- ---.. .---- ---.. ..--- ..--- ....- ..... --... ..... }

This is clearly MORSE

If we go to a MORSE translator (and remove {}) then we get this:
PICOCTFM0RS3C0D31SFUN1818224575

Flag: PICOCTF{M0RS3C0D31SFUN1818224575}
