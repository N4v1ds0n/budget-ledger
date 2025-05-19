# [Budget Ledger](https://)
(Developer: Damian Droste)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/n4v1ds0n/budget-ledger)](https://www.github.com/n4v1ds0n/budget-ledger/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/n4v1ds0n/budget-ledger)](https://www.github.com/n4v1ds0n/budget-ledger/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/n4v1ds0n/budget-ledger)](https://www.github.com/n4v1ds0n/budget-ledger)

![amiresponsive-screenshot](./docs/amiresponsive.png)
[Page on AmIResponsive](https://ui.dev/amiresponsive?url=https://n4v1ds0n.github.io/tic-tac-toe)

...for your daily transactions, cashflow clarity, and categorical control.

Budget Ledger is a **terminal-based personal finance tracker** built in Python 3, 
designed to help users manage their income and expenses through an intuitive CLI 
interface.

[Link to live CLI deployment (Heroku)](https://budget-ledger-3f04126e52ee.herokuapp.com/)

---

## Index – Table of Contents

- [Planning](#planning)
- [Design](#design)
- [UX](#ux)
  - [Program Goals](#program-goals)
  - [User Stories](#user-stories)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Possible Future Features](#possible-future-features)
- [Data Model](#data-model)
- [Testing](#testing)
  - [Validator Testing](#validator-testing)
  - [CLI Testing](#cli-testing)
  - [Testing User Stories](#testing-user-stories)
- [Debugging](#debugging)
- [Deployment](#deployment)
- [Credits](#credits)

---

## Planning

The following diagram illustrates the CLI app structure and the program flow for user interaction and database management:

![Flowchart](assets/images/budget_ledger_flowchart.png) *(placeholder)*

---

## Design

This is a **terminal-only application**, so visual styling is handled through clear, structured text layout and color formatting using `Colorama`.

Menus, user prompts, and outputs are formatted for maximum clarity and usability, even in plain text environments.

---

## UX

### Program Goals

- Allow users to track and manage personal income/expenses
- Secure user data through per-user authentication and individual databases
- Provide a simple CLI menu with options for input, summaries, export, and visualization
- Offer grouping and filtering (e.g., by date or category)
- Enable optional export to CSV for external use

### User Stories

**As a user I want to:**
- Register and log in with a unique username and password
- View and manage only my personal financial data
- Add income and expense records with category, note, and date
- View a summary of my spending grouped by category or date
- Visualize my spending using bar and line charts
- Export data to CSV within a selected date range
- View individual transaction records
- Receive clear prompts and error messages when input is invalid

**As a site administrator I want to:**
- Ensure each user's data is isolated and stored securely
- Track user creation and login events via a user database

---

## Features

### Existing Features

- **User Authentication**
  - Secure login with password hashing (SHA-256)
  - Per-user SQLite database (`data/<username>.db`)
- **Add Transaction**
  - Record income or expenses
  - Store amount, category, description, timestamp, and date
- **Summarize**
  - Group by `category` or `date`
  - Filter by custom start and end dates
- **Visualize**
  - Bar chart for spending by category
  - Line chart for spending over time
- **Export to CSV**
  - Custom date range
  - Clean CSV output with all relevant fields
- **Clean CLI Design**
  - Modular structure
  - Dynamic menus
  - Helpful validation and input checking

### Possible Future Features

- Logout and switch user
- Password reset (via CLI or token)
- Budget planning per category
- Import CSVs (e.g., from banks)
- Weekly or monthly stats overview
- Transaction deletion or editing

---

## Data Model

### `user_data` (global users.db)
| Field       | Type    | Notes                     |
|-------------|---------|---------------------------|
| `id`        | INT     | Auto-increment, primary key |
| `username`  | TEXT    | Unique                    |
| `password`  | TEXT    | SHA-256 hashed            |
| `created_at`| TEXT    | ISO timestamp             |

### `balance` (per user .db)
| Field       | Type    | Notes                |
|-------------|---------|----------------------|
| `id`        | INT     | Auto-increment        |
| `amount`    | REAL    | Positive/negative     |
| `category`  | TEXT    | e.g. Food, Salary     |
| `note`      | TEXT    | Optional description  |
| `date`      | TEXT    | YYYY-MM-DD            |
| `timestamp` | TEXT    | Full ISO datetime     |

---

## Testing

### Validator Testing

- **PEP8** compliance ensured using [PEP8 Online](http://pep8online.com/)
- Linter warnings fixed (e.g., spacing, line length)
- CLI-only app; no HTML/CSS validation required

### CLI Testing

Tested on:
| Environment       | Result |
|-------------------|--------|
| VS Code Terminal  | ✔      |
| macOS Terminal    | ✔      |
| Windows CMD       | ✔      |
| Heroku CLI App    | ✔      |

### Testing User Stories

| Goal | Outcome |
|------|---------|
| User registration with hashed password | ✔ |
| Login and access personal DB | ✔ |
| Add entry and retrieve it | ✔ |
| Summarize by category/date | ✔ |
| Export filtered data to CSV | ✔ |
| Prevent invalid input | ✔ |

---

## Debugging

### Fixed Bugs

- **Circular import error** when calling `menu()` from `user_management` — fixed by moving all menu calls to `main.py`
- **Missing directory error** when creating user DB — fixed with `os.makedirs()`
- **Unrecognized column 'date'** — resolved by adding proper SQL `DATE()` logic and schema updates

### Unfixed Bugs

None known at time of submission.

---

## Deployment

Deployed to [Heroku](https://heroku.com) using Code Institute’s Python Essentials terminal template.

**Steps to deploy:**
1. Clone the GitHub repo
2. Push to new Heroku app
3. Add Python + Node.js buildpacks
4. Create `Procfile` with:

web: python3 main.py

5. Enable deploys from GitHub branch

---

## Credits

### Code

- Code Institute’s [Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template)
- SQLite usage adapted from [official docs](https://docs.python.org/3/library/sqlite3.html)
- CSV and date parsing based on [Python standard library docs](https://docs.python.org/3/library/csv.html)
- Matplotlib chart logic based on [Matplotlib docs](https://matplotlib.org/stable/gallery/index.html)

### Acknowledgements

Thanks to the Code Institute community for debugging guidance and review advice!

---
