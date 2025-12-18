# Contributing to AI Poetry Generator

Thank you for your interest in contributing to this project!

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your feature/fix
4. Make your changes
5. Test your changes
6. Submit a pull request

## Development Setup

1. Install Python 3.7 or higher
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create your `api_key.py` file based on `api_key.py.example`
4. Add your OpenAI API key

## Code Style

- Follow PEP 8 guidelines for Python code
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and simple

## Testing Your Changes

Before submitting a pull request:

1. Test with a small number of repetitions to avoid excessive API costs:
   - In `generate_poetry.py`, temporarily set `REPS_PER_PROMPT = 2`
   - In `optimization.py`, temporarily use `range(0,2)`

2. Verify that:
   - Poetry generation creates files in `generated_poems/`
   - Rating system produces valid JSON in `ratings/`
   - Optimization creates improved poems

## Suggesting Improvements

Ideas for contributions:

- **New Prompt Templates**: Add creative prompt variations in `generate_poetry.py`
- **Multi-language Support**: Extend to support English, Spanish, etc.
- **Command-line Interface**: Add argparse for better user control
- **Web Interface**: Create a Flask/Django web app
- **Performance Optimization**: Reduce API calls or costs
- **Better Rating System**: Improve the tournament algorithm
- **Documentation**: Improve README, add tutorials, or create examples

## API Key Security

⚠️ **NEVER commit your API key!**

- Always use `api_key.py` for your key
- The `.gitignore` file prevents committing this file
- Double-check before pushing any changes

## Pull Request Guidelines

When submitting a pull request:

1. Provide a clear description of what changes you made
2. Explain why the changes are beneficial
3. Link to any related issues
4. Include example outputs if applicable
5. Keep changes focused - one feature per PR

## Questions?

If you have questions or need help:

- Open an issue on GitHub
- Describe your question clearly
- Include relevant code snippets or error messages

## Code of Conduct

- Be respectful and constructive
- Help others learn and grow
- Focus on the code, not the person
- Assume good intentions

Thank you for contributing!
