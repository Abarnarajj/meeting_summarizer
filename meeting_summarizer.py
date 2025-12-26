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
You are helping summarize a meeting transcript.

Read the transcript and produce a short summary with bullet points.

Guidelines:
- Combine everything said by the same speaker into ONE bullet
- Keep the speaker names exactly as they appear
- Write each bullet as a complete, clear sentence (not fragments)
- You may combine multiple updates using semicolons if needed
- Do not write paragraphs or extra explanations

Example:

Transcript:
Abarna: API integration is almost done.
Abarna: Authentication issue is resolved.
Sarah: UI mockups are updated.
Sarah: Client feedback is pending.
Mike: I will set up staging by Wednesday.

Summary:
• Abarna: The API integration is progressing well, and the authentication issue has been resolved.
• Sarah: The UI mockups have been updated, and client feedback is still pending.
• Mike: He will set up the staging server by Wednesday.

Now summarize the following transcript:

{transcript}
"""

    prompt = PromptTemplate(template=template_content)
    response = llm.complete(prompt.format(transcript=transcript))
    print("\n Meeting Summary:\n")
    print(response.text.strip())

if __name__ == "__main__":
    main()
