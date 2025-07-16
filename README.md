# arxiv-paper-finder

A simple terminal-based tool to semantically search arXiv papers using natural language.  
Powered by [SentenceTransformer](https://www.sbert.net/) and [FAISS](https://github.com/facebookresearch/faiss).

---

## Features

- Crawl abstracts from arXiv via their public API
- Use semantic search (vector similarity) for better query understanding
- View abstracts and direct PDF links
- No need for Streamlit or web UI – works directly in the terminal

---

## Demo

```bash
$ python arxiv_tool.py
Fetching papers from arXiv...
Loading NLP model...
Building FAISS index...

Enter your query (or 'exit' to quit): transformer for time series

Closest matching papers:

Time Series Transformer for Interpretable Forecasting
Tóm tắt: We propose a transformer-based model for time series forecasting...
Link abstract: https://arxiv.org/abs/2407.00123
Link PDF     : https://arxiv.org/pdf/2407.00123.pdf
------------------------------------------------------------
```
# arxiv-paper-finder
