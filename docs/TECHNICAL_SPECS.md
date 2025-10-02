# Technical Specifications

## System Architecture

### Overview
Single-tier web application using Streamlit framework with direct API integration to OpenAI services.

### Components

1. **Frontend (Streamlit)**
   - Handles user interface rendering
   - Manages user interactions
   - Displays chat messages

2. **Backend Logic**
   - Processes user input
   - Makes API calls to OpenAI
   - Manages conversation state

3. **External Service**
   - OpenAI API for AI responses

## Technology Stack

### Core Technologies
- **Python**: 3.9+
- **Streamlit**: 1.28.0 - Web framework
- **OpenAI Python Library**: 0.28.0 - API client
- **python-dotenv**: 1.0.0 - Environment variable management

### Development Tools
- Git for version control
- pip for package management
- Virtual environment for dependency isolation

## Data Flow

```
User Input → Streamlit UI → get_ai_response() → OpenAI API
                ↓                                      ↓
         Session State ← Message Display ← API Response
```

## Key Functions

### get_ai_response(user_question)
**Purpose:** Sends user question to OpenAI and returns response

**Input:**
- `user_question` (string): User's question text

**Output:**
- `response` (string): AI-generated answer or error message

**Process:**
1. Constructs message array with system prompt and conversation history
2. Calls OpenAI ChatCompletion API
3. Extracts response text
4. Returns response or error message

**Error Handling:**
- Catches all exceptions
- Returns user-friendly error message

## State Management

### Session State Variables

**st.session_state.messages**
- Type: List of dictionaries
- Structure: `[{"role": "user/assistant", "content": "message text"}]`
- Purpose: Stores conversation history
- Lifecycle: Persists during user session, cleared on page reload

## API Integration

### OpenAI API

**Endpoint:** ChatCompletion.create()

**Model:** gpt-3.5-turbo

**Parameters:**
- `messages`: Conversation history array
- `max_tokens`: 500 (limits response length)
- `temperature`: 0.7 (controls randomness)

**Authentication:**
- API key loaded from environment variable
- Set via `openai.api_key`

**Rate Limits:**
- Depends on OpenAI account tier
- Application does not implement rate limiting

## Configuration

### Environment Variables

**OPENAI_API_KEY**
- Required: Yes
- Format: String (sk-...)
- Source: .env file
- Usage: API authentication

### Application Settings

**Page Configuration:**
- Title: "AI Q&A Bot"
- Layout: Centered
- Icon: Robot emoji

## Security Considerations

### API Key Management
- Stored in .env file (not committed)
- Loaded at runtime via python-dotenv
- Never exposed in client-side code

### Data Privacy
- No user data stored persistently
- Conversation history only in session memory
- No logging of sensitive information

## Deployment

### Local Development
1. Install dependencies from requirements.txt
2. Set up .env file with API key
3. Run: `streamlit run app.py`
4. Access at http://localhost:8501

### Production Deployment Options

**Streamlit Community Cloud:**
- Push code to GitHub
- Connect repository to Streamlit Cloud
- Add OPENAI_API_KEY in Secrets management
- Automatic deployment on push

**Requirements:**
- Public GitHub repository
- requirements.txt file
- Valid OpenAI API key

## Performance Considerations

### Response Time
- Primarily dependent on OpenAI API latency
- Typical response: 2-4 seconds
- Displays loading spinner during wait

### Memory Usage
- Minimal base footprint
- Grows with conversation length
- Conversation limited only by session memory

## Error Handling

### API Errors
- Invalid API key: Error message displayed
- Rate limit exceeded: Error message displayed
- Network errors: Caught and displayed

### User Input
- Empty input: Ignored by Streamlit chat_input
- Very long input: Handled by OpenAI token limits

## Testing Strategy

### Manual Testing
- Verify UI loads correctly
- Test question submission
- Verify response display
- Test clear chat function
- Test error conditions (invalid API key)

### Future Automated Testing
- Unit tests for get_ai_response()
- Integration tests for API calls
- UI component testing