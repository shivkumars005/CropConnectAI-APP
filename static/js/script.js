document.addEventListener("DOMContentLoaded", function () {
    // Fetch Market Prices
    fetch('/api/market_prices')
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById("market-prices");
            data.forEach(item => {
                let li = document.createElement("li");
                li.textContent = `${item.crop}: ${item.price}`;
                list.appendChild(li);
            });
        });

    // Fetch Weather Data
    fetch('/api/weather')
        .then(response => response.json())
        .then(data => {
            document.getElementById("weather").textContent = 
                `Temperature: ${data.temperature}, Humidity: ${data.humidity}, Forecast: ${data.forecast}`;
        });

    // Fetch Crop Recommendations
    fetch('/api/crop_recommendations')
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById("crop-recommendations");
            data.forEach(item => {
                let li = document.createElement("li");
                li.textContent = `Soil: ${item.soil_type} → Crops: ${item.recommended_crops.join(", ")}`;
                list.appendChild(li);
            });
        });
});
