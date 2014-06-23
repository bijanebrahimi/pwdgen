
$(document).ready(function(){
  $(function(){
    $('a[title]').tooltip();
  });
  $('button').click(function(){
    var master_key = $('#master_key').val()
    var salt_domain = $('#salt_domain').val()
    var offset = parseInt($('#offset').val())
    var length = parseInt($('#length').val())
    
    raw_password = (master_key+salt_domain).md5().b64encode()
    mirrored_password = raw_password.repeat(Math.floor((offset+length)/44) + 1)
    password = mirrored_password.substring(offset, offset+length)
    console.log(password)
    $('#password').val(password)
  })
})
