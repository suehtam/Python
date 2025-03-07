def hello(name, lang):
    greetings = {"English": "Hello"}, {"Spanish": "Hola"}, {"French": "Bonjour"}
    msg = f"{greetings[lang]}, {name}"
    print(msg)
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description = "Provides a personal greeting.")
    parser.add_argument("-n", "--name", metavar = "name", required = True, help = "The name of the person to greet.")
    parser.add_argument("-l", "--lang", metavar = "language", required = True, choices = ["English", "Spanish", "French"], help = "The language in which to greet the person.")
    args = parser.parse_args()
    hello(args.name, args.lang)