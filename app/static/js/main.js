(function () {
  $(document).ready(function () {
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
