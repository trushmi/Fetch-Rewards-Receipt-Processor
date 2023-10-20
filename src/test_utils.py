import unittest

from utils import (
    get_points_for_retailer_name, 
    get_purchase_day_points,
    get_purchase_hour_points,
    is_total_multiple_points,
    is_total_round_dollar_amount_points,
    get_points_for_items_in_receipt,
    trimmed_length_item_description_points,
    get_total_receipt_points
)
class TestUtils(unittest.TestCase):
    def test_get_points_for_retailer_name(self):
        receipt = {"retailer": "Target"}
        result = get_points_for_retailer_name(receipt)
        self.assertEqual(result, 6, "Expected 6 points for retailer name 'Target'")

    def test_get_purchase_day_points(self):
        receipt = {"purchaseDate": "2022-01-01"}
        result = get_purchase_day_points(receipt)
        self.assertEqual(result, 6, "Expected 6 points as the purchase day is odd (1).")

    def test_get_purchase_hour_points(self):
        receipt = {"purchaseTime": "13:01"}
        result = get_purchase_hour_points(receipt)
        self.assertEqual(result, 0, "Expected 0 points as the purchase time is outside the 2:00pm to 4:00pm range.")

    def test_is_total_multiple_points(self):
        receipt = {"total": "35.35"}
        result = is_total_multiple_points(receipt)
        self.assertEqual(result, 0, "Expected 0 points as the total amount is not a multiple of 0.25.")

    def test_is_total_round_dollar_amount_points(self):
        receipt = {"total": "35.35"}
        result = is_total_round_dollar_amount_points(receipt)
        self.assertEqual(result, 0, "Expected 0 points as the total amount is not a round dollar amount.")

    def test_get_points_for_items_in_receipt(self):
        receipt = {"items": [
            {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
            },{
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
            },{
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
            },{
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
            },{
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
            }
        ],
  }
        result = get_points_for_items_in_receipt(receipt)
        self.assertEqual(result, 10, "Expected 10 points for 5 items, as there are 2 pairs of items.")

    def test_trimmed_length_item_description_points(self):
        receipt = {"items": [
            {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
            },{
            "shortDescription": "Emils Cheese Pizza",
            "price": "12.25"
            },{
            "shortDescription": "Knorr Creamy Chicken",
            "price": "1.26"
            },{
            "shortDescription": "Doritos Nacho Cheese",
            "price": "3.35"
            },{
            "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
            "price": "12.00"
            }
        ],
  }
        result = trimmed_length_item_description_points(receipt)
        self.assertEqual(result, 6, "Expected 6 points as only one item description's trimmed length is a multiple of 3.")


def test_get_total_receipt_points(self):
    receipt={
    "retailer": "Target",
    "purchaseDate": "2022-01-01",
    "purchaseTime": "13:01",
    "items": [
        {
        "shortDescription": "Mountain Dew 12PK",
        "price": "6.49"
        },{
        "shortDescription": "Emils Cheese Pizza",
        "price": "12.25"
        },{
        "shortDescription": "Knorr Creamy Chicken",
        "price": "1.26"
        },{
        "shortDescription": "Doritos Nacho Cheese",
        "price": "3.35"
        },{
        "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
        "price": "12.00"
        }
    ],
    "total": "35.35"
    }
    result = get_total_receipt_points(receipt)
    self.assertEqual(result, 28, "Expected 28 points based on the sum of points from various criteria.")
