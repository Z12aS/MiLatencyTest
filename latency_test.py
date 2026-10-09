import time
import requests

url = "https://sgp-api.buy.mi.com/bbs/api/global/apply/bl-auth"
headers = {
    "User-Agent": "okhttp/4.12.0",
    "Accept-Encoding": "gzip",
    "Content-Type": "application/json",
}

samples = 4
waiting_time_seconds = 10

latencies = []
print("Original script repo: https://github.com/MiForge/MiCommunityTool/")
print("This is AI generated strip of the latency measurement from it\n")
print(f"Measuring latency ({samples} samples, waiting {waiting_time_seconds}s between requests)...")

for i in range(1, samples + 1):
    try:
        start = time.perf_counter()
        requests.post(url, headers=headers, data='{}', timeout=2)
        raw_latency = (time.perf_counter() - start) * 1000
        adjusted_latency = raw_latency * 1.3
        latencies.append(adjusted_latency)
        print(f"Request {i}: {raw_latency:.2f} ms")
    except Exception as e:
        print(f"Request {i}: Request failed ({e})")

    if i < samples:
        print(f"Waiting {waiting_time_seconds}s...")
        time.sleep(waiting_time_seconds)

print("\nAll Results (Adjusted x1.3):")
for idx, latency in enumerate(latencies, 1):
    print(f"Result {idx}: {latency:.2f} ms")
print("\n!!! Use the most common latency, which often is the lowest in the list. if results vary too much, please run the script again")
