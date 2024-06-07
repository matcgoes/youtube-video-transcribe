import streamlit as st
from dotenv import load_dotenv

load_dotenv() # carrega as variaveis de ambiente
import os
import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

prompt='''You are a Youtube video sumarizer. You will be taking the transcript text 
and summarizing the entire video and providing the important summary in points within 250 words. The transcript text will be appended here: '''

# Obtem a transcricao do Video
def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split('=')[1] # Captura o ID do video após o "=" do URL
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ''
        for i in transcript_text:
            transcript += ' ' + i['text']

        return transcript
    
    except Exception as e:
        raise e

# Realiza o resumo do video com Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt+transcript_text)

    return response.text

st.title('Youtube Video Summarizer')
youtube_link = st.text_input('Enter the URL link')

if youtube_link:
    video_id = youtube_link.split('=')[1]
    st.image(f'http://img.youtube.com/vi/{video_id}/0.jpg', use_column_width=True)

if st.button('Summarize it!'):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown('## Details:')
        st.write(summary)

