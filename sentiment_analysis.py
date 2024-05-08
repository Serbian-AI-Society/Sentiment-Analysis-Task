import os
from typing import List

# You will need to install the OpenAI Python package
from openai import OpenAI


def sentiment_analysis(
        texts: List[str],
        model: str = "gpt-3.5-turbo"    # This is just a suggestion
) -> List[str]:
    """
    Analyze the sentiment of given texts and return a list of sentiment labels.

    Args:
    texts (List[str]): A list of texts for sentiment analysis.

    Returns:
    List[str]: A list of sentiment labels ('positive', 'negative', 'neutral')
    corresponding to the input texts.
    """
    results = []
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    for line in texts:
        line = line.strip()
        # TODO: Put your code here (logic + OpenAI API call)

        # TODO: Be free to apply "lower()" on the output
        #  retrieved from the API.
        # Example: "Positive".lower() -> "positive"

    return results
