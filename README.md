# Meeting Transcript Summarizer

This project is a simple **command-line application** that summarizes meeting transcripts using an LLM via **LlamaIndex** and **OpenRouter**.  
It reads a plain text meeting transcript, groups statements by speaker, and produces a concise bullet-point summary for each participant.

---

## Features

- Reads meeting transcripts from a `.txt` file
- Groups multiple statements from the same speaker into a single summary
- Preserves exact speaker names
- Produces short, clear bullet-point summaries
- Uses **LlamaIndex** for prompt handling
- Uses **OpenRouter** to access LLMs

---

## Example Input (`transcript.txt`)

```
Meera: The client demo went well overall, but they had concerns about the loading time.
Arjun: Yes, especially on the reports page, the load time crossed five seconds.
Sanjay: I checked the logs and found multiple redundant API calls.
Meera: Can we optimize that before the next demo?
Arjun: Yes, I will refactor the reports API and add caching.
Priya: From QA side, we also noticed intermittent failures during peak hours.
Sanjay: That might be related to database connection limits.
Priya: Please let me know once fixes are pushed so we can retest.
Meera: Timeline-wise, can we close this by Thursday?
Arjun: Backend fixes should be done by Thursday end.
Sanjay: Database optimizations will be completed by Wednesday.
Priya: I will schedule regression testing on Friday.
Meera: Good, I will update the client on progress.
```

---

## Example Output

![output](https://github.com/user-attachments/assets/da2af639-dcd5-444a-a631-fc9a0e38910d)

---

## Requirements

- Python 3.9+
- Virtual environment (recommended)
- OpenRouter API key

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Abarnarajj/meeting_summarizer.git
cd meeting_summarizer
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install llama-index llama-index-llms-openrouter
```

---

## API Key Setup

This project uses **OpenRouter**, not OpenAI directly.

Create an API key here:  
https://openrouter.ai/settings/keys

---

## Usage

Run the summarizer script:

```bash
python meeting_summarizer.py
```

When prompted, enter the transcript file name:

```
Enter the transcript file name: transcript.txt
```

---

## How It Works

- Reads transcript text from a file
- Sends the transcript to the LLM using a structured prompt
- Enforces strict rules:
  - Merges multiple updates into one summary per speaker
  - No paragraphs
- Prints the final meeting summary to the console
