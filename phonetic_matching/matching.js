var fs = require('fs');

var discarded = 'AEIHOUWY'
,   categories = ['AEIOU', 'CGJKQSXYZ', 'BFPVW', 'DT', 'MN', 'H', 'L', 'R'];


function categorise (name) {
    var letters, cname, cletter, li, ci, i;

    name = name.toUpperCase().replace(/[^A-Z]/g, '');
    letters = [name[0]];

    for (i = 1; i < name.length; i++) {
        if (discarded.indexOf(name[i]) == -1) {
            letters.push(name[i]);
        }
    }

    cname = [];
    for (li in letters) {
        for (ci in categories) {
            if (categories[ci].indexOf(letters[li]) > -1) {
                cletter = ci;
                break;
            }
        }

        if (cname.length === 0 || cletter != cname.slice(-1)) {
            cname.push(cletter);
        }
    }

    return cname;
}


function match (input_names, sample_list) {
    var names, csample_name, cinput_names, i;

    cinput_names = [];
    for (i in input_names) {
        cinput_names.push(categorise(input_names[i]));
    }

    names = [];
    for (i in sample_list) {
        csample_name = categorise(sample_list[i]);
        if (cinput_names.join().indexOf(csample_name) > -1) {
            names.push(sample_list[i]);
        }
    }

    return names;
}


function main () {
    var data = '';
    process.stdin.on('readable', function () {
        data += process.stdin.read();
    })
    .on('end', function () {
        data = data.match(/[^\r\n]+/g);
        console.log(match(process.argv.slice(2), data).join('\n'));
    });
}


if (require.main === module) main();

exports.match = match;

