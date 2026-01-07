import logging

from logger_user import create_file


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        filename="app.log",
    )

    create_file("file.txt")


if __name__ == "__main__":
    main()
