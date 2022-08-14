const button = document.querySelector('.hamburger-menu')
const leftBar = document.querySelector('.left-bar')
const body = document.querySelector('body')


button.addEventListener('click', () => {
    if (leftBar.classList.contains('hidden')) {
        leftBar.classList.remove('hidden')
        body.style.setProperty('overflow-y', 'hidden')

    } else {
        leftBar.classList.add('hidden')
        body.style.setProperty('overflow-y', 'auto')
    }
})

const placeholder = document.querySelector('#id_loan_date')
placeholder.setAttribute('placeholder', 'Formato: aaaa-mm-dd')
