# Sentiment Analysis Task
Acceptance Task for the **SAIS Hackathon 2024**

## Overview
This project serves as an acceptance task for the SAIS Hackathon and is 
designed to test your skills in natural language processing (NLP) by 
building a sentiment analysis model using the OpenAI API. The goal is 
to accurately classify texts into three categories: **positive**, 
**negative**, or **neutral**.

## Objective
Your task is to implement a Python program that reads a file with the list 
of text strings (separated by newline character) and returns a list of 
sentiment labels corresponding to each text string. The sentiments are 
classified as either 'positive', 'negative', or 'neutral'.

In order to solve this task, you will need to integrate the OpenAI API 
and invoke one of their chat-based models to perform sentiment analysis on 
the input text strings.

## Requirements
- Python 3.8 or later
- OpenAI API key

## Setup
1. **Clone the repository**: Start by cloning this repository to your local machine or development environment.
2. **Install dependencies**: Ensure that Python is installed on your system. You will need the `openai` library, which can be installed using pip:
```bash
pip install openai
```
3. **API Key**: You need to have access to an OpenAI API key. Set your API key in your environment variables:
```bash
export OPENAI_API_KEY='your_api_key_here'
```

## Implementation Guide
1. **Modify the function**: You will find a skeleton function in `sentiment_analysis.py`. Implement 
the logic which calls the OpenAI API to perform sentiment analysis.

2. **API Integration**:
- Use the 
[OpenAI Documentation](https://platform.openai.com/docs/introduction) to 
invoke OpenAI's chat-based model to get best-fitting sentiment for provided 
input text.

3. **Testing**: Test your function with different types of texts to ensure it accurately identifies the sentiment.

4. **Error Handling**: Implement error handling to manage potential issues during API calls.

## Example Usage
Below is an example of how you might run the program:
```bash
python main.py texts.txt
```

## Submission Guidelines
- Complete the implementation of the _sentiment_analysis_ function in the 
_sentiment_analysis.py_ file.
- Ensure your code is well-commented and follows the specified guidelines.
- Push your final changes to your repository before the deadline.

## Evaluation Criteria
- Accuracy of sentiment classification
- Code quality and efficiency
- Proper use of the OpenAI API
- Handling of edge cases and potential API errors

## Support
If you encounter any issues, please reach out on the class discussion forum.