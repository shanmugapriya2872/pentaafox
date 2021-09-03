Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def check(word):
    new=word
    for i in range(len(word)):
        count=word.count(word[i])
        if count>=2:
            occur=word.find(word[i])
            new=word[:occur+1]+str(count)+word[occur+count:]
    print(new,end=" ")

text=list(map(str,input().split()))
for i in range(len(text)):
    check(text[i])