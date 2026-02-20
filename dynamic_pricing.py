from typing import Dict, Any
import time

class DynamicPricingEngine:
    def __init__(self):
        self.current_prices = {}
        self.prediction_model = PricePredictor()
        
    def adjust_prices(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Adjusts subscription prices based on predictions and business constraints.
        Logs changes and ensures prices stay within acceptable ranges.
        """
        try:
            # Fetch predicted prices
            predicted_prices = self.prediction_model.predict_price(data["month"])
            
            # Apply constraints
            if predicted_prices < 10.0:
                logging.info("Price below minimum; setting to $10")
                new_price = 10.0
            elif predicted_prices > 50.0:
                logging.info("Price above maximum; setting to $50")
                new_price = 50.0
            else:
                new_price = predicted_prices
                
            # Update prices
            self.current_prices[data["plan"]] = new_price
            logging.info(f"Updated price for {data['plan']} plan: ${new_price}")
            return {"status": "success", "message": f"Pricing updated successfully"}
        except Exception as e:
            logging.error(f"Failed to adjust prices: {str(e)}")
            return {"status": "error", "message": str(e)}