num = 1;

$(function(){
	// alert('hoge');
	setInterval(function(){ 
		setImage();
	}, 2000);
})



function setImage(){
	num = num + 1;
	if (num>4){
		num = 1;
	}
	var img_string = num + ".png";
	$("#img_area").attr("src", img_string);
}