# josh_talk_assignment Documentation

## Project Setup Instructions

## Prerequisites
Make sure you have the following installed on your system:
- Python (version 3.x recommended)
- pip (Python package manager)
- Virtualenv

## Clone the github repository
```
git clone https://github.com/ankitgadling/josh_talk_assignment.git
```


## Creating a Virtual Environment
To set up a virtual environment for this project, follow these steps:

### **For macOS/Linux:**
```sh
python3 -m venv venv
source venv/bin/activate
```

### **For Windows:**
```sh
python -m venv venv
venv\Scripts\activate
```

Once activated, your terminal prompt should change to indicate the virtual environment is active.

## running the project



## This document provides details on the API endpoints

## Base URL

```
http://127.0.0.1:8000/api/tasks/
```

## Endpoints

### 1. Create a Task

**Endpoint:**
```
POST /api/tasks/
```
**Description:** Creates a new task.

**Request Body:**
```json
{
  "name": "Task 1",
  "description": "This is the first task.",
  "task_type": "Development",
  "status": "Pending",
  "assigned_users": [1]
}
```

### 2. Get All Tasks

**Endpoint:**
```
GET /api/tasks/
```
**Description:** Retrieves all tasks.


### 3. Get Tasks for a Specific User

**Endpoint:**
```
GET /api/tasks/user_tasks/?user_id=1
```
**Description:** Retrieves tasks assigned to a specific user.

### 4. Assign Task to a User

**Endpoint:**
```
POST /api/tasks/{task_id}/assign_users/
```
**Description:** Assigns a task to one or more users.

**Request Body:**
```json
{
  "user_ids": [3]
}
```

## Notes
- Ensure that the API server is running on `127.0.0.1:8000`.
- Replace `{task_id}` with the actual task ID when making requests.

