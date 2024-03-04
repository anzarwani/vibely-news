# Vibely

Vibely is a project aimed at sentiment classification of news articles using fine-tuned BERT models. It enables users to classify news articles as either positive or negative sentiment. This repository contains code for fetching live news, fine-tuning BERT, and a Streamlit application for testing the sentiment analysis model.

[Web App](vibely.streamlit.com)

Note : Due to limitations of github free version, the web app for this project has limited bandwidth because of which the app is not accesible once the bandwidth quota is over.
## Features

- Fetch live news articles
- Fine-tune BERT for sentiment classification
- Test sentiment analysis model using Streamlit application

## Installation

To install the required dependencies, use:

```
pip install -r requirements.txt
```

## Usage

### Fetching Live News

You can use the `news.py` script to fetch live news articles. This script utilizes various news RSS feeds to retrieve news articles.

```bash
python news.py
```

### Testing Sentiment Analysis Model

The sentiment analysis model can be tested using the Streamlit application provided in `test.py`. Start the Streamlit server by running:

```bash
streamlit run test.py
```

## Contributing

Contributions are welcome! If you have any suggestions, enhancements, or bug fixes, please open an issue or a pull request.

---

Happy sentiment analyzing! 📰🙂📉
