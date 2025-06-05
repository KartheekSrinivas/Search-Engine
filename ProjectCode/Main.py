from InitializeEngine import InitializeEngine
from PresentingLayer import PresentingLayer

def main():

    T = InitializeEngine.Initialize()
    k = True
    while k:
        print("Type exit to exit\n")
        query = input("Enter text to search?     ")
        if(query.lower() == "exit"):
            k = False
        else:
            PresentingLayer.FinalPresentation(query.lower())
    
    
if __name__ == '__main__':
    main()