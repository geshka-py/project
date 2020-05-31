let i = 1
$('#img_box').click(function() {
    if(i == 1){
        $('#show').css({
            'display': 'block',
        });
        i = 2
    }else{
        $('#show').css({
            'display': 'none',
        });
        i = 1
    }
});