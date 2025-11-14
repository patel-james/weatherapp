document.getElementById('searchBtn').addEventListener("click", async() =>{
    const city = document.getElementById("cityInput").value;

    if(!city){
        alert("Please enter a city name");
        return;
    }

    const response = await fetch(`/weather?city=${city}`);
    const data = await response.json();

    if(data.error){
        alert("City not found");
        return;
    }
    // Store the weather data globally for the button clicks
    document.getElementById("cityHeader").innerText = `${data.city} ${data.country}`;
    window.weatherInfo = data;

    // Reveal buttons
    document.getElementById("buttonsContainer").classList.remove("hidden");
    document.getElementById("result").innerText = "";
});

document.querySelectorAll(".info-button").forEach(button => {
    button.addEventListener("click", () => {
        const type = button.getAttribute("data-type");
        let value = window.weatherInfo[type];
        if (type === "temperature" || type === "feels_like") {
            value = value + "°C";
        }

        document.getElementById("result").innerText = `${type.toUpperCase()}: ${value}`;
    });

});