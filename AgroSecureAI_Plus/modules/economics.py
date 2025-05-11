def estimate_revenue(crop, hectares):
    market_prices = {
        "Maize": 250000,
        "Millet": 200000,
        "Rice": 300000,
        "Tomato": 350000,
        "Cowpea": 280000,
        "Sorghum": 230000,
        "Groundnut": 260000,
        "Soybean": 240000,
        "Onion": 320000
    }
    yield_per_ha = {
        "Maize": 3.5,
        "Millet": 1.8,
        "Rice": 4.0,
        "Tomato": 5.0,
        "Cowpea": 2.0,
        "Sorghum": 2.5,
        "Groundnut": 2.0,
        "Soybean": 2.5,
        "Onion": 4.5
    }

    price = market_prices.get(crop, 200000)
    yield_ha = yield_per_ha.get(crop, 2.0)

    gross = hectares * yield_ha * price
    inputs = hectares * 50000  # estimated cost
    profit = gross - inputs

    return f"Estimated Revenue: ₦{gross:,.0f} | Cost: ₦{inputs:,.0f} | Net Profit: ₦{profit:,.0f}"
