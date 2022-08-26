let labels = document.querySelectorAll("label")
let inputs = document.querySelectorAll("input")

for (let index = 5; index > 3; index--) {
    const element = labels[index];
    console.log(element);
    console.log(inputs[index-3]);
    inputs[index-3].placeholder = element.innerHTML.replace(":", "");    
}
