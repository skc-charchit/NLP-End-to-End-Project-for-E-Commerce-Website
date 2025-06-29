from src.news.fetch_news_data import NewsAPIClient
from src.mongodb.mongodb import collection

def run_news_pipeline():
    # Instantiate News API client
    news_api = NewsAPIClient()
    
    # Fetch publishers data
    publishers_data = news_api.fetch_publishers(query = "india")
    
    if publishers_data:
        # Insert fetched data into MongoDB
        result = collection.insert_one({
            "type": "publishers",
            "data": publishers_data
        })
        print(f"Publishers data inserted with _id: {result.inserted_id}")
    else:
        print("No publishers data fetched.")

if __name__ == "__main__":
    run_news_pipeline()
