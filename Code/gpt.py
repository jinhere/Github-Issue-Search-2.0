import openai

# OpenAI API 키 설정
openai.api_key = "[YOURAPIKEY]"
def process_url_with_command(url, command, model="gpt-3.5-turbo", max_tokens=500):

    try:
        prompt = f"Please perform the following command on the content of this URL: {url}\n\nCommand: {command}"
        
        completion = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an AI assistant that analyzes web content and performs user commands."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.7,
        )
        
        return completion.choices[0].message['content'].strip()
    
    except Exception as e:
        return f"An error occurred during processing: {e}"
