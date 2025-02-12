import requests
import time

# Replace with your Healthchecks.io ping URL
PING_URL = "https://hc-ping.com/1d335288-2467-4c3c-a5c3-c477d8cbcb61"

def send_ping(status="working", message=""):
    """Sends a message to Healthchecks.io"""
    payload = {"status": status, "message": message}
    response = requests.post(PING_URL, json=payload)
    print(f"📩 Sent ping: {message} - Status: {response.status_code}")

try:
    # Notify Healthchecks.io that the script has started
    send_ping("start", "Script has started!")

    # Simulating a long-running task (10 minutes)
    for i in range(10):
        message = f"Processing step {i+1}/10"
        send_ping("working", message)
        print(f"⏳ {message}")
        time.sleep(60)  # Simulating work for 1 minute

    # Notify Healthchecks.io that the script completed successfully
    send_ping("success", "Script completed successfully!")
    print("✅ Script completed successfully!")

except Exception as e:
    # Notify Healthchecks.io of failure with error details
    send_ping("fail", f"Script failed! Error: {str(e)}")
    print(f"❌ Script failed! Error: {e}")
