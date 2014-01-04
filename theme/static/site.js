$(document).ready(function () {

  // See http://stackoverflow.com/a/7691922/355252
  function qualifyURL( url ){
    var img = document.createElement('img');
    img.src = url; // set string url
    url = img.src; // get qualified url
    img.src = null; // no server request
    return url;
  }

  var windowLocation = $(location).attr('href');

  // Mark the current navigation link as active
  $('.navbar .nav li a')
    .filter(function (index) {
      var qualifiedHref = qualifyURL($(this).attr('href'));
      return windowLocation.lastIndexOf(qualifiedHref) == 0;
    })
    .parent('li')
    .addClass('active');

  // Bootstrap'ify admonitions
  var alert2Adminitions = {
    'info': ['hint', 'tip', 'note'],
    'warning': ['warning', 'important', 'attention'],
    'danger': ['caution', 'danger', 'error']
  };

  for (alert in alert2Adminitions) {
    if (alert2Adminitions.hasOwnProperty(alert)) {
      var admonitions = alert2Adminitions[alert]
            .map(function(a) { return 'div.' + a; })
            .join(', ');
      $(admonitions).addClass('alert alert-'+alert);
    }
  }

  // Make some inline titles stand out
  $('.admonition-title,.topic-title').wrapInner('<strong />');

  // Turn figures into panels
  $('.figure')
    .addClass('panel panel-default')
    .wrapInner('<div class="panel-body"/>');
  $('.figure .caption').each(function () {
    var caption = $(this);
    var panel = caption.parents('.panel');
    var footer = $('<div class="panel-footer"/>');
    footer.html(caption.html());
    footer.appendTo(panel);
    caption.remove();
  });

  // Bootstrap'ify ReST alignments
  $('.align-center').addClass('text-center');
});
