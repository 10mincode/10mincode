from textblob import TextBlob

def correct(a):
    b = TextBlob(a.lower())
    return b.correct()
if __name__=="__main__":
    while True:
        a=input("Incorrect word/line/para ")
        b=TextBlob(a.lower())
        print(f'Original Word is {a}')
        print(f'The correct word is {b.correct()}')

        c=input("write yes to ask more ")
        if c.lower()=="yes":
            continue
        else:
            break
