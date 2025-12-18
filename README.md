# AI Poetry Generator and Tournament

An AI-powered poetry generation and selection system that uses OpenAI's GPT-3.5 to create, rate, and optimize German poems about a person based on their characteristics.

## Overview

This project demonstrates an innovative approach to automated poetry generation by:
1. **Generating** multiple variations of poems using different creative prompts
2. **Rating** poems against each other in tournament-style comparisons
3. **Optimizing** the best poems through iterative AI refinement

The system was created to generate personalized birthday poems in German, starting from a simple list of facts about a person (in this case, Noah).

## What This Project Does

The project implements a three-stage pipeline:

### 1. **Poetry Generation** (`generate_poetry.py`)
- Reads personal facts from `Noah.txt`
- Generates poems using 8 different creative prompts:
  - Standard poems with mean-to-kind progression
  - Well-rhymed birthday poems
  - Poems in the style of Johann Wolfgang von Goethe
  - Poems by fictional poet Sophie Meier
- Creates 8 variations per prompt (64 poems total)
- Saves all generated poems to `generated_poems/` directory

### 2. **Tournament Rating** (`rating.py`)
- Implements a tournament-style elimination system
- Compares poems pairwise using AI ratings across three categories:
  - Content (Inhalt)
  - Rhymes (Reime)
  - Style (Stil)
- Ratings are stored as JSON files in `ratings/` directory
- Winners advance to the next round until a champion emerges

### 3. **Optimization** (`optimization.py`)
- Takes the best poems and iteratively refines them
- Uses AI to optimize the poem quality
- Creates 10 optimization iterations
- Saves optimized versions to `optimized_poem/` directory

## Project Structure

```
poetry/
├── generate_poetry.py      # Main poetry generation script with embedded prompts
├── rating.py               # Tournament-style poem rating system
├── optimization.py         # Poem optimization through AI refinement
├── prompts.py             # Legacy file (not currently used)
├── Noah.txt               # Input file with personal facts
├── selfwrittenpoem.txt    # Self-written poem for comparison
├── generated_poems/       # 64 AI-generated poems (8 prompts × 8 reps)
├── ratings/               # JSON files with tournament ratings
├── optimized_poem/        # 11 iterations of optimized poems (0-10)
└── api_key.py            # OpenAI API key configuration (not in repo)
```

## Requirements

- Python 3.7+
- OpenAI Python library
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/MarcoFurrer/poetry.git
cd poetry
```

2. Install dependencies:
```bash
pip install openai
```

3. Create an `api_key.py` file with your OpenAI API key:
```python
API_KEY = "your-openai-api-key-here"
```

## Usage

### Generate Poems

Run the poetry generation script to create 64 poems based on the facts in `Noah.txt`:

```bash
python generate_poetry.py
```

This will:
- Read facts from `Noah.txt`
- Generate 64 poems (8 prompts × 8 repetitions)
- Save them to the `generated_poems/` directory

### Rate Poems in Tournament

Run the rating system to determine the best poems:

```bash
python rating.py
```

This will:
- Randomly shuffle the generated poems
- Compare them pairwise using AI ratings
- Eliminate weaker poems in each round
- Save ratings to `ratings/` directory
- Continue until one winner remains

### Optimize the Best Poem

After finding the best poem, optimize it:

```bash
python optimization.py
```

This will:
- Take poems from `optimized_poem/optimized0.txt` through `optimized9.txt`
- Ask AI to optimize each one
- Save the next iteration as `optimized1.txt` through `optimized10.txt`

## Features

- **Multi-prompt Strategy**: Uses diverse creative approaches including:
  - Mean-to-kind emotional progression
  - Birthday-appropriate verses
  - Literary style emulation (Goethe)
  - Fictional poet persona (Sophie Meier)

- **Tournament Selection**: Implements elimination rounds to objectively select the best poems

- **Iterative Refinement**: Continuously improves poems through AI optimization

- **German Language**: All prompts and poems are in German

## Input File Format

The `Noah.txt` file contains facts about the person, one per line:

```
Matura bestanden, weil mit mir Mathematik gelernt
Lissabon spontan übers Wochenende mit ihm besucht
in Italien ist sein Handy dauernd abgestürzt
...
```

## Output Examples

Generated poems follow various styles. For example, a standard generated poem starts:

```
Noah, der faule Schlendrian, 
Der immer zu spät kommen kann. 
Matura bestanden, doch nur mit meinem Rat, 
Mathematik lernte er erst spät.
...
```

After optimization, the poem becomes more refined:

```
Im Schatten des Vesuvs geboren,
Mit großen Träumen, oft verloren.
Noah, der Goldsucher, meisterhaft im Graben,
Beim Monopoly manchmal verzagt und arg geplagt.
...
```

## API Usage and Costs

This project makes extensive use of the OpenAI API:
- **Generation**: 64 API calls for initial poem generation
- **Rating**: Multiple rounds of comparisons (starts with 32 comparisons)
- **Optimization**: 10 API calls for refinement

⚠️ **Cost Warning**: Running all three scripts will consume OpenAI API credits. Consider starting with fewer repetitions during testing.

## Configuration

Edit the following constants in the scripts to adjust behavior:

- `generate_poetry.py`:
  - `REPS_PER_PROMPT = 8`: Number of variations per prompt (must be power of 2)
  
- `optimization.py`:
  - `range(0,10)`: Number of optimization iterations

## Security Note

**Never commit your API key!** The `.gitignore` file is configured to exclude `api_key.py` to prevent accidental commits of sensitive credentials.

## Future Improvements

Potential enhancements:
- Support for multiple languages
- Web interface for generating poems
- Fine-tuning on specific poetry styles
- Export to formatted PDF for presentations
- Command-line arguments for customization

## License

This project is provided as-is for educational and personal use.

## Author

Created by Marco Furrer

## Acknowledgments

- OpenAI GPT-3.5 for poetry generation
- Johann Wolfgang von Goethe for inspiration
- Sophie Meier (fictional poet persona) for creative style
