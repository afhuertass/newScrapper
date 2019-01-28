# newScrapper
A scraper for news from the Colombian Magazine Semana.com
All the data scrapped with this belongs to the owners and should be used just for learning process

Also includes a sumary generation method that works like this:
* each article is tokenized in sentences. 

* for each sentence turn the text data into vectors using the spanish embeddings in (https://www.kaggle.com/rtatman/pretrained-word-vectors-for-spanish)

* each pair of vector, calculate the cosine similarity and build a graph with this data

* Run Pagerank algorithm and extract the most relevant sentences per article as a summary for the article.


