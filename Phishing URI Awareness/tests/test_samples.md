# Test Results of Phishing URL Checker

## Test Details
- Python Version: 3.15
- Operating System: Windows

| Sr No | Sample URL Tested | Expected Output | Actual Output | Status |
| ----- | ----------------- | --------------- | ------------- | ------ |
| 1 | https://www.example.com/login | No warning signs | No listed warning signs found. This does NOT prove safety. | PASS |
| 2 | http://192.0.2.10/account | IP address and HTTP warnings | Uses an IP address instead of a familiar domain. Uses HTTP. | PASS |
| 3 | http://example.com@sample.invalid/login | @ symbol and HTTP warnings | Contains an @ symbol; inspect carefully. Uses HTTP. | PASS |
| 4 | https://a.b.c.d.e.example.invalid/path | Many subdomains warning | Contains many hostname segments/subdomains. | PASS |
| 5 | https://xn--example.invalid/ | Punycode warning | Contains a punycode-style hostname. | PASS |

## Conclusion
- All 5 sample URLs were tested successfully in the terminal.
- The program correctly detected all visual indicators without opening any links online.
-