from langchain_groq import ChatGroq
from typing import Dict, List, Any
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Groq LLM with optimized settings for speed
llm = ChatGroq(
    model="llama-3.1-8b-instant",  # Much faster model
    temperature=0.3,  # Lower temperature for more focused responses
    groq_api_key="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",
    max_tokens=200,  # Limit response length for faster generation
    timeout=10  # 10 second timeout
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
    # Create concise system prompt for faster processing
    system_prompt = """You are Mindy, a mental health assistant. Be empathetic, supportive, and concise. 
    If you detect crisis content (suicidal thoughts, self-harm), provide immediate crisis resources."""
    
    # Prepare messages for the LLM - limit to last 5 messages for speed
    messages = [{"role": "system", "content": system_prompt}]
    
    # Add only recent conversation history (last 5 messages) for faster processing
    recent_history = state.conversation_history[-5:] if len(state.conversation_history) > 5 else state.conversation_history
    messages.extend(recent_history)
    
    try:
        # Get response from Groq LLM with optimized parameters
        response = llm.invoke(messages)
        
        # Parse response and add to state
        state.add_message("assistant", response.content)
        
        # Quick analysis for mental health indicators
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
    """Fast analysis for mental health indicators"""
    response_lower = response.lower()
    
    # Quick crisis detection
    crisis_keywords = ['suicide', 'kill myself', 'end it all', 'want to die', 'harm myself']
    is_crisis = any(keyword in response_lower for keyword in crisis_keywords)
    
    # Quick emotion detection
    emotion = "neutral"
    if any(word in response_lower for word in ['anxious', 'anxiety', 'worried']):
        emotion = "anxiety"
    elif any(word in response_lower for word in ['sad', 'depressed', 'down']):
        emotion = "depression"
    elif any(word in response_lower for word in ['stressed', 'overwhelmed']):
        emotion = "stress"
    elif any(word in response_lower for word in ['happy', 'good', 'great']):
        emotion = "positive"
    
    # Simple urgency assessment
    urgency = "crisis" if is_crisis else "low"
    
    return {
        "emotion": emotion,
        "urgency": urgency,
        "requires_intervention": is_crisis,
        "suggestions": get_quick_suggestions(emotion, urgency)
    }

def get_quick_suggestions(emotion: str, urgency: str) -> List[str]:
    """Fast suggestion generation"""
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

# Flask API to connect with frontend
app = Flask(__name__)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat_endpoint():
    try:
        data = request.json
        user_message = data.get('message', '')
        conversation_id = data.get('conversation_id')
        
        # Quick validation
        if not user_message.strip():
            return jsonify({"success": False, "error": "Empty message"}), 400
        
        # Create or retrieve state
        if conversation_id and conversation_id in conversation_states:
            state = conversation_states[conversation_id]
        else:
            state = State()
            conversation_id = id(state)
            conversation_states[conversation_id] = state
        
        # Add user message
        state.add_message("user", user_message)
        
        # Get bot response
        result = superbot(state)
        
        # Return minimal response for speed
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

# Store conversation states
conversation_states = {}

if __name__ == "__main__":
    print("Starting Mental Health Chatbot Backend...")
    print("Make sure to replace 'your-groq-api-key-here' with your actual Groq API key")
    print("Backend will be available at: http://localhost:5000")
    app.run(debug=True, port=5000)
