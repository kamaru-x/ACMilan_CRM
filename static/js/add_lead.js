$(document).ready(function(){
    $('#lead_text').hide()
    $('#lead_mode').change(function(){
        let lead_mode = $('#lead_mode').val()
        if(lead_mode == 'other'){
            $('#lead_text').show()
        }else{
            $('#lead_text').hide() 
        }
    })
})