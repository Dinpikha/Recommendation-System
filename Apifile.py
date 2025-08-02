import subprocess
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello from FastAPI!"}

@app.post("/retrain")
def retrain_model():
    try:
      
        result = subprocess.run(
            [sys.executable, "-u", r"C:\Users\dipik\Desktop\rec_sys\hybrid.py"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'
        )
        
        return {
            "success": True,
            "message": "Training Complete",
            "output": result.stdout,  
            "error": result.stderr
        }
    except subprocess.CalledProcessError as e:
        return {
            "success": False,
            "message": "Training Failed",
            "output": e.stdout,
            "error": e.stderr,
            "returncode": e.returncode
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"Critical Error: {str(e)}"
        }
    