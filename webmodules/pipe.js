function run(){
	var rawFile = new XMLHttpRequest();
	rawFile.open("GET", "http://21-days.github.io/play/pyout.txt", false);
	rawFile.onreadystatechange = function (){
		if(rawFile.readyState === 4){
			if(rawFile.status === 200 || rawFile.status == 0){
				return rawFile.responseText;
			}
		}
	}
	rawFile.send(null);
	var new=document.getElementById("game").textContent;
	String y=new+"/n"+rawFile.responseText;
	document.getElementById("game").textContent= y;
}
while(True){
	run()
}
