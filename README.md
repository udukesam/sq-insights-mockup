
# 🧩 SQ Insights Mockup API

This is a mock FastAPI application that simulates **SonarQube API endpoints** to help you test integrations for dashboards, reports, and analytics systems — **without connecting to a live SonarQube instance**.

---

## 🚀 Features

- Mocks major SonarQube endpoints including:
  - `/api/measures/component`
  - `/api/measures/component_tree`
  - `/api/issues/search`
  - `/api/metrics/search`
  - `/api/qualitygates/project_status`
  - `/api/components/tree`
- Fully asynchronous FastAPI app.
- Returns realistic JSON responses from local mock data files.
- Useful for testing, prototyping, or front-end integration demos.

---

## 🗂 Directory Structure

```
sq-insights-mockup/
│
├── main.py               # FastAPI app with mocked endpoints
├── data/
│   ├── measures.json
│   ├── component_tree.json
│   ├── metrics.json
│   ├── issues.json
│   ├── quality_gate.json
│   └── components.json
└── requirements.txt      # Python dependencies
```

---

## ⚙️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-org/sq-insights-mockup.git
   cd sq-insights-mockup
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**
   ```bash
   uvicorn main:app --reload --port 8080
   ```

5. **Access the Endpoints**
   - Swagger UI: [http://localhost:8080/docs](http://localhost:8080/docs)
   - Example: [http://localhost:8080/api/issues/search](http://localhost:8080/api/issues/search)

---

## 🧪 Example Endpoints

| Endpoint | Description | Sample JSON |
|-----------|--------------|--------------|
| `/api/measures/component` | Returns component measures data | `measures.json` |
| `/api/issues/search` | Returns issue details | `issues.json` |
| `/api/metrics/search` | Returns available metric definitions | `metrics.json` |
| `/api/qualitygates/project_status` | Returns quality gate evaluation | `quality_gate.json` |
| `/api/components/tree` | Returns project component hierarchy | `components.json` |
| `/api/measures/component_tree` | Returns aggregated component tree measures | `component_tree.json` |

---

## 🧰 Tech Stack

- **Python 3.10+**
- **FastAPI** — for REST API simulation
- **Uvicorn** — for running the ASGI server
- **JSON** — for static data mockups

---

## 📄 License

This project is intended for **internal testing and educational purposes** only.  
Not affiliated with or endorsed by SonarSource.

---

## 👨‍💻 Author

**Duke Sam**  
Application Architect | IBM Cloud & AI  
