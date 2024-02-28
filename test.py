import tensorflow as tf
import tensorflow_text as text
import streamlit as st

from news import fetch_news_from_rss

# FRONTEND

st.header("Personalized News")
st.title(':blue[Positive] or :red[Negative] news | As _you_ want it.')
#st.divider()

pos_dict = {}
neg_dict = {}
headline = []
examples = []

@st.cache_resource
def load_model():
    saved_model_path = "news_sentiment_bert_tuned"
    reloaded_model = tf.saved_model.load(saved_model_path)
    st.success("Our AI news genie is loaded and ready to serve")
    return reloaded_model

reloaded_model = load_model()

def fetch_news():
    
    feed_url = 'https://feeds.skynews.com/feeds/rss/home.xml'
    num_articles = 10
    news_articles = fetch_news_from_rss(feed_url, num_articles)


    for idx, article in enumerate(news_articles, 1):
        examples.append(article['text'])
        headline.append(article['headline'])
        
    st.success("News has been fetch")
            
def run_batch_pred():
    serving_results = reloaded_model \
                .signatures['serving_default'](tf.constant(examples))

    serving_results = tf.sigmoid(serving_results['classifier'])
    
    serving_results_np = serving_results.numpy()

    for i in range(len(serving_results_np)):
        output_value = serving_results_np[i][0]
        if output_value <= 0.50:
            neg_dict[f"news{i}"] = {"headline": headline[i], "text": examples[i]}
            #print("Negative News")
        else:
            pos_dict[f"news{i}"] = {"headline": headline[i], "text": examples[i]}
            #print("Positive News")    
                    
fetch_news()
run_batch_pred()


head_pos = []
text_pos = []

head_neg = []
text_neg = []

def sort_news():
    for news_info_pos in pos_dict.values():
        head_pos.append(news_info_pos["headline"])
        text_pos.append(news_info_pos["text"])
        
    for news_info in neg_dict.values():
        head_neg.append(news_info["headline"])
        text_neg.append(news_info["text"])

sort_news()  

#st.divider()
st.subheader('Select Your News Mood :blue[positive] or :red[Negative]')
option = st.selectbox(
    'Choose Mood',
    ('Positive', 'Negative')
    )

if option == "Positive":
    for headline_pos, text_pos in zip(head_pos, text_pos):
        st.subheader(headline_pos)
        st.caption(text_pos)
#        st.divider()
elif option == "Negative":
    for headline_neg, text_neg in zip(head_neg, text_neg):
        st.subheader(headline_neg)
        st.caption(text_neg)
#        st.divider()

url = 'https://www.kaggle.com/anzarwani2'       
st.markdown("Developed by Anzar - Connect with me on [Kaggle](%s)" % url)