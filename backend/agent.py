import os
import json
from groq import Groq
from dotenv import load_dotenv
from tools import get_bookings, book_table

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_bookings",
            "description": "Get all current bookings from the CSV file",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "book_table",
            "description": "Book a table for a customer",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Customer last name"},
                    "time": {"type": "string", "description": "Time slot like 19:00"},
                    "party_size": {"type": "integer", "description": "Number of people"}
                },
                "required": ["name", "time", "party_size"]
            }
        }
    }
]

def run_agent(user_message: str, chat_history: list) -> str:
    messages = [
        {
                "role": "system",
            "content": """You are a warm and friendly booking assistant for Urban Feast restaurant. 
            
Follow this EXACT conversation flow:
1. First warmly GREET the customer and welcome them to Urban Feast
2. Ask how many people will be dining (2 or 4)
3. Based on party size, call get_bookings tool and show ONLY the AVAILABLE time slots to the customer in a clean list
4. Ask which time slot they prefer
5. Ask for their name
6. Call book_table tool to confirm the booking
7. End with a warm confirmation message like: "Your table for [party_size] people, Ms./Mr. [name], at [time] PM is confirmed! We look forward to welcoming you at Urban Feast! 🍽️"

Rules:
- Always be warm, polite and professional
- Never skip any step in the flow
- Only show time slots that are actually available
- Tables for 2 people: table1_2p to table4_2p
- Tables for 4 people: table5_4p to table8_4p
- Available time slots: 12:00 to 21:00 in 30 minute intervals"""
        }
    ] + chat_history + [{"role": "user", "content": user_message}]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    response_message = response.choices[0].message

    if response_message.tool_calls:
        messages.append(response_message)

        for tool_call in response_message.tool_calls:
            fn_name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)

            if fn_name == "get_bookings":
                result = get_bookings()
            elif fn_name == "book_table":
                result = book_table(**args)

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            })

        final_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
        )
        return final_response.choices[0].message.content

    return response_message.content