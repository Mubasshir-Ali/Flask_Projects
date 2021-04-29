// $("form[name=signup_form").submit(function(e) {

//     var $form = $(this);
//     var $error = $form.find(".error");
//     var data = $form.serialize();

//     $.ajax({
//         url: "/user/signup",
//         type:"POST",
//         data: data,
//         dataType: "json",
//         success: function(resp){
//             console.log(resp);
//         }, 
//         error: function(resp){
//             console.log(resp);
//         }

//     });

//     e.preventDefault();

// });

$(document).ready(function(){
    $("#submitbtn").click(function(event){
    // var $form = $(this);
    // var $error = $form.find(".error");
    // var data = $("#form").serializeArray();
    var FirstName = $("#FirstName").val();
    alert(data);

    $.ajax({
      url: "/user/signup",
      type: "POST",
      data: {
          firstname:FirstName,
      },
      dataType: "json",
      success: function(resp) {
        window.location.href = "/dashboard/";
      },
      error: function(resp) {
        $error.text(resp.responseJSON.error).removeClass("error--hidden");
      }
    });
  
    e.preventDefault();
  });
});
  
  $("form[name=login_form").submit(function(e) {
  
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();
  
    $.ajax({
      url: "/user/login",
      type: "POST",
      data: data,
      dataType: "json",
      success: function(resp) {
        window.location.href = "/dashboard/";
      },
      error: function(resp) {
        $error.text(resp.responseJSON.error).removeClass("error--hidden");
      }
    });
  
    e.preventDefault();
  });