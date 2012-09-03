$$('pre').each(function(pre){
  if(pre.getScrollSize().x == pre.getSize().x){
    pre.addClass('noExpand')
  }
})