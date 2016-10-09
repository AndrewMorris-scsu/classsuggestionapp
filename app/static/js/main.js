(function () {
$(document).ready(function () {
  $('a#fetch_data').bind('click', function() {
    console.log($SCRIPT_ROOT);
    console.log('test');
    $.getJSON($SCRIPT_ROOT + 'api/fetch_data', {
      val: $('input[name="filter"]').val()
    }, function(data) {
      $("#result").text(data);
    });
    return false;
  });
});

})();
