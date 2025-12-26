import os
from llama_index.llms.openrouter import OpenRouter
from llama_index.core import PromptTemplate
def main():
    file= input("Enter the transcript file name: ").strip()
    if not os.path.exists(file):
        print(" File not found:", file)
        return
    with open(file, "r", encoding="utf-8") as f:
        transcript = f.read()
    llm = OpenRouter(
        model="gpt-3.5-turbo",
        api_key="",  
        temperature=0.2,
    )
    template_content = """
You are an assistant that summarizes meeting transcripts.

IMPORTANT RULES (follow strictly):
- Group all statements by the same speaker into ONE bullet point
- Preserve speaker names exactly
- Merge multiple actions/updates into a single concise summary per speaker
- Do NOT write paragraphs
--- Example ---
Transcript:
Abarna: API integration is almost done.
Abarna: Authentication issue is resolved.
Sarah: UI mockups are updated.
Sarah: Client feedback is pending.
Mike: I will set up staging by Wednesday.

Summary:
• Abarna: API integration progressing well; authentication issue resolved
• Sarah: UI mockups updated; awaiting client feedback
• Mike: Will set up staging server by Wednesday
--- End Example ---

Transcript:
{transcript}
"""
    prompt = PromptTemplate(template=template_content)
    response = llm.complete(prompt.format(transcript=transcript))
    print("\n Meeting Summary:\n")
    print(response.text.strip())

if __name__ == "__main__":
    main()







