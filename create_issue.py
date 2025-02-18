import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://mail-team-iznn07u5.atlassian.net/rest/api/3/issue"
API_Token = "ATATT3xFfGF0t8XOtq42WWutM2tKc9wcFo91aObUQN-4-CGdIIKaRJm5_cc7_Y9S6pYr9wbnUa3Pt4oVJhT04NWOANNdjXBdCCJsU-cQODo-osXPeaeUB1TN0XLI_oggdUM2mBGjDNFCFJrD9Q0H2GwoVMkgnCNI3KS_mJeZf10sX33JvaIGCDc=0D1A2108"  # Replace with actual API token
auth = HTTPBasicAuth("holla@mail.bradley.edu", API_Token)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps({
    "fields": {
        "project": {
            "key": "SCRUM"
        },
        "summary": "Automated Bug Created via API",
        "description": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "This is a test bug created from Python."
                        }
                    ]
                }
            ]
        },
        "issuetype": {
            "id": "10002"  # Ensure this is correct for "Bug"
        },
        "duedate": "2024-03-11"
    }
})



response = requests.post(
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print("Status Code:", response.status_code)
print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
