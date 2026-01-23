import json
import requests
import csv
from pathlib import Path

# Base directory (src folder)
BASE_DIR = Path(__file__).parent

# Paths
DATA_FILE = BASE_DIR / "data" / "books.json"
CSV_FILE = BASE_DIR / "books_report.csv"

API_URL = "https://openlibrary.org/search.json"


def load_books():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


def save_books(books):
    # Ensure data folder exists
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4)


def add_book(title, author, year):
    books = load_books()
    books.append({
        "title": title,
        "author": author,
        "year": year
    })
    save_books(books)
    print("✅ Book added successfully!")


def list_books():
    books = load_books()
    if not books:
        print("No books available.")
        return

    for book in books:
        print(f"{book['title']} | {book['author']} | {book['year']}")


def search_books(keyword):
    books = load_books()
    results = [
        book for book in books
        if keyword.lower() in book["title"].lower()
        or keyword.lower() in book["author"].lower()
    ]

    if not results:
        print("No matching books found.")
        return

    for book in results:
        print(f"{book['title']} | {book['author']} | {book['year']}")


def fetch_books_from_api(query):
    response = requests.get(API_URL, params={"q": query})
    data = response.json()

    print("\n📡 Books from Open Library API:")
    for book in data.get("docs", [])[:5]:
        title = book.get("title", "N/A")
        author = ", ".join(book.get("author_name", []))
        year = book.get("first_publish_year", "N/A")
        print(f"{title} | {author} | {year}")


def generate_csv_report():
    books = load_books()
    if not books:
        print("No books available to generate report.")
        return

    # Ensure src directory exists (safe)
    CSV_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Author", "Year"])

        for book in books:
            writer.writerow([book["title"], book["author"], book["year"]])

    print(f"📄 CSV report generated successfully at:\n{CSV_FILE}")


def menu():
    while True:
        print("\n📚 Mini Library Manager")
        print("1. Add Book")
        print("2. List Books")
        print("3. Search Books")
        print("4. Fetch Books from API")
        print("5. Generate CSV Report")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            add_book(title, author, year)

        elif choice == "2":
            list_books()

        elif choice == "3":
            keyword = input("Enter title or author: ")
            search_books(keyword)

        elif choice == "4":
            query = input("Search keyword: ")
            fetch_books_from_api(query)

        elif choice == "5":
            generate_csv_report()

        elif choice == "6":
            print("👋 Exiting Mini Library Manager")
            break

        else:
            print("❌ Invalid choice!")


if __name__ == "__main__":
    menu()

