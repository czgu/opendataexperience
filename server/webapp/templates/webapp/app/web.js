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
	window.location.href = window.location.href + "#openModal";
}
