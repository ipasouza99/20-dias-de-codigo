document.addEventListener('DOMContentLoaded', function() {
    const apiKey = 'coloque aqui  sua chave api ';
    const city = 'Juiz de Fora';
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric&lang=pt_br`;


    fetch(url)
        .then(response => response.json())
        .then(data => {
            const weatherElement = document.getElementById('weather');
            const temperature = data.main.temp;
            const description = data.weather[0].description;
            const humidity = data.main.humidity;
            const windSpeed = data.wind.speed;


            weatherElement.innerHTML = `
                <p>Temperatura: ${temperature}°C</p>
                <p>Descrição: ${description}</p>
                <p>Umidade: ${humidity}%</p>
                <p>Velocidade do Vento: ${windSpeed} m/s</p>
            `;
        })
        .catch(error => {
            const weatherElement = document.getElementById('weather');
            weatherElement.innerHTML = `<p>Erro ao obter dados do tempo. Tente novamente mais tarde.</p>`;
            console.error('Erro:', error);
        });
});
 