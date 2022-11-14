

  function signup(){
    if(document.getElementById("name").value==""){
      swal("Error!", "Please enter the name!", "error");
      return false;
    }
    if(document.getElementById("phone").value==""){
      swal("Error!", "Please enter the phone number!", "error");
      return false;
    }
    if(document.getElementById("email").value==""){
      swal("Error!", "Please enter the Email!", "error");
      return false;
    }
    if(document.getElementById("pass").value==""){
      swal("Error!", "Please enter the password!", "error");
      return false;
    }
    if(document.getElementById("name")!=""&& document.getElementById("phone")!=""&&document.getElementById("email")!=""&&document.getElementById("pass")!=""){
      swal({
        title: "Are you sure?",
        text: "You want to notify me",
        icon: "warning",
        buttons: true,
        dangerMode: true,
      })
      .then((willDelete) => {
        if (willDelete) {
          swal("Yes your message will receive me", {
            icon: "success",
          });
        } else {
          
          swal("ok fine",{icon : "info", });
        }
      });
    }
  }