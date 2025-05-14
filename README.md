# SenseWay MVP

SenseWay is a lightweight proof of concept tool that allows developers to paste a **code block with an error** and receive related real-world cases from Stack Overflow. It's meant as an open exploration of how we can improve debugging using contextual search — with a focus on simplicity, accessibility, and human insight.

## How It Works

- Paste a code block (with an error inside)
- The app scans for common keywords, error names and structures
- Builds a query to search Stack Overflow
- Returns the top 5 most relevant related posts

## How to Run Locally

1. Clone this repository or download the files
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   streamlit run senseway.py
   ```

## Why It Exists

This is a study-oriented project for reflection on how human reasoning and open community knowledge can help junior to senior devs approach errors.

## License

This code is provided as-is, for educational and experimental use.
