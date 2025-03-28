const tg = window.Telegram.WebApp;

function sendData() {
  tg.sendData("Рыскелди нажал кнопку!");
  tg.close(); // Закрывает мини-апп
}