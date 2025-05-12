# Quick URL Shortener

A simple tool to quickly shorten long URLs and automatically copy the result to your clipboard. Supports both TinyURL and Bitly services, and can be customized via a configuration file.

## Features

* One-command URL shortening.
* Automatically copies the shortened URL to clipboard.
* Supports TinyURL and Bitly (Bitly requires an access token).
* Debug output for reliable results.
* Open-source and free to use.

## Installation

Clone the repository:

```bash
git clone https://github.com/username/quick-url-shortener.git
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Optionally customize `config.json` (see Configuration section).

## Usage

Run the following command in your terminal:

```bash
python shortener.py <long_url>
```

Example:

```bash
python shortener.py https://example.com/very/long/url
```

Output:

```
INFO: Shortened URL: https://tinyurl.com/xyz123 (Copied to clipboard!)
```

## Configuration

You can choose the service and provide credentials using the `config.json` file:

```json
{
  "service": "tinyurl",
  "bitly_token": "your_bitly_access_token"
}
```

* `service`: Choose between `"tinyurl"` or `"bitly"`.
* `bitly_token`: Required only if using Bitly. So if you are going to use TinyURL, you do not need to fill it out. Obtain a token via Bitly's API dashboard.

## Testing

Run the test script:

```bash
python test_shortener.py
```

## Contributing

Contributions are welcome! Please feel free to open a pull request.

## License

This project is licensed under the MIT License.
