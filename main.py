import argparse
import logging
import time

from app.banner import print_banner
from app.calc import add_numbers
from app.hello import get_greeting


def run_once() -> None:
    left = 2
    right = 3
    result = add_numbers(left, right)

    print_banner("WSL Test App")
    print(get_greeting())
    print(f"{left} + {right} = {result}")


def run_loop(interval: int) -> None:
    logging.info("service mode started with interval=%s seconds", interval)

    while True:
        left = 2
        right = 3
        result = add_numbers(left, right)
        logging.info("%s | %d + %d = %d", get_greeting(), left, right, result)
        time.sleep(interval)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Minimal WSL Python demo app")
    parser.add_argument(
        "--loop",
        action="store_true",
        help="run continuously for service management practice",
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=10,
        help="seconds between log messages in loop mode",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.loop:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(message)s",
        )
        run_loop(args.interval)
        return

    run_once()


if __name__ == "__main__":
    main()
