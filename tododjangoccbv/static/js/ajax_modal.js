'use strict';
(function(w,d,$){
  $(d).ready(function(){
    let loadForm = function() {
      let btn = $(this);
      $.ajax({
        url: btn.attr("href"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal").modal("show");
        },
        success: function (data) {
          $("#modal .modal-content").html(data.html_form);
        }
      });
      return false;
    };

    let saveForm = function() {
      let form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            $("#modal").modal("hide");
            location.reload();
          }
          else {
            $("#modal .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };
    $("body").on('click', '.js-load-form', loadForm);
    $("body").on('submit', '.js-save-form', saveForm);
  }) /* document ready */


})(window,document,jQuery)
