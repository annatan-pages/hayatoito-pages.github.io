$(document).ready(function () {

  var windowLocation = $(location).attr('href');

  // Mark the current navigation link as active
  $('.navbar .nav li a')
    .filter(function (index) {
      return windowLocation.lastIndexOf($(this).attr('href')) == 0;
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

  // Markdown footnote extention.
  $('.footnote > hr').after($('<div class="site-footnote-title">Footnotes:</div>'));

});
