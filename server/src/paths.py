from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

KEYFILE = BASE_DIR / "certificates" / "key.pem"
CERTFILE = BASE_DIR / "certificates" / "certificate.pem"