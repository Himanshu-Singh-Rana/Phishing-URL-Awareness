Phishing URL Awareness Checker

## Overview

This Python tool inspects URL text for 6 visual indicators commonly found in phishing links.

## Features Checked

@ Symbol in URL

URLs longer than 100 characters

IP address hostnames

Multiple subdomains (5+)

Punycode markers (xn--)

Insecure HTTP scheme

## How to Run

`bash

python phishing_checker.py

## Screenshots

![Sample Run](screenshots/sample_run.png) ![Test Results](screenshots/test_results.png)

## Limitations

Educational tool only. It reads text only and does not scan or visit links online.

## Author

[Himanshu kumar] - EWB Courses