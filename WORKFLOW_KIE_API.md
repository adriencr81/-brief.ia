# Workflow Kie.ai API - Image Generation

## Endpoints

### 1. Create Task (POST)
```
POST https://api.kie.ai/api/v1/jobs/createTask
Authorization: Bearer {API_KEY}
Content-Type: application/json
```

**Body:**
```json
{
  "model": "nano-banana-2",
  "prompt": "Your image description",
  "aspect_ratio": "1:1",
  "resolution": "1K",
  "output_format": "PNG",
  "callBackUrl": "https://yourapi.com/webhook" // optional
}
```

**Response:**
```json
{
  "task_id": "abc-123-def",
  ...
}
```

### 2. Poll Task Status (GET)
```
GET https://api.kie.ai/api/v1/jobs/recordInfo?taskId={task_id}
Authorization: Bearer {API_KEY}
```

**Response:**
```json
{
  "task_id": "abc-123-def",
  "model": "nano-banana-2",
  "state": "success",  // waiting | queuing | generating | success | fail
  "resultJson": {
    "image_url": "https://...",
    "image_bytes": "...",  // base64 if requested
    "cost": 0.04
  },
  "failCode": null,
  "failMsg": null,
  "createTime": "2026-04-14T10:00:00Z",
  "updateTime": "2026-04-14T10:02:30Z"
}
```

## Polling Strategy

1. **Exponential backoff** : Start with 2-3 sec, increase gradually
2. **Max retries** : ~100 (timeout ~5-10 min)
3. **Production** : Use webhooks instead of polling (callBackUrl)

## Task States

| State | Meaning | Continue Polling? |
|-------|---------|------------------|
| `waiting` | Queued | ✅ Yes |
| `queuing` | In queue | ✅ Yes |
| `generating` | Processing | ✅ Yes |
| `success` | Done ✓ | ❌ Stop - extract image_url |
| `fail` | Error ✗ | ❌ Stop - check failMsg |

## Response Format in resultJson

- **image_url** : HTTP(S) URL to download PNG
- **image_bytes** : Base64-encoded image (if requested)
- **cost** : Credit consumed (e.g., $0.04 for 1080x1080)

## Example: Python Implementation

```python
import requests
import time

API_KEY = "your_kie_api_key"
BASE_URL = "https://api.kie.ai/api/v1/jobs"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

# Step 1: Create task
create_resp = requests.post(
    f"{BASE_URL}/createTask",
    headers=HEADERS,
    json={
        "model": "nano-banana-2",
        "prompt": "A beautiful sunset over mountains",
        "aspect_ratio": "1:1",
        "resolution": "1K"
    }
)
task_id = create_resp.json()["task_id"]
print(f"Task created: {task_id}")

# Step 2: Poll until done
for attempt in range(100):
    time.sleep(2 + attempt * 0.5)  # Exponential backoff
    poll_resp = requests.get(
        f"{BASE_URL}/recordInfo",
        headers=HEADERS,
        params={"taskId": task_id}
    )
    task = poll_resp.json()
    
    if task["state"] == "success":
        image_url = task["resultJson"]["image_url"]
        print(f"✅ Done! Image: {image_url}")
        break
    elif task["state"] == "fail":
        print(f"❌ Failed: {task['failMsg']}")
        break
    else:
        print(f"⏳ {task['state']}... ({attempt+1}/100)")
```

## Integration with newsletter-to-instagram-with-ai-images

The skill should:
1. For each slide, create a task with the slide content
2. Store `task_id` in memory
3. After all 5 tasks are created, poll them in parallel
4. When all are `success`, download images and save to `images/YYYY-MM-DD_topic/slide_N.png`
5. Generate the markdown with image references

---

## References

- [Kie.ai Docs - Nano Banana 2](https://docs.kie.ai/market/google/nanobanana2)
- [Kie.ai Docs - Get Task Details](https://docs.kie.ai/market/common/get-task-detail)
- [GitHub - kie-nano-banana-skill](https://github.com/trin-zenityx/kie-nano-banana-skill)
