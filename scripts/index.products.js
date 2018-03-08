function page_down(pnum,page_count,cat){
    console.log('down btn')
    if (pnum == ''){
        pnum = 1
        cat = 0
    }
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
    var products = $('#products')
    console.log(pnum)
    if (pnum.length == ){
        console.log('hey hey hye')
        pnum = 1
        cat = 0
    }
    if (pnum == page_count){
        pnum = pnum
    } else {
        pnum = pnum + 1
    }
    $('#pnum').replaceWith(pnum)
    products.load('/catalog/index.products/' + cat + '/' + pnum)
}