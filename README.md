
# Intent Recognition API

This repository contains a FastAPI-based intent recognition service, containerized with Docker and deployed on AWS EC2 using Kubernetes (K3s).


## Tech Stack

**Programming Language:** Python

**Framework:** FastAPI

**NLP Integration:**  Gemini API

**Database:** MongoDB

**Containerization:** Docker

**Deployment:** DockerHub , Kubernetes, AWS
# Installation & setup

## Prerequisites
Ensure you have the following installed:

- Python 3.8+

- Docker

- MongoDB


### Option 1: Clone the Repository

```
git clone https://github.com/salshevde/intent-recognition-ai-assistant.git
cd intent-recognition-ai-assistant
```
Install Dependencies
```
pip install -r requirements.txt
```
Run the FastAPI Server
```
uvicorn main:app --reload
```
### Option 2: Pull from DockerHub

```
docker pull salshe/intent-recognition
```
Run with docker
```
docker run -p 8000:8000 intent-recognition
```

# Testing
```
  pytest tests/api.py
```

# API Reference

#### Home

```http
  GET /api/v1/
```

**Description**: Returns a successful response to confirm the API is running.

#### Create New User

```http
  POST /api/v1/register
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username` | `string` | **Required**. User's name |
| `password` | `string` | **Required**. User's password |

#### Login

```http
  POST /api/v1/login
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username` | `string` | **Required**. User's name |
| `password` | `string` | **Required**. User's password |

#### Process Input

```http
  POST /api/v1/process
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `text` | `string` | **Required**. Input text to process |
| `username` | `string` | Optional. Defaults to `anonymous` |

Response Format:
```json
{
  "intent": "string",
  "confidence": 0,
  "response": "string",
  "entities": {
    "additionalProp1": "string",  
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
}
```

#### Get User Chat History

```http
  POST /api/v1/chat/${user_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `user_id` | `string` | **Required**. Unique user ID |

Response Format:
```json
[
  {
    "username": "string",
    "input_text": "string", 
    "response": {
      "intent": "string",
      "confidence": 0,
      "response": "string",
      "entities": {
        "additionalProp1": "string",
        "additionalProp2": "string",
        "additionalProp3": "string"
      }
    },
    "timestamp": "2025-02-21T23:50:51.870Z",
    "entities": {
      "additionalProp1": "string",
      "additionalProp2": "string", 
      "additionalProp3": "string"
    }
  }
]
```
