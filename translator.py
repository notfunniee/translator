from translate import Translator

# Getting user input
text = input("Enter Text to Translate (Separate destination language with '#' symbol) :")
try:
    # Splitting Translation Text and Destination Language
    s_t = text.split(" # ")
    tr_txt = s_t[0]
    d_l = s_t[1]
except:
    # if above operation fails program will set input as translation text and destination language as sinhala
    tr_txt = text
    d_l = "si"

trans = Translator(to_lang=d_l)
translation = trans.translate(tr_txt)
print(translation)
