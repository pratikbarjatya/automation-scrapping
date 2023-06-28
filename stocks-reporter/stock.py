# Importing all the necessary libraries
from time import sleep
import random
import numpy as np
from datetime import datetime
from flask import Flask
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)


class ShareData(Resource):
    def get(self):
        """Returns share price data to the client."""
        
        while True:

            price_now = np.round(a=random.randint(0, 2000) + random.random(), decimals=2)
            prev_close = np.round(a=random.randint(0, 2000) + random.random(), decimals=2)
            price_updown = np.round(a=price_now - prev_close, decimals=2)
            price_percent = np.round(a=(price_now - prev_close) / prev_close, decimals=2)
            price_units = 'INR'
            time =  datetime.now().strftime("%H:%M:%S")
            time_units = "IST"
            open_ = np.round(a=random.randint(0, 2000) + random.random(), decimals=2)
            high_ = np.round(a=random.randint(0, 2000) + random.random(), decimals=2)
            low_ = np.round(a=random.randint(0, 2000) + random.random(), decimals=2)
            mkt_cap = np.round(a=random.randint(5, 15) + random.random(), decimals=2)
            pe_ratio = np.round(a=random.randint(20, 50) + random.random(), decimals=2)
            div_yield = np.round(a=random.randint(0, 5) + random.random(), decimals=2)
            wk52_high = np.round(a=random.randint(0, 2000) + random.random(), decimals=2)
            wk52_low = np.round(a=random.randint(0, 2000) + random.random(), decimals=2)

            # Data placeholder in the form of JSON
            data = {'price_now' : price_now, 'price_updown' : price_updown, 'price_percent': price_percent, 
                   'price_units' : price_units, 'time' : time, 'time_units' : time_units, 'open' : open_, 'high' : high_, 'low' : low_, 
                   'market_cap' : mkt_cap, 'pe_ratio' : pe_ratio, 'div_yield' : div_yield, 'prev_close' : prev_close, 
                   'wk52_high' : wk52_high, 'wk52_low' : wk52_low}

            # Set random sleep time
            sleep(random.randint(5, 15))
            
            # Return data if success
            return {'data': data}, 200

    
# Add shareprice endpoint to the base url    
api.add_resource(ShareData, '/shareprices')


# Run the flask app
if __name__ == '__main__':
    app.run()