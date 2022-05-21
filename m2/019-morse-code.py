#this program convert a string insered by the user in a morse coding
msg=input('insert a word for convert in morse coding')
morse_coding={
    "a":"._", "b":"_...", 
    "c":"_._.", "d":"_..", 
    "e":".", "f":".._.", 
    "g":"__.", "h":"....", 
    "i":"..", "j":".___", 
    "k":"_._", "l":"._..", 
    "m":"__", "n":"_.", 
    "o":"___", "p":".__.", 
    "q":"__._", "r":"._.", 
    "s":"...", "t":"_", 
    "u":".._", "v":"..._", 
    "w":".__", "x":"_.._", 
    "y":"_.__", "z":"__..", 
    "à":".__._", "é":".._..", 
    "1":".____", "2":"..___", 
    "3":"...__", "4":"...._", 
    "5":".....", "6":"_....", 
    "7":"__...", "8":"___..", 
    "9":"____.", "0":"_____"
    }
text=str()
for i in range(0,len(msg)):
    if msg[i] in morse_coding:
        text += morse_coding[msg[i]]
        text += ' '
print(text)