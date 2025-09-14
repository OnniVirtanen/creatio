from creatio import address, name

def main():
    print("# Example generated addresses and names from creatio library\n")

    print("Home Address (kotiosoite):")
    print(address.kotiosoite())
    print()  # Blank line

    print("Random First Name:")
    print(name.first_name())
    print()

    print("Random Last Name:")
    print(name.last_name())
    print()

    print("Random Full Name:")
    print(name.full_name())
    print()

if __name__ == "__main__":
    main()
