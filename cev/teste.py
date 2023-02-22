import openai
import customtkinter

openai.api_key = "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"

def get_openai_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response["choices"][0]["text"]

def ask_question():
    question = question_entry.get()
    answer = get_openai_response(question)
    answer_label.configure(text=answer, wraplength=350)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("ChatGPT Interface")
root.geometry("400x400")

question_label = customtkinter.CTkLabel(root, text="Question:")
question_label.pack()

question_entry = customtkinter.CTkEntry(root)
question_entry.pack()

answer_label = customtkinter.CTkLabel(root, text="Answer:")
answer_label.configure(text="Answer will appear here", wraplength=350)
answer_label.pack()

ask_button = customtkinter.CTkButton(root, text="Ask", command=ask_question)
ask_button.pack()

root.mainloop()


