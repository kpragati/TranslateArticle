from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
 
article = "「継続は力なり」このことわざは、継続的な努力と長期的な献身の力の重要性を強調しています。"

prompt = f"Translate an article into an English {article}"

def translate_Article(prompt):
     
     response = client.chat.completions.create(
        model = "gpt-4o",
        messages = [{"role": "user", "content": prompt},
                   {"role": "assistent", "content": "You are a professional translator. Translate a news into an English"},
                   {"role": "system", "content": "direct english translator"}],
        temperature = 0.1,
        max_token = 300 

     )

     return response.choices[0].message.content

print(translate_Article(prompt))
