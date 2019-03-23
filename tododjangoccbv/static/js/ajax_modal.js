$(document).ready(function(){


  var loadForm = function() {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal").modal("show");
      },
      success: function (data) {
        $("#modal .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function() {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#table tbody").html(data.list);
          $("#modal").modal("hide");
        }
        else {
          $("#modal .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  $("body").on('click', '.js-create', loadForm);
  $("body").on('submit', '.js-create-form', saveForm);
  // Update {{model}}
  $("body").on("click", '.js-update', loadForm);
  $("body").on('submit', '.js-update-form', saveForm)
  // Delete {{model}}

  $("body").on('click', '.js-delete', loadForm);
  $("body").on('submit', '.js-delete-form', saveForm);
})
