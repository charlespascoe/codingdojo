var fs = require('fs');

var discarded = 'AEIHOUWY'
,   categories = ['AEIOU', 'CGJKQSXYZ', 'BFPVW', 'DT', 'MN', 'H', 'L', 'R'];


function categorise (name) {
    name = name.toUpperCase().replace(/[^A-Z]/g, '');
    var letters = [name[0]];

    for (var i = 1; i < name.length; i++) {
        if (discarded.indexOf(name[i]) == -1) {
            letters.push(name[i]);
        }
    }

    var cname = [];

    for (var li in letters) {
        for (var ci in categories) {
            if (categories[ci].indexOf(letters[li]) > -1) {
                var cletter = ci;
                break;
            }
        }

        if (cname.length == 0 || cletter != cname.slice(-1)) {
            cname.push(cletter);
        }
    }

    return cname;
}


function match (input_names, sample_list) {
    var names = [];

    var cinput_names = [];
    for (var i in input_names) {
        cinput_names.push(categorise(input_names[i]));
    }

    for (var i in sample_list) {
        var csample_name = categorise(sample_list[i]);
        if (cinput_names.join().indexOf(csample_name) > -1) {
            names.push(sample_list[i]);
        }
    }

    return names;
}


var data = '';
process.stdin.on('readable', function () {
    data += process.stdin.read();
})
.on('end', function () {
    data = data.split('\r\n');
    console.log(match(process.argv.slice(2), data).join('\n'));
});


