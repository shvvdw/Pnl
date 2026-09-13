from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# ==================== YOUR KEYS ====================
VALID_KEYS = {
    "TEST-1234-ABCD-5678": {
        "used": False,
        "hwid": None,
        "expires": "2026-12-31"
    },
    "PREMIUM-9999-XXXX-0000": {
        "used": False,
        "hwid": None,
        "expires": "2027-06-30"
    },
}
# ==================================================

class ValidateRequest(BaseModel):
    key: str
    hwid: str

@app.post("/api/validate")
async def validate(data: ValidateRequest):
    key = data.key.upper().strip()
    hwid = data.hwid

    if key not in VALID_KEYS:
        return {"valid": False, "message": "Invalid key"}

    key_data = VALID_KEYS[key]

    # Check expiration
    if key_data.get("expires"):
        expire_date = datetime.strptime(key_data["expires"], "%Y-%m-%d")
        if datetime.now() > expire_date:
            return {"valid": False, "message": "Key has expired"}

    # First time activation
    if not key_data["used"]:
        key_data["used"] = True
        key_data["hwid"] = hwid
        return {"valid": True, "message": "Activated successfully"}

    # Same computer only
    if key_data["hwid"] == hwid:
        return {"valid": True, "message": "License valid"}

    return {"valid": False, "message": "Key already used on another PC"}

@app.get("/")
def home():
    return {"status": "Key server is running"}
