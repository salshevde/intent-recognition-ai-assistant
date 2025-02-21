import openai
import re
from ..core.config import settings
import google.generativeai as genai
from typing import Optional, Dict

import json
from ..models.models import Response
prompt_template = settings.PROMPT_TEMPLATE
# GEMINI


# OPENAI
openai.api_key = settings.OPENAI_API_KEY
model = settings.OPENAI_AI_MODEL


async def recognize_intent(text: str, user_info: Optional[dict]=None)->Response:


    try:
        prompt = prompt_template.format(text=text)
        print(prompt)
        genai.configure(api_key=settings.GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-pro')

        result=model.generate_content(prompt).candidates[0].content.parts[0].text

        result = json.loads(re.sub(r"```json|```", "", result).strip())


        if user_info:
            result["entities"]["username"]= user_info["username"]
            if "username" not in result["response"]:
                result["response"] = f"{user_info['username']}, {result['response']}"
        return Response(**result)

    except Exception as e:
        return Response(
            intent="UNKNOWN",
            confidence = 0.0,
            response="I'm having trouble understanding. Could you please rephrase that?",
            entities={}
        )