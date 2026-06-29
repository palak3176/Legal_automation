import os
import base64
import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

load_dotenv()


class DocumentAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=os.getenv("GEMINI_API_KEY"),
            temperature=0
        )

    async def extract_party_details(self, file_bytes: bytes):
        base64_file = base64.b64encode(file_bytes).decode("utf-8")

        message = HumanMessage(
            content=[
                {"type": "text",
                 "text": "Extract Name, Address, and ID details. Return ONLY a JSON object: {'name': '', 'address': '', 'id_number': ''}"},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_file}"}}
            ]
        )

        response = await self.llm.ainvoke([message])
        content = response.content.strip()
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        return json.loads(content)

    async def generate_final_text(self, parties, format_text):
        # This agent takes the format and injects the party details
        prompt = f"""
        Format Template: {format_text}
        Party Details: {json.dumps(parties)}

        Generate the full legal document. Replace placeholders with the party details. 
        Maintain a formal legal tone.
        """
        response = await self.llm.ainvoke(prompt)
        return response.content