import minModul

def main():
    h1 = "anslag högst upp"
    h2 = "anslag i mitten"
    h3 = "anslag längst ned"
    while True:
        minModul.clear()
        minModul.header(h1, h2, h3)
        post = input("Nytt anslag: ")

        if post == "exit":
            break

        h1 = h2
        h2 = h3
        h3 = post
        

if __name__ == "__main__":
    main()