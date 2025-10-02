# Coding Standards and Guidelines

## Code Style

### Python Style Guide
This project follows PEP 8 - Python's official style guide.

### Key Conventions

**Naming:**
- Functions: `snake_case` (e.g., `get_ai_response`)
- Variables: `snake_case` (e.g., `user_question`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `MAX_TOKENS`)
- Classes: `PascalCase` (e.g., `MessageHandler`)

**Indentation:**
- 4 spaces per indentation level
- No tabs

**Line Length:**
- Maximum 88 characters (Black formatter standard)
- Break long lines at logical points

**Imports:**
- Standard library imports first
- Third-party imports second
- Local imports last
- One import per line

**Spacing:**
- Two blank lines before function definitions
- One blank line between logical sections
- No trailing whitespace

## Documentation Standards

### Code Comments
- Use comments sparingly
- Comment only complex logic or non-obvious decisions
- Keep comments up-to-date with code changes
- Avoid stating the obvious

**Good Comment:**
```python
# OpenAI API requires messages in specific format
messages = [{"role": "system", "content": prompt}]
```

**Bad Comment:**
```python
# This sets x to 5
x = 5
```

### Docstrings
- Use for all functions
- Follow Google style guide format
- Include purpose, parameters, and return values

**Example:**
```python
def get_ai_response(user_question):
    """
    Sends user question to OpenAI and returns response.
    
    Args:
        user_question (str): The question from the user
        
    Returns:
        str: AI-generated response or error message
    """
```

## File Organization

### Project Structure
- Keep related files together
- Separate documentation from code
- Use clear, descriptive file names

### Import Organization
```python
# Standard library
import os

# Third-party
import streamlit as st
import openai

# Local
from config import settings
```

## Git Practices

### Commit Messages
Follow conventional commits format:

**Format:** `type: brief description`

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples:**
- `feat: add clear chat button`
- `fix: handle empty API key error`
- `docs: update README with setup steps`

### Commit Frequency
- Commit small, logical changes
- Each commit should be a working state
- Commit before major refactoring

### What Not to Commit
- `.env` files (contains secrets)
- `__pycache__/` directories
- `.pyc` files
- IDE-specific files
- Log files

## Error Handling

### Principles
- Always catch specific exceptions when possible
- Provide user-friendly error messages
- Log errors for debugging
- Never expose sensitive information in errors

**Example:**
```python
try:
    response = openai.ChatCompletion.create(...)
except openai.error.AuthenticationError:
    return "Invalid API key. Please check your configuration."
except Exception as e:
    return f"An error occurred: {str(e)}"
```

## Security Guidelines

### API Keys
- Never hardcode API keys in source code
- Always use environment variables
- Use `.env` file for local development
- Add `.env` to `.gitignore`

### Dependencies
- Keep dependencies up to date
- Review security advisories
- Use specific version numbers in requirements.txt

### User Input
- Validate user input when necessary
- Be cautious with eval() or exec()
- Sanitize data before external API calls

## Testing Standards

### Test Coverage
- Test main functionality
- Test error conditions
- Test edge cases

### Test Organization
- Keep tests in separate directory
- Mirror source code structure
- Use descriptive test names

**Example:**
```python
def test_get_ai_response_with_valid_input():
    # Arrange
    question = "What is Python?"
    
    # Act
    response = get_ai_response(question)
    
    # Assert
    assert response is not None
    assert len(response) > 0
```

## Code Review Checklist

Before submitting code:
- [ ] Code follows PEP 8 style guide
- [ ] No hardcoded secrets or API keys
- [ ] All functions have docstrings
- [ ] Error handling is implemented
- [ ] Comments explain complex logic
- [ ] No unnecessary comments
- [ ] Git commits are meaningful
- [ ] requirements.txt is updated
- [ ] README reflects current setup
- [ ] Code has been tested locally

## Dependency Management

### requirements.txt
- Pin major versions for stability
- Include all direct dependencies
- Keep file organized and commented if needed

**Format:**
```
streamlit==1.28.0
openai==0.28.0
python-dotenv==1.0.0
```

### Virtual Environment
- Always use virtual environment
- Never install packages globally for project
- Document setup in README

## Performance Guidelines

### General Principles
- Keep functions small and focused
- Avoid unnecessary API calls
- Use appropriate data structures
- Consider memory usage for session state

### Streamlit-Specific
- Minimize st.rerun() calls
- Use st.cache_data for expensive operations
- Keep session state clean and minimal

## Documentation Requirements

### README.md
Must include:
- Project description
- Installation instructions
- Usage guide
- Prerequisites
- Troubleshooting section

### Code Documentation
- Document all public functions
- Explain non-obvious design decisions
- Keep documentation in sync with code

### Project Documentation
- Requirements document
- Technical specifications
- This standards guide

## Maintenance

### Regular Tasks
- Update dependencies quarterly
- Review and update documentation
- Check for security advisories
- Clean up unused code

### Before Release
- Test all functionality
- Update version numbers
- Review all documentation
- Test deployment process