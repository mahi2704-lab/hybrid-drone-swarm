import os
import sys

# Track the direct absolute paths on Windows
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Import the actual variable object directly, bypassing string lookup errors
from ai_server.api import app

if __name__ == "__main__":
    import uvicorn

    print("🚀 [FRAMEWORK] Booting Secure Hybrid Edge-Cloud Swarm API Core...")

    # We remove reload=True because it creates a sub-process that drops paths on Windows
    uvicorn.run(app, host="0.0.0.0", port=8000)
