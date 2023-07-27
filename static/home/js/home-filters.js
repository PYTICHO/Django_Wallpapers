const cat = document.querySelector("#selectCat")
const selectedCat = document.querySelectorAll(".option-cat")

const sort = document.querySelector("#sort")



let href = window.location.href.split("/")
const indexFilters = href.indexOf("filter")

for(const selCat of selectedCat) {

    if(selCat.value === href[indexFilters + 1]) {
        selCat.setAttribute("selected", "selected")
    }
}
value = cat.value


cat.addEventListener("click", event => {
    if(cat.value != value) {

        value = cat.value
        
        href.splice(indexFilters + 1, 1)      // Делаю норм Url
        href.pop()
        href.splice(indexFilters + 1, 0, String(value))
        href = href.join("/")

        window.location.href = href     // Перенаправляю  
    }

})





