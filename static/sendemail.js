function invokeAWSAPI(e) {
    e.preventDefault();           
    var name = $("#form-name").val();
    var email = $("#form-email").val();
    var message = $("#form-message").val();
    var data = {
       name : name,
       email : email,
       message : message
     };
     
     $.ajax({
      type: "POST",
      url : "https://vmy9bo2nx2.execute-api.us-east-1.amazonaws.com/prod/submit",
      dataType: "json",
      crossDomain: "true",
      contentType: "application/json; charset=utf-8",
      data: JSON.stringify(data),
      success: function () {
        alert("Successful");
        document.getElementById("contact-form").reset();
      },
      error: function () {
        alert("unsuccessful");
      }});
  }