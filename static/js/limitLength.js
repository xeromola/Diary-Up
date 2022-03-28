const entries = document.querySelectorAll('span');
console.log(entries);
entries.forEach((entry) => {
    let elementText = entry.innerText;
    let maxLength = 150;

    console.log(entry);

    if (elementText.length > maxLength) {
        elementText = elementText.substr(0, maxLength);
    }

    entry.innerText = elementText;

    console.log(entry);
});
