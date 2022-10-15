import os

try:
    import wikipedia
except:
    try:
        os.system("pip3 install wikipedia")
    except:
        try:
            os.system("pip install wikipedia")
        except:
            print("\n Error...")
            exit()

def wiki_serch():
    wikipedia.set_lang("en")
    wiki_serch = input("\n Type what you want to search: ")
    if(wiki_serch == ""):
        print("\n Error")
    else:
        try:
            print("\n\n", wikipedia.summary(wiki_serch), "\n\n")
        except:
            print("\n Nothing found :(")
wiki_serch()