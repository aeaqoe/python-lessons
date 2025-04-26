# with open('tekst.txt', encoding='utf=8') as f:
#     teksts = f.read

# teksts_list = []
# bann = [' ', '.', ',', '!', '?', '"', '(', ')', '\n']
# tekst_word = ''
# for l in teksts:
#     l = l.lower()
   
#     if l not in bann:
#         tekst_word += l
#     else:
#         if tekst_word:
#             tekst_word.append(tekst_word)
#         tekst_word = ''
# check_dupes = {}
# for w in teksts_list:
    
#     if l not in check_dupes:
#         check_dupes[l] = 1
#     else:
#         check_dupes[l] += 1
