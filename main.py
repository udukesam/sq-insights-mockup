from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import json, os

app = FastAPI(title='Mock SonarQube API')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

def load(name):
    """
    Loads a JSON file from the data directory and returns its parsed content.
    """
    file_path = os.path.join(DATA_DIR, name)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail=f"File '{name}' not found in data directory.")
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail=f"Error decoding JSON file '{name}'.")


@app.get('/api/measures/component')
async def measures_component(component: str = None, metricKeys: str = None):
    data = load('measures.json')
    return JSONResponse(content=data)

@app.get('/api/issues/search')
async def issues_search(componentKeys: str = None, types: str = None, severities: str = None):
    data = load('issues.json')
    return JSONResponse(content=data)

@app.get('/api/metrics/search')
async def metrics_search():
    data = load('metrics.json')
    return JSONResponse(content=data)

@app.get('/api/qualitygates/project_status')
async def qualitygate(projectKey: str = None):
    data = load('quality_gate.json')
    return JSONResponse(content=data)

@app.get('/api/components/tree')
async def components_tree(component: str = None, metricKeys: str = None):
    data = load('components.json')
    return JSONResponse(content=data)

@app.get('/api/measures/component_tree')
async def measures_component_tree(component: str = None, metricKeys: str = None):
    data = load('component_tree.json')
    return JSONResponse(content=data)

@app.get('/')
async def root():
    return {'message':'Mock SonarQube API - FastAPI is up'}
