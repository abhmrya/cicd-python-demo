import sys
import time
import urllib.request

BASE_URL = sys.argv[1]
LIMIT_SECONDS = 0.5
REQUESTS = 100

for i in range(1, REQUESTS + 1):
    start = time.perf_counter()
    with urllib.request.urlopen(f"{BASE_URL}/", timeout=5) as resp:
        resp.read()
    elapsed = time.perf_counter() - start
    if elapsed > LIMIT_SECONDS:
        sys.exit(f"FAIL: request {i} took {elapsed:.3f}s (limit {LIMIT_SECONDS}s)")

print(f"{REQUESTS} requests, all under {LIMIT_SECONDS}s")