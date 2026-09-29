import json
import sys
import time
import urllib.request


def get(url: str):
    with urllib.request.urlopen(url, timeout=5) as resp:
        return json.loads(resp.read())


def main(base_url: str, expected_env: str) -> None:
    print(f"Waiting for {base_url}/health ...")
    for _ in range(20):
        try:
            if get(f"{base_url}/health").get("status") == "ok":
                break
        except OSError:          # connection refused, reset, timeout, etc.
            pass
        time.sleep(2)
    else:
        sys.exit("FAIL: service never became healthy")

    info = get(f"{base_url}/")
    print("Response:", info)
    if info.get("environment") != expected_env:
        sys.exit(f"FAIL: expected environment {expected_env!r}, got {info.get('environment')!r}")

    if get(f"{base_url}/add?a=2&b=3").get("result") != 5:
        sys.exit("FAIL: business logic check")

    print("Smoke test passed")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])