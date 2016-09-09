<html>
<head>
<script type="text/javascript" src="jquery.min.js"></script>
<link rel="stylesheet" type="text/css" href="style.css">
<script language="Javascript">
$(document).ready(function(){
  $(document).keypress(function(e){
    $.post( "/ajax", {arrow:e.which}, function( data ) {
      //console.log(e);
    });
  });

  $(document).keyup(function(e){
    $.post( "/ajax", {arrow:e.which}, function( data ) {
      //console.log(e);
    });
  });

  $("#f")
    .mousedown(function(){
      $.post( "/ajax", {arrow:119}, function( data ) {});
    })
    .mouseup(function(){
      $.post( "/ajax", {arrow:87}, function( data ) {});
    });

  $("#b")
    .mousedown(function(){
      $.post( "/ajax", {arrow:115}, function( data ) {});
    })
    .mouseup(function(){
      $.post( "/ajax", {arrow:83}, function( data ) {});
    });

  $("#l")
    .mousedown(function(){
      $.post( "/ajax", {arrow:97}, function( data ) {});
    })
    .mouseup(function(){
      $.post( "/ajax", {arrow:65}, function( data ) {});
    });

  $("#r")
    .mousedown(function(){
      $.post( "/ajax", {arrow:100}, function( data ) {});
    })
    .mouseup(function(){
      $.post( "/ajax", {arrow:68}, function( data ) {});
    });
});

</script>
</head>
<body>
  <div class="Table">
    <div class="Heading">
      <div class="Cell"></div>
      <div class="Cell" style="background-color:Blue;" id="f"></div>
      <div class="Cell"></div>
    </div>
    <div class="Row">
      <div class="Cell" style="background-color:Green;" id="l"></div>
      <div class="Cell"></div>
      <div class="Cell" style="background-color:Pink;" id="r"></div>
    </div>
    <div class="Row">
      <div class="Cell"></div>
      <div class="Cell" style="background-color:Yellow" id="b"></div>
      <div class="Cell"></div>
    </div>
  </div>
</body>
</html>

