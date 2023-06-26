import sys
import armt


version = "2.3"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        text = open(sys.argv[1]).read()
        armt.run('<stdin>', text)
    else:
        print("Arment " + version + " Copyright (C) 2023, Etec João Baptista de Lima Figueiredo")
        while True:
            text = input('> ')
            if text.strip() == "":
                continue
            if text[0] == "#":
                continue
            result, error, should_exit = armt.run('<stdin>', text)

            if error:
                print(error.as_string())
            elif result:
                if len(result.elements) == 1:
                    print(repr(result.elements[0]))
                else:
                    print(repr(result))
            if should_exit:
                break
