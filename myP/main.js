$('footer').focus();
$(document).ready(function(){
  $('#pagepiling').pagepiling({
    menu: null,
    direction: 'vertical', 
    verticalCentered: false,
    sectionsColor: [],
    anchors: ['Home', 'About', 'Features', 'Contact'],
    scrollingSpeed: 700,
    easing: 'swing',
    loopBottom: false,
    loopTop: false,
    css3: true,
    navigation: {
      'textColor': '#000',
      'bulletsColor': '#000',
      'position': 'right',
      'tooltips': []
    },
    normalScrollElements: null,
    normalScrollElementTouchThreshold: 3,
    touchSensitivity: 5,
    keyboardScrolling: true,
    sectionSelector: '.section',
    animateAnchor: true,
    onLeave: function(index, nextIndex, direction){},
    afterLoad: function(anchorLink, index){},
    afterRender: function(){},
  });
});