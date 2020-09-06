import string
def String_preet(Str):
    new=''
    for i in Str:
        if i=='':
            Ascii=ord(i)
        else:
            for j in string.punctuation:
                if i==j:
                    Ascii=ord(i)
                    break
                Ascii=(ord(i)-3)
                if i.isnumeric():
                    Ascii=ord(i)
                if i.isalpha():
                    if((i.isupper()and Ascii>90)or(i.islower() and Ascii>122)):
                        Ascii=Ascii-26
                    if((i.isupper and Ascii<65) or (i.islower() and Ascii<97)):
                        Ascii=Ascii+26
                    new=new+chr(Ascii)
                print(new)
                
Str=input("enter the string:")
String_preet(Str)
        
