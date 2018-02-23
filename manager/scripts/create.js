$(function(){
    var choice = $('#id_TYPE_CHOICES');
    console.log(choice)
    choice.on('change', function(){
        if (choice.val() == 1){
            
            $('#id_pid').closest('p').hide(1000)
            $('#id_max_rental_days').closest('p').hide(1000)
            $('#id_retire_date').closest('p').hide(1000)

            $('#id_quantity').closest('p').show(1000)
            $('#id_reorder_quantity').closest('p').show(1000)
            $('#id_reorder_trigger').closest('p').show(1000)

        } else if(choice.val()==2){
            $('#id_quantity').closest('p').hide(1000)
            $('#id_reorder_quantity').closest('p').hide(1000)
            $('#id_reorder_trigger').closest('p').hide(1000)
            $('#id_max_rental_days').closest('p').hide(1000)
            $('#id_retire_date').closest('p').hide(1000)

            $('#id_pid').closest('p').show(1000)
        } else {
            $('#id_quantity').closest('p').hide(1000)
            $('#id_reorder_quantity').closest('p').hide(1000)
            $('#id_reorder_trigger').closest('p').hide(1000)

            $('#id_max_rental_days').closest('p').show(1000)
            $('#id_retire_date').closest('p').show(1000)
            $('#id_pid').closest('p').show(1000)
            
        }
        })
    
})