(function () {
  $(document).ready(function () {
    function update_major_list() {
      setInterval(function(){
        $.getJSON($SCRIPT_ROOT + 'api/fetch_majors', {
        }).done(function(data) {
          console.log(data);
        }).fail(function() {
        });
        update_major_list();
      }, 5000);
      update_major_list();
    }
    update_major_list();

    $('button#fetch_data').bind('click', function() {
      $.getJSON($SCRIPT_ROOT + 'api/fetch_data', {
        data: $('input[name="major"]').val()
      }).done(function(data) {
        $("#result").text(data);
      }).fail(function() {
        $("#result").text("FAILED");
      });
      $.getJSON($SCRIPT_ROOT + 'api/fetch_major_count', {
        data: $('input[name="major"]').val()
      }).done(function(data) {
        $("#count").text(data);
      }).fail(function() {
        $("#count").text("FAILED");
      });
    });
  });
})();
