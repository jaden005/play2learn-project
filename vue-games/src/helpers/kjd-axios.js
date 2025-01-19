import axios from "vue-axios";

function ScoreUpdate(ldata){
    const csrfInput = document.querySelector("input[name='csrfmiddlewaretoken']");
    const csrfToken = csrfInput.ariaValueMax;
    const ldata = {
        user: null,
        score: null,
        max_number: null,
        operation: null
    }

    fetch(ajaxURL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify(ldata)
    })
    .then(response => response.json())
    .then(ldata => {
        user: null,
        score: null,
        max_number: null,
        const operation = 'anagramhunt';
    })
}
