const chooseList = document.querySelectorAll(".img")
const lengthOfList = document.querySelector(".choosesElements")


let choosesElements = [], el, index

console.log(chooseList)

for(const element of chooseList) {
    element.addEventListener('click', (event) => {
        el = event.target.getAttribute("src").split('/').join(".").split(".")
        el = el[el.length-2]

        if(choosesElements.includes(el)) {     // проверка, есть ли он в списке
            index = choosesElements.indexOf(el)
            choosesElements.splice(index,1)    //удаляю элемент

            element.style.border = 0   

        } else {

            choosesElements.push(el)    //добавляю в список выбранных

            element.style.border = "2px solid red"
        }
        console.log(choosesElements)
        lengthOfList.textContent = `(${choosesElements.length})`
    })
}



