// -------------------------- Drop Down Menu------------------------------

let a_parent =  document.querySelectorAll(".a_parent");
let dd_menu_a = document.querySelectorAll(".dd_menu_a");

a_parent.forEach(function(aitem){

		aitem.addEventListener("mouseover", function(){
			a_parent.forEach(function(aitem){
				aitem.classList.remove("active");
			})
			dd_menu_a.forEach(function(dd_menu_item){
				dd_menu_item.classList.remove("active");
			})
			aitem.classList.add("active");
		})
})


