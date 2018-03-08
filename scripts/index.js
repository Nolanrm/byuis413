$(function(context) {
    return function() {
        console.log('hey hey' + context.cat)
        var products = $('#products')
        
        products.load('/catalog/index.products/' + context.cat + '/' + context.pnum)
        
        
    }
}(DMP_CONTEXT.get()))


function page_down(pnum,page_count,cat){
    console.log('down btn index')
    
    var products = $('#products')
    if (pnum == 1){
        pnum = pnum
    } else {
        pnum = pnum - 1
    }
    $('#pnum').replaceWith(pnum)
    products.load('/catalog/index.products/' + cat + '/' + pnum)

}

function page_up(pnum,page_count,cat){
    console.log('btn up index')
    var products = $('#products')
    
    if (pnum == page_count){
        pnum = pnum
    } else {
        pnum = pnum + 1
    }
    $('#pnum').replaceWith(pnum)
    products.load('/catalog/index.products/' + cat + '/' + pnum)
}