from easygui import integerbox, msgbox, textbox


def Queue(*args) -> list:
    return [x for x in args]


def addToQueue(e, queue: list):
    queue.append(e)


def pull(queue:list):
    if(len(queue) > 0):
        return queue.pop(0)
    else:
        return None
def printOptions():
    print("Menu de la queue:")
    print("1: ajouter element")
    print("2: dépiler le premier element")
    print("3: quitter")

def saisieNombreCorrect() -> int:
    choice = integerbox("Saisissez un nombre entre 1 et 3","",None, 1,3)

    return  choice

if __name__ == "__main__":
    fifo = Queue();

    while True:
        printOptions()
        choix = saisieNombreCorrect()
        if(choix == 1):
            addToQueue(textbox("Element a ajouter"),fifo)
            print(fifo)
        elif (choix == 2):
            if len(fifo) <= 0:
                print("Liste vide")
            else:
                print(pull(fifo))
            print(fifo)
        else:
            break