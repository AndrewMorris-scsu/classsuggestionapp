(function () {
  $(document).ready(function () {
    $('button#fetch_data').bind('click', function() {
      $.post($SCRIPT_ROOT + 'api/fetch_data', {
        data: $('input[name="filter"]').val()
      }).done(function(data) {
        $("#result").text(data);
      }).fail(function() {
        $("#result").text("FAILED");
      });
    });
  });
})();
