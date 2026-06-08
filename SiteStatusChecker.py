import sys
import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

TIMEOUT = 10
MAX_WORKERS = 10

def check_url(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    try:
        start = time.time()
        r = requests.get(url, timeout=TIMEOUT, allow_redirects=True)
        ms = int((time.time() - start) * 1000)
        return {
            "url": url,
            "status": r.status_code,
            "ms": ms,
            "server": r.headers.get("Server", "-"),
            "content_type": r.headers.get("Content-Type", "-").split(";")[0],
            "redirected": r.url if r.url != url else None,
            "ok": r.status_code < 400,}
    except requests.ConnectionError:
        return {"url": url, "error": "Connection failed"}
    except requests.Timeout:
        return {"url": url, "error": "Timeout"}
    except Exception as e:
        return {"url": url, "error": str(e)}

def format_result(r):
    lines = []
    if "error" in r:
        lines.append(f"[FAIL] {r['url']} — {r['error']}")
    else:
        tag = "[OK] " if r["ok"] else "[ERR]"
        lines.append(f"{tag} {r['url']} | {r['status']} | {r['ms']}ms | {r['server']} | {r['content_type']}")
        if r["redirected"]:
            lines.append(f"       ↳ Redirected to: {r['redirected']}")
    return "\n".join(lines)

def main():
    if len(sys.argv) > 1:
        urls = sys.argv[1:]
    else:
        urls = input("Enter URLs (space-separated): ").split()

    results = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(check_url, u): u for u in urls}
        for f in as_completed(futures):
            results.append(f.result())

    output_lines = []
    for r in results:
        line = format_result(r)
        print(line)
        output_lines.append(line)

    save = input("\nSave results to file? (y/n): ").strip().lower()
    if save == "y":
        filename = f"results_{time.strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(output_lines))
        print(f"Saved to {filename}")
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
