//-------Search field
function validateForm() {
    console.log('validating form');
    let x = document.forms["search_form"]["search_key"].value;
    if (x.trim() == "") {
    //   alert("Please enter a search keyword");
        return false;
        // document.getElementsByClassName('search_key')[0].placeholder = 'Search products...';
    }
}


//------- add to cart 
var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'Action:', action)
		console.log('USER:', user)

		if (user == 'AnonymousUser'){
			console.log('User is not authenticated')
			
		}else{
			// updateUserOrder(productId, action)
            updateCartTotal(productId)
		}
	})
}

var cartTotal = 0;
function updateCartTotal(productId){
    console.log('Updating cart total...')

    cartTotal +=1;
    document.getElementById("cart-total").innerHTML = cartTotal;
    return true;
}

// $(function(){
//   $("#addToCart").bind('click', function(){
//     console.log('addtocart clicked');
//   });
// });

