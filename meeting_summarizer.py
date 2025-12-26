import os
from llama_index.llms.openrouter import OpenRouter
from llama_index.core import PromptTemplate

def main():
    file_path = input("Enter the transcript file name: ").strip()

    if not os.path.exists(file_path):
        print(" File not found:", file_path)
        return

    
    with open(file_path, "r", encoding="utf-8") as f:
        transcript = f.read()

    llm = OpenRouter(
        model="gpt-3.5-turbo",
        api_key="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",  
        temperature=0.2,
    )

    template_str = """
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


    prompt = PromptTemplate(template=template_str)

    
    response = llm.complete(prompt.format(transcript=transcript))

    print("\n Meeting Summary:\n")
    print(response.text.strip())

if __name__ == "__main__":
    main()







# from llama_index.core import SimpleDirectoryReader, SummaryIndex
# from llama_index.llms.openrouter import OpenRouter
# import os

# def main():
#     # Ask user for the transcript file
#     file_path = input("Enter the transcript file name (e.g., transcript.txt): ").strip()

#     # Check if file exists
#     if not os.path.exists(file_path):
#         print(" File not found:", file_path)
#         return

#     # Load document content from the file
#     documents = SimpleDirectoryReader(input_files=[file_path]).load_data()

#     # Initialize OpenRouter LLM
#     llm = OpenRouter(
#         model="gpt-3.5-turbo",
#         api_key="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",
#         temperature=0.2,
#     )

#     # Build summary index
#     index = SummaryIndex.from_documents(documents)

#     # Create query engine
#     query_engine = index.as_query_engine(
#         response_mode="tree_summarize",
#         llm=llm
#     )

#     # Query the model to generate bullet-point summary
#     response = query_engine.query(
#         "Summarize this meeting transcript into clear bullet points focusing on decisions and action items."
#     )

#     # Print the summary
#     print("\n Meeting Summary:\n")
#     print(response)

# if __name__ == "__main__":
#     main()
