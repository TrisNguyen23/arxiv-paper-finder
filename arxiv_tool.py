import feedparser
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import urllib.parse

# ===== 1. Cào dữ liệu từ arXiv =====
def fetch_arxiv(query="machine learning", max_results=50):
    query_encoded = urllib.parse.quote(query)
    url = f"http://export.arxiv.org/api/query?search_query=all:{query_encoded}&start=0&max_results={max_results}"
    feed = feedparser.parse(url)
    papers = []
    for entry in feed.entries:
        paper = {
            "title": entry.title,
            "summary": entry.summary,
            "link": entry.link
        }
        papers.append(paper)
    return papers

# ===== 2. Tạo FAISS index =====
def build_index(papers, model):
    summaries = [paper["summary"] for paper in papers]
    vectors = model.encode(summaries)
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(np.array(vectors))
    return index

# ===== 3. Semantic Search =====
def search(query, papers, index, model, top_k=5):
    q_vector = model.encode([query])
    D, I = index.search(np.array(q_vector), k=top_k)

    print("\nGợi ý bài báo gần nghĩa:")
    for i in I[0]:
        paper = papers[i]
        pdf_link = paper["link"].replace("/abs/", "/pdf/") + ".pdf"
        print(f"\n🔹 {paper['title']}")
        print(f"Tóm tắt: {paper['summary'][:300]}...")
        print(f"Link abstract: {paper['link']}")
        print(f"Link PDF     : {pdf_link}")
        print("-" * 60)

def main():
    print("Đang tải bài báo từ arXiv...")
    papers = fetch_arxiv("machine learning", max_results=30)

    print("Đang tải mô hình NLP...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("Đang xây FAISS index...")
    index = build_index(papers, model)

    while True:
        query = input("\nNhập từ khóa (hoặc 'exit' để thoát): ").strip()
        if query.lower() == "exit":
            print("Tạm biệt!")
            break
        search(query, papers, index, model)

if __name__ == "__main__":
    main()
