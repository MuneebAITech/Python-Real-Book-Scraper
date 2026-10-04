import requests
from bs4 import BeautifulSoup
from logger import write_error


def scrape_books():

    books = []

    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    # base_url = "https://wrongwebsite12345.com/page-{}.html"

    for page in range(1, 51):

        print(f"Scraping Page {page}...")

        url = base_url.format(page)

        try:

            response = requests.get(
                url,
                timeout=10
            )

            response.raise_for_status()

        except requests.exceptions.RequestException as error:

            write_error(
                f"Page {page} Failed : {error}"
            )

            print(
                f"Failed To Access Page {page}"
            )

            continue

        soup = BeautifulSoup(response.text, "html.parser")

        all_books = soup.find_all(
            "article",
            class_="product_pod"
        )

        for book in all_books:

            title = book.h3.a["title"]

            price = (
                book.find(
                    "p",
                    class_="price_color"
                )
                .text
                .replace("Â£", "")
            )

            availability = (
                book.find(
                    "p",
                    class_="instock availability"
                )
                .text
                .strip()
            )

            rating = book.p["class"][1]

            books.append({
                "Title": title,
                "Price": price,
                "Availability": availability,
                "Rating": rating
            })

    return books