import requests
from typing import Dict, Any
import logging

class DataCollector:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.data_store = {}
        self.url = "https://api.example.com/data"
        
    def fetch_data(self) -> Dict[str, Any]:
        """
        Fetches data from external APIs and stores it locally.
        Handles errors and logs issues if data collection fails.
        """
        try:
            response = requests.get(
                self.url,
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
            response.raise_for_status()
            data = response.json()
            self.data_store.update({
                "sales_data": data.get("sales", {}),
                "market_trends": data.get("trends", {}),
                "customer_feedback": data.get("feedback", {})
            })
            logging.info("Data fetched successfully")
            return self.data_store
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to fetch data: {str(e)}")
            return None
            
    def save_data(self, filename: str) -> bool:
        """
        Saves collected data to a local file for backup.
        """
        try:
            with open(filename, "w") as f:
                f.write(str(self.data_store))
            logging.info(f"Data saved to {filename}")
            return True
        except Exception as e:
            logging.error(f"Failed to save data: {str(e)}")
            return False