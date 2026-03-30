import streamlit as st
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

#setting up the page
st.set_page_config(page_title ="Smart Support AI")
st.title("Smart Support Agent",)
st.markdown("Analyze customer sentiment and specific issues in real-time.")

#loading in azure key and endpoitn
load_dotenv()
key = os.getenv("AZURE_LANGUAGE_KEY")
endpoint = os.getenv("AZURE_LANGUAGE_ENDPOINT")

#safety check 
if not key:
    print("ERROR: COULD NOT FIND KEY CHECK env file")
if not endpoint:
    print("ERROR: COULD NOT FIND ENDPOINT CHECK env file")
def get_client():
  return TextAnalyticsClient(endpoint=endpoint, credential = AzureKeyCredential(key))

#UI layout'
user_input = st.text_area("Enter Customer Message",height=150, placeholder="e.g. The food was great but the delivery was late.")
if st.button("Analyze Message"):
    if user_input:
        client = get_client()
        results = client.analyze_sentiment(documents=[user_input], show_opinion_mining=True)

        for doc in results:
            sentiment = doc.sentiment.upper()
            if sentiment == "POSITIVE":
                st.success(f"Overall Sentiment: {sentiment}")
            elif sentiment == "NEGATIVE":
                st.error(f"Overall Sentiment:{sentiment}")
                st.warning("ALERT: High-priority escalation triggered for Management.")
            else:
                st.info(f"Overall Sentiment:{sentiment}")
            #extracting opinions
            opinion_list = []
            for sentence in doc.sentences:
                # If there are specific opinions (Aspect-based sentiment)
                for op in sentence.mined_opinions:
                    aspect = op.target.text.capitalize()
                    
                    # A single aspect (like 'Food') can have multiple assessments
                    for assessment in op.assessments:
                        feeling = assessment.sentiment.capitalize()
                        description = assessment.text
                        
                        opinion_list.append({
                            "Aspect": aspect, 
                            "Feeling": feeling, 
                            "Description": description
                        })
            #display a table with opinions
            st.subheader("Detailed Insights")
            if opinion_list:
                df = pd.DataFrame(opinion_list)
                
                col1, col2 = st.columns(2)

                with col1:
                    st.metric("Total Insights", len(df))
                    
                with col2:
                    sentiment_counts = df['Feeling'].value_counts()
                    st.bar_chart(sentiment_counts)

                #remove duplicate entries
                df = df.drop_duplicates()
                
                def color_sentiment(val):
                    color = '#2ecc71' if val == 'Positive' else '#e74c3c' if val == 'Negative' else '#f1c40f'
                    return f'background-color: {color}; color: white'

            # Use this to display
                st.dataframe(df.style.applymap(color_sentiment, subset=['Feeling']), use_container_width=True,hide_index=True)
            

                #allow download of findings
                st.divider()
                st.subheader("Export results")
                timestamp = datetime.now().strftime("%Y-%m-%d")
                dynamic_filename = f"customer_insights_{timestamp}.csv"
                csv_data = df.to_csv(index=False).encode('utf-8')
                st.download_button(label="Download Insights as CSV",data= csv_data,file_name=dynamic_filename,mime ='text/csv',)
            else:
                st.write("No specific opinions found.")
    else:
        st.warning("Please enter customer message first!")

#footer
st.divider()
st.caption("Built by Brendan Gobvu | Powered by Microsoft Azure AI | 2026")