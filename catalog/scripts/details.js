
$(function(context) {
    return function() {
        $(".thumbnail").mouseover(function(){
            var current_image = this.src
        $(".main_image").attr("src",current_image)

        })     
    }
}(DMP_CONTEXT.get()))

