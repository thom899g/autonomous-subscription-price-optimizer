from typing import Dict, Any
import numpy as np
from sklearn.linear_model import LinearRegression

class PricePredictor:
    def __init__(self):
        self.model = LinearRegression()
        self.data = None
        
    def train_model(self, data: Dict[str, Any]) -> bool:
        """
        Trains the machine learning model using historical sales data.
        Returns True if training is successful, False otherwise.
        """
        try:
            # Extract features and target
            X = np.array([data["sales_data"][i]["month"] 
                         for i in range(len(data["sales_data"]))]).reshape(-1, 1)
            y = np.array([data["sales_data"][i]["revenue"] 
                         for i in range(len(data["sales_data"]))])
            
            self.model.fit(X, y)
            logging.info("Model trained successfully")
            return True
        except Exception as e:
            logging.error(f"Training failed: {str(e)}")
            return False
            
    def predict_price(self, month: int) -> float:
        """
        Predicts the optimal price for a given month.
        Handles cases where prediction might be negative or unrealistic.
        """
        try:
            prediction = self.model.predict([[month]])[0]
            if prediction < 0:
                logging.warning("Negative price predicted; using minimum viable price.")
                return 10.0
            return round(prediction, 2)
        except Exception as e:
            logging.error(f"Prediction failed: {str(e)}")
            return None