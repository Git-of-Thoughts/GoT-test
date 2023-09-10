from greeting import Greeting

def main():
    """The entry point of the application."""
    greeting = Greeting()
    print(greeting.get_greeting())

if __name__ == "__main__":
    main()
