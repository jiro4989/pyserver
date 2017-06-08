window.onload = function() {
  window.onkeyup = function(e) {
    let input = document.getElementsByTagName("input")[0];
    if (document.activeElement != input) {
      switch (e.keyCode) {
        case 73 :
          input.focus();
          break;
      }
    }
  }
}
