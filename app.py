import gradio as gr
from summarizer import summarize

gr.Interface(
    fn=summarize,                                 
    inputs=gr.Textbox(label="Website URL"),
    outputs=gr.Markdown(label="Summary"),
    title="🔎 AI Website Summarizer",
).launch(share=True)            #share=True will give us a public link to the app. We created the frontend using gradio. The summarize function is imported from summarizer.py, which uses the fetch_website_contents function from scraper.py to get the website content and then summarizes it using OpenAI's API.