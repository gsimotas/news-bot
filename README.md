# News Bot

News bot that sends an email once a week of a positive news story.

## How it Works

### NewsAPI

NewsAPI is an external API used to fetch real-time news data. It provides a simple HTTP REST API for accessing headlines and articles from various news sources around the world.

### Python

The programming language used to write the Lambda function code. Python is a versatile language and commonly used for scripting, automation, and web development.

### AWS Lambda

AWS Lambda is a serverless computing service provided by Amazon Web Services. It allows you to run code without provisioning or managing servers. In this case, Lambda is used to execute the positive news fetching and email sending logic on a schedule.

### Amazon Simple Email Service (SES)

Amazon SES is a cloud-based email sending service. It is used to send the positive news article to your email address. SES provides a reliable and scalable email infrastructure.

### AWS CloudWatch Events

AWS CloudWatch Events is a service that enables you to respond to system events in near-real-time. We use CloudWatch Events to schedule the execution of the Lambda function every Monday at 9 AM.
