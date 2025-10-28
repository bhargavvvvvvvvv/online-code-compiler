from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Online Code Compiler")

class CodeRequest(BaseModel):
    language: str
    code: str

@app.get("/")
def root():
    return {"status": "ok", "service": "online-code-compiler"}

@app.post("/compile")
def compile_code(req: CodeRequest):
    if req.language.lower() != "python":
        return {"status": "error", "error": "unsupported language"}
    # Placeholder: you can expand this to actually execute code later
    return {"status": "success", "output": "Hello from FastAPI"}
