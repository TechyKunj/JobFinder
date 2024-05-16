# 🕵️‍♂️ Job Finder using Web Scraping and Python

Welcome to the Job Finder project! This repository contains the code and documentation for a job finder tool that scrapes job listings from the Timesjobs website using Python.

## 📋 Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## 💡 Introduction
This project aims to create a job finder tool that scrapes job listings from the Timesjobs website. The tool is built using Python and employs web scraping techniques to gather job data, which can be filtered and displayed according to user preferences.

## ✨ Features
- Scrape job listings from Timesjobs
- Filter jobs by skills
- Display job details including company name, required skills, and application link
- Simple command-line interface for interaction

## 🔧 Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library

## 💾 Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/job-finder.git
    ```
2. Navigate to the project directory:
    ```bash
    cd job-finder
    ```
3. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage
1. Run the scraper script:
    ```bash
    python scrape_jobs.py
    ```
2. Enter your familiar skill sets when prompted, separated by commas.

## 🖥️ Example
```bash
$ python scrape_jobs.py
Provide your Familiar skill sets in comma-separated way: Python,Machine Learning
waiting for 5 seconds
Company name : CompanyA
Skills needed : ['Python', 'MachineLearning']
Apply link : https://www.timesjobs.com/candidate/job-detail/jobid-XXXXXX
#############
waiting for 5 seconds
```

🌟 Contributing
Contributions are welcome! Please fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

Fork the repository
Create your feature branch (git checkout -b feature/YourFeature)
Commit your changes (git commit -m 'Add some feature')
Push to the branch (git push origin feature/YourFeature)
Open a pull request


📜 License
This project is licensed under the MIT License. See the LICENSE file for more details.

Made with ❤️ by Kunj
