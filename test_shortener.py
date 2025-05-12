import subprocess

def test_shortener():
    result = subprocess.run(
        ["python", "shortener.py", "https://example.com"],
        capture_output=True,
        text=True
    )
    assert "Shortened URL" in result.stdout, "URL Shortening Failed!"
    print("Test Successful!")

if __name__ == "__main__":
    test_shortener()
