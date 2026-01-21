document.addEventListener('DOMContentLoaded', () => {
    const countdownElement = document.getElementById('countdown');
    const targetDateStr = countdownElement.getAttribute('data-date');
    const targetDate = new Date(targetDateStr).getTime();

    const updateCountdown = () => {
        const now = new Date().getTime();
        const distance = targetDate - now;

        if (distance < 0) {
            document.getElementById('countdown').innerHTML = "<h3>¡Es hoy!</h3>";
            return;
        }

        document.getElementById('days').innerText = Math.floor(distance / (1000 * 60 * 60 * 24));
        document.getElementById('hours').innerText = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        document.getElementById('minutes').innerText = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        document.getElementById('seconds').innerText = Math.floor((distance % (1000 * 60)) / 1000);
    };

    setInterval(updateCountdown, 1000);
    updateCountdown();
});