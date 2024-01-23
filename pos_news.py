import json
import requests
import boto3
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

ses = boto3.client('ses', region_name='us-east-2')

def lambda_handler(event, context):
    positive_news = fetch_positive_news()
    send_email(positive_news)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Email sent successfully!')
    }

def fetch_positive_news():
    api_key = os.getenv("NEWSAPI_KEY")    
    endpoint = "https://newsapi.org/v2/everything"
    params = {
        "apiKey": api_key,  
        "pageSize": 20,  # Retrieve multiple articles to increase chances of finding positive news
        "q": "positive or uplifting",  # Use a positive keyword to filter articles
        "searchIn": "title,description",
    }

    response = requests.get(endpoint, params=params)

    try:
        news_data = response.json()
    except json.JSONDecodeError:
        print("Failed to decode JSON response:", response.text)
        return "Error decoding news response"

    print("News API Response:", news_data)  # Add this line for logging

    if response.status_code == 200 and news_data.get("status") == "ok":
        articles = news_data.get("articles", [])
        print("Number of Articles:", len(articles))  # Add this line for logging

        if articles:
            selected_article = articles[0]
            print("Selected Positive Article:", selected_article)  # Add this line for logging
            return f"Positive News: {selected_article['title']} - {selected_article['url']}"
        else:
            return "No positive articles found"
    else:
        return f"Error fetching news - {response.status_code}"



def send_email(message):
    # Replace with your SES email details
    sender_email = os.getenv("SES_SENDER_EMAIL")
    recipient_email = os.getenv("RECIPIENT_EMAIL")
    subject = "Positive News Weekly"
    
    # Compose the email
    email_body = f"Hello,\n\n{message}\n\nBest regards,\nYour Positive News Bot"

    # Send email using SES
    response = ses.send_email(
        Source=sender_email,
        Destination={
            'ToAddresses': [recipient_email],
        },
        Message={
            'Subject': {
                'Data': subject,
            },
            'Body': {
                'Text': {
                    'Data': email_body,
                },
            },
        },
    )

    print("Email sent with MessageId:", response['MessageId'])