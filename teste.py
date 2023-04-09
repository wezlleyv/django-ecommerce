a = ".... . -.--   .--- ..- -.. ."
'''text = ""
for word in a:
    if a[-1] == word: text += word
    else: text += f"{word} "
'''
list_text = []
text_cache = ''
text = ""

for x in range(0, len(a)):
    if len(a) == x+1:
            list_text.append(text_cache + a[-1])
    try:
        if a[x] == " ":
            if not text_cache == "":
                list_text.append(text_cache)
                text_cache = ""

            if a[x+1] == " " and a[x+2] == " ":
                list_text.append(" ")
        else:
            text_cache += a[x]

    except: pass

print(list_text)

for x in list_text:
     if x == " ": text += " "
     else: text += x
print(text)