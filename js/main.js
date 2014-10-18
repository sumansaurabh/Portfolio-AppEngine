$(document).ready(function(){
    
    $('#subbut').click(function(){
    	var subject = $("#subjectid").val();
    
    	var msg = $("#messageid").val();
    	var data={"subject":subject, "message":msg};
    
      
        $.ajax({
            url: '/post',
            type: 'POST',
            data: data,
            dataType: 'json',
            success: function(data,status){
              if(data.login_url)
              {
                alert("Please Sign In to 'Google' account before sending the message.");
                window.location=data.login_url;
              }
              else
              {
                $('#contact_form').html("<div id='message'></div>");
              $('#message').html("<h2>Message Submitted</h2>")
              .append("<p>I will be in touch soon.</p>")
              .hide()
              .fadeIn(1500, function() {
                $('#message').append("");
              });
                //alert("Message was Successfully sent.");
              }
            }
       });
       return false;
    });
});
