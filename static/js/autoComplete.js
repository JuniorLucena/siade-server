var substringMatcher = function(strs) {
	return function findMatches(q, cb) {
		var matches, substrRegex;

    // an array that will be populated with substring matches
    matches = [];

    // regex used to determine if a string contains the substring `q`
    substrRegex = new RegExp(q, 'i');

    // iterate through the pool of strings and for any string that
    // contains the substring `q`, add it to the `matches` array
    $.each(strs, function(i, str) {
    	if (substrRegex.test(str)) {
        // the typeahead jQuery plugin expects suggestions to a
        // JavaScript object, refer to typeahead docs for more info
        matches.push({ value: str });
    }
});

    cb(matches);
};
};

var states = ['Março', 'Abril', 'Maio', 'Junho', 'Julho',
'Agosto', 'Stembro', 'Outubro', 'Novembro', 'Dezembro', 'Janeiro',
'Fevereiro', '1', '2', '3', '4', '5', '6',
'7', '8', '9', '10', '11',
'12', 'Cristiano Nunes', 'Arthur Henrique', 'Evangilo', 'Junior Lucena', 'Luziana Feitosa',
'Demétrios Coutinho', 'Lucas', 'Jefferson Lima'
];

$('#the-basics .typeahead').typeahead({
	hint: true,
	highlight: true,
	minLength: 1
},
{
	name: 'states',
	displayKey: 'value',
	source: substringMatcher(states)
});
