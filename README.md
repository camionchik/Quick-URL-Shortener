# Quick URL Shortener 🚀

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square) ![CLI Tool](https://img.shields.io/badge/CLI-Tool-orange?style=flat-square) ![Open Source](https://img.shields.io/badge/Open%20Source-Yes-green?style=flat-square)

Welcome to **Quick URL Shortener**, a simple Python CLI tool designed to help you shorten URLs instantly using TinyURL or Bitly. Whether you're a developer, a marketer, or just someone who frequently shares links, this tool will enhance your productivity by making URL shortening quick and easy.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Supported APIs](#supported-apis)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Releases](#releases)

## Features

- **Instant URL Shortening**: Quickly shorten any URL using either TinyURL or Bitly.
- **Command-Line Interface**: User-friendly CLI for easy access and operation.
- **Clipboard Integration**: Automatically copy the shortened URL to your clipboard.
- **Open Source**: Contribute to the project and help improve it.

## Installation

To get started with Quick URL Shortener, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/camionchik/Quick-URL-Shortener.git
   ```

2. **Navigate to the Directory**:
   ```bash
   cd Quick-URL-Shortener
   ```

3. **Install Dependencies**:
   Ensure you have Python 3 installed. You can install the required packages using:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

After installation, you can use the tool directly from the command line. Here’s how:

1. **Shorten a URL**:
   To shorten a URL, use the following command:
   ```bash
   python shorten.py <your-url>
   ```

2. **Choose API**:
   You can specify which API to use (TinyURL or Bitly):
   ```bash
   python shorten.py <your-url> --api tinyurl
   ```
   or
   ```bash
   python shorten.py <your-url> --api bitly
   ```

3. **Copy to Clipboard**:
   The shortened URL will be automatically copied to your clipboard for easy sharing.

## Supported APIs

### TinyURL
TinyURL is a free URL shortening service that allows you to create short links quickly. It is straightforward and does not require an account.

### Bitly
Bitly is a more robust URL shortening service that provides tracking and analytics. To use Bitly, you will need to create an account and obtain an API key.

## Contributing

We welcome contributions! If you'd like to help improve Quick URL Shortener, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes.
4. Submit a pull request.

Please ensure that your code adheres to our coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to reach out:

- **Email**: your.email@example.com
- **GitHub**: [camionchik](https://github.com/camionchik)

## Releases

You can find the latest releases of Quick URL Shortener [here](https://github.com/camionchik/Quick-URL-Shortener/releases). Please download the latest version and execute it to get started.

![Release Button](https://img.shields.io/badge/Download%20Latest%20Release-blue?style=flat-square&logo=github)

## Conclusion

Quick URL Shortener is a simple yet powerful tool for anyone who needs to share links efficiently. With its easy-to-use CLI and support for both TinyURL and Bitly, you can streamline your workflow and focus on what matters most.

Feel free to explore the code, contribute, and share your thoughts. Happy shortening!