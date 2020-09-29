$(document).ready(function () {

	//CONST
	const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
	const recognition = new SpeechRecognition();

	const startBtn = $(".buttonStart");
	const result = $(".media-content");
	const processing = $(".arin-result-p");

	//BUTTON CHANGE
	var toggleBtn = null;

	// var isLetterENG= function(context){ 
	// 	return /[qwertyuiopasdfghjklzxcvbnm]/i.test(context) ?  "ENG" : 0;
	// }
	// var isLetterRU= function(context) {
	// 	return /[а-яыъэёъ]/i.test(context) ? "RU" : 0; 
	// }
	// // var isLetterUA= function(context) {
	// // 	return /[а-яіїє]/i.test(context) ? "UA" : 0;
	// // }
	// var lang= function(iscontent){
	// 	return 	isLetterENG(iscontent) ? "ENG": 
	// 			// isLetterUA(iscontent) ? "UA": 
	// 			isLetterRU(iscontent) ? "RU" : 0;

	// }


	// PROCESS
	function process(rawText) {
		var text = rawText.replace(/\s/g, "");
		text = text.toLowerCase();
		return answer(text);
	}

	// speech to text

	if (typeof SpeechRecognition === "undefined") {
		startBtn.remove();
		result.html("<b>Browser does not support Speech API. Please download latest chrome.<b>");
	}
	else {
		recognition.continuous = true;
		recognition.interimResults = true;
		recognition.onresult = event => {
			recognition.lang = $("#selectelem option:selected").text();
			const last = event.results.length - 1;
			const res = event.results[last];
			const text = res[0].transcript;
			if (res.isFinal) {
				processing.html("processing ....");
				const response = process(text);
				const p = document.createElement("p");
				p.innerHTML = `<b> You </b> said: ${text} <br> <b> Aid </b> said: ${response}`;
				processing.html("");
				result.append(p);
				// text to speech
				speechSynthesis.speak(new SpeechSynthesisUtterance(response));
			}
			else {
				processing.html(`listening: ${text}`);
			}
		}
		var listening = false;
		function toggleBtn() {
			if (listening) {
				recognition.stop();
				startBtn.html("Start listening");
			}
			else {
				recognition.start();
				startBtn.html("Stop listening");
			}
			listening = !listening;
		};
		startBtn.click(toggleBtn);
	}





	//QUESTION AND ANSWERS
	var answer = function (text) {
		var response = null;
		if (recognition.lang == "ENG") {
			//eng-ENG
			switch (text) {
				case "hello":
					response = "hi, how are you doing?"; break;
				case "what'syourname":
					response = "My name's AID."; break;
				case "howareyou":
					response = "I'm good."; break;
				case "whattimeisit":
					response = new Date().toLocavarimeString(); break;
				case "stop":
					response = "Bye!!";
					toggleBtn();
				case "post":
					response = "Check, it`s last post";
					window.open(`http://127.0.0.1:8000/post/3/`, "_blank"); break;
				case "login":
					response = "Okey";
					window.open(`http://127.0.0.1:8000/login/`, "_blank"); break;
				case "news":
					response = "Check, it`s last news";
					window.open(`http://127.0.0.1:8000/news/`, "_blank"); break;
				case "calculator":
					response = "Okey, what to count?";
					break;
				case "help":
					response = " I 'news'- open news in site, 'login' - open page login, 'post' - open last post, 'stop' - and lissing, 'what time is it' - time, ' '"
					break;
				default:
					window.open(`http://google.com/search?q=${rawText.replace("search", "")}`, "_blank");
					return `I found some information for ${rawText}`;
			}
		}
		else if (recognition.lang == "RUS") {
			//ru-RU
			switch (text) {
				case "привет":
					response = "Привет, что подсказать?"; break;
				case "кактебязовут":
					response = "My name's Siri."; break;
				case "":
					response = "I'm good."; break;
				case "":
					response = new Date().toLocavarimeString(); break;
				case "":
					response = "Bye!!";
					toggleBtn();
				case "новости":
					window.open(`http://127.0.0.1:8000/post/3/`, "_blank"); break;
				case "":
					window.open(`http://127.0.0.1:8000/news/`, "_blank"); break;

				default:
					window.open(`http://google.com/search?q=${rawText.replace("search", "")}`, "_blank");
					return `I found some information for ${rawText}`;
			}
		}
		return response;
	}

});
