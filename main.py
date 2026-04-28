from app.banner import print_banner
from app.calc import add_numbers
from app.hello import get_greeting


def main() -> None:
    left = 2
    right = 3
    result = add_numbers(left, right)

    print_banner("WSL Test App")
    print(get_greeting())
    print(f"{left} + {right} = {result}")


if __name__ == "__main__":
    main()
