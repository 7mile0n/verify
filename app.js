let tg = window.Telegram.WebApp;

tg.expand();

tg.MainButton.textColor = '#FFFFFF';
tg.MainButton.color = '#2cab37';
let userip = "";

$(document).ready(()=>{
    $.getJSON("https://api.ipify.org?format=json",
    function (data) {

        // Displayin IP address on screen
        userip = data.ip;
    })
});
let btn1 = document.getElementById("btn1");


btn1.addEventListener("click", function(){
	if (tg.MainButton.isVisible) {
		tg.MainButton.hide();
	}
	else {
		tg.MainButton.setText("Click to complete verification");
		tg.MainButton.show();
	}
});




Telegram.WebApp.onEvent("mainButtonClicked", function(){
	tg.sendData(userip);
});


let usercard = document.getElementById("usercard");

let p = document.createElement("p");

p.innerText = `${tg.initDataUnsafe.user.first_name}
${tg.initDataUnsafe.user.last_name}`;

usercard.appendChild(p);








