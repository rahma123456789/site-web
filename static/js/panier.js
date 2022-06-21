//add to cart
$("#addtocart"),on('click',function(){
var _vm=$(this)
var _quantité=$("#quantité").val();

var _cod_art=$("#cod_art").val();

$.ajax({
    url:'/achat',
    data:{
      
      'quantité':_quantité,
   
      'cod_art':_cod_art

    },

dataType:'json',
beforeSend:function(){
    _vm.attr('disabled',true)
    
},
success:function(res){
    console.log(res);
    _vm.attr('disabled',false)
}
})
 }



);