# Activity Tracker ⚡

A simple web-based Activity Tracker built with **Python** and **Flask**.  
Track your activities, stop them, and see how much time you spent on each task, all in a colorful and responsive dashboard.

## Features

- Add new activities
- View active activities
- Stop an activity
- View stopped activities with total time spent
- Dashboard shows statistics: active count, stopped count, and average time
- Color-coded statuses and icons for better visualization

## Requirements
- Python 3.9 or newer
- Flask 2.2 or newer
- Flask-SQLAlchemy 3.0 or newer

# Installation
## MacOS

***1. install the required tools***
```bash
brew install python3

pip install Flask Flask-SQLAlchemy
```
## Windows
```bash
winget install Python.Python.3.14

pip install Flask Flask-SQLAlchemy
```

***2. Clone the repository and run project:***

```bash
git clone https://github.com/Fawloqq/activity-tracker-app.git

cd activity-tracker-app/src/main.py

python3 run main.py