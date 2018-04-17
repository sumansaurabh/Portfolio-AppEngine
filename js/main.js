$(document).ready(function(){
    
    $('#subbut').click(function(){
    	var subject = $("#subjectid").val();
    	var msg = $("#messageid").val();
      var emailid= $("#emailid").val();
    	var data={"subject":subject, "message":msg, "email": emailid};

      if(emailid.indexOf('@') < 1) {
        alert("Invalid email Id");
        return;
      }
    
      
        $.ajax({
            url: '/sendMail',
            type: 'POST',
            data: data,
            dataType: 'json',
            success: function(data,status){
              
              $('#contact_form').html("<div id='message'></div>");
              $('#message').html("<h2>Message Submitted</h2>")
                .append("<p>I will be in touch soon.</p>")
                .hide()
                .fadeIn(1500, function() {
                  $('#message').append("");
                });
                //alert("Message was Successfully sent.");
              
            }
       });
       return false;
    });
});
