from datetime import datetime


def write_log(message):

    current_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(
        "logs/scraper.log",
        "a",
        encoding="utf-8"
    ) as log_file:

        log_file.write(
            f"{current_time} - {message}\n"
        )


def write_error(error_message):

    current_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(
        "logs/error.log",
        "a",
        encoding="utf-8"
    ) as error_file:

        error_file.write(
            f"{current_time} - ERROR - {error_message}\n"
        )