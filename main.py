from fastapi import FastAPI, UploadFile, File
from app.agent import DocumentAgent
from app.schemas import AgreementState
import uvicorn

app = FastAPI()
agent = DocumentAgent()


@app.post("/extract")
async def extract_data(file: UploadFile = File(...)):
    # In a real app, use an OCR library like pytesseract or Google Vision here.
    # For now, we simulate reading the text content.
    content = await file.read()
    raw_text = content.decode("utf-8", errors="ignore")

    extracted_parties = await agent.extract_info(raw_text)
    return {"parties": extracted_parties}


@app.post("/generate")
async def generate_doc(state: AgreementState):
    # This is where you'd use python-docx to fill a template.
    return {"message": "Document Generated", "data": state}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)