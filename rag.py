from openai import OpenAI
client = OpenAI()
def ask_llm(question, context):
    prompt = f"""
You are a helpful assistant. 
Use the following context to answer the question.
Context: {context}
Question: {question}
Answer:"""
    response = client.responses.create(
        model="gpt-4.1",
        input=prompt
    )
    return response.choices[0].message.content