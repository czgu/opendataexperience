function configureDropDownLists(ddl1,ddl2) {
	var colours = new Array('Black', 'White', 'Blue');
	var shapes = new Array('Square', 'Circle', 'Triangle');
	var names = new Array('John', 'David', 'Sarah');

	switch (ddl1.value) {
		case 'Colours':
			ddl2.options.length = 0;
			for (i = 0; i < colours.length; i++) {
				createOption(ddl2, colours[i], colours[i]);
			}
			break;
		case 'Shapes':
			ddl2.options.length = 0; 
			for (i = 0; i < shapes.length; i++) {
				createOption(ddl2, shapes[i], shapes[i]);
			}
			break;
		case 'Names':
			ddl2.options.length = 0;
			for (i = 0; i < names.length; i++) {
				createOption(ddl2, names[i], names[i]);
			}
			break;
		default:
			ddl2.options.length = 0;
		break;
	}

}

function createOption(ddl, text, value) {
	var opt = document.createElement('option');
	opt.value = value;
	opt.text = text;
	ddl.options.add(opt);
}

function open() {
	var text = document.getElementById('hihi');
	text.innerHTML += "hihi";
	$(function(){ // On DOM ready
		$('#openOnLoad').click();
	});
}

var xmlhttp = new XMLHttpRequest();
var nut = ["energy","protein","carbohydrate","total_sugar","total_dietary_fibre","total_fat","saturated_fat","cholesterol","calcium","iron","sodium","potassium","magnesium","phosphorus","vitaminA","vitaminC","alcohol","caffeine"];

var nutName = {"energy": "KiloCalories","protein":"Protein","carbohydrate":"Carbohydrate","total_sugar":"Total Sugar","total_dietary_fibre":"Total Dietary Fibre","total_fat":"Total Fat","saturated_fat":"Saturated Fat","cholesterol":"Cholesterol","calcium":"Calcium","iron":"Iron","sodium":"Sodium","potassium":"Potassium","magnesium":"Magnesium","phosphorus":"Phosphorus","vitaminA":"Vitamin A","vitaminC":"Vitamin C","alcohol":"Alcohol","caffeine":"Caffeine"};

function getJson(request, success) {
	xmlhttp.onreadystatechange = function() {
	    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
	        var myArr = JSON.parse(xmlhttp.responseText);
	        success(myArr);
	    }
	}
	xmlhttp.open("GET", "/api/food/?name=" + request, true);
	xmlhttp.send();
}

function printData(arr) {
	var out = document.getElementById('tbl-list');
	out.innerHTML = '<tr><th>Nutrient</th><th>Amount</th></tr>';

	for (i = 0; i < nut.length; i++) {
		out.innerHTML += "<tr><td>" + nutName[ nut[i] ] + "</td><td>" + arr[ nut[i] ] + "</td></tr>";
	}

}