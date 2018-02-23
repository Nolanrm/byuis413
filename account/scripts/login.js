//delayed
//closure (for scope)

$(function() {

    var choice = $('#id_type');
    console.log(choice);
    choice.on('change', function(){
        console.log('hey, hey hey')
    })
    console.log('hey');



})