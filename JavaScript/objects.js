let person = {
    identification: {name: 'David',
    age: 19,
    school: 'Pendo',
    'marital status': 'single'},
    'contact details': {
        email: 'johndoe@gmail.com',
        'phone number': '+254700000000'
    }
}
//accessing the age property
let personAge = person['identification']['age'];
console.log(personAge);

//looping through the person object
for(let psn in person['identification']){
    console.log(`${psn}`);
}

