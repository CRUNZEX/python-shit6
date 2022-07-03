import re

class checkRegx:
    def __init__(self, word):
        self.word = word
        self.checkTH = False
        self.checkEN = False

    def checkWordTH(self):
        _check = re.search(u'[\u0E00-\u0E7F]', self.word)
        if _check :
            self.checkTH = True
        return self.checkTH

    def checkWordEN(self):
        _check = re.search(u'[A-Za-z0-9]', self.word)
        if _check :
            self.checkEN = True
        return self.checkEN 

    def getCheckTH(self):
        return self.checkTH

    def getCheckEN(self):
        return self.checkEN

    

# """
# แตก เมื่อ เป็นคำผสม เพราะมันจะเช็คไทยก่อนถ้ามี ก็ได้ Thai เลย
# """
# import re
# _input = input('Enter : ')

# def checkTH(word):
#     regexp_thai = re.search(u"[\u0E00-\u0E7F]", word) # u"[\u0E00-\u0E7F' ]|^'|'$|''"
#     # print("THAI: ", regexp_thai)
#     return regexp_thai
    
# def checkEN(word):
#     regex_en = re.search(u"[a-zA-Z0-9]", word) # u"[a-zA-Z' ]|^'|'$|''"
#     # print("ENG: ", regex_en)
#     return regex_en

# def check(word):
#     return 'Thai' if checkTH(word) else ('Eng' if checkEN(word) else 'oh o//' )
#     # return checkTH(word), checkEN(word)

# # print(checkTH(_input))
# # print(checkEN(_input))
# print(check(_input))