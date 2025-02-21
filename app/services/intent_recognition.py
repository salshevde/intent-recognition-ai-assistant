import re
from ..core.config import settings
import google.generativeai as genai
from typing import Optional, Dict

import json
from ..models.models import Response

prompt_template = settings.PROMPT_TEMPLATE

async def recognize_intent(text: str, user_info: Optional[dict]=None)->Response:


    try:
        
        prompt = prompt_template.format(text=text)
        genai.configure(api_key=settings.GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-pro')

        result=model.generate_content(prompt).candidates[0].content.parts[0].text

        result = json.loads(re.sub(r"```json|```", "", result).strip())

        return Response(**result)

    except Exception as e:
        return Response(
            intent="UNKNOWN",
            confidence = 0.0,
            response="Err",
            entities={}
        )