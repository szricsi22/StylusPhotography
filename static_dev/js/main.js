let menu_visible = false

function mobile_menu_clicked(){
    let nav_menu = document.getElementById("nav-menu")
    let menu_container = document.getElementById("menu-container")
    let category_menu = document.getElementById("category-menu")

    let category_menu_default_top = "54px"

    if(menu_visible){
        // hide menu
        menu_visible = false
        nav_menu.style.display = "none"

        if(category_menu){
            category_menu.style.top = category_menu_default_top
        }

    }else{
        // show menu
        menu_visible = true
        nav_menu.style.display = "flex"

        if(category_menu){
            category_menu.style.top = menu_container.clientHeight + "px"
        }
    }
}
