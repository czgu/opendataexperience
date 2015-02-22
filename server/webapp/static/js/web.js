function initOpt(arr) {
	var ddl = document.getElementById('ddl');
	var names = arr['categories']
	for (i = 0; i < names.length; i++) {
        if (!names[i]) {
            continue;
        }
		createOption(ddl, names[i]["category_name"], names[i]["category_name"]);
	}
}

function configureDropDownLists(arr) {
	var cat = document.getElementById('ddl').value;
    var opts;

	for (i = 0; i < arr["categories"].length; i++) {
		if (cat == arr["categories"][i]["category_name"]) {
			opts = arr["categories"][i]["sub_categories"];
			break;
		}
	}

	var ddl2 = document.getElementById('ddl2');

	for (i = 0; i < opts.length; i++) {
		createOption(ddl2, opts[i]["category_name"],opts[i]["category_name"]);
	}
}

function configDP2(ddl2) {
	var request = "search/food/?category=" + dll2.value + "&&only_name=true";
	getJson(request,configureDropDownLists2);
}

function configureDropDownLists2(arr) {
	var cat = document.getElementById('ddl2').value;
    var opts;

	for (i = 0; i < arr["categories"].length; i++) {
		if (cat == arr["categories"][i]["category_name"]) {
			opts = arr["categories"][i]["sub_categories"];
			break;
		}
	}

	var ddl2 = document.getElementById('ddl3');

	for (i = 0; i < opts.length; i++) {
		createOption(ddl2, opts[i]["category_name"],opts[i]["category_name"]);
	}
}

function createOption(ddl, text, value) {
	var opt = document.createElement('option');
	opt.value = value;
	opt.text = text.toLowerCase();
	ddl.options.add(opt);
}

function search(ddl3){
	var request = "food/?name=" + ddl3.value;
	getJson(request,printData);
}



$(document).ready(function () {
    $( '#openWrapper' ).click(function() {
        $( '#openModal' ).fadeTo(0.5, 1);
        $( '#openModal' ).css( 'pointer-events', 'auto' );
        console.log('hello');
    });
    $( '#closeModal' ).click(function(e) {
        console.log('world');
        e.preventDefault();
        $( '#openModal' ).fadeTo(0.5, 0);
        $( '#openModal' ).css( 'pointer-events', 'none' );
    });
    getJson("categories/all/",initOpt);
});

var xmlhttp = new XMLHttpRequest();
var nut = ["energy","protein","carbohydrate","total_sugar","total_dietary_fibre","total_fat","cholesterol","calcium","vitaminA","vitaminC"];

var nutName = {"energy": "KiloCalories","protein":"Protein","carbohydrate":"Carbohydrate","total_sugar":"Total Sugar","total_dietary_fibre":"Total Dietary Fibre","total_fat":"Total Fat","cholesterol":"Cholesterol","calcium":"Calcium","vitaminA":"Vitamin A","vitaminC":"Vitamin C"};

function getJson(request, success) {
	xmlhttp.onreadystatechange = function() {
	    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
	        var myArr = JSON.parse(xmlhttp.responseText);
	        success(myArr);
	    }
	}
	xmlhttp.open("GET", "/api/" + request, true);
	xmlhttp.send();
}

function printData(arr) {
	var text = document.getElementById('items');
	text.innerHTML = '<p> ' + arr["food_name"] + '           <button onclick="clearPage()">remove</button></p>';

	var out = document.getElementById('tbl-list');
	out.innerHTML = '<tr><th>Nutrient</th><th>Amount</th></tr>';

	for (i = 0; i < nut.length; i++) {
		if (arr[ nut[i] ] != "0") {
			out.innerHTML += "<tr><td>" + nutName[ nut[i] ] + "</td><td>" + arr[ nut[i] ] + "</td></tr>";
		}
	}
}

function clearPage() {
	document.getElementById('items').innerHTML = 'cleared';
	document.getElementById('tbl-list').innerHTML = '';
}

