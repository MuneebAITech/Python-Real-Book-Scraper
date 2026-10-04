from scraper import scrape_books
from exporter import save_to_csv, save_to_excel
from logger import write_log, write_error


try:

    write_log("Scraping Started")

    books = scrape_books()

    write_log(
        f"{len(books)} Books Collected"
    )

    save_to_csv(books)
    save_to_excel(books)

    write_log("CSV File Saved")

    print("\n")
    print("=" * 50)

    print(
        f"Total Books Collected: {len(books)}"
    )

    print("=" * 50)

except Exception as error:

    write_error(str(error))

    print(
        f"Unexpected Error: {error}"
    )

print("\nProcess Completed Successfully")