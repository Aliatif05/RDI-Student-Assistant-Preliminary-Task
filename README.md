# RDI-Student-Assistant-Preliminary-Task

# RDI Student Assistant Preliminary Task

This repository contains my solution for the **RDI Student Assistant Preliminary Task**.  
The program is a simple command-line application that uses the [NewsAPI](https://newsapi.org/) service to fetch and display news articles.

Users can:

1. View current top headlines.
2. Search for news articles using a keyword.

---

## Features

### 1. Show current top news
- Fetches the latest top headlines from NewsAPI.
- Currently uses `country=us` (can be changed in the code).
- Displays:
  - Article title  
  - Source name  
  - URL to the full article  

### 2. Search news by keyword
- Asks the user to input a search keyword (e.g. *bitcoin*, *AI*, *football*).
- Fetches recent articles matching that keyword.
- Displays:
  - Article title  
  - Source name  
  - URL to the full article  

### 3. Simple text menu
- Looping menu with options:
  - `1` – Show current top news  
  - `2` – Search news by keyword  
  - `3` – Quit the program  

---

## Technologies Used

- **Language:** Python 3
- **HTTP client:** `requests` library
- **API:** [NewsAPI.org](https://newsapi.org/)

---

## Requirements

- Python **3.8+** (earlier versions may also work, but this is what it’s tested with)
- An active **NewsAPI API key**
- Python dependencies:
  - `requests`

Install the dependency with:

```bash
pip install requests
