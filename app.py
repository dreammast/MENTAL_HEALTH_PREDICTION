from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from langchain_groq import ChatGroq
from typing import Dict, List, Any
import json
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize Groq LLM with environment variable for API key
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3,
    groq_api_key=os.getenv('GROQ_API_KEY', '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'),
    max_tokens=200,
    timeout=10
)

# State management for conversation
class State:
    def __init__(self):
        self.messages = []
        self.conversation_history = []
    
    def add_message(self, role: str, content: str):
        self.messages.append({"role": role, "content": content})
        self.conversation_history.append({"role": role, "content": content})
    
    def get_last_message(self) -> str:
        if self.messages:
            return self.messages[-1]["content"]
        return ""

# Mental Health Superbot with LangChain
def superbot(state: State) -> Dict[str, Any]:
    system_prompt = """You are Mindy, a mental health assistant. Be empathetic, supportive, and concise. 
    If you detect crisis content (suicidal thoughts, self-harm), provide immediate crisis resources."""
    
    messages = [{"role": "system", "content": system_prompt}]
    recent_history = state.conversation_history[-5:] if len(state.conversation_history) > 5 else state.conversation_history
    messages.extend(recent_history)
    
    try:
        response = llm.invoke(messages)
        state.add_message("assistant", response.content)
        analysis = quick_analyze_response(response.content)
        
        return {
            "messages": [response.content],
            "analysis": analysis,
            "conversation_id": id(state)
        }
    except Exception as e:
        error_response = "I'm having trouble connecting. Please try again."
        state.add_message("assistant", error_response)
        return {
            "messages": [error_response],
            "analysis": {"emotion": "neutral", "urgency": "low", "requires_intervention": False},
            "error": str(e)
        }

def quick_analyze_response(response: str) -> Dict[str, Any]:
    response_lower = response.lower()
    
    crisis_keywords = ['suicide', 'kill myself', 'end it all', 'want to die', 'harm myself']
    is_crisis = any(keyword in response_lower for keyword in crisis_keywords)
    
    emotion = "neutral"
    if any(word in response_lower for word in ['anxious', 'anxiety', 'worried']):
        emotion = "anxiety"
    elif any(word in response_lower for word in ['sad', 'depressed', 'down']):
        emotion = "depression"
    elif any(word in response_lower for word in ['stressed', 'overwhelmed']):
        emotion = "stress"
    elif any(word in response_lower for word in ['happy', 'good', 'great']):
        emotion = "positive"
    
    urgency = "crisis" if is_crisis else "low"
    
    return {
        "emotion": emotion,
        "urgency": urgency,
        "requires_intervention": is_crisis,
        "suggestions": get_quick_suggestions(emotion, urgency)
    }

def get_quick_suggestions(emotion: str, urgency: str) -> List[str]:
    if urgency == "crisis":
        return ["Contact crisis helpline (988)", "Reach out to campus counseling"]
    elif emotion == "anxiety":
        return ["Try deep breathing", "Practice grounding techniques"]
    elif emotion == "depression":
        return ["Talk to a friend", "Consider professional help"]
    elif emotion == "stress":
        return ["Try mindfulness", "Take breaks"]
    else:
        return ["Tell me more", "How can I help?"]

# Store conversation states
conversation_states = {}

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat_endpoint():
    try:
        data = request.json
        user_message = data.get('message', '')
        conversation_id = data.get('conversation_id')
        
        if not user_message.strip():
            return jsonify({"success": False, "error": "Empty message"}), 400
        
        if conversation_id and conversation_id in conversation_states:
            state = conversation_states[conversation_id]
        else:
            state = State()
            conversation_id = id(state)
            conversation_states[conversation_id] = state
        
        state.add_message("user", user_message)
        result = superbot(state)
        
        return jsonify({
            "success": True,
            "response": result["messages"][0],
            "analysis": result["analysis"],
            "conversation_id": conversation_id
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": "Server error"
        }), 500

if __name__ == "__main__":
    print("Starting Campus Mind Mental Health Chatbot...")
    print("Backend will be available at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
